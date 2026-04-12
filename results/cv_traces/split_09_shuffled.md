## Analysis Framework

I'll identify the key predictive patterns in the training data, then apply them with domain knowledge of the 2008 crisis.

### Key Patterns in Training Data

**1. High appreciation alone doesn't determine crash severity.** The bubble states (>60% appreciation) range from 0.00 (DE) to -27.60 (AZ). The critical moderator is population growth: high pop growth signals fundamental demand that cushions the fall.

| State | Appreciation | Pop Growth | Crash |
|-------|-------------|-----------|-------|
| NV | 79.74 | 12.18 | -4.15 |
| FL | 74.37 | 6.84 | -13.11 |
| HI | 80.67 | 4.68 | -18.48 |
| AZ | 73.44 | 9.41 | -27.60 |
| DC | 70.23 | 0.38 | -20.44 |

**2. Midwest/industrial states can crash hard even without a big bubble.** IN (-44.73), OH (-26.95), MO (-29.40) all had appreciation under 20% but suffered from manufacturing decline, subprime concentration, and weak demand fundamentals (low pop growth).

**3. Very low UR + moderate features = resilience.** States like MT (3.37 UR, -3.57), DE (3.58 UR, 0.00), and UT (2.87 UR, -10.14) with tight pre-crisis labor markets tended toward milder declines.

**4. Extreme outliers (MN -55.69, IN -44.73, VT -46.01) are driven by state-specific factors** not fully captured in these four features (foreclosure laws, subprime concentration geography, vacation-home market collapse). I'll avoid anchoring too heavily on these.

---

## State-by-State Predictions

### CA (California): -27.0
California is the clearest call in this set. 73.96% appreciation is virtually identical to AZ (73.44%, -27.60), but CA's pop growth (2.18%) is drastically lower than AZ's (9.41%). This means far less of CA's appreciation was backed by real migration-driven demand; it was overwhelmingly speculative. CA's higher income (41,454) provides some foreclosure buffer relative to AZ (34,460), but the Inland Empire and Central Valley had extreme subprime exposure and speculative construction. CA should be similar to or worse than AZ.

Comparable anchors: AZ (-27.60 with much higher pop growth), DC (-20.44 with similar low pop growth but very high income), FL (-13.11 with much higher pop growth).

### WI (Wisconsin): -22.0
Midwest state with moderate appreciation (22.65%) and low pop growth (1.80%). Manufacturing exposure in the Milwaukee/Racine corridor. Most comparable to WV (25.64% app, 0.86 pop, -22.13), MO (18.82% app, 2.33 pop, -29.40), and PA (34.06% app, 1.10 pop, -21.93). WI's higher income (36,047) than MO (33,860) and WV (28,528) provides modest buffer. The MN outlier (-55.69) is geographically adjacent but appears driven by idiosyncratic factors; I won't anchor on it.

### KS (Kansas): -12.0
Low appreciation (12.49%), moderate UR (4.42%), stable Great Plains economy. Virtually identical appreciation to CO (11.88%, -13.06) and close to OK (14.28%, -10.06). KS's pop growth (1.47%) is lower than both CO (4.23%) and OK (2.54%), which slightly increases vulnerability. Kansas had limited subprime exposure and no meaningful speculative construction.

### IL (Illinois): -22.0
Moderate appreciation (25.87%) with very low pop growth (0.70%), the combination most associated with bad outcomes in the training data. Cook County/south suburban Chicago had significant subprime exposure and foreclosure cascades. Comparable to PA (-21.93 with 34% app, 1.10 pop) and MA (-24.38 with 28% app, -0.19 pop). IL's higher income (40,021) relative to PA (37,803) provides slight buffer, but the near-zero population growth signals that demand was not supporting prices.

### AL (Alabama): -9.0
Low-moderate appreciation (18.37%), low UR (4.01%), low income (31,264), moderate pop growth (2.79%). Classic Southern non-bubble state. Closest matches are AR (20.02% app, -7.30), SC (19.42% app, -7.26), and NC (16.94% app, -6.55). AL's lower pop growth than SC/NC (2.79 vs 5-6%) and lower income push it slightly worse, but the low UR is a stabilizer.

### WY (Wyoming): -8.0
Energy-sector state with very low UR (3.07%), high income (43,805), and moderate pop growth (3.82%). The energy boom provided exceptional economic insulation. Most comparable to MT (36.61% app, 3.37 UR, -3.57), which is the training set's most resilient similar state. WY's higher appreciation (34.89 vs 36.61%) is offset by higher income and slightly higher pop growth. AK (36.14% app, -21.83) is another energy state but had much higher UR (6.62%), explaining its worse outcome.

### ND (North Dakota): -7.0
North Dakota's oil-driven economy (Bakken shale) was accelerating into 2006-2008, reflected in its very low UR (3.12%). Moderate appreciation (22.30%) was more fundamentally supported than speculative. Comparable to OK (-10.06) and UT (-10.14), but ND's energy tailwind and very low UR suggest slightly better resilience. Small market size also limits speculative activity.

### IA (Iowa): -10.0
Low appreciation (13.29%), low UR (3.69%), moderate income (34,197), low pop growth (1.38%). Stable agricultural economy with no meaningful bubble. Most comparable to OK (14.28% app, 3.91 UR, -10.06) with very similar fundamentals. IA's slightly lower UR is offset by slightly lower pop growth.

### SD (South Dakota): -7.0
Lowest UR in the held-out set (3.01%), low-moderate appreciation (17.95%), moderate pop growth (2.53%). Small, stable housing market with limited speculative activity. The tight labor market is a strong positive signal. Comparable to MT (-3.57) and OK (-10.06), sitting between them.

### NE (Nebraska): -10.0
Exactly matching CO's appreciation (11.88%) with much lower UR (3.04% vs 4.25%). Stable Plains economy. Lower pop growth (1.96 vs 4.23) and lower income (35,718 vs 39,869) than CO partially offset the UR advantage. Similar profile to OK (-10.06) and IA prediction.

### VA (Virginia): -10.0
High appreciation (53.63%) but strong counterbalancing fundamentals: very low UR (3.08%), high income (42,164), moderate pop growth (4.16%), and government/military employment providing recession resistance. Most directly comparable to MD (65.16% app, 3.85 UR, 2.39 pop, -8.92) and DE (45.63% app, 3.58 UR, 5.04 pop, 0.00). VA has lower appreciation than MD (favorable), lower UR (favorable), but lower income and less pop growth than DE. Northern Virginia declined meaningfully, but the state's diversified economy and strong labor market kept the overall decline moderate.

---

## Final Predictions

```json
[
  {"state": "CA", "predicted_crash_pct": -27.00},
  {"state": "WI", "predicted_crash_pct": -22.00},
  {"state": "KS", "predicted_crash_pct": -12.00},
  {"state": "IL", "predicted_crash_pct": -22.00},
  {"state": "AL", "predicted_crash_pct": -9.00},
  {"state": "WY", "predicted_crash_pct": -8.00},
  {"state": "ND", "predicted_crash_pct": -7.00},
  {"state": "IA", "predicted_crash_pct": -10.00},
  {"state": "SD", "predicted_crash_pct": -7.00},
  {"state": "NE", "predicted_crash_pct": -10.00},
  {"state": "VA", "predicted_crash_pct": -10.00}
]
```
