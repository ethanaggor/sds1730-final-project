## Analysis and Predictions

### Identifying Key Patterns in the Training Data

Before predicting, I'll extract the relationships that matter most.

**1. Appreciation is the dominant crash predictor, but the relationship is nonlinear.**

The Sand States (NV, AZ, FL) with 73-80% appreciation crashed -44% to -56%. But DC with 70% appreciation crashed only -12%. The difference: speculative overbuilding vs. supply constraints.

**2. Population growth amplifies appreciation into crashes.** High appreciation + high pop growth = speculative overbuilding = severe crash. High appreciation + low pop growth = price-driven bubble in constrained markets = moderate crash.

Crash-to-appreciation ratios by pop growth:
- NV (pop 12.2%): -55.69 / 79.74 = **-0.70**
- AZ (pop 9.4%): -46.01 / 73.44 = **-0.63**
- FL (pop 6.8%): -44.73 / 74.37 = **-0.60**
- MD (pop 2.4%): -25.30 / 65.16 = **-0.39**
- DC (pop 0.4%): -11.93 / 70.23 = **-0.17**

**3. Resource/energy economies were insulated.** AK (36% appreciation, 0% crash), ND (22%, 0%), SD (18%, 0%), LA (23%, -4.2%). Energy and agricultural commodity booms provided a floor.

**4. High UR signals structural economic weakness that can drive crashes independent of bubbles.** OH (9.4% appreciation, 5.4% UR) crashed -12.9%, worse than many states with double the appreciation.

**5. High income is modestly protective.** DC ($55k PCPI, -12% crash despite 70% appreciation) and VT ($37k, -6.6% despite 42% appreciation) show that wealthy, supply-constrained markets with low pop growth resist crashes.

---

### State-by-State Predictions

#### GA (Georgia): **-14.0%**

| Feature | GA | NC (comp) | SC (comp) |
|---|---|---|---|
| appreciation | 15.17 | 16.94 | 19.42 |
| ur_2006 | 4.66 | 4.73 | 6.35 |
| pcpi_2006 | 34,574 | 34,189 | 30,789 |
| pop_growth | 6.18 | 5.87 | 5.00 |
| crash_pct | ? | -13.06 | -13.02 |

Georgia is nearly identical to North Carolina across all four features. Both are fast-growing Southern states with moderate appreciation and middling incomes. Georgia's slightly higher population growth (6.18% vs 5.87%) suggests more suburban sprawl, particularly around Atlanta, which was a major center for subprime lending and speculative exurban development. The low appreciation (15.17%) means the bubble was more about overbuilding than price inflation, which limits how far prices can fall. I shade slightly worse than NC due to the higher pop growth and Atlanta's known subprime exposure.

**Prediction: -14.0%**

---

#### IA (Iowa): **-4.0%**

| Feature | IA | KS (comp) | SD (comp) |
|---|---|---|---|
| appreciation | 13.29 | 12.49 | 17.95 |
| ur_2006 | 3.69 | 4.42 | 3.01 |
| pcpi_2006 | 34,197 | 35,411 | 34,983 |
| pop_growth | 1.38 | 1.47 | 2.53 |
| crash_pct | ? | -4.97 | 0.00 |

Iowa is a stable, agricultural Midwestern state with characteristics nearly identical to Kansas: similar appreciation (~12-13%), similar income (~$34-35k), similar low pop growth (~1.4%). Iowa has meaningfully lower unemployment (3.69% vs 4.42%), indicating a tighter, healthier labor market. No bubble dynamics are present: low appreciation, low pop growth, no speculative building. Iowa sits between Kansas (-4.97%) and the Great Plains states that experienced no decline at all (SD, ND). The stronger labor market pushes it slightly better than Kansas.

**Prediction: -4.0%**

---

#### AR (Arkansas): **-8.0%**

| Feature | AR | AL (comp) | TN (comp) | KY (comp) |
|---|---|---|---|---|
| appreciation | 20.02 | 18.37 | 17.18 | 14.25 |
| ur_2006 | 5.23 | 4.01 | 5.22 | 5.73 |
| pcpi_2006 | 29,376 | 31,264 | 32,878 | 30,476 |
| pop_growth | 3.56 | 2.79 | 4.12 | 2.48 |
| crash_pct | ? | -9.90 | -8.92 | -4.45 |

Arkansas is a low-income Southern state with modest appreciation and a weak labor market. Most comparable to Alabama and Tennessee: similar appreciation range (17-20%), similar UR (~5%), similar income levels. Arkansas has the lowest PCPI in the held-out set ($29,376), which makes homeowners more fragile, but also means homes were more affordable and less leveraged. The 20% appreciation is moderate, not speculative. Its UR (5.23%) is essentially identical to Tennessee's (5.22%), and Tennessee crashed -8.92%. Arkansas has slightly higher appreciation than TN but lower income and lower pop growth. The net effect is roughly equivalent.

**Prediction: -8.0%**

---

#### OR (Oregon): **-25.0%**

| Feature | OR | WA (comp) | NJ (comp) |
|---|---|---|---|
| appreciation | 44.87 | 42.91 | 48.76 |
| ur_2006 | 5.39 | 4.99 | 4.69 |
| pcpi_2006 | 34,488 | 39,744 | 47,366 |
| pop_growth | 3.48 | 4.37 | 0.70 |
| crash_pct | ? | -25.19 | -22.13 |

Oregon is the natural twin of Washington: Pacific Northwest neighbor with nearly identical appreciation (44.87% vs 42.91%). Oregon is slightly more vulnerable on several margins: higher unemployment (5.39% vs 4.99%), meaningfully lower income ($34,488 vs $39,744), which reduces homeowner resilience. The lower income means the same price levels represent a larger affordability stretch. Oregon's pop growth is lower (3.48% vs 4.37%), which slightly reduces overbuilding risk. On balance, the higher UR and lower income roughly offset the lower pop growth, landing Oregon very close to Washington's outcome. RI (48.5% appreciation, 5.26% UR) crashed -27.60%, providing an upper bound for a state with similar appreciation and high UR.

**Prediction: -25.0%**

---

#### HI (Hawaii): **-26.0%**

| Feature | HI | NV (comp) | DC (comp) | MD (comp) |
|---|---|---|---|---|
| appreciation | 80.67 | 79.74 | 70.23 | 65.16 |
| ur_2006 | 2.57 | 4.17 | 5.83 | 3.85 |
| pcpi_2006 | 38,315 | 39,437 | 55,384 | 45,293 |
| pop_growth | 4.68 | 12.18 | 0.38 | 2.39 |
| crash_pct | ? | -55.69 | -11.93 | -25.30 |

Hawaii is the hardest prediction. It has the highest appreciation in the entire dataset (80.67%), matching or exceeding Nevada. But the economic logic is completely different. Nevada, Arizona, and Florida crashed catastrophically because extreme appreciation was paired with extreme overbuilding on cheap, available land. Hawaii is an island chain with severe geographic supply constraints, so builders simply could not oversupply the market the way they did in Las Vegas or Phoenix.

Hawaii's bubble was driven by scarcity pricing and investment demand rather than speculative construction. Its very low UR (2.57%, lowest in the dataset) signals a tight, healthy economy with military base and tourism employment. However, tourism is cyclical and contracted sharply during the recession, removing a demand pillar.

DC provides the best structural analog: very high appreciation (70%) + supply constraints + unique employment base = only -12% crash. But Hawaii's appreciation is 10 points higher, its income is much lower ($38k vs $55k), and it lacks government employment stability. Maryland (65% appreciation, 2.4% pop growth) crashed -25.3% and represents a supply-moderately-constrained, high-income market.

I estimate about 32% of the appreciation deflated (between DC's 17% and the Sand States' 60-70%), yielding: 80.67 * 0.32 = -25.8.

**Prediction: -26.0%**

---

#### NE (Nebraska): **-3.5%**

| Feature | NE | KS (comp) | SD (comp) | OK (comp) |
|---|---|---|---|---|
| appreciation | 11.88 | 12.49 | 17.95 | 14.28 |
| ur_2006 | 3.04 | 4.42 | 3.01 | 3.91 |
| pcpi_2006 | 35,718 | 35,411 | 34,983 | 34,650 |
| pop_growth | 1.96 | 1.47 | 2.53 | 2.54 |
| crash_pct | ? | -4.97 | 0.00 | -3.57 |

Nebraska is almost indistinguishable from Kansas in appreciation and income, but has a substantially better labor market (UR 3.04% vs 4.42%). Nebraska's UR is essentially identical to South Dakota's (3.01%) and North Dakota's (3.12%), both of which experienced zero decline. Nebraska is a diversified agricultural economy without speculation or overbuilding. Its low UR groups it with the Great Plains states that were the most resilient in the entire crisis. Slightly worse than SD/ND because it lacks the energy boom that provided an extra floor, but better than Kansas due to stronger employment.

**Prediction: -3.5%**

---

#### VA (Virginia): **-22.0%**

| Feature | VA | MD (comp) | DC (comp) | NH (comp) |
|---|---|---|---|---|
| appreciation | 53.63 | 65.16 | 70.23 | 31.83 |
| ur_2006 | 3.08 | 3.85 | 5.83 | 3.52 |
| pcpi_2006 | 42,164 | 45,293 | 55,384 | 42,866 |
| pop_growth | 4.16 | 2.39 | 0.38 | 2.23 |
| crash_pct | ? | -25.30 | -11.93 | -19.98 |

Virginia is structurally linked to the DC/Maryland metro economy through Northern Virginia. Its appreciation (53.63%) is about 12 points lower than Maryland's, but its population growth (4.16%) is about 2 points higher, reflecting exurban sprawl through Prince William County, Loudoun County, and other outlying areas where speculative building was significant.

Virginia's very low UR (3.08%) reflects the stability of government-adjacent employment and military installations (Norfolk, Virginia Beach). Its income ($42,164) is moderately high, providing some cushion.

Lower appreciation than MD pushes toward a milder crash. Higher pop growth (suggesting more overbuilding in outer suburbs) pushes toward a worse crash. The very low UR is a protective factor that MD and DC also share. On net, I estimate Virginia slightly better than Maryland. NJ (48.76% appreciation, -22.13% crash) provides an additional reference point at similar appreciation levels.

**Prediction: -22.0%**

---

#### CA (California): **-37.0%**

| Feature | CA | FL (comp) | NV (comp) | MD (comp) |
|---|---|---|---|---|
| appreciation | 73.96 | 74.37 | 79.74 | 65.16 |
| ur_2006 | 4.89 | 3.28 | 4.17 | 3.85 |
| pcpi_2006 | 41,454 | 38,009 | 39,437 | 45,293 |
| pop_growth | 2.18 | 6.84 | 12.18 | 2.39 |
| crash_pct | ? | -44.73 | -55.69 | -25.30 |

California is the most consequential prediction. Its appreciation (73.96%) matches Florida and Arizona, firmly in Sand State territory. But its population growth (2.18%) is dramatically lower, closer to Maryland (2.39%) than to any Sand State (6.8-12.2%).

This creates a tension. The pure feature-based estimate, scaling from Maryland's -25.3% crash upward for the ~9 points of additional appreciation and adjusting for CA's weaker labor market, lands around -30% to -33%.

But California had characteristics that the features understate. The 2.18% statewide pop growth masks massive suburban sprawl in the Inland Empire, Central Valley, and other inland areas where land was cheap and builders constructed aggressively. California was the epicenter of subprime lending: option ARMs, no-doc loans, and negative amortization products were concentrated in California markets. The state's economy was also more exposed to construction employment than its income figures suggest.

Additionally, California's higher UR (4.89%) compared to FL (3.28%) and MD (3.85%) indicates more latent economic fragility. As the construction sector collapsed and mortgage defaults cascaded, the feedback loop between job losses and foreclosures was particularly acute.

I estimate about 50% of appreciation deflated (between MD's 39% and FL's 60%): 73.96 * 0.50 = -37.0. This splits the difference between the feature-based estimate and the full Sand State trajectory.

**Prediction: -37.0%**

---

#### MI (Michigan): **-20.0%**

| Feature | MI | OH (comp) | IN (comp) | MS (comp) |
|---|---|---|---|---|
| appreciation | 8.86 | 9.43 | 8.68 | 16.40 |
| ur_2006 | 6.87 | 5.43 | 5.02 | 6.38 |
| pcpi_2006 | 33,563 | 33,976 | 32,905 | 27,827 |
| pop_growth | -0.05 | 0.41 | 2.20 | 1.28 |
| crash_pct | ? | -12.93 | -7.30 | -8.67 |

Michigan is the anti-California: minimal bubble, maximal economic collapse. Its appreciation (8.86%) is among the lowest in the dataset, which normally predicts a mild correction of -5% to -8%. But Michigan's 6.87% unemployment rate is the highest in the entire dataset (training + held-out), signaling the auto industry's accelerating decline well before the financial crisis arrived.

Ohio is the closest feature match (similar appreciation, similar income, similar geography), and Ohio crashed -12.93%. But Michigan's UR is 1.44 points higher (6.87% vs 5.43%), and its population growth is negative (-0.05% vs 0.41%), indicating that people were already leaving the state.

The auto industry collapse created a cascading economic shock that far exceeded what the housing bubble alone would have produced. Detroit became the poster child for the crisis, with extreme foreclosure rates and neighborhood abandonment. While cities like Ann Arbor and Grand Rapids were more resilient, the Detroit metro area's weight in the state average is enormous.

In the training data, the jump from Indiana (-7.30%, UR 5.02%) to Ohio (-12.93%, UR 5.43%) shows that UR has a strong nonlinear effect in Rust Belt states. Extrapolating this sensitivity to Michigan's extreme UR, and incorporating the auto industry's structural collapse (which the training data doesn't have a clean analog for), I estimate roughly 50-55% worse than Ohio.

**Prediction: -20.0%**

---

#### DE (Delaware): **-23.0%**

| Feature | DE | WA (comp) | NJ (comp) | NH (comp) |
|---|---|---|---|---|
| appreciation | 45.63 | 42.91 | 48.76 | 31.83 |
| ur_2006 | 3.58 | 4.99 | 4.69 | 3.52 |
| pcpi_2006 | 40,736 | 39,744 | 47,366 | 42,866 |
| pop_growth | 5.04 | 4.37 | 0.70 | 2.23 |
| crash_pct | ? | -25.19 | -22.13 | -19.98 |

Delaware is a small state straddling the Philadelphia and Baltimore-Washington metro corridors. Its appreciation (45.63%) places it squarely in the WA/NJ/RI cluster (~43-49% appreciation), which crashed -22% to -28%.

Compared to Washington (the closest match): similar appreciation (45.63% vs 42.91%), similar income ($40,736 vs $39,744), but much lower UR (3.58% vs 4.99%) and higher pop growth (5.04% vs 4.37%). The low UR is protective; the higher pop growth suggests more speculative demand (particularly in the beach communities and suburban Wilmington). These two factors partially offset.

NJ at 48.76% appreciation crashed -22.13%. Delaware has lower appreciation, much lower UR, but much higher pop growth. I estimate Delaware slightly worse than NJ and slightly better than WA.

**Prediction: -23.0%**

---

#### CT (Connecticut): **-16.0%**

| Feature | CT | NY (comp) | MA (comp) | PA (comp) |
|---|---|---|---|---|
| appreciation | 36.58 | 40.29 | 28.21 | 34.06 |
| ur_2006 | 4.42 | 4.50 | 4.69 | 4.73 |
| pcpi_2006 | 53,224 | 43,760 | 47,311 | 37,803 |
| pop_growth | 0.95 | -0.37 | -0.19 | 1.10 |
| crash_pct | ? | -14.02 | -17.56 | -9.38 |

Connecticut is a high-income Northeast state with moderate appreciation and minimal population growth. Its income ($53,224) is second only to DC in the full dataset, and its appreciation (36.58%) is bracketed by PA (34.06%) and NY (40.29%).

New York is the best structural comparable: similar appreciation, nearly identical UR, similar low/negative pop growth. Connecticut has somewhat lower appreciation (-3.7 points) but also sits in the wealthy NY-Boston corridor. However, Connecticut's economy is heavily concentrated in financial services (Fairfield County hedge funds, insurance in Hartford), which were directly impacted by the crisis, unlike NY's more diversified economy.

Massachusetts (28.21% appreciation, -17.56% crash) provides a lower-appreciation bound. Connecticut's higher appreciation should produce a worse crash than MA in isolation, but its much higher income ($53k vs $47k) provides a stronger buffer.

On net, I place Connecticut between NY (-14.02%) and MA (-17.56%), reflecting its intermediate appreciation level. The financial sector exposure pushes it closer to MA's worse outcome, while the high income moderates the effect.

**Prediction: -16.0%**

---

## Final Predictions

```json
[
  {"state": "GA", "predicted_crash_pct": -14.00},
  {"state": "IA", "predicted_crash_pct": -4.00},
  {"state": "AR", "predicted_crash_pct": -8.00},
  {"state": "OR", "predicted_crash_pct": -25.00},
  {"state": "HI", "predicted_crash_pct": -26.00},
  {"state": "NE", "predicted_crash_pct": -3.50},
  {"state": "VA", "predicted_crash_pct": -22.00},
  {"state": "CA", "predicted_crash_pct": -37.00},
  {"state": "MI", "predicted_crash_pct": -20.00},
  {"state": "DE", "predicted_crash_pct": -23.00},
  {"state": "CT", "predicted_crash_pct": -16.00}
]
```
