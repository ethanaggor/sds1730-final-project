# What Predicted the 2008 Housing Crash?

State-level regression analysis of the 2008 housing crisis. We use FRED economic data (house price index, unemployment, income, population) for all 50 states plus DC to test whether the crash was purely a bubble deflation or whether pre-crisis economic fundamentals determined which states were resilient. The analysis includes OLS regression, permutation testing, and an LLM prediction experiment with contamination control.

![Pre-crisis appreciation vs. crash severity](hero_scatter.png)

[Read the full report (PDF)](final_project.pdf)

## Setup

### Python

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
cd sds-1730
uv venv .venv --python 3.12
uv pip install -r final-project/pyproject.toml
```

### Jupyter kernel

Register the venv as a Jupyter kernel so notebooks use the correct Python:

```bash
uv run --project final-project python -m ipykernel install --user --name python3 --display-name "Python 3 (sds1730)"
```

This overwrites the default `python3` kernel to point at the project venv. After running this, restart any running Jupyter server or kernel.

### Environment

The prompt optimizer requires a `GEMINI_API_KEY` in a `.env` file at the sds-1730 root. Original results are already in `results/` and served by the dashboard, so this is only needed to run new optimizations.

### Data

Download raw FRED time series (204 CSVs, one per state-series pair):

```bash
python data/build_dataset.py
```

See [data/README.md](data/README.md) for series descriptions and the transformation algorithm.

### Rendering

The notebook renders to PDF via Quarto:

```bash
quarto render final_project.ipynb --cache-refresh --to pdf
```

## Project Structure

```
final-project/
  final_project.ipynb     Main report and analysis
  llm_experiment.ipynb    Full LLM experiment methodology and per-model results
  final_project.pdf       Rendered PDF
  pyproject.toml          Python dependencies

  data/
    build_dataset.py      FRED download script
    raw/                  204 state-level CSV files (4 series x 51 states)

  prompts/
    rlm.md                RLM agent instructions (DSPy/GEPA input)
    predict.md            Pure-reasoning predict prompt (DSPy harness)
    chat_predict.md       Chat-based predict prompt (manual, with inline data)
    reward_hacked.md      GEPA-optimized prompt (reward-hacked, preserved)
    GEPA_reflection_template.md   Teacher reflection constraints

  prompt-optimizer/
    optimize.py           Two-phase GEPA optimization (baseline + constrained)
    metric.py             GEPA metric: RMSE-based scoring with trajectory feedback
    signatures.py         DSPy signatures and state constants
    data_utils.py         Dataset loading and cross-validation split generation
    local_interpreter.py  Sandboxed Python REPL for RLM code execution
    smoke_test.py         Single-split RLM test runner
    server.ts             Bun SSE dashboard server
    index.html            Dashboard UI

  results/                Per-model evaluation writeups, GEPA run logs, and 20-split scores
```

## Running the Prompt Optimizer

```bash
cd prompt-optimizer

# Start the dashboard
bun run dev

# Run GEPA optimization (long-running)
python optimize.py

# Resume from an existing run
python optimize.py <run-id>

# Single-split smoke test
python smoke_test.py
```

The dashboard streams optimization progress at http://localhost:3456.
