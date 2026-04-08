"""Local Python interpreter implementing the CodeInterpreter protocol for RLM."""

import copy
import io
import re
from typing import Any, Callable

import numpy as np
import pandas as pd

from dspy.primitives.code_interpreter import CodeInterpreterError, FinalOutput

BANNED_PATTERNS = [
    r"import\s+statsmodels",
    r"from\s+statsmodels",
    r"import\s+sklearn",
    r"from\s+sklearn",
    r"from\s+scipy\.optimize",
    r"from\s+scipy\.stats\s+import\s+linregress",
    r"np\.polyfit",
    r"np\.linalg\.lstsq",
]


class _SubmitSignal(Exception):
    def __init__(self, fields):
        self.fields = fields


class LocalInterpreter:
    """Python interpreter with numpy/pandas, banned-method enforcement, and SUBMIT support."""

    def __init__(self):
        self._base: dict[str, Any] = {"np": np, "pd": pd, "__builtins__": __builtins__}
        self.namespace: dict[str, Any] = dict(self._base)
        self.tools: dict[str, Callable[..., str]] = {}
        self.output_fields: list[dict] | None = None
        self._tools_registered: bool = False

    def __deepcopy__(self, memo):
        return LocalInterpreter()

    def start(self) -> None:
        pass

    def execute(self, code: str, variables: dict[str, Any] | None = None) -> Any:
        if variables:
            self.namespace.update(variables)

        self.namespace.update(self.tools)
        self.namespace["SUBMIT"] = _make_submit(self.output_fields)

        for pattern in BANNED_PATTERNS:
            match = re.search(pattern, code)
            if match:
                raise CodeInterpreterError(
                    f"Banned method: {match.group()}. Only numpy and pandas are available."
                )

        buf = io.StringIO()
        self.namespace["print"] = lambda *args, **kwargs: print(*args, file=buf, **kwargs)
        try:
            exec(code, self.namespace)
            return buf.getvalue()
        except _SubmitSignal as s:
            return FinalOutput(s.fields)
        except SyntaxError:
            raise
        except Exception as e:
            raise CodeInterpreterError(str(e)) from e

    def shutdown(self):
        self.namespace = dict(self._base)
        self.tools.clear()
        self._tools_registered = False


def _make_submit(output_fields=None):
    if output_fields:
        names = [f["name"] for f in output_fields]
        # Build positional-arg SUBMIT matching DSPy's default convention
        code = f"def SUBMIT({', '.join(names)}):\n    raise _SubmitSignal({{{', '.join(f'\"{n}\": {n}' for n in names)}}})"
        ns = {"_SubmitSignal": _SubmitSignal}
        exec(code, ns)
        return ns["SUBMIT"]
    def SUBMIT(**kwargs):
        raise _SubmitSignal(kwargs)
    return SUBMIT
