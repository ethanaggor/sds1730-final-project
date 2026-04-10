# GEPA Run 2: Constrained Teacher (Flash Looping)

**Run ID:** `2026-04-07T21-06-58`
**Label:** `constrained-teacher-flash-loops`
**Status:** Killed manually after ~2h 48m. Zero mutations accepted.

## Configuration

| Parameter | Value |
|-----------|-------|
| Student model | gemini/gemini-3-flash-preview (reasoning: high) |
| Teacher model | gemini/gemini-3.1-pro-preview (reasoning: high) |
| Sub model | gemini/gemini-3-flash-preview (reasoning: high) |
| GEPA auto | light (6 candidates, ~850 metric calls) |
| Reflection template | Custom constrained (no answer embedding) |
| Instruction proposer | Custom ProposalFn wrapping InstructionProposalSignature |
| Valset | 20 cross-validation splits, 11 held-out states each |
| Metric | score = max(0, 1 - RMSE/20) |
| Two-phase compile | Phase 1: baseline only (20 evals), Phase 2: constrained optimization |

Changes from Run 1: added a custom reflection template (`prompts/GEPA_reflection_template.md`) that forbids the teacher from embedding actual data values in mutated instructions. Added two-phase compilation with baseline checkpoint preservation.

## Cost

| Role | Cost | Calls | Input tokens | Output tokens |
|------|------|-------|--------------|---------------|
| Student | $31.27 | 2,383 | 39,938,896 | 7,534,039 |
| Teacher | $0.70 | 3 | 257,524 | 15,388 |
| Sub | $0.00 | 0 | 0 | 0 |
| **Total** | **$31.96** | **2,386** | **40,196,420** | **7,549,427** |

Duration: 2 hours 48 minutes. Killed at 165/~850 evals (19% of budget).

The student cost was 7.5x Run 1 despite fewer evals because the looping problem caused most evals to run all 20 RLM iterations (vs 1 iteration in the reward-hacked run). Each iteration incurs a full LM call with the entire trajectory in context.

## Results

| Phase | Evals | Mean score | Mean RMSE |
|-------|-------|------------|-----------|
| Baseline (Phase 1) | 20 | 0.679 | 6.42 |
| Mutations (Phase 2) | 145 | 0.680 | 6.40 |
| Best-per-split (cherry-picked)* | 20 | 0.783 | 4.33 |

*Best-per-split is cherry-picked from a Pareto frontier: for each of the 20 splits, we select the single best-scoring eval across all candidates and iterations. This is not a realistic estimator of prompt quality; it represents the upper bound of what any eval in the run achieved on each split, regardless of which candidate produced it.

**Zero mutations accepted by GEPA.** The single surviving candidate is the unmodified seed prompt. The teacher proposed 3 mutations; none passed GEPA's full-validation acceptance test.

## Comparison to Other Methods

| Method | Mean RMSE | Notes |
|--------|-----------|-------|
| OLS Regression | 8.88 | 20-split CV, statsmodels |
| Predict (no tools) | 5.80 | 20-split CV, Gemini 3 Flash, pure inference |
| RLM unoptimized (notebook) | 5.33 | Split 0 only, Gemini 3 Flash |
| GEPA Baseline (this run) | 6.42 | 20-split CV, Gemini 3 Flash + REPL |
| GEPA best-per-split* | 4.33 | Cherry-picked from Pareto frontier, not a realistic estimator |

The GEPA baseline (6.42) is worse than the notebook's Predict baseline (5.80), despite having access to a Python REPL. The REPL should help, but the looping problem negates the advantage.

## Finding 1: Gemini 3 Flash loops catastrophically

**72% of evals (118/165) exhibit output looping.** The model produces good predictions by iteration 5-7, then repeats the same code with cosmetic variable name changes for the remaining iterations.

| Metric | Value |
|--------|-------|
| Evals with looping | 118/165 (72%) |
| Evals hitting 20-iteration cap | 78/165 (47%) |
| Total wasted iterations | 542/2,366 (23%) |
| Evals that never call SUBMIT | 75/165 (45%) |
| Max-iter evals that loop | 95% |

The loop pattern: the model computes predictions, assigns them to a variable like `analytical_forecast`, prints the results, then in the next iteration renames it to `final_analytical_map` and prints again. The numerical values are identical. The reasoning text claims "I have completed the analysis" or "The final phase involves consolidating..." in nearly every looping step.

**Root cause: a bug in our `local_interpreter.py`.** DSPy's RLM prompt template teaches the model to call `SUBMIT(predictions)` as a positional argument, matching the convention of DSPy's default `PythonInterpreter` which generates `def SUBMIT(predictions):`. Our `LocalInterpreter` instead defined `def SUBMIT(**kwargs):` (keyword-only), so every `SUBMIT(predictions)` call failed with "takes 0 positional arguments but 1 was given." The model had no way to know the correct syntax was `SUBMIT(predictions=value)`.

This explains both looping populations:

- **75 of 76 max-iteration evals never attempt SUBMIT.** After seeing (or learning from trajectory context that) `SUBMIT(predictions)` fails, the model falls back to printing predictions to stdout and looping until the iteration cap.
- **1 eval (the top scorer at 0.909) fights SUBMIT for 14 iterations,** alternating between `SUBMIT(predictions)` (positional, rejected) and `SUBMIT()` (no args, rejected for missing fields), never discovering the keyword-arg workaround.

The bug was in `_make_submit()`: it ignored the `output_fields` list that RLM injects (e.g. `[{"name": "predictions"}]`) and always created a kwargs-only function. DSPy's default interpreter uses `output_fields` to generate a positional-arg SUBMIT matching the prompt. **Fixed post-run** by making `_make_submit` generate `def SUBMIT(predictions):` when `output_fields` is provided.

Early-stop evals (< 20 iterations) waste < 1 iteration on average and score comparably (0.688 vs 0.672). The difference is that they successfully call SUBMIT.

## Finding 2: The prompt is not the bottleneck

Looping evals and non-looping evals score nearly identically (0.683 vs 0.675, r = -0.018 between loop rate and score). The analytical quality of the model's reasoning is comparable across prompt variants. What varies is:

1. **Whether the agent calls `llm_query`:** Evals using `llm_query` for domain context score 0.705 vs 0.658 without. Every top-10 eval used it.
2. **Whether the agent submits:** 55% of evals produce a SUBMIT/FINAL output. The rest compute good predictions but fail to terminate.
3. **Split difficulty:** Per-split mean scores range from 0.456 (split 15) to 0.802 (split 9), driven by which states are held out.

None of these factors are addressable by prompt-level optimization. The prompt already describes the right analytical approach. GEPA's teacher can rephrase the strategy description, but it cannot fix the model's inability to use the SUBMIT API or its stochastic decision to call `llm_query`.

## Finding 3: Strategy taxonomy

Analysis of all 165 trajectories reveals consistent patterns in what works and what doesn't:

**Winning strategy (all top-10 evals):** KNN with feature normalization + `llm_query` for historical domain context + manual adjustment for known extreme states (Sand States, Rust Belt). Completed in 6-9 iterations.

**Losing strategy (bottom-10 evals):** Rigid archetype classification ("Sand State," "Rust Belt," "Commodity Shield") with hardcoded multipliers. Too coarse; states that straddle archetypes get systematically mispredicted. Mean score ~0.45-0.50.

**The best single eval** (split 2, score 0.909, RMSE 1.82): Computed correlations, built weighted KNN (k=3), called `llm_query` for qualitative state-level context, then synthesized. However, it spent 14 of 20 iterations fighting SUBMIT errors, meaning the actual analytical work took 6 iterations.

## Finding 4: GEPA cannot converge

GEPA requires a mutation to beat the current best candidate across the full validation set (all 20 splits) to accept it. With high within-split variance (same prompt, same split produces scores from 0.52 to 0.91), a prompt mutation that helps on some splits hurts on others purely due to reasoning stochasticity. The acceptance test is comparing signal (prompt quality) against noise (reasoning variance), and the noise dominates.

The teacher produced only 3 mutation proposals in 2h 48m. This is expected: GEPA evaluates candidates on minibatches first, and when minibatch performance doesn't clearly improve, it skips the full validation step and moves to the next iteration. The constrained teacher's mutations were stylistic rewrites that didn't change the analytical strategy.

## Takeaways

1. **The SUBMIT bug invalidates this run's conclusions about model capability.** The looping, the 45% submission failure rate, and the 23% iteration waste were caused by our `LocalInterpreter` rejecting valid SUBMIT calls, not by Gemini 3 Flash being too weak. The model was calling SUBMIT correctly per DSPy's prompt; our interpreter rejected the calls. Scores, convergence behavior, and cost are all artifacts of this bug.

2. **GEPA convergence failure is a downstream consequence.** With nearly half of evals failing to submit and most evals burning iterations on a broken API, the score signal was dominated by whether the harness happened to extract predictions from stdout rather than from SUBMIT. GEPA's acceptance test was comparing noise, not prompt quality. Whether GEPA can converge on this task remains an open question for a run with the fixed interpreter.

3. **The constrained teacher works as intended.** It blocked reward hacking. Whether the legitimate strategy space is wide enough for GEPA to find improvements is untested, since this run never gave the teacher clean signal to work with.

4. **The task is solvable.** Best-per-split RMSE of 4.33 (vs OLS at 8.88) shows the ceiling is high even with the SUBMIT bug, since the harness extracted predictions from stdout for some evals. With the fix, consistent SUBMIT success should reduce variance and give GEPA clean signal.

5. **Cost was inflated ~3-4x by the bug.** $31.96 for 165 evals. Each looping eval ran 20 LM calls when 6-7 would suffice. With the SUBMIT fix, evals should terminate in 6-9 iterations (matching the early-stop evals that accidentally discovered the keyword-arg workaround), cutting per-eval cost substantially.
