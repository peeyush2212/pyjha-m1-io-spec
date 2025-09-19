# pyjha package initializer

__version__ = "0.1.1"

from typing import Any as _Any
import importlib as _importlib
import importlib.util as _spec

# Build __all__ dynamically (don't expose 'models' unless it exists)
__all__ = ["__version__", "pd"]
if _spec.find_spec(__name__ + ".models") is not None:
    __all__.append("models")

def __getattr__(name: str) -> _Any:
    # Lazy pandas alias: pyjha.pd  /  from pyjha import pd
    if name == "pd":
        import pandas as _pd
        return _pd
    # Lazy submodule import: pyjha.models (only if it actually exists)
    if name == "models":
        mod = _spec.find_spec(__name__ + ".models")
        if mod is None:
            raise AttributeError("pyjha has no submodule 'models'")
        return _importlib.import_module(".models", __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

# Hints for type checkers (no runtime cost)
from typing import TYPE_CHECKING as _TYPE_CHECKING  # noqa: E402
if _TYPE_CHECKING:  # pragma: no cover
    import pandas as pd  # noqa: F401
    # 'models' may or may not exist
