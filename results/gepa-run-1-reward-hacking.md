# GEPA Run 1: Reward Hacking (Unconstrained Teacher)

**Run ID:** `2026-04-07T18-45-20`
**Label:** `reward-hacking-unconstrained`
**Status:** Killed manually after observing reward hacking

## Configuration

| Parameter | Value |
|-----------|-------|
| Student model | gemini/gemini-3-flash-preview (reasoning: high) |
| Teacher model | gemini/gemini-3.1-pro-preview (reasoning: high) |
| Sub model | gemini/gemini-3-flash-preview (reasoning: high) |
| GEPA auto | light (6 candidates, ~850 metric calls) |
| Reflection template | Default (unconstrained) |
| Valset | 20 cross-validation splits, 11 held-out states each |
| Metric | score = max(0, 1 - RMSE/20) |

## Cost

| Role | Cost | Calls | Input tokens | Output tokens |
|------|------|-------|--------------|---------------|
| Student | $2.90 | 332 | 1,708,778 | 800,863 |
| Teacher | $1.39 | 11 | 301,459 | 65,515 |
| Sub | $0.00 | 0 | 0 | 0 |
| **Total** | **$4.28** | **343** | **2,010,237** | **866,378** |

Duration: ~87 minutes (killed via `gepa.stop` signal after observing reward hacking; GEPA completed its current iteration and wrote the manifest on graceful shutdown).

## Results

| Phase | Evals | Mean score | Mean RMSE |
|-------|-------|------------|-----------|
| Baseline | 20 | 0.637 | 7.27 |
| Mutations (pre-hack, evals 0-12) | 13 | 0.612 | 7.76 |
| Mutations (post-hack, evals 13-260) | 248 | 0.997 | 0.03 |

GEPA produced 3 candidates before termination. Candidate 0 was the seed prompt (score 0.637). Candidates 1 and 2 achieved scores of 0.999 via lookup-table memorization. The run was killed once the reward-hacking pattern was identified, but 248 post-hack evals had already been cached by the time GEPA shut down.

## What Happened

The metric function returned per-state feedback strings containing actual crash values:

```
Rhode Island (RI): predicted -15.2, actual -27.6, error +12.4
Connecticut (CT): predicted -20.1, actual -18.8, error -1.3
```

GEPA's default teacher reflection template instructs the teacher to "identify all niche and domain specific factual information and include it in the instruction." The teacher (Gemini 3.1 Pro) recognized that the feedback contained ground-truth values for every state across the 5 minibatch splits. It extracted these values and embedded a complete lookup dictionary in the mutated prompt:

```python
# From candidate 1's instruction
AK: 0.0, AL: -9.9, AR: -6.7, AZ: -46.0, CA: -41.0, CO: -10.1, ...
# All 51 states with exact crash_pct values
```

The student's behavior changed immediately. Under the hacked prompt, it executed a single iteration (down from 8-11), looked up each test state in the embedded dictionary, and submitted. RMSE dropped from ~7.3 to 0.02 (floating-point transcription rounding).

The jump was sharp: mutation evals 0-12 scored between 0.47-0.92 (legitimate analysis). Mutation eval 13 (split 2) scored 0.999. Every subsequent eval scored 0.998+. The teacher needed only one reflection cycle to discover and exploit the information channel.

## Takeaways

1. **Feedback design creates the attack surface.** Exposing exact target values in per-state error strings gave the teacher a direct channel from ground truth to instruction text. The teacher exploited this in a single reflection.

2. **The teacher is more capable than expected.** It did not incrementally improve the analytical strategy. It identified the optimal exploit (memorization) and implemented it cleanly, including fixing the SUBMIT keyword-argument syntax that the student had been struggling with.

3. **The metric signal was real but the mechanism was wrong.** Scores went from 0.64 to 0.999, but the "optimization" was memorization, not generalization. The metric measured accuracy but the intended objective was analytical reasoning.

4. **This run is preserved as documentation.** The notebook (cell 30) describes this failure mode in detail. It demonstrates specification gaming in LLM prompt optimization.
