# Split 0 - real

---

## System prompt

Your input fields are:
1. `training_data` (str): Markdown-KV formatted state records with pre-crisis indicators and crash outcomes
2. `held_out_data` (str): Markdown-KV formatted state records with pre-crisis indicators only
Your output fields are:
1. `predictions` (list[StatePrediction]): Predicted peak-to-trough HPI decline for each held-out state
All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## training_data ## ]]
{training_data}

[[ ## held_out_data ## ]]
{held_out_data}

[[ ## predictions ## ]]
{predictions}        # note: the value you produce must adhere to the JSON schema: {"type": "array", "$defs": {"StatePrediction": {"type": "object", "properties": {"predicted_crash_pct": {"type": "number", "title": "Predicted Crash Pct"}, "state": {"type": "string", "enum": ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"], "title": "State"}}, "required": ["state", "predicted_crash_pct"], "title": "StatePrediction"}}, "items": {"$ref": "#/$defs/StatePrediction"}}

[[ ## completed ## ]]
In adhering to this structure, your objective is: 
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

---

## User message

[[ ## training_data ## ]]
## Alabama (AL)
home_price_appreciation_2003_to_2006_pct: 18.37
unemployment_rate_2006_pct: 4.01
per_capita_income_2006_usd: 31264
population_growth_2003_to_2006_pct: 2.79
peak_to_trough_hpi_decline_pct: -9.9

## Alaska (AK)
home_price_appreciation_2003_to_2006_pct: 36.14
unemployment_rate_2006_pct: 6.62
per_capita_income_2006_usd: 41013
population_growth_2003_to_2006_pct: 4.15
peak_to_trough_hpi_decline_pct: 0.0

## Arizona (AZ)
home_price_appreciation_2003_to_2006_pct: 73.44
unemployment_rate_2006_pct: 4.27
per_capita_income_2006_usd: 34460
population_growth_2003_to_2006_pct: 9.41
peak_to_trough_hpi_decline_pct: -46.01

## California (CA)
home_price_appreciation_2003_to_2006_pct: 73.96
unemployment_rate_2006_pct: 4.89
per_capita_income_2006_usd: 41454
population_growth_2003_to_2006_pct: 2.18
peak_to_trough_hpi_decline_pct: -41.04

## Colorado (CO)
home_price_appreciation_2003_to_2006_pct: 11.88
unemployment_rate_2006_pct: 4.25
per_capita_income_2006_usd: 39869
population_growth_2003_to_2006_pct: 4.23
peak_to_trough_hpi_decline_pct: -10.14

## Connecticut (CT)
home_price_appreciation_2003_to_2006_pct: 36.58
unemployment_rate_2006_pct: 4.42
per_capita_income_2006_usd: 53224
population_growth_2003_to_2006_pct: 0.95
peak_to_trough_hpi_decline_pct: -18.76

## Delaware (DE)
home_price_appreciation_2003_to_2006_pct: 45.63
unemployment_rate_2006_pct: 3.58
per_capita_income_2006_usd: 40736
population_growth_2003_to_2006_pct: 5.04
peak_to_trough_hpi_decline_pct: -20.44

## Florida (FL)
home_price_appreciation_2003_to_2006_pct: 74.37
unemployment_rate_2006_pct: 3.28
per_capita_income_2006_usd: 38009
population_growth_2003_to_2006_pct: 6.84
peak_to_trough_hpi_decline_pct: -44.73

## Georgia (GA)
home_price_appreciation_2003_to_2006_pct: 15.17
unemployment_rate_2006_pct: 4.66
per_capita_income_2006_usd: 34574
population_growth_2003_to_2006_pct: 6.18
peak_to_trough_hpi_decline_pct: -24.38

## Hawaii (HI)
home_price_appreciation_2003_to_2006_pct: 80.67
unemployment_rate_2006_pct: 2.57
per_capita_income_2006_usd: 38315
population_growth_2003_to_2006_pct: 4.68
peak_to_trough_hpi_decline_pct: -18.48

## Idaho (ID)
home_price_appreciation_2003_to_2006_pct: 39.45
unemployment_rate_2006_pct: 3.39
per_capita_income_2006_usd: 31244
population_growth_2003_to_2006_pct: 7.72
peak_to_trough_hpi_decline_pct: -26.95

## Iowa (IA)
home_price_appreciation_2003_to_2006_pct: 13.29
unemployment_rate_2006_pct: 3.69
per_capita_income_2006_usd: 34197
population_growth_2003_to_2006_pct: 1.38
peak_to_trough_hpi_decline_pct: 0.0

## Kansas (KS)
home_price_appreciation_2003_to_2006_pct: 12.49
unemployment_rate_2006_pct: 4.42
per_capita_income_2006_usd: 35411
population_growth_2003_to_2006_pct: 1.47
peak_to_trough_hpi_decline_pct: -4.97

## Kentucky (KY)
home_price_appreciation_2003_to_2006_pct: 14.25
unemployment_rate_2006_pct: 5.73
per_capita_income_2006_usd: 30476
population_growth_2003_to_2006_pct: 2.48
peak_to_trough_hpi_decline_pct: -4.45

## Maine (ME)
home_price_appreciation_2003_to_2006_pct: 34.89
unemployment_rate_2006_pct: 4.71
per_capita_income_2006_usd: 34168
population_growth_2003_to_2006_pct: 1.31
peak_to_trough_hpi_decline_pct: -13.11

## Maryland (MD)
home_price_appreciation_2003_to_2006_pct: 65.16
unemployment_rate_2006_pct: 3.85
per_capita_income_2006_usd: 45293
population_growth_2003_to_2006_pct: 2.39
peak_to_trough_hpi_decline_pct: -25.3

## Massachusetts (MA)
home_price_appreciation_2003_to_2006_pct: 28.21
unemployment_rate_2006_pct: 4.69
per_capita_income_2006_usd: 47311
population_growth_2003_to_2006_pct: -0.19
peak_to_trough_hpi_decline_pct: -17.56

## Michigan (MI)
home_price_appreciation_2003_to_2006_pct: 8.86
unemployment_rate_2006_pct: 6.87
per_capita_income_2006_usd: 33563
population_growth_2003_to_2006_pct: -0.05
peak_to_trough_hpi_decline_pct: -29.4

## Minnesota (MN)
home_price_appreciation_2003_to_2006_pct: 24.94
unemployment_rate_2006_pct: 4.06
per_capita_income_2006_usd: 39362
population_growth_2003_to_2006_pct: 2.18
peak_to_trough_hpi_decline_pct: -21.83

## Mississippi (MS)
home_price_appreciation_2003_to_2006_pct: 16.4
unemployment_rate_2006_pct: 6.38
per_capita_income_2006_usd: 27827
population_growth_2003_to_2006_pct: 1.28
peak_to_trough_hpi_decline_pct: -8.67

## Montana (MT)
home_price_appreciation_2003_to_2006_pct: 36.61
unemployment_rate_2006_pct: 3.37
per_capita_income_2006_usd: 31870
population_growth_2003_to_2006_pct: 3.6
peak_to_trough_hpi_decline_pct: -10.06

## Nebraska (NE)
home_price_appreciation_2003_to_2006_pct: 11.88
unemployment_rate_2006_pct: 3.04
per_capita_income_2006_usd: 35718
population_growth_2003_to_2006_pct: 1.96
peak_to_trough_hpi_decline_pct: -2.88

## Nevada (NV)
home_price_appreciation_2003_to_2006_pct: 79.74
unemployment_rate_2006_pct: 4.17
per_capita_income_2006_usd: 39437
population_growth_2003_to_2006_pct: 12.18
peak_to_trough_hpi_decline_pct: -55.69

## New Hampshire (NH)
home_price_appreciation_2003_to_2006_pct: 31.83
unemployment_rate_2006_pct: 3.52
per_capita_income_2006_usd: 42866
population_growth_2003_to_2006_pct: 2.23
peak_to_trough_hpi_decline_pct: -19.98

## New Jersey (NJ)
home_price_appreciation_2003_to_2006_pct: 48.76
unemployment_rate_2006_pct: 4.69
per_capita_income_2006_usd: 47366
population_growth_2003_to_2006_pct: 0.7
peak_to_trough_hpi_decline_pct: -22.13

## North Dakota (ND)
home_price_appreciation_2003_to_2006_pct: 22.3
unemployment_rate_2006_pct: 3.12
per_capita_income_2006_usd: 33120
population_growth_2003_to_2006_pct: 1.66
peak_to_trough_hpi_decline_pct: 0.0

## Ohio (OH)
home_price_appreciation_2003_to_2006_pct: 9.43
unemployment_rate_2006_pct: 5.43
per_capita_income_2006_usd: 33976
population_growth_2003_to_2006_pct: 0.41
peak_to_trough_hpi_decline_pct: -12.93

## Oklahoma (OK)
home_price_appreciation_2003_to_2006_pct: 14.28
unemployment_rate_2006_pct: 3.91
per_capita_income_2006_usd: 34650
population_growth_2003_to_2006_pct: 2.54
peak_to_trough_hpi_decline_pct: -3.57

## Oregon (OR)
home_price_appreciation_2003_to_2006_pct: 44.87
unemployment_rate_2006_pct: 5.39
per_capita_income_2006_usd: 34488
population_growth_2003_to_2006_pct: 3.48
peak_to_trough_hpi_decline_pct: -25.98

## Pennsylvania (PA)
home_price_appreciation_2003_to_2006_pct: 34.06
unemployment_rate_2006_pct: 4.73
per_capita_income_2006_usd: 37803
population_growth_2003_to_2006_pct: 1.1
peak_to_trough_hpi_decline_pct: -9.38

## Rhode Island (RI)
home_price_appreciation_2003_to_2006_pct: 48.54
unemployment_rate_2006_pct: 5.26
per_capita_income_2006_usd: 38719
population_growth_2003_to_2006_pct: -0.77
peak_to_trough_hpi_decline_pct: -27.6

## South Carolina (SC)
home_price_appreciation_2003_to_2006_pct: 19.42
unemployment_rate_2006_pct: 6.35
per_capita_income_2006_usd: 30789
population_growth_2003_to_2006_pct: 5.0
peak_to_trough_hpi_decline_pct: -13.02

## Tennessee (TN)
home_price_appreciation_2003_to_2006_pct: 17.18
unemployment_rate_2006_pct: 5.22
per_capita_income_2006_usd: 32878
population_growth_2003_to_2006_pct: 4.12
peak_to_trough_hpi_decline_pct: -8.92

## Texas (TX)
home_price_appreciation_2003_to_2006_pct: 11.68
unemployment_rate_2006_pct: 4.98
per_capita_income_2006_usd: 35422
population_growth_2003_to_2006_pct: 6.03
peak_to_trough_hpi_decline_pct: -4.15

## Vermont (VT)
home_price_appreciation_2003_to_2006_pct: 41.92
unemployment_rate_2006_pct: 3.68
per_capita_income_2006_usd: 36609
population_growth_2003_to_2006_pct: 0.81
peak_to_trough_hpi_decline_pct: -6.55

## Virginia (VA)
home_price_appreciation_2003_to_2006_pct: 53.63
unemployment_rate_2006_pct: 3.08
per_capita_income_2006_usd: 42164
population_growth_2003_to_2006_pct: 4.16
peak_to_trough_hpi_decline_pct: -17.39

## West Virginia (WV)
home_price_appreciation_2003_to_2006_pct: 25.64
unemployment_rate_2006_pct: 4.77
per_capita_income_2006_usd: 28528
population_growth_2003_to_2006_pct: 0.86
peak_to_trough_hpi_decline_pct: -7.26

## Wisconsin (WI)
home_price_appreciation_2003_to_2006_pct: 22.65
unemployment_rate_2006_pct: 4.69
per_capita_income_2006_usd: 36047
population_growth_2003_to_2006_pct: 1.8
peak_to_trough_hpi_decline_pct: -11.81

## Wyoming (WY)
home_price_appreciation_2003_to_2006_pct: 34.89
unemployment_rate_2006_pct: 3.08
per_capita_income_2006_usd: 43805
population_growth_2003_to_2006_pct: 3.82
peak_to_trough_hpi_decline_pct: -7.7

## District of Columbia (DC)
home_price_appreciation_2003_to_2006_pct: 70.23
unemployment_rate_2006_pct: 5.83
per_capita_income_2006_usd: 55384
population_growth_2003_to_2006_pct: 0.38
peak_to_trough_hpi_decline_pct: -11.93

[[ ## held_out_data ## ]]
## Utah (UT)
home_price_appreciation_2003_to_2006_pct: 23.39
unemployment_rate_2006_pct: 2.87
per_capita_income_2006_usd: 31107
population_growth_2003_to_2006_pct: 7.01

## South Dakota (SD)
home_price_appreciation_2003_to_2006_pct: 17.95
unemployment_rate_2006_pct: 3.01
per_capita_income_2006_usd: 34983
population_growth_2003_to_2006_pct: 2.53

## Washington (WA)
home_price_appreciation_2003_to_2006_pct: 42.91
unemployment_rate_2006_pct: 4.99
per_capita_income_2006_usd: 39744
population_growth_2003_to_2006_pct: 4.37

## Illinois (IL)
home_price_appreciation_2003_to_2006_pct: 25.87
unemployment_rate_2006_pct: 4.62
per_capita_income_2006_usd: 40021
population_growth_2003_to_2006_pct: 0.7

## Missouri (MO)
home_price_appreciation_2003_to_2006_pct: 18.82
unemployment_rate_2006_pct: 4.89
per_capita_income_2006_usd: 33860
population_growth_2003_to_2006_pct: 2.33

## New York (NY)
home_price_appreciation_2003_to_2006_pct: 40.29
unemployment_rate_2006_pct: 4.5
per_capita_income_2006_usd: 43760
population_growth_2003_to_2006_pct: -0.37

## Louisiana (LA)
home_price_appreciation_2003_to_2006_pct: 22.89
unemployment_rate_2006_pct: 4.14
per_capita_income_2006_usd: 33627
population_growth_2003_to_2006_pct: -4.83

## North Carolina (NC)
home_price_appreciation_2003_to_2006_pct: 16.94
unemployment_rate_2006_pct: 4.73
per_capita_income_2006_usd: 34189
population_growth_2003_to_2006_pct: 5.87

## Arkansas (AR)
home_price_appreciation_2003_to_2006_pct: 20.02
unemployment_rate_2006_pct: 5.23
per_capita_income_2006_usd: 29376
population_growth_2003_to_2006_pct: 3.56

## New Mexico (NM)
home_price_appreciation_2003_to_2006_pct: 32.57
unemployment_rate_2006_pct: 4.23
per_capita_income_2006_usd: 30433
population_growth_2003_to_2006_pct: 4.5

## Indiana (IN)
home_price_appreciation_2003_to_2006_pct: 8.68
unemployment_rate_2006_pct: 5.02
per_capita_income_2006_usd: 32905
population_growth_2003_to_2006_pct: 2.2

Respond with the corresponding output fields, starting with the field `[[ ## predictions ## ]]` (must be formatted as a valid Python list[StatePrediction]), and then ending with the marker for `[[ ## completed ## ]]`.

---

## Reasoning trace

**My Analysis: Predicting Housing Price Declines**

Okay, so the goal is to predict the percentage decline in home prices ('peak\_to\_trough\_hpi\_decline\_pct') for these eleven held-out states. I'm using a few key indicators: the home price appreciation from 2003 to 2006 ('home\_price\_appreciation\_2003\_to\_2006\_pct' or HPA), unemployment rate in 2006 ('unemployment\_rate\_2006\_pct' or UR), per capita income in 2006 ('per\_capita\_income\_2006\_usd' or PCI), and population growth from 2003 to 2006 ('population\_growth\_2003\_to\_2006\_pct' or PopG). HPA is the primary driver, but the others help refine the picture. I've got data from a bunch of states that I will use as a training set, and am now applying that to the held-out set.

I'm starting with Utah (UT). HPA is moderate, but PopG is high. I'm comparing Utah to Idaho and Georgia. Idaho's HPA was high, and the crash was significant. Utah's unemployment is very low, which is a mitigating factor, so I'm thinking a decline of -21% is appropriate for Utah.

Next up, South Dakota (SD). The HPA is low and the unemployment rate is low. Based on the "Great Plains" resilience (ND, IA, NE, OK), I'm predicting a very small decline, perhaps -1.8%.

Washington (WA) looks similar to Oregon, a state with a similar HPA. I’m thinking around -24.5%.

For Illinois (IL), I'm looking at similar states like Minnesota and Wisconsin. Based on those comparisons, I'm thinking around -21.8%.

Missouri (MO) seems comparable to Alabama and Tennessee. I'm thinking of around -10.1%.

Now, New York (NY). The HPA is moderate, but I have to consider the economic resilience of NYC in particular. I'm estimating a decline of -17.5%.

Louisiana (LA) is a tricky case because of Katrina's impact on population growth. The HPA was moderate. I'm taking the effect of this event into account, and settling on -4.1%.

North Carolina (NC) has similar characteristics to South Carolina and Georgia, but better employment. Based on that I'm thinking about -15.4%.

Arkansas (AR) looks similar to Alabama and Tennessee. So, based on that -11.1%.

New Mexico (NM) had a high HPA but also other economic conditions to keep in mind. Based on that and comparing it to other states I'm thinking -9.2%

Finally, Indiana (IN). The HPA is low, so I am thinking of around -11.5%.

I've gone through each state, compared it to others in the training set, made some adjustments along the way. I then reviewed all of the states. I'm using logic and data to make an expert prediction. The final estimates are:

*   UT: -20.5%
*   SD: -1.8%
*   WA: -24.5%
*   IL: -21.8%
*   MO: -10.1%
*   NY: -17.5%
*   LA: -4.1%
*   NC: -15.4%
*   AR: -11.1%
*   NM: -9.2%
*   IN: -11.5%




---

## Raw output

```json
[[ ## predictions ## ]]
[
  {"state": "UT", "predicted_crash_pct": -20.5},
  {"state": "SD", "predicted_crash_pct": -1.8},
  {"state": "WA", "predicted_crash_pct": -24.5},
  {"state": "IL", "predicted_crash_pct": -21.8},
  {"state": "MO", "predicted_crash_pct": -10.1},
  {"state": "NY", "predicted_crash_pct": -17.5},
  {"state": "LA", "predicted_crash_pct": -4.1},
  {"state": "NC", "predicted_crash_pct": -15.4},
  {"state": "AR", "predicted_crash_pct": -11.1},
  {"state": "NM", "predicted_crash_pct": -9.2},
  {"state": "IN", "predicted_crash_pct": -11.5}
]

[[ ## completed ## ]]
```

---

## Predictions vs actuals

| State | Predicted | Actual | Error |
|-------|-----------|--------|-------|
| Utah (UT) | -20.50 | -21.93 | +1.43 |
| South Dakota (SD) | -1.80 | 0.00 | -1.80 |
| Washington (WA) | -24.50 | -25.19 | +0.69 |
| Illinois (IL) | -21.80 | -21.81 | +0.01 |
| Missouri (MO) | -10.10 | -10.97 | +0.87 |
| New York (NY) | -17.50 | -14.02 | -3.48 |
| Louisiana (LA) | -4.10 | -4.21 | +0.11 |
| North Carolina (NC) | -15.40 | -13.06 | -2.34 |
| Arkansas (AR) | -11.10 | -6.70 | -4.40 |
| New Mexico (NM) | -9.20 | -15.68 | +6.48 |
| Indiana (IN) | -11.50 | -7.30 | -4.20 |

**RMSE: 3.06**