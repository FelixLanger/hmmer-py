from importlib import import_module as _import_module

from . import typing
from ._example import example_filepath
from ._testit import test
from .domtbl import read_domtbl
from .hmmer import HMMER
from .tbl import read_tbl

try:
    __version__ = getattr(_import_module("hmmer._version"), "version", "x.x.x")
except ModuleNotFoundError:
    __version__ = "x.x.x"

__all__ = [
    "HMMER",
    "__version__",
    "example_filepath",
    "read_domtbl",
    "read_tbl",
    "test",
    "typing",
]
