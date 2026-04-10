from pathlib import Path

import dspy
import numpy as np
import pandas as pd

from signatures import STATE_NAMES

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

STATES = list(STATE_NAMES.keys())


def _load_fred(series_id: str) -> pd.DataFrame:
    path = DATA_DIR / f"{series_id}.csv"
    df = pd.read_csv(path)
    df.columns = ["date", "value"]
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df


def build_dataset() -> pd.DataFrame:
    rows = []
    for st in STATES:
        row = {"state": st}

        hpi = _load_fred(f"{st}STHPI")
        peak_val = hpi["value"].max()
        peak_date = hpi.loc[hpi["value"].idxmax(), "date"]
        trough_val = hpi[hpi["date"] >= peak_date]["value"].min()
        row["crash_pct"] = (trough_val - peak_val) / peak_val * 100

        hpi_2003 = hpi[hpi["date"] == "2003-01-01"]["value"].values[0]
        hpi_2006 = hpi[hpi["date"] == "2006-01-01"]["value"].values[0]
        row["appreciation_03_06"] = (hpi_2006 - hpi_2003) / hpi_2003 * 100

        ur = _load_fred(f"{st}UR")
        row["ur_2006"] = ur[(ur["date"] >= "2006-01-01") & (ur["date"] <= "2006-12-31")]["value"].mean()

        pcpi = _load_fred(f"{st}PCPI")
        row["pcpi_2006"] = pcpi[pcpi["date"] == "2006-01-01"]["value"].values[0]

        pop = _load_fred(f"{st}POP")
        pop_2003 = pop[pop["date"] == "2003-01-01"]["value"].values[0]
        pop_2006 = pop[pop["date"] == "2006-01-01"]["value"].values[0]
        row["pop_growth_03_06"] = (pop_2006 - pop_2003) / pop_2003 * 100

        rows.append(row)

    return pd.DataFrame(rows)


def make_examples(df: pd.DataFrame, n_splits: int = 20, seed: int = 42) -> list[dspy.Example]:
    examples = []
    for i in range(n_splits):
        rng = np.random.RandomState(seed + i)
        test_idx = rng.choice(len(df), size=11, replace=False)
        train_idx = np.setdiff1d(np.arange(len(df)), test_idx)
        df_train = df.iloc[train_idx].reset_index(drop=True)
        df_test = df.iloc[test_idx].reset_index(drop=True)

        ex = dspy.Example(
            train_df=df_train,
            test_df=df_test.drop(columns=["crash_pct"]),
            actual_values=df_test["crash_pct"].values,
            test_states=df_test["state"].values.tolist(),
            split_idx=i,
        ).with_inputs("train_df", "test_df")
        examples.append(ex)

    return examples
