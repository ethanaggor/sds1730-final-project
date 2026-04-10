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

_PREDICTION_KEY_ALIASES = {
    "pred_crash_pct": "predicted_crash_pct",
    "crash_pct": "predicted_crash_pct",
    "prediction": "predicted_crash_pct",
    "predicted": "predicted_crash_pct",
    "pct": "predicted_crash_pct",
    "pred": "predicted_crash_pct",
}

_FLOAT_RE = re.compile(r"-?\d+\.\d+")


def _coerce_predictions(value):
    """Coerce common prediction formats to list[dict] for Pydantic validation."""
    if isinstance(value, pd.DataFrame):
        value = value.to_dict("records")

    if isinstance(value, dict) and all(isinstance(v, (int, float)) for v in value.values()):
        value = [{"state": k, "predicted_crash_pct": float(v)} for k, v in value.items()]

    if isinstance(value, list) and value and hasattr(value[0], "__dict__") and not isinstance(value[0], dict):
        value = [
            {k: v for k, v in (item.model_dump() if hasattr(item, "model_dump") else item.__dict__).items()}
            for item in value
        ]

    if isinstance(value, list):
        normalized = []
        for item in value:
            if isinstance(item, dict):
                row = {}
                for k, v in item.items():
                    canonical = _PREDICTION_KEY_ALIASES.get(k, k)
                    row[canonical] = v
                if "predicted_crash_pct" in row:
                    try:
                        row["predicted_crash_pct"] = float(row["predicted_crash_pct"])
                    except (ValueError, TypeError):
                        pass
                normalized.append(row)
            else:
                normalized.append(item)
        value = normalized

    return value


def _extract_float_fingerprint(text: str) -> tuple[float, ...] | None:
    """Extract sorted rounded floats from text as a hashable fingerprint."""
    matches = _FLOAT_RE.findall(text)
    if len(matches) < 3:
        return None
    return tuple(sorted(round(float(m), 1) for m in matches))


def _build_submit_hint(ns: dict) -> str | None:
    """Scan interpreter namespace for prediction data and build SUBMIT call."""
    for var_name, val in ns.items():
        if var_name.startswith("_") or var_name in ("np", "pd", "print", "SUBMIT", "__builtins__"):
            continue

        records = None

        if isinstance(val, pd.DataFrame) and len(val) >= 5:
            cols = set(val.columns)
            state_col = next((c for c in cols if c.lower() == "state"), None)
            pred_col = next((c for c in cols if "crash" in c.lower() or "pred" in c.lower()), None)
            if state_col and pred_col:
                records = [
                    {"state": str(row[state_col]), "predicted_crash_pct": float(row[pred_col])}
                    for _, row in val.iterrows()
                ]

        if records is None and isinstance(val, dict) and len(val) >= 5:
            if all(isinstance(k, str) and len(k) == 2 and isinstance(v, (int, float)) for k, v in val.items()):
                records = [{"state": k, "predicted_crash_pct": float(v)} for k, v in val.items()]

        if records is None and isinstance(val, list) and len(val) >= 5 and isinstance(val[0], dict):
            if "state" in val[0]:
                pred_key = next((k for k in val[0] if "crash" in k.lower() or "pred" in k.lower()), None)
                if pred_key:
                    records = [
                        {"state": str(r["state"]), "predicted_crash_pct": float(r[pred_key])}
                        for r in val
                    ]

        if records and len(records) >= 5:
            entries = ", ".join(
                f'{{"state": "{r["state"]}", "predicted_crash_pct": {r["predicted_crash_pct"]:.4f}}}'
                for r in records
            )
            return (
                f"\n\nYou have been repeating the same predictions. "
                f"Your data is ready. Run this code exactly:\n\n"
                f"SUBMIT(predictions=[{entries}])"
            )

    return None


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
    def _float_fingerprints(self) -> list[tuple[float, ...] | None]:
        if not hasattr(self._tls, "float_fingerprints"):
            self._tls.float_fingerprints = []
        return self._tls.float_fingerprints

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
            fields = s.fields
            if "predictions" in fields:
                fields["predictions"] = _coerce_predictions(fields["predictions"])
            return FinalOutput(fields)
        except SyntaxError:
            raise
        except Exception as e:
            raise CodeInterpreterError(str(e)) from e

        fp = _extract_float_fingerprint(output)
        history = self._float_fingerprints
        history.append(fp)
        if len(history) > _LOOP_THRESHOLD:
            history.pop(0)
        if (
            fp is not None
            and len(history) >= _LOOP_THRESHOLD
            and all(h == fp for h in history)
        ):
            hint = _build_submit_hint(ns)
            if hint:
                output += hint

        return output

    def shutdown(self):
        self.namespace = dict(self._base)
        self._tls.float_fingerprints = []
        self.tools.clear()


def _make_submit(output_fields=None):
    if output_fields:
        names = [f["name"] for f in output_fields]
        code = f"def SUBMIT({', '.join(names)}):\n    raise _SubmitSignal({{{', '.join(f'\"{n}\": {n}' for n in names)}}})"
        ns = {"_SubmitSignal": _SubmitSignal}
        exec(code, ns)
        return ns["SUBMIT"]
    def SUBMIT(**kwargs):
        raise _SubmitSignal(kwargs)
    return SUBMIT
