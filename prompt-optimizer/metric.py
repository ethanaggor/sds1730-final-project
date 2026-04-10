import numpy as np

from signatures import STATE_NAMES

_event_log = None


def set_event_log(log):
    global _event_log
    _event_log = log


def _extract_instruction(pred_trace):
    if not pred_trace:
        return None
    try:
        predictor = pred_trace[0][0]
        sig = predictor.signature
        return getattr(sig, "instructions", None)
    except Exception:
        return None


def crash_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    from dspy.teleprompt.gepa.gepa_utils import ScoreWithFeedback

    actual = np.array(gold.actual_values)
    test_states = gold.test_states

    try:
        preds_dict = {p.state: p.predicted_crash_pct for p in pred.predictions}
    except Exception:
        return ScoreWithFeedback(score=0.0, feedback="Failed to parse predictions")

    pred_values = np.array([preds_dict.get(st, np.nan) for st in test_states])
    valid = ~np.isnan(pred_values)
    if not valid.all():
        missing = [st for st, v in zip(test_states, valid) if not v]
        return ScoreWithFeedback(score=0.0, feedback=f"Missing predictions for: {', '.join(missing)}")

    rmse = float(np.sqrt(np.nanmean((actual - pred_values) ** 2)))
    score = max(0.0, 1.0 - rmse / 20.0)

    per_state = []
    for st, a in zip(test_states, actual):
        p = preds_dict.get(st, float("nan"))
        per_state.append(f"{STATE_NAMES[st]} ({st}): predicted {p:.1f}, actual {a:.1f}, error {p - a:+.1f}")

    trajectory = getattr(pred, "trajectory", [])
    final_reasoning = getattr(pred, "final_reasoning", "")

    parts = [f"RMSE: {rmse:.2f}\n"]
    if trajectory:
        parts.append("## Agent Trajectory\n")
        for i, t in enumerate(trajectory):
            parts.append(f"### Iteration {i + 1}")
            r = t.get("reasoning", "")
            if r:
                parts.append(f"Reasoning: {r[:3000]}")
            c = t.get("code", "")
            if c:
                parts.append(f"Code:\n{c[:3000]}")
            o = t.get("output", "")
            if o:
                parts.append(f"Output:\n{o[:2000]}")
            parts.append("")
    if final_reasoning:
        parts.append(f"## Final Reasoning\n{final_reasoning[:3000]}\n")
    parts.append("## Optimization Constraints")
    parts.append(
        "When improving the prompt, do NOT copy specific crash_pct values, "
        "state-specific results, verbatim phrases, or lookup tables from these examples. "
        "Generalize to analytical rules that apply broadly."
    )
    parts.append(
        "You must NOT change the output format, SUBMIT mechanics, or REPL interaction pattern. "
        "Only improve the analytical reasoning strategy."
    )
    parts.append("## Per-State Results")
    parts.extend(per_state)
    feedback = "\n".join(parts)

    if _event_log is not None:
        event = {
            "type": "eval",
            "split": getattr(gold, "split_idx", None),
            "rmse": rmse,
            "score": score,
            "n_iterations": len(trajectory),
            "trajectory": [
                {
                    "reasoning": t.get("reasoning", "")[:3000],
                    "code": t.get("code", "")[:3000],
                    "output": t.get("output", "")[:2000],
                }
                for t in trajectory
            ],
        }
        instruction = _extract_instruction(pred_trace)
        if instruction:
            event["instruction_preview"] = instruction[:2000]
            event["pred_name"] = pred_name
        _event_log.emit(event)

    return ScoreWithFeedback(score=score, feedback=feedback)
