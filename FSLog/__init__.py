__version__ = "0.1.2"

from typing import Tuple
from .fslog import FSLog, Colors, create_logger

_default_logger = FSLog()

__all__: Tuple[str, ...] = (
    "Colors",
    "create_logger",
    "server",
    "logging",
    "error",
    "warning",
    "info",
    "debug",
    "custom",
    "log",
    "lib_debug",
    "logging_stats",
)

server = _default_logger.server
logging = _default_logger.logging
error = _default_logger.error
warning = _default_logger.warning
info = _default_logger.info
debug = _default_logger.debug
custom = _default_logger.custom
log = _default_logger.log
lib_debug = _default_logger.lib_debug
logging_stats = _default_logger.logging_stats

def __dir__() -> Tuple[str, ...]:
    return __all__ + ("__version__", "__doc__")

def __getattr__(name: str) -> object:
    if name not in __all__:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return globals()[name]