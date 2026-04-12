## Analysis Framework

The training data reveals three primary drivers of crash severity:

1. **Pre-crisis appreciation** (strongest signal): The bubble's size determines how far prices can fall. NV (80% appreciation, -56% crash), AZ (73%, -46%), FL (74%, -45%) show the clearest pattern.
2. **Population growth**: Rapid in-migration fueled speculative overbuilding. NV's 12% pop growth compounded its bubble; DC's 0.4% growth cushioned its 70% appreciation to only a -12% crash.
3. **Economic structure**: Energy states (AK, OK, TX, LA) and government-backed markets (DC) proved resilient regardless of appreciation levels. Manufacturing-dependent states (MI: -29% crash on only 9% appreciation) were vulnerable to sector-specific shocks.

---

## State-by-State Predictions

### CA (appreciation: 73.96, pop_growth: 2.18)

California was the epicenter of the subprime crisis. Its appreciation (73.96%) sits squarely with AZ (73.44 → -46%) and FL (74.37 → -45%). However, CA's pop growth (2.18%) is far lower than AZ (9.41%) and FL (6.84%), closer to MD (2.39 → -25.3%). Lower pop growth means less speculative overbuilding statewide. But CA's exposure to subprime lending (Inland Empire, Central Valley, Stockton, Bakersfield) was extreme and isn't fully captured by these features. A simple three-point regression through the sand states (NV, AZ, FL) yields about -40% for CA's appreciation/pop_growth combination. Supply-constrained coastal markets (SF, LA coast) moderate the statewide average slightly versus pure sand states.

**Prediction: -40.00%**

---

### VA (appreciation: 53.63, UR: 3.08, pop_growth: 4.16)

Northern Virginia drove appreciation via DC-area spillover and suburban sprawl. Nearest comparables by appreciation: NJ (48.76 → -22.1%), DE (45.63 → -20.4%), MD (65.16 → -25.3%). Linear interpolation between NJ and MD puts VA around -23%. VA's very low UR (3.08%) and significant federal/military employment base provide a DC-like cushion, but VA is far more suburban and less government-concentrated than DC itself (70% appreciation, only -12% crash). The government floor is real but partial. Hampton Roads adds a secondary metro with its own modest decline.

**Prediction: -22.00%**

---

### IL (appreciation: 25.87, UR: 4.62, pop_growth: 0.70)

Chicago's south and west suburbs had meaningful subprime exposure, but statewide appreciation was moderate. Closest comparables: MN (24.94 → -21.8%), MA (28.21 → -17.6%), MO (18.82 → -11.0%). IL's very low pop growth (0.70%) is critical: it matches NJ (0.70 → -22.1%), but NJ had nearly double the appreciation (48.76%). Scaling NJ's excess crash by IL's lower appreciation suggests about -14%. The low pop growth limits overbuilding; the moderate appreciation limits the height from which prices fall. Chicago's subprime pockets add a couple of points versus what appreciation alone would predict.

**Prediction: -14.00%**

---

### WI (appreciation: 22.65, UR: 4.69, pop_growth: 1.80)

Neighboring MN (24.94 → -21.8%) is the obvious comparable, but MN's crash seems outsized for its appreciation level (possibly driven by Twin Cities suburban dynamics and higher pop growth at 2.18%). More conservative comparables: MO (18.82, pop 2.33 → -11.0%), MA (28.21, pop -0.19 → -17.6%). WI sits between MO and MA in appreciation, with moderate pop growth. Milwaukee and Madison had modest declines, and WI's diversified manufacturing/agricultural economy limits the damage.

**Prediction: -13.00%**

---

### AL (appreciation: 18.37, UR: 4.01, pop_growth: 2.79)

Typical Southern state profile. Best comparables: TN (17.18, UR 5.22 → -8.9%), MO (18.82, UR 4.89 → -11.0%), SC (19.42, UR 6.35 → -13.0%), AR (20.02, UR 5.23 → -6.7%). AL's UR (4.01%) is the lowest in this group, which is favorable. Pop growth (2.79%) is moderate. Birmingham and Mobile had some decline but no extreme bubble. Averaging TN and MO, adjusted for AL's stronger labor market.

**Prediction: -9.00%**

---

### WY (appreciation: 34.89, UR: 3.07, PCPI: 43805)

Energy-dependent economy (coal, oil, gas) with high per-capita income. MT (36.61, UR 3.37 → -10.1%) is the closest non-energy comparable. But energy states were consistently resilient: AK (36.14 → 0.0%), OK (14.28 → -3.6%), TX (11.68 → -4.2%), LA (22.89 → -4.2%). WY's appreciation is higher than most energy states but lower than AK. Its energy economy and very low UR provide a significant floor. Between the energy cluster (-3 to 0) and MT (-10), closer to the energy states.

**Prediction: -6.00%**

---

### SD (appreciation: 17.95, UR: 3.01, pop_growth: 2.53)

Low UR and moderate appreciation in a stable agricultural/services economy. Comparable to TN (17.18 → -8.9%) and MS (16.40 → -8.7%) by appreciation, but SD has a much stronger labor market (3.01% vs 5.22%/6.38% UR). Lower pop growth than TN (2.53 vs 4.12). The tight labor market and stable economic base moderate the impact well below TN/MS levels.

**Prediction: -6.00%**

---

### KS (appreciation: 12.49, UR: 4.42, pop_growth: 1.47)

Classic Plains state with minimal bubble. CO has identical appreciation (11.88 → -10.1%) but higher pop growth (4.23 vs 1.47). More apt comparables: TX (11.68 → -4.2%), OK (14.28 → -3.6%), KY (14.25 → -4.5%). Kansas City (split with MO) had some decline, but KS as a whole had very modest appreciation and a stable, diversified economy. Slightly worse than TX/OK due to higher UR and less energy cushion.

**Prediction: -5.00%**

---

### IA (appreciation: 13.29, UR: 3.69, pop_growth: 1.38)

Agricultural economy with low appreciation and a strong labor market. Nearly identical profile to KS. Comparables: KY (14.25 → -4.5%), OK (14.28 → -3.6%), TX (11.68 → -4.2%). Iowa's farm economy provided remarkable stability during the financial crisis. Des Moines had moderate insurance/financial services exposure but no significant bubble. Very low UR confirms economic health.

**Prediction: -5.00%**

---

### NE (appreciation: 11.88, UR: 3.04, pop_growth: 1.96)

Identical appreciation to CO (11.88%) but with a far lower UR (3.04% vs 4.25%) and lower pop growth (1.96% vs 4.23%). CO crashed -10.1%, but CO's higher pop growth and ongoing recovery from the early 2000s tech bust made it more volatile. NE's profile is closer to TX/OK: stable economy, low appreciation, no bubble. NE's very low UR (3.04%) is among the strongest in the dataset. Agricultural and services base provided insulation.

**Prediction: -4.00%**

---

### ND (appreciation: 22.30, UR: 3.12, pop_growth: 1.66)

ND is unique: the Bakken oil boom was ramping up during 2006-2008 and accelerated dramatically through 2008-2012, creating intense housing demand in western North Dakota precisely when the rest of the country was crashing. Energy states in the training data were the most resilient: AK (36.14 → 0.0%), OK (14.28 → -3.6%), TX (11.68 → -4.2%), LA (22.89 → -4.2%). ND's energy boom during the crash window makes it comparable to AK. Very low UR (3.12%) confirms the strength. Housing demand was being actively created during the period when the target variable measures declines.

**Prediction: -1.00%**

---

## Final Predictions

```json
[
  {"state": "CA", "predicted_crash_pct": -40.00},
  {"state": "WI", "predicted_crash_pct": -13.00},
  {"state": "KS", "predicted_crash_pct": -5.00},
  {"state": "IL", "predicted_crash_pct": -14.00},
  {"state": "AL", "predicted_crash_pct": -9.00},
  {"state": "WY", "predicted_crash_pct": -6.00},
  {"state": "ND", "predicted_crash_pct": -1.00},
  {"state": "IA", "predicted_crash_pct": -5.00},
  {"state": "SD", "predicted_crash_pct": -6.00},
  {"state": "NE", "predicted_crash_pct": -4.00},
  {"state": "VA", "predicted_crash_pct": -22.00}
]
```
