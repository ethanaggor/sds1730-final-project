# Housing Crash Severity Predictions

## Analytical Framework

Before predicting individual states, I'll identify the key patterns in the training data:

**Appreciation vs. crash is noisy but directional.** Grouping training states by appreciation bracket reveals a trend:
- <15% appreciation: mean crash ~-10% (range: 0 to -29)
- 15-25%: mean ~-12% (range: 0 to -27)
- 25-40%: mean ~-19% (range: 0 to -45)
- 40-60%: mean ~-21% (range: -4 to -56)
- 60%+: mean ~-24% (range: -11 to -46)

The variance within each bracket is enormous, which means the other features matter significantly.

**Key moderating factors from the training data:**
- Very low unemployment (UT 2.87 → -2.88; SD 3.01 → -3.57; NE 3.04 → 0.00) strongly buffers
- Resource/energy economies resist crashes (AK: 36% appreciation → 0.00)
- High population growth can buffer (NV: 80% appreciation, 12% pop growth → only -10.97) or coexist with severe decline (AZ: 73%, 9.4% pop → -46)
- Several states crash far beyond what their features predict (WA -55.69, IL -44.73, CT -41.04, KS -29.40), likely due to sector-specific shocks (financial, manufacturing) or localized foreclosure spirals

---

## State-by-State Predictions

### NM (New Mexico) → **-13.0%**

| Feature | NM | NH | PA | MT |
|---|---|---|---|---|
| appreciation | 32.57 | 31.83 | 34.06 | 36.61 |
| ur_2006 | 4.23 | 3.52 | 4.73 | 3.37 |
| pcpi_2006 | 30,433 | 42,866 | 37,803 | 31,870 |
| pop_growth | 4.50 | 2.23 | 1.10 | 3.60 |
| crash_pct | **?** | -12.93 | -13.11 | -4.15 |

NM sits in the moderate appreciation bracket (32.57%) with middling unemployment and decent population growth. NH and PA, with nearly identical appreciation, both crashed ~-13%. MT at -4.15 had lower unemployment (3.37 vs. 4.23) and is more rural/insulated. NM's notably lower income (30,433, well below the training mean ~37,000) introduces foreclosure vulnerability that MT and NH didn't face. NM tracks closest to the NH/PA cluster.

### MA (Massachusetts) → **-12.0%**

| Feature | MA | NJ | RI | NH |
|---|---|---|---|---|
| appreciation | 28.21 | 48.76 | 48.54 | 31.83 |
| ur_2006 | 4.69 | 4.69 | 5.26 | 3.52 |
| pcpi_2006 | 47,311 | 47,366 | 38,719 | 42,866 |
| pop_growth | -0.19 | 0.70 | -0.77 | 2.23 |
| crash_pct | **?** | -4.97 | -13.06 | -12.93 |

MA's appreciation (28.21) is actually the *lowest* among its northeastern peers, which argues for a moderate crash. Its income (47,311) is nearly identical to NJ (47,366 → -4.97), providing a buffer. However, MA's negative population growth (-0.19) is a vulnerability; RI with similar negative pop growth (-0.77) and much higher appreciation crashed -13.06. MA's lower appreciation relative to RI and NJ argues for something milder than RI but worse than NJ, given the pop growth drag. The strong knowledge economy (biotech, education, tech) provides structural resilience that pure income figures understate.

### KY (Kentucky) → **-12.0%**

| Feature | KY | OK | AR | OH |
|---|---|---|---|---|
| appreciation | 14.25 | 14.28 | 20.02 | 9.43 |
| ur_2006 | 5.73 | 3.91 | 5.23 | 5.43 |
| pcpi_2006 | 30,476 | 34,650 | 29,376 | 33,976 |
| pop_growth | 2.48 | 2.54 | 3.56 | 0.41 |
| crash_pct | **?** | -10.14 | -11.93 | -11.81 |

KY has nearly identical appreciation to OK (14.28 → -10.14), but its unemployment is substantially higher (5.73 vs. 3.91) and income is lower (30,476 vs. 34,650). Both are vulnerabilities that increase foreclosure risk even without a large bubble. AR (-11.93) and OH (-11.81) are better labor market comparables with similar unemployment and low-to-moderate appreciation. KY's combination of low income, high unemployment, and small bubble size places it in the structural distress category rather than the bubble-burst category, tracking the AR/OH cluster.

### GA (Georgia) → **-8.0%**

| Feature | GA | NC | MO | WI |
|---|---|---|---|---|
| appreciation | 15.17 | 16.94 | 18.82 | 22.65 |
| ur_2006 | 4.66 | 4.73 | 4.89 | 4.69 |
| pcpi_2006 | 34,574 | 34,189 | 33,860 | 36,047 |
| pop_growth | 6.18 | 5.87 | 2.33 | 1.80 |
| crash_pct | **?** | 0.00 | -7.26 | -9.38 |

GA's features are strikingly close to NC (0.00): nearly identical appreciation, unemployment, income, and high population growth. This data-driven anchor argues for a very mild crash. However, domain knowledge complicates this; Atlanta's sprawling suburban development created localized foreclosure hotspots, especially in exurban counties, which NC's more diversified metro areas (Charlotte, Raleigh-Durham) avoided. MO (-7.26) and WI (-9.38) provide a secondary bracket for states with similar appreciation and moderate economies. I place GA at -8, pulled toward NC's strong fundamentals but adjusted downward for Atlanta-specific speculative development patterns.

### VT (Vermont) → **-10.0%**

| Feature | VT | ME | MT | ID |
|---|---|---|---|---|
| appreciation | 41.92 | 34.89 | 36.61 | 39.45 |
| ur_2006 | 3.68 | 4.71 | 3.37 | 3.39 |
| pcpi_2006 | 36,609 | 34,168 | 31,870 | 31,244 |
| pop_growth | 0.81 | 1.31 | 3.60 | 7.72 |
| crash_pct | **?** | -6.70 | -4.15 | -22.13 |

VT's 41.92% appreciation is substantial, but VT is small, rural, and lacks the speculative construction pipelines that drove states like ID (-22.13) or AZ to severe crashes. ME (-6.70) is the closest geographic and structural analog (rural New England), but VT's higher appreciation (41.92 vs. 34.89) argues for a worse outcome. MT at -4.15 had similar low unemployment but higher pop growth (3.60 vs. 0.81), which provided demand support. VT's low pop growth means less fundamental demand to absorb any speculative excess. VT's low unemployment (3.68) and small scale are protective, but the appreciation overshoot pulls the estimate above ME.

### SC (South Carolina) → **-15.0%**

| Feature | SC | AR | AL | TN |
|---|---|---|---|---|
| appreciation | 19.42 | 20.02 | 18.37 | 17.18 |
| ur_2006 | 6.35 | 5.23 | 4.01 | 5.22 |
| pcpi_2006 | 30,789 | 29,376 | 31,264 | 32,878 |
| pop_growth | 5.00 | 3.56 | 2.79 | 4.12 |
| crash_pct | **?** | -11.93 | -20.44 | -26.95 |

SC's defining feature is its very high unemployment (6.35), second only to MI (6.87 → -21.83) among low-appreciation states. Combined with the lowest income bracket (30,789), SC has significant foreclosure vulnerability. AR (-11.93) has similar features but lower unemployment (5.23); AL (-20.44) has similar appreciation and income but much lower unemployment (4.01). TN with even lower unemployment (5.22) crashed -26.95, showing that Southeastern states can crash hard even without extreme bubbles. SC's good population growth (5.00) provides some demand buffer that TN (4.12) and AL (2.79) had less of. Among training states with unemployment > 5.5%, average crash is ~-15% (excluding the resource-economy outlier AK). SC lands here.

### ND (North Dakota) → **-4.0%**

| Feature | ND | SD | NE | UT |
|---|---|---|---|---|
| appreciation | 22.30 | 17.95 | 11.88 | 23.39 |
| ur_2006 | 3.12 | 3.01 | 3.04 | 2.87 |
| pcpi_2006 | 33,120 | 34,983 | 35,718 | 31,107 |
| pop_growth | 1.66 | 2.53 | 1.96 | 7.01 |
| crash_pct | **?** | -3.57 | 0.00 | -2.88 |

ND fits cleanly into the "very low unemployment, Plains/Mountain" cluster alongside SD (-3.57), NE (0.00), and UT (-2.88). All share unemployment under 3.2% and moderate appreciation. ND's appreciation (22.30) is higher than SD (17.95) or NE (11.88) but comparable to UT (23.39 → -2.88). The emerging Bakken oil boom provided economic tailwinds similar to AK's resource economy (0.00). ND's slightly higher appreciation than SD argues for slightly worse than -3.57, while the energy economy argues for resilience. I split the difference.

### NY (New York) → **-15.0%**

| Feature | NY | RI | NJ | DC |
|---|---|---|---|---|
| appreciation | 40.29 | 48.54 | 48.76 | 70.23 |
| ur_2006 | 4.50 | 5.26 | 4.69 | 5.83 |
| pcpi_2006 | 43,760 | 38,719 | 47,366 | 55,384 |
| pop_growth | -0.37 | -0.77 | 0.70 | 0.38 |
| crash_pct | **?** | -13.06 | -4.97 | -21.81 |

NY presents a contradictory profile. Its appreciation (40.29) is high but lower than RI (48.54) or NJ (48.76). Its income (43,760) is high, providing a buffer. But its negative population growth (-0.37) is a drag, similar to RI (-0.77 → -13.06). NJ with nearly identical unemployment and income but *higher* appreciation only crashed -4.97, which argues for something mild. But RI with negative pop growth and lower income crashed -13.06. DC at -21.81 demonstrates that high-income, high-appreciation markets with flat pop growth can crash significantly. NY state combines resilient NYC (rapid financial sector recovery) with deeply affected Long Island, Westchester, and upstate markets. The state-level average gets pulled down by suburban and exurban distress despite Manhattan's recovery.

### HI (Hawaii) → **-18.0%**

| Feature | HI | NV | FL | CA |
|---|---|---|---|---|
| appreciation | 80.67 | 79.74 | 74.37 | 73.96 |
| ur_2006 | 2.57 | 4.17 | 3.28 | 4.89 |
| pcpi_2006 | 38,315 | 39,437 | 38,009 | 41,454 |
| pop_growth | 4.68 | 12.18 | 6.84 | 2.18 |
| crash_pct | **?** | -10.97 | -21.93 | -25.30 |

HI has the highest appreciation in the entire dataset (80.67%), which signals a massive bubble. NV at 79.74 crashed only -10.97, but NV had extraordinary population growth (12.18%) generating genuine demand; HI's pop growth (4.68) is far more modest. FL (-21.93) and CA (-25.30) are better demand-side comparables. However, Hawaii is uniquely supply-constrained: island geography limits buildable land, preventing the speculative oversupply that devastated AZ, NV, and FL's inland markets. HI also has the lowest unemployment in the entire dataset (2.57%), indicating exceptionally strong labor market fundamentals. Military installations and tourism provide structural demand floors. These factors prevent HI from reaching the -25 to -46 range of other extreme-appreciation states, but 80.67% appreciation inevitably means reversion. FL (-21.93) is the best structural analog: similar income, coastal, tourism-dependent, but FL had far more excess supply.

### OR (Oregon) → **-20.0%**

| Feature | OR | WA | ID | RI |
|---|---|---|---|---|
| appreciation | 44.87 | 42.91 | 39.45 | 48.54 |
| ur_2006 | 5.39 | 4.99 | 3.39 | 5.26 |
| pcpi_2006 | 34,488 | 39,744 | 31,244 | 38,719 |
| pop_growth | 3.48 | 4.37 | 7.72 | -0.77 |
| crash_pct | **?** | -55.69 | -22.13 | -13.06 |

OR shares Pacific NW geography and economy with WA (42.91 → -55.69), but WA's crash is the most extreme outlier in the training data. ID (-22.13) provides a more grounded comparison: similar appreciation (39.45), Mountain West/Pacific region, but ID had much lower unemployment (3.39 vs. 5.39) and much higher pop growth (7.72 vs. 3.48). OR's higher unemployment and lower pop growth relative to ID argue for a somewhat worse outcome. OR's elevated unemployment (5.39) and moderate income (34,488) compound the vulnerability. Portland's timber and manufacturing-dependent economy was hit harder than average during the recession. I anchor near ID's -22.13, adjusted slightly upward for OR's better income profile.

### MS (Mississippi) → **-15.0%**

| Feature | MS | WV | AR | OH |
|---|---|---|---|---|
| appreciation | 16.40 | 25.64 | 20.02 | 9.43 |
| ur_2006 | 6.38 | 4.77 | 5.23 | 5.43 |
| pcpi_2006 | 27,827 | 28,528 | 29,376 | 33,976 |
| pop_growth | 1.28 | 0.86 | 3.56 | 0.41 |
| crash_pct | **?** | -19.98 | -11.93 | -11.81 |

MS has the lowest income (27,827) and second-highest unemployment (6.38) in the entire dataset including all held-out states. Despite low appreciation (16.40), meaning no speculative bubble to burst, economic fundamentals drive foreclosure risk: low-income households with limited savings are disproportionately affected by any downturn. WV is the closest analog (similar income at 28,528, low pop growth at 0.86), crashing -19.98, but WV had higher appreciation (25.64) and lower unemployment (4.77). MS's lower appreciation argues for a milder decline than WV, but its much higher unemployment argues for a worse one. Post-Katrina distortions also complicate MS's dynamics. Net effect places MS between WV (-19.98) and AR (-11.93).

---

## Final Predictions

```json
[
  {"state": "NM", "predicted_crash_pct": -13.00},
  {"state": "MA", "predicted_crash_pct": -12.00},
  {"state": "KY", "predicted_crash_pct": -12.00},
  {"state": "GA", "predicted_crash_pct": -8.00},
  {"state": "VT", "predicted_crash_pct": -10.00},
  {"state": "SC", "predicted_crash_pct": -15.00},
  {"state": "ND", "predicted_crash_pct": -4.00},
  {"state": "NY", "predicted_crash_pct": -15.00},
  {"state": "HI", "predicted_crash_pct": -18.00},
  {"state": "OR", "predicted_crash_pct": -20.00},
  {"state": "MS", "predicted_crash_pct": -15.00}
]
```
