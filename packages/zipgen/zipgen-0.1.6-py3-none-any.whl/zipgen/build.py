from asyncio import StreamReader
from dataclasses import dataclass
from io import BufferedIOBase, RawIOBase, UnsupportedOperation
from os import name, stat, walk, stat_result
from os.path import relpath, join, splitext, dirname, abspath
from typing import AnyStr, Dict, AsyncGenerator, Generator, Tuple, Union, Optional, cast, Callable, Any

from .compress import *
from .constant import *
from .convert import *
from .pack import *


__all__ = (
    "WalkIgnoreCallable",
    "WalkNoCompressCallable",
    "walk_ignore_default",
    "walk_no_compress_default",
    "get_version_system",
    "ZipContext",
    "BuilderCallableContext",
    "ZipBuilder",
)


# WalkIgnoreCallable
def walk_ignore_default(path: AnyStr, ext: AnyStr, folder: bool, stat: stat_result) -> bool:
    """Never ignores a file."""
    return False


# WalkNoCompressCallable
def walk_no_compress_default(path: AnyStr, ext: AnyStr, stat: stat_result) -> bool:
    """Check if file extension is DEFAULT_NO_COMPRESS_FILE_EXTENSIONS and file size under 256."""
    return ext in DEFAULT_NO_COMPRESS_FILE_EXTENSIONS or stat.st_size < 256


def get_version_system(name: str) -> int:
    """Returns version integer for current OS:"""
    return MADE_BY_WINDOWS if name == "nt" else MADE_BY_UNIX


@dataclass
class ZipContext(object):
    path: bytes
    compression: int
    compressor: CompressorBase
    compressor_ctx: CompressorContext
    flag: int
    time: int
    date: int
    version: int
    external_attributes: int
    comment: bytes
    relative_offset: int


@dataclass
class BuilderCallableContext(object):
    done: bool = False
    ctx: Optional[ZipContext] = None
    folderPath: Optional[bytes] = None

    @property
    def is_folder(self) -> bool:
        """Returns true if folderPath is defined."""
        return self.folderPath is not None

    @property
    def is_file(self) -> bool:
        """Returns true if ctx is defined."""
        return self.ctx is not None

    @property
    def path(self) -> bytes:
        """Gets folder or ctx path."""
        if self.folderPath is not None:
            return self.folderPath

        if self.ctx is not None:
            return self.ctx.path

        raise TypeError("paths are none")


# Callback for methods
BuilderCallable = Callable[[BuilderCallableContext, Any], None]
WalkNoCompressCallable = Callable[[AnyStr, AnyStr, stat_result], bool]
WalkIgnoreCallable = Callable[[AnyStr, AnyStr, bool, stat_result], bool]


class ZipBuilder(object):
    __slots__ = (
        "buffer",
        "version_system",
        "version_extract",
        "headers",
        "ctx",
        "offset",
        "callbacks",
    )

    def __init__(self, buffer_size=65536, system=get_version_system(name)) -> None:
        self.buffer = memoryview(bytearray(buffer_size))
        self.version_system = system
        self.version_extract = CREATE_DEFAULT
        self.headers: Dict[bytes, bytes] = {}
        self.ctx: Optional[ZipContext] = None
        self.offset: int = 0
        self.callbacks: Dict[BuilderCallable, Any] = {}

    def _clear_ctx(self) -> None:
        """Clear context."""
        self.ctx = None

    def _new_file_ctx(self, path: AnyStr, io: Optional[Union[BufferedIOBase, RawIOBase]], utc_time: Optional[float], compression: int, comment: AnyStr) -> ZipContext:
        """Adds file and returns generator which yields LocalFile header and data."""
        if self.ctx is not None:
            raise ValueError("File operation pending.")

        # Path
        path_bytes = norm_path(path, False)
        if path_bytes in self.headers:
            raise ValueError("Path already in headers.")

        # Comment
        if comment is None:
            comment_bytes = b""
        elif isinstance(comment, str):
            comment_bytes = comment.encode("utf8")
        elif isinstance(comment, (bytes, bytearray,)):
            comment_bytes = comment
        else:
            raise ValueError("Comment has to be bytes or str.")

        # Set file attr default
        file_attr: Tuple[int, Optional[float]]
        file_attr = (DEFAULT_EXTERNAL_ATTR, None,)

        # Try file attr from file
        if io is not None:
            try:
                file_stat = stat(io.fileno())
                file_attr = (
                    (file_stat.st_mode & 0xFFFF) << 16,  # File mode
                    file_stat.st_mtime,  # File modified time
                )
            except UnsupportedOperation:
                pass

        # External attr
        external_attr = file_attr[0]

        # Time and date
        if utc_time is None:
            utc_time = file_attr[1]
        time, date = dos_time(utc_time)

        # Extract version
        extract_version = get_extract_version(compression, False)
        if extract_version >= self.version_extract:
            self.version_extract = extract_version

        return ZipContext(
            path=path_bytes,
            compression=compression,
            compressor=get_compressor(compression),
            compressor_ctx=CompressorContext(),
            flag=FLAG_DEFAULT_LZMA_FILE if compression == COMPRESSION_LZMA else FLAG_DEFAULT_FILE,
            time=time,
            date=date,
            version=extract_version,
            external_attributes=external_attr,
            comment=comment_bytes,
            relative_offset=self.offset,
        )

    def _write(self, buf: bytes) -> bytes:
        """Returns buffer and increases offset by length of the buffer."""
        self.offset += len(buf)
        return buf

    def _write_local_file(self) -> bytes:
        """Returns buffer containing LocalFile header."""
        if self.ctx is None:
            raise ValueError("No current context.")

        return self._write(pack_header_with_data(HEADER_LOCAL_FILE, LocalFile(
            self.ctx.version,
            self.ctx.flag,
            self.ctx.compression,
            self.ctx.time,
            self.ctx.date,
            0,  # crc32
            0,  # compressed size
            0,  # uncompressed size
            len(self.ctx.path),
            0  # extra len
        ), self.ctx.path))

    def _write_data_descriptor(self) -> bytes:
        """Returns buffer containing DataDescriptor(64) header."""
        if self.ctx is None:
            raise ValueError("No current context.")

        use_zip64 = self.ctx.compressor_ctx.compressed_size >= INT32_MAX
        crc32 = self.ctx.compressor_ctx.crc32
        comp_size = self.ctx.compressor_ctx.compressed_size
        uncompsize = self.ctx.compressor_ctx.uncompressed_size

        if use_zip64:
            return self._write(pack_header(HEADER_DATA_DESCRIPTOR64, DataDescriptor64(crc32, comp_size, uncompsize)))
        else:
            return self._write(pack_header(HEADER_DATA_DESCRIPTOR64, DataDescriptor(crc32, comp_size, uncompsize)))

    def _write_end(self, comment: bytes) -> bytes:
        """Returns buffer containing End Of Central directory and zip64 headers if necessary."""
        try:
            buf = bytearray()
            count = len(self.headers)

            # Write all headers into bytearr
            for header in self.headers.values():
                buf += header

            # Check if offset past int32 max
            size = len(buf)
            offset = self.offset + size
            use_zip64 = offset >= INT32_MAX or count >= 0xFFFF

            # Zip64 record and locator
            if use_zip64:
                # Record
                buf += pack_header(HEADER_CENTRAL_DIRECTORY_RECORD64, CentralDirectoryRecord64(
                    SIZE_CENTRAL_DIRECTORY_RECORD64_REMAINING,
                    self.version_extract,
                    self.version_system,
                    self.version_extract,
                    0,  # Disk number
                    0,  # Disk start
                    count,
                    count,
                    size,
                    self.offset,
                ))

                # Locator
                buf += pack_header(HEADER_CENTRAL_DIRECTORY_LOCATOR64, CentralDirectoryLocator64(
                    0,  # Disk number
                    offset,
                    1,  # Total disks
                ))

            # End of Central Directory
            buf += pack_header_with_data(HEADER_END_OF_CENTRAL_DIRECTORY, EndOfCentralDirectory(
                0,  # Disk number
                0,  # Disk start
                0xFFFF if use_zip64 else count,
                0xFFFF if use_zip64 else count,
                0xFFFFFFFF if use_zip64 else size,
                0xFFFFFFFF if use_zip64 else self.offset,
                len(comment),
            ), comment)

            return bytes(buf)
        finally:
            # Reset
            self.offset = 0
            self.headers.clear()

    def _set_header(self) -> None:
        """Sets headers key to context"s path which point to CentralDirectory bytes."""
        if self.ctx is None:
            raise ValueError("No current context.")

        cctx = self.ctx.compressor_ctx
        use_zip64 = cctx.compressed_size >= INT32_MAX or self.ctx.relative_offset >= INT32_MAX

        # Extended information for zip64
        extra = pack_header(TAG_EXTENDED_INFORMATION64, ExtendedInformation64(
            SIZE_EXTENDED_INFORMATION,  # Size of extended information.
            cctx.uncompressed_size,
            cctx.compressed_size,
            self.ctx.relative_offset,
            0,  # Disk start number
        )) if use_zip64 else b""

        # Store header bytes.
        self.headers[self.ctx.path] = pack_header_with_data(HEADER_CENTRAL_DIRECTORY, CentralDirectory(
            self.ctx.version,
            self.version_system,
            self.ctx.version,
            self.ctx.flag,
            self.ctx.compression,
            self.ctx.time,
            self.ctx.date,
            cctx.crc32,
            0xFFFFFFFF if use_zip64 else cctx.compressed_size,
            0xFFFFFFFF if use_zip64 else cctx.uncompressed_size,
            len(self.ctx.path),
            len(extra),
            len(self.ctx.comment),
            0,  # Disk start
            0,  # Internal Attributes
            self.ctx.external_attributes,
            0xFFFFFFFF if use_zip64 else self.ctx.relative_offset,
        ), self.ctx.path, extra, self.ctx.comment)

    def _call(self, done: bool = False, ctx: Optional[ZipContext] = None, folderPath: Optional[bytes] = None) -> None:
        """Calls builder's all callbacks."""
        if self.callbacks:
            bctx = BuilderCallableContext(done, ctx, folderPath)

            for cb, extra in self.callbacks.items():
                cb(bctx, extra)

    def set_callback(self, cb: BuilderCallable, extra: Optional[Any] = None) -> None:
        """Adds callback for watching events."""
        self.callbacks[cb] = extra

    def add_buf(self, path: AnyStr, buf: Union[bytes, bytearray, memoryview], utc_time: Optional[float] = None, compression=COMPRESSION_STORED, comment="") -> Generator[bytes, None, None]:
        """Adds the buffer and returns Generator of bytes object."""
        # Create file context.
        self.ctx = self._new_file_ctx(
            path, None, utc_time, compression, comment
        )

        # Yield file's header and content.
        try:
            self._call(done=False, ctx=self.ctx)
            yield self._write_local_file()

            for buf in compress_buf(self.ctx.compressor, self.ctx.compressor_ctx, buf, len(self.buffer)):
                yield self._write(buf)

            yield self._write_data_descriptor()
        finally:
            self._call(done=True, ctx=self.ctx)
            self._set_header()
            self._clear_ctx()

    def add_io(self, path: AnyStr, io: Union[BufferedIOBase, RawIOBase], utc_time: Optional[float] = None, compression=COMPRESSION_STORED, comment="") -> Generator[bytes, None, None]:
        """Adds the io and returns Generator of bytes object."""
        with io:
            # Create file context.
            self.ctx = self._new_file_ctx(
                path, io, utc_time, compression, comment
            )

            # Yield file's header and content.
            try:
                self._call(done=False, ctx=self.ctx)
                yield self._write_local_file()

                for buf in compress_io(self.ctx.compressor, self.ctx.compressor_ctx, io, self.buffer):
                    yield self._write(buf)

                yield self._write_data_descriptor()
            finally:
                self._call(done=True, ctx=self.ctx)
                self._set_header()
                self._clear_ctx()

    async def add_io_async(self, path: AnyStr, io: Union[BufferedIOBase, RawIOBase], utc_time: Optional[float] = None, compression=COMPRESSION_STORED, comment="") -> AsyncGenerator[bytes, None]:
        """Adds the io and returns async Generator of bytes object."""
        with io:
            # Create file context.
            self.ctx = self._new_file_ctx(
                path, io, utc_time, compression, comment
            )

            # Yield file's header and content.
            try:
                self._call(done=False, ctx=self.ctx)
                yield self._write_local_file()

                async for buf in compress_io_async(self.ctx.compressor, self.ctx.compressor_ctx, io, self.buffer):
                    yield self._write(buf)

                yield self._write_data_descriptor()
            finally:
                self._call(done=True, ctx=self.ctx)
                self._set_header()
                self._clear_ctx()

    def add_gen(self, path: AnyStr, gen: Generator[bytes, None, None], utc_time: Optional[float] = None, compression=COMPRESSION_STORED, comment="") -> Generator[bytes, None, None]:
        """Adds the generator and returns Generator of bytes object."""
        self.ctx = self._new_file_ctx(
            path, None, utc_time, compression, comment
        )

        # Yield file's header and content.
        try:
            self._call(done=False, ctx=self.ctx)
            yield self._write_local_file()

            for buf in compress_gen(self.ctx.compressor, self.ctx.compressor_ctx, gen):
                yield self._write(buf)

            yield self._write_data_descriptor()
        finally:
            self._call(done=True, ctx=self.ctx)
            self._set_header()
            self._clear_ctx()

    async def add_gen_async(self, path: AnyStr, gen: AsyncGenerator[bytes, None], utc_time: Optional[float] = None, compression=COMPRESSION_STORED, comment="") -> AsyncGenerator[bytes, None]:
        """Adds the async generator and returns async Generator of bytes object."""
        self.ctx = self._new_file_ctx(
            path, None, utc_time, compression, comment
        )

        # Yield file's header and content.
        try:
            self._call(done=False, ctx=self.ctx)
            yield self._write_local_file()

            async for buf in compress_gen_async(self.ctx.compressor, self.ctx.compressor_ctx, gen):
                yield self._write(buf)

            yield self._write_data_descriptor()
        finally:
            self._call(done=True, ctx=self.ctx)
            self._set_header()
            self._clear_ctx()

    async def add_stream_async(self, path: AnyStr, reader: StreamReader, utc_time: Optional[float] = None, compression=COMPRESSION_STORED, comment="", buf_size=4096) -> AsyncGenerator[bytes, None]:
        """Adds the stream and returns async Generator of bytes object."""
        # Create file context.
        self.ctx = self._new_file_ctx(
            path, None, utc_time, compression, comment
        )

        # Yield file's header and content.
        try:
            self._call(done=False, ctx=self.ctx)
            yield self._write_local_file()

            async for buf in compress_stream_async(self.ctx.compressor, self.ctx.compressor_ctx, reader, buf_size):
                yield self._write(buf)

            yield self._write_data_descriptor()
        finally:
            self._call(done=True, ctx=self.ctx)
            self._set_header()
            self._clear_ctx()

    def add_folder(self, path: AnyStr, utc_time: Optional[float] = None, comment: AnyStr = None) -> bytes:
        """Adds the folder and returns Generator of bytes object."""
        if self.ctx is not None:
            raise ValueError("File operation pending.")

        if comment is None:
            comment_bytes = b""
        elif isinstance(comment, str):
            comment_bytes = comment.encode("utf8")
        elif isinstance(comment, (bytes, bytearray,)):
            comment_bytes = comment
        else:
            raise ValueError("Comment has to be bytes or str.")

        path_bytes = norm_path(path, True)
        if path_bytes in self.headers:
            raise ValueError("Path already in headers.")

        offset = self.offset
        time, date = dos_time(utc_time)
        use_zip64 = offset >= INT32_MAX

        # LocalFile
        buf = self._write(pack_header_with_data(HEADER_LOCAL_FILE, LocalFile(
            self.version_extract,
            0,  # Flag
            0,  # Compression
            time,
            date,
            0,  # Crc32
            0,  # Compressed size
            0,  # Uncompressed size
            len(path_bytes),
            0,  # Len extra
        ), path_bytes))

        # Extended information for zip64
        extra = pack_header(TAG_EXTENDED_INFORMATION64, ExtendedInformation64(
            SIZE_EXTENDED_INFORMATION,  # Size of extended information.
            0,
            0,
            offset,
            0,  # Disk start number
        )) if use_zip64 else b""

        # CentralDirectory
        self.headers[path_bytes] = pack_header_with_data(HEADER_CENTRAL_DIRECTORY, CentralDirectory(
            self.version_extract,
            self.version_system,
            self.version_extract,
            0,  # Flag
            0,  # Compression
            time,
            date,
            0,  # Crc32
            0xFFFFFFFF if use_zip64 else 0,  # Compressed len
            0xFFFFFFFF if use_zip64 else 0,  # Uncompressed len
            len(path_bytes),
            len(extra),  # Extra len
            len(comment_bytes),
            0,  # Disks tart
            0,  # Internal attr
            DEFAULT_EXTERNAL_DIR_ATTR,  # External attr
            0xFFFFFFFF if use_zip64 else offset,
        ), path_bytes, extra, comment_bytes,)

        self._call(done=True, folderPath=path_bytes)

        return buf

    def walk(self, src: AnyStr, dest: AnyStr, utc_time: Optional[float] = None, compression=COMPRESSION_STORED, comment: AnyStr = None,
             ignore: Optional[WalkIgnoreCallable] = walk_ignore_default, no_compress: Optional[WalkNoCompressCallable] = walk_no_compress_default) -> Generator[bytes, None, None]:
        """Generates the file headers and contents from src directory."""
        src_abs = abspath(src)

        for folder_abs, _, files in walk(src_abs, followlinks=False):
            # Relative path
            rel_path = relpath(folder_abs, src_abs)

            # Create Folder
            if len(files) == 0:
                # On ignore skip
                if ignore is not None and ignore(folder_abs, "", True, stat(folder_abs)):
                    continue

                # Add folder
                dest_path = join(dest, rel_path)
                yield self.add_folder(dest_path, utc_time)

                # Goto next
                continue

            # Write Files
            for file in files:
                # Absolute
                file_abs = join(folder_abs, file)

                # File extension
                ext = splitext(file_abs)[1].lower()
                file_stat = stat(file_abs)

                # On ignore skip
                if ignore is not None and ignore(file_abs, ext, False, file_stat):
                    continue

                # Check if file needs to be compressed
                file_compression = (
                    COMPRESSION_STORED
                    if no_compress is not None and no_compress(file_abs, ext, file_stat) else
                    compression
                )

                # Open file
                fs = cast(RawIOBase, open(file_abs, "rb", buffering=False))

                # Yield file contents
                dest_path = join(dest, rel_path, file)
                for buf in self.add_io(dest_path, fs, utc_time, file_compression):
                    yield buf

    async def walk_async(self, src: AnyStr, dest: AnyStr, utc_time: Optional[float] = None, compression=COMPRESSION_STORED, comment: AnyStr = None,
                         ignore: Optional[WalkIgnoreCallable] = walk_ignore_default, no_compress: Optional[WalkNoCompressCallable] = walk_no_compress_default) -> AsyncGenerator[bytes, None]:
        """Generates the file headers and contents from src directory asyncnorously."""
        src_abs = abspath(src)

        for folder_abs, _, files in walk(src_abs, followlinks=False):
            # Relative path
            rel_path = relpath(folder_abs, src_abs)

            # Create Folder
            if len(files) == 0:
                # On ignore skip
                if ignore is not None and ignore(folder_abs, "", True, stat(folder_abs)):
                    continue

                # Add folder
                dest_path = join(dest, rel_path)
                yield self.add_folder(dest_path, utc_time)

                # Goto next
                continue

            # Write Files
            for file in files:
                # Absolute
                file_abs = join(folder_abs, file)

                # File extension
                ext = splitext(file_abs)[1].lower()
                file_stat = stat(file_abs)

                # On ignore skip
                if ignore is not None and ignore(file_abs, ext, False, file_stat):
                    continue

                # Check if file needs to be compressed
                file_compression = (
                    COMPRESSION_STORED
                    if no_compress is not None and no_compress(file_abs, ext, file_stat) else
                    compression
                )

                # Open file
                fs = cast(RawIOBase, open(file_abs, "rb", buffering=False))

                # Yield file contents
                dest_path = join(dest, rel_path, file)
                async for buf in self.add_io_async(dest_path, fs, utc_time, file_compression):
                    yield buf

    def end(self, comment: AnyStr = None) -> bytes:
        """Returns EOCD bytes which contains headers for all added files."""
        if comment is None:
            comment_bytes = b""
        elif isinstance(comment, str):
            comment_bytes = comment.encode("utf8")
        elif isinstance(comment, (bytes, bytearray,)):
            comment_bytes = comment
        else:
            raise ValueError("Comment has to be bytes, bytearray or str.")

        return self._write_end(comment_bytes)
