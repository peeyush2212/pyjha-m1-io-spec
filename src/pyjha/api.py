from .io import use
from .spec.parser import parse_spec
from dataclasses import dataclass
from typing import Any, Iterable, Optional


__all__ = ["use", "parse_spec", "run"]




@dataclass
class RunResult:
    ok: bool
    y: Optional[str]
    X: list[str]
    n: Optional[int]

def run(*, y: Optional[str] = None, X: Optional[Iterable[str]] = None, data: Any = None, **kwargs) -> RunResult:
    """Lightweight placeholder so tests can import `run` now.
    Returns only simple metadata; real modeling comes in m3/m4."""
    n = None
    try:
        # pandas / numpy DataFrame/array friendly check
        if hasattr(data, "shape") and len(getattr(data, "shape")) > 0:
            n = int(data.shape[0])
    except Exception:
        pass
    return RunResult(ok=True, y=y, X=list(X or []), n=n)