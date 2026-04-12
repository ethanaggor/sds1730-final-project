## Analysis Framework

Before predicting each state, I'll identify the key patterns in the training data.

**Primary driver: appreciation magnitude.** The bubble size (appreciation_03_06) is the strongest predictor of crash severity. States above 70% appreciation (NV, AZ, FL, CA) all crashed 40%+. States below 15% (KS, NE, OK, TX, IA) rarely exceeded -5%.

**Key amplifiers and dampeners:**

| Factor | Effect | Training evidence |
|---|---|---|
| High pop growth + high appreciation | Amplifies crash (overbuilding) | NV (-55.69, pop 12.18), AZ (-46.01, pop 9.41), ID (-26.95, pop 7.72) |
| Supply constraints | Dampens crash relative to appreciation | HI (-18.48 despite 80.67% appreciation), DC (-11.93 despite 70.23%) |
| Energy sector | Insulates prices | AK (0.00 with 36.14% appreciation), ND (0.00 with 22.30%) |
| Manufacturing/auto collapse | Crash without bubble | MI (-29.40 with only 8.86% appreciation) |
| Subprime exposure (low income + high pop growth) | Amplifies crash | GA (-24.38 with only 15.17% appreciation) |

---

## State-by-State Predictions

### UT (Utah) — predicted: **-20.0**

Appreciation is moderate (23.39%), but population growth is very high (7.01%), signaling a construction boom, particularly in suburban Salt Lake and St. George. The extremely low unemployment (2.87%) reflects a strong economy, but much of that employment was construction-driven, meaning the labor market was exposed to a housing downturn. Comparable states: Idaho (39.45% appreciation, 7.72 pop growth, crashed -26.95) had a similar growth profile but much higher appreciation. Minnesota (-21.83 with 24.94% appreciation, 2.18 pop growth) had similar appreciation but lower pop growth. Utah's high pop growth amplifies the effect beyond MN, but lower appreciation than ID moderates it. Net result lands around -20%.

### SD (South Dakota) — predicted: **-5.0**

A low-population plains/agricultural state with modest appreciation (17.95%), very low unemployment (3.01%), and moderate pop growth (2.53%). SD's housing market is small and largely driven by fundamental demand rather than speculation. Closest comparables: ND (22.30% appreciation, 0.00 crash) benefited from the Bakken oil boom that SD lacked; KS (-4.97 with 12.49% appreciation) and NE (-2.88 with 11.88%) are similar plains economies but had lower appreciation. SD's slightly higher appreciation nudges it past NE/KS but nowhere near the southern states (AL, TN, MS at -8% to -10%) that had different structural exposures.

### WA (Washington) — predicted: **-22.0**

High appreciation (42.91%) with moderate pop growth (4.37%) and moderate unemployment (4.99%). The most natural comparison is Oregon (44.87% appreciation, 3.48 pop growth, crashed -25.98), its Pacific Northwest neighbor. Washington's tech sector (Microsoft, Amazon, Boeing) provides meaningfully more economic resilience than Oregon's economy, which should moderate the crash by a few percentage points. However, areas outside Seattle (Spokane, Tacoma, eastern WA) lacked that tech cushion. The appreciation level places WA firmly in the -20% to -25% crash band for medium-high appreciation states.

### IL (Illinois) — predicted: **-16.0**

Moderate appreciation (25.87%), low pop growth (0.70%), moderate unemployment (4.62%), and high income (40021). Chicago's south side and south suburbs had significant subprime exposure. Comparables: Massachusetts (-17.56 with 28.21% appreciation, -0.19 pop growth) is the closest match by profile; Wisconsin (-11.81 with 22.65% appreciation) represents the lower bound; Minnesota (-21.83 with 24.94% appreciation, 2.18 pop growth) represents the upper bound. IL's low pop growth limits overbuilding exposure, but Chicago's subprime concentration pushes the crash past WI levels. I place it between WI and MA, leaning toward MA given the subprime factor.

### MO (Missouri) — predicted: **-10.0**

Moderate appreciation (18.82%), moderate pop growth (2.33%), moderate unemployment (4.89%). A classic Midwestern profile. St. Louis and Kansas City are the main housing markets, neither of which had extreme bubble dynamics. Very similar to Alabama (18.37% appreciation, 2.79 pop growth, crash -9.90) and Tennessee (17.18% appreciation, 4.12 pop growth, crash -8.92). MO's slightly higher appreciation than TN and similar pop growth to AL puts it right at -10%.

### NY (New York) — predicted: **-12.0**

High appreciation (40.29%) but negative pop growth (-0.37%) and high income (43760). NYC is one of the most supply-constrained housing markets in the country, which structurally limits downside, similar to how Hawaii (-18.48 despite 80.67% appreciation) and DC (-11.93 despite 70.23%) were dampened. However, the 2008 financial sector collapse hit NYC employment directly, and areas outside NYC (Long Island, Hudson Valley, upstate) lacked supply constraints. Vermont (-6.55 with 41.92% appreciation, 0.81 pop growth) shows how high appreciation with low growth can produce mild crashes in constrained markets. Connecticut (-18.76 with 36.58% appreciation) shows the downside for Northeast corridor states. NY's supply constraints and high income push toward the mild end of this range.

### LA (Louisiana) — predicted: **-6.0**

Moderate appreciation (22.89%) but extremely negative pop growth (-4.83%), driven entirely by Hurricane Katrina (August 2005). Katrina destroyed massive housing stock, reducing supply and creating scarcity that supported prices even as the national market declined. Post-Katrina federal reconstruction spending and insurance payouts injected capital. Louisiana's oil and gas sector provided additional insulation (similar to Alaska at 0.00 and North Dakota at 0.00). Without Katrina, Louisiana's profile would suggest a crash around -10% based on appreciation level; the supply destruction and energy sector together moderate this to roughly -6%.

### NC (North Carolina) — predicted: **-13.0**

Low-moderate appreciation (16.94%) but high pop growth (5.87%). The Charlotte metro (banking hub: Bank of America, Wachovia) had financial sector exposure; Raleigh-Durham (Research Triangle) was more resilient. Comparables: South Carolina (-13.02 with 19.42% appreciation, 5.00 pop growth) is the closest match. Georgia (-24.38 with 15.17% appreciation, 6.18 pop growth) represents the worst case for this profile, but Atlanta's extreme subprime exposure was exceptional. Texas (-4.15 with 11.68% appreciation, 6.03 pop growth) shows how regulatory protections can insulate high-growth states. NC lacks Texas's regulatory protections but has better economic diversification than GA. I place NC near SC's -13%.

### AR (Arkansas) — predicted: **-8.0**

Moderate appreciation (20.02%), moderate-high unemployment (5.23%), low income (29376), and moderate pop growth (3.56%). Arkansas's low income limits speculative mortgage activity; the housing market is small and fundamentals-driven. Very similar to Tennessee (-8.92 with 17.18% appreciation, 5.22 UR, 32878 income, 4.12 pop growth). AR has slightly higher appreciation but slightly lower pop growth than TN, and lower income limits exposure. Mississippi (-8.67 with 16.40% appreciation) confirms the range. I place AR at -8%.

### NM (New Mexico) — predicted: **-15.0**

Moderate-high appreciation (32.57%), moderate pop growth (4.50%), and low income (30433). Sun Belt location adjacent to Arizona's catastrophic bubble, but NM's market was much smaller and less speculative. Government employment (Los Alamos, Sandia, military bases) provided some stability. Comparables: Montana (-10.06 with 36.61% appreciation, 3.60 pop growth) is the closest match but had lower pop growth and possible energy sector support. New Hampshire (-19.98 with 31.83% appreciation, 2.23 pop growth) had lower pop growth but crashed worse, partly due to Boston-area spillover dynamics. NM's higher pop growth than MT but Sun Belt dynamics land it between MT and NH, around -15%.

### IN (Indiana) — predicted: **-9.0**

Very low appreciation (8.68%), moderate unemployment (5.02%), and moderate pop growth (2.20%). Rust Belt state with auto industry exposure, but less dependent on manufacturing than Michigan (8.86% appreciation, 6.87 UR, crashed -29.40) or Ohio (9.43% appreciation, 5.43 UR, crashed -12.93). Indianapolis provided economic diversification (healthcare, logistics, finance). Indiana's lower unemployment than OH/MI suggests less structural vulnerability. Comparables: Ohio crashed -12.93 with similar appreciation but worse unemployment; Kansas crashed -4.97 with slightly higher appreciation but better unemployment. IN sits between these, with some auto industry drag but diversified enough to avoid OH-level damage.

---

## Final Predictions

```json
[
  {"state": "UT", "predicted_crash_pct": -20.00},
  {"state": "SD", "predicted_crash_pct": -5.00},
  {"state": "WA", "predicted_crash_pct": -22.00},
  {"state": "IL", "predicted_crash_pct": -16.00},
  {"state": "MO", "predicted_crash_pct": -10.00},
  {"state": "NY", "predicted_crash_pct": -12.00},
  {"state": "LA", "predicted_crash_pct": -6.00},
  {"state": "NC", "predicted_crash_pct": -13.00},
  {"state": "AR", "predicted_crash_pct": -8.00},
  {"state": "NM", "predicted_crash_pct": -15.00},
  {"state": "IN", "predicted_crash_pct": -9.00}
]
```
