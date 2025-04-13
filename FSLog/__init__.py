__version__ = "0.1.0" 

from typing import Tuple

from .fslog import (FSLog, Colors, create_logger)

__all__: Tuple[str, ...] = ("FSLog", "Colors", "create_logger",)

def __dir__() -> Tuple[str, ...]:
    return __all__ + ("__version__", "__doc__")

def __getattr__(name: str) -> object:
    if name not in __all__:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return globals()[name]