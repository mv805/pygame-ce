from typing import Any, Tuple, Callable

__version__: str

class error(RuntimeError): ...
class BufferError(Exception): ...
class PygameDebugWarning(Warning): ...

# Always defined
HAVE_NEWBUF: int = 1

def init() -> Tuple[int, int]: ...
def quit() -> None: ...
def get_init() -> bool: ...
def get_error() -> str: ...
def set_error(error_msg: str, /) -> None: ...
def get_sdl_version(linked: bool = True) -> Tuple[int, int, int]: ...
def get_sdl_byteorder() -> int: ...
def register_quit(callable: Callable[[], Any], /) -> None: ...

# undocumented part of pygame API, kept here to make stubtest happy
def get_array_interface(arg: Any, /) -> dict: ...
