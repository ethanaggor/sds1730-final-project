## Analysis Approach

I'll identify comparable training states for each held-out state, focusing on the key drivers that emerge from the training data:

1. **High income ($42k+) strongly buffers crashes** -- CT (0.00), NJ (-2.88), VA (-4.45) despite high appreciation
2. **Bubble size (appreciation) alone doesn't determine severity** -- FL (-15.68) and CA (-12.93) had massive appreciation but moderate crashes in this dataset
3. **Weak economies crash badly even without bubbles** -- IA (-41.04), NE (-29.40), IN (-22.13) with sub-15% appreciation
4. **Population growth signals overbuilding risk** -- speculative construction creates supply overhang when demand evaporates

---

## State-by-State Predictions

### WI (Wisconsin): -10.0

Comparable training states:
- MN: 24.94 appr, 4.06 ur, $39.4k pcpi → -13.02
- IL: 25.87 appr, 4.62 ur, $40.0k pcpi → -6.70

WI (22.65 appr, 4.69 ur, $36.0k pcpi, 1.80 pop) slots between MN and IL. Slightly lower appreciation than both is protective, but lower income ($36k vs $39-40k) adds vulnerability. Manufacturing exposure (paper, machinery) brings economic risk but less severe than MI's auto dependence. Splitting MN and IL: **-10.0**.

### DE (Delaware): -13.0

Comparable training states:
- NJ: 48.76 appr, 4.69 ur, $47.4k pcpi → -2.88
- PA: 34.06 appr, 4.73 ur, $37.8k pcpi → -7.70
- MD: 65.16 appr, 3.85 ur, $45.3k pcpi → -14.02

DE (45.63 appr, 3.58 ur, $40.7k pcpi, 5.04 pop) has NJ-level appreciation but significantly lower income ($40.7k vs $47.4k), removing the buffer that protected NJ. The 5.04% pop growth (coastal beach town development, Wilmington corridor) signals meaningful overbuilding. Financial sector exposure (corporate headquarters state) adds systemic risk. Lands between PA and MD: **-13.0**.

### AZ (Arizona): -22.0

Comparable training states:
- FL: 74.37 appr, 3.28 ur, $38.0k pcpi, 6.84 pop → -15.68
- CA: 73.96 appr, 4.89 ur, $41.5k pcpi, 2.18 pop → -12.93

AZ (73.44 appr, 4.27 ur, $34.5k pcpi, 9.41 pop) is a classic "sand state" with nearly identical appreciation to FL and CA but worse on every other dimension: higher UR than FL, lower income than both, and dramatically higher population growth (9.41%). That pop growth, the highest in training or test except NV, represents massive speculative Phoenix suburb construction. Lower income ($34.5k) means homeowners had less cushion. When construction employment evaporated, it created a vicious cycle. Significantly worse than FL: **-22.0**.

### GA (Georgia): -11.0

Comparable training states:
- NC: 16.94 appr, 4.73 ur, $34.2k pcpi, 5.87 pop → -10.97
- TN: 17.18 appr, 5.22 ur, $32.9k pcpi, 4.12 pop → -7.30

GA (15.17 appr, 4.66 ur, $34.6k pcpi, 6.18 pop) is nearly identical to NC across all four features. Slightly lower appreciation (positive) offset by slightly higher pop growth (negative), reflecting Atlanta metro expansion. Both states had moderate appreciation, similar income, similar UR, and high Sunbelt population growth. Atlanta's construction boom and suburban sprawl mirror Charlotte/Raleigh dynamics. Essentially matches NC: **-11.0**.

### CO (Colorado): -6.0

Comparable training states:
- TX: 11.68 appr, 4.98 ur, $35.4k pcpi, 6.03 pop → -6.55
- KS: 12.49 appr, 4.42 ur, $35.4k pcpi, 1.47 pop → -4.97

CO (11.88 appr, 4.25 ur, $39.9k pcpi, 4.23 pop) has near-identical appreciation to TX and KS but notably higher income ($39.9k vs $35.4k), providing a strong buffer. Colorado had already experienced a mini-correction after the 2001 tech/telecom bust, keeping 2003-06 appreciation modest. The economy is well-diversified (tech, defense, energy, tourism). Lower UR than TX and comparable to KS. Despite NE having identical appreciation (11.88) and crashing -29.40, CO's economy is fundamentally different from Nebraska's agricultural base. Tracks TX with a slight income advantage: **-6.0**.

### NH (New Hampshire): -6.0

Comparable training states:
- VT: 41.92 appr, 3.68 ur, $36.6k pcpi, 0.81 pop → -7.26
- PA: 34.06 appr, 4.73 ur, $37.8k pcpi, 1.10 pop → -7.70
- WA: 42.91 appr, 4.99 ur, $39.7k pcpi, 4.37 pop → -8.67

NH (31.83 appr, 3.52 ur, $42.9k pcpi, 2.23 pop) has lower appreciation than all three comparables, the lowest UR of the group, and significantly higher income ($42.9k). No state income tax supports housing demand. Boston commuter zone provides economic stability. NH outperforms VT and PA on every protective metric. The income advantage alone (6k+ above VT) is meaningful in a dataset where income is the strongest protective factor: **-6.0**.

### NV (Nevada): -30.0

Comparable training states:
- HI: 80.67 appr, 2.57 ur, $38.3k pcpi, 4.68 pop → -44.73
- FL: 74.37 appr, 3.28 ur, $38.0k pcpi, 6.84 pop → -15.68

NV (79.74 appr, 4.17 ur, $39.4k pcpi, 12.18 pop) has HI-level appreciation with the most extreme population growth in the entire dataset by a wide margin. Las Vegas was the epicenter of speculative construction, investor-driven purchases, and subprime lending. The 12.18% pop growth is nearly double FL's and triple HI's, representing unprecedented overbuilding. The economy was concentrated in gaming, tourism, and construction; when construction collapsed, it took a massive share of employment with it. NV is worse than FL on every risk dimension. Not quite as extreme as HI (island market dynamics amplified HI's crash), but the overbuilding signal is the most severe in the data: **-30.0**.

### RI (Rhode Island): -16.0

Comparable training states:
- NJ: 48.76 appr, 4.69 ur, $47.4k pcpi, 0.70 pop → -2.88
- OR: 44.87 appr, 5.39 ur, $34.5k pcpi, 3.48 pop → -21.93
- NY: 40.29 appr, 4.50 ur, $43.8k pcpi, -0.37 pop → -21.83

RI (48.54 appr, 5.26 ur, $38.7k pcpi, -0.77 pop) has NJ-level appreciation without NJ's income protection ($38.7k vs $47.4k). The declining population (-0.77%) means the bubble was built on speculative, not fundamental, demand. Higher UR (5.26) signals pre-existing economic weakness. RI lacks NJ's proximity to Wall Street jobs. Income below the ~$45k threshold that protected CT, NJ, and VA. But not as bad as OR or NY due to somewhat higher income than OR and smaller magnitude of bubble than NY's metro-influenced market: **-16.0**.

### AL (Alabama): -8.0

Comparable training states:
- TN: 17.18 appr, 5.22 ur, $32.9k pcpi, 4.12 pop → -7.30
- AR: 20.02 appr, 5.23 ur, $29.4k pcpi, 3.56 pop → -8.92
- MS: 16.40 appr, 6.38 ur, $27.8k pcpi, 1.28 pop → -3.57

AL (18.37 appr, 4.01 ur, $31.3k pcpi, 2.79 pop) has moderate appreciation in line with TN and AR. The notably lower UR (4.01 vs 5.2+) is a meaningful protective factor, reflecting a healthier pre-crisis labor market (auto manufacturing plants from Hyundai, Honda, Mercedes). Income is low but comparable to TN. No significant bubble to deflate; risk is primarily economic. Splits TN and AR: **-8.0**.

### MA (Massachusetts): -4.0

Comparable training states:
- NJ: 48.76 appr, 4.69 ur, $47.4k pcpi, 0.70 pop → -2.88
- CT: 36.58 appr, 4.42 ur, $53.2k pcpi, 0.95 pop → 0.00

MA (28.21 appr, 4.69 ur, $47.3k pcpi, -0.19 pop) has lower appreciation than both NJ and CT while matching NJ's high income and UR almost exactly. The economy is highly diversified and resilient (biotech, education, healthcare, finance). Lower appreciation (28.21 vs NJ's 48.76) means a smaller bubble to deflate. Slight negative population growth (-0.19%) is a minor concern but negligible. The $47.3k income is solidly in the "protected" zone observed in the training data. Should perform close to NJ, slightly worse due to population decline: **-4.0**.

### ME (Maine): -10.0

Comparable training states:
- PA: 34.06 appr, 4.73 ur, $37.8k pcpi, 1.10 pop → -7.70
- MT: 36.61 appr, 3.37 ur, $31.9k pcpi, 3.60 pop → -10.06
- VT: 41.92 appr, 3.68 ur, $36.6k pcpi, 0.81 pop → -7.26

ME (34.89 appr, 4.71 ur, $34.2k pcpi, 1.31 pop) has PA-level appreciation and UR but lower income ($34.2k vs $37.8k). Maine's economy is less diversified (tourism, paper/forestry, fishing), making it more vulnerable to economic shocks. Lower income than PA and VT removes some cushion. Closest match is MT (-10.06), which has similar appreciation, similar income, and a similarly resource-dependent economy. ME's higher UR (4.71 vs 3.37) is offset by lower pop growth (less overbuilding). Tracks MT: **-10.0**.

---

## Final Predictions

```json
[
  {"state": "WI", "predicted_crash_pct": -10.0},
  {"state": "DE", "predicted_crash_pct": -13.0},
  {"state": "AZ", "predicted_crash_pct": -22.0},
  {"state": "GA", "predicted_crash_pct": -11.0},
  {"state": "CO", "predicted_crash_pct": -6.0},
  {"state": "NH", "predicted_crash_pct": -6.0},
  {"state": "NV", "predicted_crash_pct": -30.0},
  {"state": "RI", "predicted_crash_pct": -16.0},
  {"state": "AL", "predicted_crash_pct": -8.0},
  {"state": "MA", "predicted_crash_pct": -4.0},
  {"state": "ME", "predicted_crash_pct": -10.0}
]
```
