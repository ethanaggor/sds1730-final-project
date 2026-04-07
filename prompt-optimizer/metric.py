import numpy as np

from signatures import STATE_NAMES

_event_log = None


def set_event_log(log):
    global _event_log
    _event_log = log


def _extract_instruction(pred_trace):
    """Extract candidate instruction text from GEPA's pred_trace."""
    if not pred_trace:
        return None
    try:
        predictor = pred_trace[0][0]
        sig = predictor.signature
        return getattr(sig, "instructions", None)
    except Exception:
        return None


def crash_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """GEPA-compatible metric returning ScoreWithFeedback."""
    from dspy.teleprompt.gepa.gepa_utils import ScoreWithFeedback

    actual = np.array(gold.actual_values)
    test_states = gold.test_states

    try:
        preds_dict = {p.state: p.predicted_crash_pct for p in pred.predictions}
    except Exception:
        return ScoreWithFeedback(score=0.0, feedback="Failed to parse predictions")

    pred_values = np.array([preds_dict.get(st, np.nan) for st in test_states])
    valid = ~np.isnan(pred_values)
    if not valid.any():
        return ScoreWithFeedback(score=0.0, feedback="No valid predictions")

    rmse = float(np.sqrt(np.nanmean((actual - pred_values) ** 2)))
    score = 1.0 / (1.0 + rmse)

    per_state = []
    for st, a in zip(test_states, actual):
        p = preds_dict.get(st, float("nan"))
        per_state.append(f"{STATE_NAMES[st]} ({st}): predicted {p:.1f}, actual {a:.1f}, error {p - a:+.1f}")
    feedback = f"RMSE: {rmse:.2f}\n" + "\n".join(per_state)

    if _event_log is not None:
        trajectory = getattr(pred, "trajectory", [])
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
