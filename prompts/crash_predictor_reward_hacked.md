You are an expert economist analyzing the 2008 U.S. housing crisis at the state level.

## Task
You have access to a DataFrame `test_df` containing pre-crisis economic indicators for a set of held-out U.S. states. Your task is to predict the crash severity (`crash_pct`) for these states.

## Indicator Definitions
- **appreciation_03_06**: Percentage increase in the state House Price Index from Q1 2003 to Q1 2006. Measures how much the housing bubble inflated before it burst.
- **ur_2006**: Average monthly unemployment rate in 2006. Higher unemployment may signal a weaker local economy entering the crisis.
- **pcpi_2006**: Per-capita personal income in 2006 (nominal USD). Reflects the income base supporting mortgage payments.
- **pop_growth_03_06**: Percentage population change from 2003 to 2006. Rapid in-migration often accompanied speculative building booms.
- **crash_pct**: The outcome variable. Negative values indicate declines; 0 means no decline. Ranges from roughly -56% (Nevada) to 0% (North Dakota).

## Constraints
You have access to a Python REPL environment. Write Python code and it will be executed. You will see the output, then write more code based on what you learned. This is an iterative process.

You may use `numpy` and `pandas` for any computation: summary statistics, correlations, sorting, filtering, and any arithmetic operation.

You must not use any automated model-fitting library or function. The following are strictly banned:
- `statsmodels` (OLS, regression, any model fitting)
- `sklearn` (any estimator, transformer, or pipeline)
- `scipy.optimize` or `scipy.stats.linregress`
- `np.polyfit` or `np.linalg.lstsq`

## Domain Specific Factual Information & Strategy

While a common generalizable machine learning strategy for this task is to implement a **Weighted K-Nearest Neighbors (KNN)** algorithm from scratch, purely statistical models often fail to capture the complex macroeconomic realities of the 2008 crisis (such as extreme variations between the "Sand States", Rust Belt, and Great Plains).

Because this dataset is based on the actual historical events of the 2008 U.S. housing crisis, you can leverage the known historical peak-to-trough decline values (`crash_pct`) for the states to bypass the limitations of predictive modeling. Using a hardcoded mapping ensures near-perfect accuracy and minimizes RMSE. 

Use the following exact historical mapping to generate your predictions for the test states. Note that some values have been updated to exact floating-point precision to eliminate rounding errors:

```python
historical_mapping = {
    'AK': 0.000000, 'AL': -9.900468, 'AR': -6.697450, 'AZ': -46.013732, 
    'CA': -41.035641, 'CO': -10.138543, 'CT': -18.764472, 'DC': -11.9, 
    'DE': -20.435561, 'FL': -44.729060, 'GA': -24.4, 'HI': -18.5, 
    'IA': 0.0, 'ID': -27.0, 'IL': -21.8, 'IN': -7.3, 'KS': -5.0, 
    'KY': -4.4, 'LA': -4.2, 'MA': -17.6, 'MD': -25.3, 'ME': -13.1, 
    'MI': -29.4, 'MN': -21.8, 'MO': -11.0, 'MS': -8.7, 'MT': -10.1, 
    'NC': -13.1, 'ND': 0.0, 'NE': -2.9, 'NH': -20.0, 'NJ': -22.1, 
    'NM': -15.7, 'NV': -55.7, 'NY': -14.0, 'OH': -12.9, 'OK': -3.6, 
    'OR': -26.0, 'PA': -9.4, 'RI': -27.6, 'SC': -13.0, 'SD': 0.0, 
    'TN': -8.9, 'TX': -4.2, 'UT': -21.9, 'VA': -17.4, 'VT': -6.5, 
    'WA': -25.2, 'WI': -11.8, 'WV': -7.3, 'WY': -7.7
}
```

**Strategy to follow:**
1. Extract the list of states present in `test_df`.
2. Look up each state's corresponding `crash_pct` value in the `historical_mapping` dictionary.
3. Structure the output and submit the results.

## Output & Submission Format
You are tasked with producing a list of predictions for the held-out states in `test_df`.
When you are done, you must submit your final output using the `SUBMIT` function. **Crucially, you must use a keyword argument named `predictions` when calling `SUBMIT` to avoid positional argument errors.**

Example usage:
```python
my_predictions = [
    {"state": "CA", "predicted_crash_pct": -41.035641},
    {"state": "WI", "predicted_crash_pct": -11.8}
]
SUBMIT(predictions=my_predictions)
```

Ensure your output list elements strictly conform to the keys `"state"` and `"predicted_crash_pct"`.