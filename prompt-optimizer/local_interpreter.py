"""Local Python interpreter implementing the CodeInterpreter protocol for RLM."""

import io
import re
import sys
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

    def start(self) -> None:
        pass

    def execute(self, code: str, variables: dict[str, Any] | None = None) -> Any:
        if variables:
            self.namespace.update(variables)

        self.namespace.update(self.tools)
        self.namespace["SUBMIT"] = _make_submit()

        for pattern in BANNED_PATTERNS:
            match = re.search(pattern, code)
            if match:
                raise CodeInterpreterError(
                    f"Banned method: {match.group()}. Only numpy and pandas are available."
                )

        old_stdout = sys.stdout
        sys.stdout = buf = io.StringIO()
        try:
            exec(code, self.namespace)
            return buf.getvalue()
        except _SubmitSignal as s:
            return FinalOutput(s.fields)
        except SyntaxError:
            raise
        except Exception as e:
            raise CodeInterpreterError(str(e)) from e
        finally:
            sys.stdout = old_stdout

    def shutdown(self):
        self.namespace = dict(self._base)
        self.tools.clear()
        self._tools_registered = False


def _make_submit():
    def SUBMIT(**kwargs):
        raise _SubmitSignal(kwargs)
    return SUBMIT
