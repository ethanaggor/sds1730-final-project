You are an expert economic analyst specializing in the 2008 US housing crisis. You will be given economic indicators for 40 US states along with their actual housing crash severity (peak-to-trough decline in home prices, 2006-2012). You must predict the crash severity for 11 held-out states using only the training data and your domain knowledge.

You may not use the internet or search for any information online. Work only from the data provided and your own reasoning. Do not use any programmatic tools or tools to analyze the data. This is a pure reasoning task.

## Features

- **appreciation_03_06**: Home price appreciation 2003-2006 (%). Proxy for bubble size.
- **ur_2006**: Unemployment rate in 2006 (%). Pre-crash labor market health.
- **pcpi_2006**: Per-capita personal income in 2006 ($). Economic baseline.
- **pop_growth_03_06**: Population growth 2003-2006 (%). Migration-driven demand.
- **crash_pct**: Peak-to-trough home price decline 2006-2012 (%). This is the target variable. More negative = worse crash.

## Training Data (40 states)

| state | crash_pct | appreciation_03_06 | ur_2006 | pcpi_2006 | pop_growth_03_06 |
|-------|-----------|-------------------|---------|-----------|-----------------|
| AL | -9.90 | 18.37 | 4.01 | 31264 | 2.79 |
| AK | 0.00 | 36.14 | 6.62 | 41013 | 4.15 |
| AZ | -46.01 | 73.44 | 4.27 | 34460 | 9.41 |
| CA | -41.04 | 73.96 | 4.89 | 41454 | 2.18 |
| CO | -10.14 | 11.88 | 4.25 | 39869 | 4.23 |
| CT | -18.76 | 36.58 | 4.42 | 53224 | 0.95 |
| DE | -20.44 | 45.63 | 3.58 | 40736 | 5.04 |
| FL | -44.73 | 74.37 | 3.28 | 38009 | 6.84 |
| GA | -24.38 | 15.17 | 4.66 | 34574 | 6.18 |
| HI | -18.48 | 80.67 | 2.57 | 38315 | 4.68 |
| ID | -26.95 | 39.45 | 3.39 | 31244 | 7.72 |
| IA | 0.00 | 13.29 | 3.69 | 34197 | 1.38 |
| KS | -4.97 | 12.49 | 4.42 | 35411 | 1.47 |
| KY | -4.45 | 14.25 | 5.73 | 30476 | 2.48 |
| ME | -13.11 | 34.89 | 4.71 | 34168 | 1.31 |
| MD | -25.30 | 65.16 | 3.85 | 45293 | 2.39 |
| MA | -17.56 | 28.21 | 4.69 | 47311 | -0.19 |
| MI | -29.40 | 8.86 | 6.87 | 33563 | -0.05 |
| MN | -21.83 | 24.94 | 4.06 | 39362 | 2.18 |
| MS | -8.67 | 16.40 | 6.38 | 27827 | 1.28 |
| MT | -10.06 | 36.61 | 3.37 | 31870 | 3.60 |
| NE | -2.88 | 11.88 | 3.04 | 35718 | 1.96 |
| NV | -55.69 | 79.74 | 4.17 | 39437 | 12.18 |
| NH | -19.98 | 31.83 | 3.52 | 42866 | 2.23 |
| NJ | -22.13 | 48.76 | 4.69 | 47366 | 0.70 |
| ND | 0.00 | 22.30 | 3.12 | 33120 | 1.66 |
| OH | -12.93 | 9.43 | 5.43 | 33976 | 0.41 |
| OK | -3.57 | 14.28 | 3.91 | 34650 | 2.54 |
| OR | -25.98 | 44.87 | 5.39 | 34488 | 3.48 |
| PA | -9.38 | 34.06 | 4.73 | 37803 | 1.10 |
| RI | -27.60 | 48.54 | 5.26 | 38719 | -0.77 |
| SC | -13.02 | 19.42 | 6.35 | 30789 | 5.00 |
| TN | -8.92 | 17.18 | 5.22 | 32878 | 4.12 |
| TX | -4.15 | 11.68 | 4.98 | 35422 | 6.03 |
| VT | -6.55 | 41.92 | 3.68 | 36609 | 0.81 |
| VA | -17.39 | 53.63 | 3.08 | 42164 | 4.16 |
| WV | -7.26 | 25.64 | 4.77 | 28528 | 0.86 |
| WI | -11.81 | 22.65 | 4.69 | 36047 | 1.80 |
| WY | -7.70 | 34.89 | 3.07 | 43805 | 3.82 |
| DC | -11.93 | 70.23 | 5.83 | 55384 | 0.38 |

## Held-Out States (predict crash_pct)

| state | appreciation_03_06 | ur_2006 | pcpi_2006 | pop_growth_03_06 |
|-------|-------------------|---------|-----------|-----------------|
| UT | 23.39 | 2.87 | 31107 | 7.01 |
| SD | 17.95 | 3.01 | 34983 | 2.53 |
| WA | 42.91 | 4.99 | 39744 | 4.37 |
| IL | 25.87 | 4.62 | 40021 | 0.70 |
| MO | 18.82 | 4.89 | 33860 | 2.33 |
| NY | 40.29 | 4.50 | 43760 | -0.37 |
| LA | 22.89 | 4.14 | 33627 | -4.83 |
| NC | 16.94 | 4.73 | 34189 | 5.87 |
| AR | 20.02 | 5.23 | 29376 | 3.56 |
| NM | 32.57 | 4.23 | 30433 | 4.50 |
| IN | 8.68 | 5.02 | 32905 | 2.20 |

## Instructions

For each held-out state, predict the crash_pct value. Use your understanding of the 2008 housing crisis, bubble dynamics, regional economic structure, speculative vs. fundamental demand, and labor market vulnerability, combined with patterns in the training data.

Explain your reasoning for each state, identifying comparable training states and the economic logic behind your prediction.

Return your final predictions as a JSON array:
```json
[
  {"state": "XX", "predicted_crash_pct": -0.00},
  ...
]
```
