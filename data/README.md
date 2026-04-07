# Data

## Source

All data comes from the Federal Reserve Economic Data (FRED) platform:
https://fred.stlouisfed.org

No API key is required. The download script uses FRED's public CSV endpoint:
`https://fred.stlouisfed.org/graph/fredgraph.csv?id={SERIES_ID}&cosd=2000-01-01&coed=2012-12-31`

## raw/

204 CSV files, one per FRED series. Each file has two columns: `observation_date` and the series value. Four series per state (50 states + DC):

| Series pattern | Description | Frequency |
|---|---|---|
| `{ST}STHPI` | FHFA All-Transactions House Price Index | Quarterly |
| `{ST}UR` | Unemployment Rate, seasonally adjusted | Monthly |
| `{ST}PCPI` | Per Capita Personal Income (dollars) | Annual |
| `{ST}POP` | Resident Population (thousands) | Annual |

`{ST}` is the two-letter state abbreviation (e.g., `CASTHPI` for California HPI).

## Downloading

```
python data/build_dataset.py
```

Populates `data/raw/`. Takes ~45 seconds (rate-limited). Skips files that already exist.

## Transformation

The notebook (`final_project.ipynb`) reads from `data/raw/` and constructs the analysis DataFrame in memory. No intermediate processed files are written to disk. See the "Data wrangling" section of the notebook for the full transformation logic.
