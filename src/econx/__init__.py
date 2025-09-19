# Back-compat shim: econx -> pyjha
import warnings as _w
import pyjha as _pyjha
from pyjha import __version__  


pd = _pyjha.pd 

# Forward 'models' only if pyjha actually has it
try:
    from pyjha import models  # noqa: F401
except Exception:
    pass

_w.warn(
    "Package 'econx' is deprecated; use 'pyjha' instead. "
    "For now, 'econx' forwards to 'pyjha'.",
    DeprecationWarning,
    stacklevel=2,
)
