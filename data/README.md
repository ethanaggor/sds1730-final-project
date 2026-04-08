# Data

## Source

All data comes from the Federal Reserve Economic Data (FRED) platform:
https://fred.stlouisfed.org

The download script uses FRED's public CSV endpoint:
`https://fred.stlouisfed.org/graph/fredgraph.csv?id={SERIES_ID}&cosd=2000-01-01&coed=2012-12-31`

## raw/

204 CSV files, one per FRED series. Each file has two columns: `observation_date` and the series value. Four series per state (50 states + DC):

| Series pattern | Description | Frequency |
|---|---|---|
| `{ST}STHPI` | FHFA All-Transactions House Price Index (index, base=100) | Quarterly |
| `{ST}UR` | Unemployment Rate, seasonally adjusted (%) | Monthly |
| `{ST}PCPI` | Per Capita Personal Income (nominal USD) | Annual |
| `{ST}POP` | Resident Population (thousands of persons) | Annual |

`{ST}` is the two-letter state abbreviation (e.g., `CASTHPI` for California HPI).

Example raw file (`NVSTHPI.csv`, first 5 rows):

| observation_date | NVSTHPI |
|---|---|
| 2000-01-01 | 192.75 |
| 2000-04-01 | 195.18 |
| 2000-07-01 | 197.06 |
| 2000-10-01 | 199.87 |
| 2001-01-01 | 204.38 |

## Downloading

```
python data/build_dataset.py
```

Populates `data/raw/`.

## Transformation

The notebook (`final_project.ipynb`) transforms the 204 raw time series into one cross-sectional row per state. For each state:

1. Load the HPI series (`{ST}STHPI`). Find the peak index value in the 2000-2012 window. Find the minimum index value after the peak date. Compute `crash_pct = (trough - peak) / peak * 100` (%, more negative = worse crash).
2. From the same HPI series, extract the Q1 2003 and Q1 2006 values. Compute `appreciation_03_06 = (hpi_2006 - hpi_2003) / hpi_2003 * 100` (%, pre-crisis bubble size).
3. Load the unemployment series (`{ST}UR`). Average all monthly values in calendar year 2006 to produce `ur_2006` (%, pre-crash labor market health).
4. Load the income series (`{ST}PCPI`). Extract the 2006 value as `pcpi_2006` (nominal USD, economic baseline).
5. Load the population series (`{ST}POP`). Extract the 2003 and 2006 values. Compute `pop_growth_03_06 = (pop_2006 - pop_2003) / pop_2003 * 100` (%, migration-driven demand).

The result is a 51-row DataFrame (50 states + DC) with one outcome column (`crash_pct`) and four predictor columns.

Assembled dataset (5 most severe crashes):

| state | appreciation_03_06 (%) | ur_2006 (%) | pcpi_2006 ($) | pop_growth_03_06 (%) | crash_pct (%) |
|---|---|---|---|---|---|
| NV | 79.74 | 4.17 | 39437 | 12.18 | -55.69 |
| AZ | 73.44 | 4.27 | 34460 | 9.41 | -46.01 |
| FL | 74.37 | 3.28 | 38009 | 6.84 | -44.73 |
| CA | 73.96 | 4.89 | 41454 | 2.18 | -41.04 |
| MI | 8.86 | 6.87 | 33563 | -0.05 | -29.40 |
