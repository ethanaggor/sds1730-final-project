import copy
import io
import re
import threading
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

_LOOP_THRESHOLD = 3
_LOOP_WARNING = (
    "\nWARNING: You have produced identical output 3 times in a row. "
    "Try a different analytical approach or call SUBMIT with your current best predictions."
)


class _SubmitSignal(Exception):
    def __init__(self, fields):
        self.fields = fields


class LocalInterpreter:
    def __init__(self):
        self._base: dict[str, Any] = {"np": np, "pd": pd, "__builtins__": __builtins__}
        self._tls = threading.local()
        self.tools: dict[str, Callable[..., str]] = {}
        self.output_fields: list[dict] | None = None

    @property
    def namespace(self) -> dict[str, Any]:
        if not hasattr(self._tls, "ns"):
            self._tls.ns = dict(self._base)
        return self._tls.ns

    @namespace.setter
    def namespace(self, value: dict[str, Any]):
        self._tls.ns = value

    @property
    def _recent_outputs(self) -> list[str]:
        if not hasattr(self._tls, "recent_outputs"):
            self._tls.recent_outputs = []
        return self._tls.recent_outputs

    def __deepcopy__(self, memo):
        return LocalInterpreter()

    def start(self) -> None:
        pass

    def execute(self, code: str, variables: dict[str, Any] | None = None) -> Any:
        ns = self.namespace
        if variables:
            ns.update(copy.deepcopy(variables))

        ns.update(self.tools)
        ns["SUBMIT"] = _make_submit(self.output_fields)

        for pattern in BANNED_PATTERNS:
            match = re.search(pattern, code)
            if match:
                raise CodeInterpreterError(
                    f"Banned method: {match.group()}. Only numpy and pandas are available."
                )

        buf = io.StringIO()
        ns["print"] = lambda *args, **kwargs: print(*args, file=buf, **kwargs)
        try:
            exec(code, ns)
            output = buf.getvalue()
        except _SubmitSignal as s:
            return FinalOutput(s.fields)
        except SyntaxError:
            raise
        except Exception as e:
            raise CodeInterpreterError(str(e)) from e

        history = self._recent_outputs
        history.append(output)
        if len(history) > _LOOP_THRESHOLD:
            history.pop(0)
        if len(history) >= _LOOP_THRESHOLD and len(set(history)) == 1:
            output += _LOOP_WARNING

        return output

    def shutdown(self):
        self.namespace = dict(self._base)
        self._tls.recent_outputs = []
        self.tools.clear()


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
