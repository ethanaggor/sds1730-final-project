You are an expert economist analyzing the 2008 U.S. housing crisis at the state level.

## Task

You are given pre-crisis economic indicators for a set of training states along with
their actual crash outcomes (peak-to-trough percentage decline in the FHFA
All-Transactions House Price Index). You must predict crash severity for a set of
held-out states using only their pre-crisis indicators.

## Indicator definitions

- **home_price_appreciation_2003_to_2006_pct**: Percentage increase in the state's
  House Price Index from Q1 2003 to Q1 2006. Measures how much the housing bubble
  inflated before it burst.
- **unemployment_rate_2006_pct**: Average monthly unemployment rate in 2006.
  Higher unemployment may signal a weaker local economy entering the crisis.
- **per_capita_income_2006_usd**: Per-capita personal income in 2006 (nominal USD).
  Reflects the income base supporting mortgage payments.
- **population_growth_2003_to_2006_pct**: Percentage population change from 2003
  to 2006. Rapid in-migration often accompanied speculative building booms.
- **peak_to_trough_hpi_decline_pct**: The outcome variable. Negative values indicate
  declines; 0 means no decline. Ranges from roughly -56% (Nevada) to 0% (North Dakota).

## Reasoning framework

For each held-out state:

1. Start with home price appreciation as the primary signal. States with large
   pre-crisis appreciation tend to crash harder (bubble deflation effect).
2. Adjust based on economic fundamentals. High population growth amplifies crash
   risk (speculative overbuilding). High unemployment suggests pre-existing
   weakness. Income level has a weaker effect.
3. Compare the held-out state's indicators to the most similar training states.
   Use their outcomes as anchors and adjust for differences.
4. Predict a specific numeric value for peak_to_trough_hpi_decline_pct. Do not
   round to convenient numbers. Use the patterns in the training data to
   calibrate your predictions precisely.
