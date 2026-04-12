## Analysis Framework

I'll identify the key patterns in the training data, then predict each held-out state using comparable training states and economic logic.

**Key patterns from training data:**

1. **Appreciation is the primary crash driver**, but the relationship is nonlinear and heavily modulated by other factors.
2. **Population growth amplifies crashes** by proxy for speculative overbuilding (NV, AZ, UT all show this).
3. **High unemployment worsens outcomes** independent of appreciation (MI is the extreme case; OH, SC also show this).
4. **Energy/resource economies are resilient**: ND (0.0), SD (0.0), LA (-4.2), WY (-7.7), OK (-3.6) all crashed less than appreciation alone would predict.
5. **Government-dominated economies are resilient**: DC (-11.9 despite 70% appreciation), VA (-17.4 despite 54%).
6. **The Sand States cluster**: NV, AZ, CA with 73-80% appreciation and high pop growth crashed -41 to -56. Pop growth within this cluster strongly correlates with severity (NV 12.2% pop, -55.7; AZ 9.4%, -46.0; CA 2.2%, -41.0).
7. **Upper Midwest anomaly**: MN (-21.8), IL (-21.8), UT (-21.9) all crashed about -22% despite only 23-26% appreciation, suggesting subprime exposure and foreclosure dynamics beyond what appreciation captures.

---

## State-by-State Predictions

### AK (Alaska): **-12.0**

**Features**: 36.1% appreciation, 6.62% UR, $41K PCPI, 4.15% pop growth

**Comparable training states** at ~35% appreciation: ME (-13.1), MT (-10.1), CT (-18.8), WY (-7.7), PA (-9.4). Range: -7.7 to -18.8, average ~-11.8.

Alaska is a resource/energy economy (oil, fisheries, military). Energy states in the training data consistently outperform their appreciation level: WY (34.9% appreciation, -7.7), ND (22.3%, 0.0), OK (14.3%, -3.6). This provides resilience. However, Alaska's 6.62% UR is the second-highest in the entire dataset (only MI at 6.87 is worse). This is partly structural (seasonal fishing and construction), but it signals labor market fragility. The high income ($41K) from resource extraction provides a buffer. Net: the energy economy resilience and high income partially offset the very high UR. Slightly worse than the peer average due to UR drag.

---

### WA (Washington): **-18.0**

**Features**: 42.9% appreciation, 4.99% UR, $39.7K PCPI, 4.37% pop growth

**Comparable training states**: NY (40.3%, -14.0), NJ (48.8%, -22.1), VT (41.9%, -6.6, rural outlier).

Washington's appreciation places it between NY and NJ. However, WA has meaningfully worse features than NY: higher UR (4.99 vs 4.50), much higher pop growth (4.37 vs -0.37). Population growth in the Pacific NW reflected both genuine tech migration (Seattle) and speculative suburban building. The tech economy (Microsoft, Amazon) provides resilience for the Seattle core, but eastern WA and outlying suburbs are more vulnerable. WA should crash more than NY but less than NJ given the appreciation gap. The UR and pop growth penalties versus NY add roughly -4 to the baseline.

---

### GA (Georgia): **-14.0**

**Features**: 15.2% appreciation, 4.66% UR, $34.6K PCPI, 6.18% pop growth

**Comparable training states**: NC (16.9%, pop 5.87, -13.1), SC (19.4%, pop 5.0, -13.0), AL (18.4%, pop 2.8, -9.9), TN (17.2%, pop 4.12, -8.9).

NC is the best comparable: nearly identical UR, income, and pop growth, with slightly higher appreciation. The training data shows pop growth is a powerful crash amplifier: compare OK (14.3% appreciation, 2.5% pop, -3.6) to NC (16.9%, 5.9% pop, -13.1). The high pop growth in GA reflects the Atlanta metro's rapid suburban sprawl, which produced significant overbuilding and subprime exposure. GA's 6.18% pop growth exceeds even NC's 5.87%, which should slightly worsen the outcome. Slightly lower appreciation partially offsets, netting to roughly NC's level or slightly worse.

---

### AR (Arkansas): **-10.0**

**Features**: 20.0% appreciation, 5.23% UR, $29.4K PCPI, 3.56% pop growth

**Comparable training states**: TN (17.2%, UR 5.22, -8.9), AL (18.4%, UR 4.01, -9.9), MO (18.8%, UR 4.89, -11.0), MS (16.4%, UR 6.38, -8.7).

Arkansas is a low-cost Southern state without major metro speculative dynamics. TN is the closest match: nearly identical UR (5.23 vs 5.22), similar income range, similar pop growth. AR has somewhat higher appreciation (20.0 vs 17.2), which should push the crash slightly worse than TN's -8.9. AR's very low income ($29.4K, lowest in the dataset) increases borrower vulnerability, adding marginal downside. The result lands between TN (-8.9) and MO (-11.0).

---

### DE (Delaware): **-20.0**

**Features**: 45.6% appreciation, 3.58% UR, $40.7K PCPI, 5.04% pop growth

**Comparable training states**: NJ (48.8%, UR 4.69, pop 0.70, -22.1), VA (53.6%, UR 3.08, pop 4.16, -17.4), MD (65.2%, UR 3.85, pop 2.39, -25.3).

Delaware is squarely in the Mid-Atlantic bubble corridor. Linear interpolation between PA (-9.4 at 34.1%) and NJ (-22.1 at 48.8%) by appreciation gives about -19.4 for DE's 45.6%. DE's low UR (3.58, better than NJ's 4.69) is a positive. However, DE's very high pop growth (5.04%, far above NJ's 0.70%) signals overbuilding, particularly in Sussex County beach communities which were among the most speculative markets nationally. The UR advantage and pop growth disadvantage roughly offset, keeping DE close to the interpolated baseline.

---

### WI (Wisconsin): **-16.0**

**Features**: 22.7% appreciation, 4.69% UR, $36.0K PCPI, 1.80% pop growth

**Comparable training states**: MN (24.9%, UR 4.06, -21.8), IL (25.9%, UR 4.62, -21.8), MO (18.8%, UR 4.89, -11.0), OH (9.4%, UR 5.43, -12.9).

WI is geographically and economically closest to MN and IL, which both crashed -21.8 at 24-26% appreciation. WI's lower appreciation (22.65% vs 25%) provides some buffer, and its pop growth (1.80%) is slightly below MN's (2.18%). The Upper Midwest cluster shows these states crashed harder than their appreciation alone would suggest, likely due to subprime lending patterns and foreclosure dynamics in metros like Minneapolis, Chicago, and (for WI) Milwaukee. WI should follow this cluster but at a discount proportional to its lower appreciation. It sits between the MN/IL cluster (-22) and the moderate Southern states (-10 to -13).

---

### FL (Florida): **-43.0**

**Features**: 74.4% appreciation, 3.28% UR, $38.0K PCPI, 6.84% pop growth

**Comparable training states**: NV (79.7%, pop 12.2, -55.7), AZ (73.4%, pop 9.4, -46.0), CA (74.0%, pop 2.2, -41.0).

Florida is the canonical Sand State. Its appreciation (74.4%) is nearly identical to AZ (73.4%) and CA (74.0%). Within the Sand States, pop growth strongly predicts crash severity: NV (12.2% pop, -55.7), AZ (9.4%, -46.0), CA (2.2%, -41.0). FL at 6.84% pop growth falls between CA and AZ, yielding an interpolated crash of about -44. FL's very low UR (3.28%) reflects a construction boom absorbing all available labor, meaning the reversal hit harder when building stopped. FL had massive speculative dynamics: Miami condo flipping, Cape Coral new construction, Orlando/Tampa suburban sprawl. The retirement migration pipeline provides some fundamental demand floor, which may slightly cushion the blow versus AZ. Net: very slightly below the AZ-CA interpolation.

---

### OR (Oregon): **-22.0**

**Features**: 44.9% appreciation, 5.39% UR, $34.5K PCPI, 3.48% pop growth

**Comparable training states**: RI (48.5%, UR 5.26, pop -0.77, -27.6), NJ (48.8%, UR 4.69, pop 0.70, -22.1), NY (40.3%, UR 4.50, pop -0.37, -14.0).

Oregon's high appreciation and high UR is a dangerous combination. RI is the closest UR match (5.26 vs 5.39) with higher appreciation (48.5 vs 44.9). RI crashed -27.6. OR should crash less than RI due to lower appreciation and positive pop growth (3.48% vs RI's -0.77%), which maintains some housing demand. OR's low income ($34.5K) increases borrower vulnerability compared to the higher-income NJ/NY. Portland's economy (tech, Nike, healthcare) provides some resilience, but eastern Oregon's resource-dependent economy is more fragile. Net: between NY (-14) and RI (-27.6), closer to NJ's level.

---

### IA (Iowa): **-5.0**

**Features**: 13.3% appreciation, 3.69% UR, $34.2K PCPI, 1.38% pop growth

**Comparable training states**: KS (12.5%, UR 4.42, -5.0), NE (11.9%, UR 3.04, -2.9), OK (14.3%, UR 3.91, -3.6), KY (14.3%, UR 5.73, -4.5).

Iowa is a stable agricultural Midwestern state with low appreciation, low UR, and low pop growth. It sits squarely in the cluster of heartland states (KS, NE, OK) that experienced minimal housing crashes. IA's appreciation (13.3%) is slightly above KS (12.5%) and NE (11.9%), and its UR (3.69%) falls between NE (3.04) and KS (4.42). Agricultural stability and the absence of speculative building kept these markets grounded. Iowa should land right at the KS level.

---

### ID (Idaho): **-27.0**

**Features**: 39.5% appreciation, 3.39% UR, $31.2K PCPI, 7.72% pop growth

**Comparable training states**: UT (23.4%, pop 7.01, UR 2.87, -21.9), AZ (73.4%, pop 9.41, -46.0), MT (36.6%, pop 3.60, -10.1).

Idaho's combination of high appreciation (39.5%) and very high pop growth (7.72%) is its defining risk. The training data shows pop growth is a severe crash amplifier: UT at only 23.4% appreciation but 7.01% pop growth crashed -21.9, far worse than its appreciation alone would predict. ID has 69% more appreciation than UT with slightly higher pop growth. Interpolating between UT (23.4% appreciation, -21.9 crash) and AZ (73.4%, -46.0) by appreciation gives roughly -30. Idaho's low income ($31.2K, comparable to UT's $31.1K) means borrowers are heavily stretched. The Boise metro experienced rapid speculative growth driven by California migration. Low UR (3.39%) mirrors the pre-crisis construction boom pattern. ID should crash significantly worse than UT but far less than the true Sand States.

---

### MA (Massachusetts): **-17.0**

**Features**: 28.2% appreciation, 4.69% UR, $47.3K PCPI, -0.19% pop growth

**Comparable training states**: NH (31.8%, UR 3.52, -20.0), CT (36.6%, UR 4.42, -18.8), IL (25.9%, UR 4.62, -21.8), NJ (48.8%, UR 4.69, PCPI $47.4K, -22.1).

MA is the center of the Boston metro housing market. NH, its commuter neighbor, crashed -20.0 at 31.8% appreciation. MA's lower appreciation (28.2%) should produce a less severe crash than NH. MA's very high income ($47.3K) is a strong stabilizer, and its economy (education, healthcare, biotech, finance) is among the most resilient in the country. However, the flat/negative pop growth (-0.19%) reduces demand support and RI shows that negative pop growth in New England can amplify crashes (RI: pop -0.77, -27.6). MA's UR (4.69%) is higher than NH's (3.52%), which is a moderate drag. Net: the lower appreciation and high-income resilience discount MA versus NH by about 3 points.

---

## Final Predictions

```json
[
  {"state": "AK", "predicted_crash_pct": -12.00},
  {"state": "WA", "predicted_crash_pct": -18.00},
  {"state": "GA", "predicted_crash_pct": -14.00},
  {"state": "AR", "predicted_crash_pct": -10.00},
  {"state": "DE", "predicted_crash_pct": -20.00},
  {"state": "WI", "predicted_crash_pct": -16.00},
  {"state": "FL", "predicted_crash_pct": -43.00},
  {"state": "OR", "predicted_crash_pct": -22.00},
  {"state": "IA", "predicted_crash_pct": -5.00},
  {"state": "ID", "predicted_crash_pct": -27.00},
  {"state": "MA", "predicted_crash_pct": -17.00}
]
```
