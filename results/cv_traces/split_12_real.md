## Analysis Framework

I'll identify key patterns in the training data, then apply them to each held-out state.

### Key Patterns from Training Data

**1. Appreciation is the primary crash driver, but not linearly.** States above ~70% appreciation saw catastrophic declines (-41% to -56%), while states below ~15% generally stayed above -10%.

**2. Population growth amplifies bubbles.** High appreciation + high pop growth = speculative overbuilding, which is the mechanism that creates oversupply. The three worst crashes (NV, FL, AZ) all combined >73% appreciation with >6.8% pop growth.

**3. Supply constraints buffer high-appreciation markets.** DC had 70.23% appreciation but only -11.93% decline. Its constrained geography + government-driven demand meant appreciation reflected genuine scarcity, not just speculation.

**4. Industrial weakness can crash prices independent of bubbles.** Michigan had only 8.86% appreciation but crashed -29.40% because the auto industry collapsed, destroying demand fundamentals.

**5. Agriculture/resource economies are insulated.** AK (oil), ND (oil/ag), IA (ag) all posted 0.00% declines despite modest appreciation. Commodity-driven economies had their own demand cycle.

---

## State-by-State Predictions

### HI (Hawaii)
**Features:** 80.67% appreciation (highest in dataset), 2.57% UR (lowest in dataset), $38,315 income, 4.68% pop growth

Hawaii has the highest appreciation of any state, exceeding even Nevada (79.74 → -55.69). However, Hawaii is fundamentally different from the sand states:

- **Island supply constraint**: Unlike the Inland Empire or Phoenix exurbs, you cannot build subdivisions across an ocean. This is the DC dynamic (70.23% appreciation → -11.93%) applied at state scale.
- **Lowest UR in the dataset** (2.57%) signals a fundamentally healthy economy, not one propped up by construction jobs.
- **Military + tourism** provide a durable demand floor, though tourism is cyclical and cratered in 2008-2009.
- **Pop growth (4.68%)** is moderate, between CA (2.18%) and FL (6.84%).

Comps: CA (73.96 → -41.04) is the nearest in appreciation, but CA had massive elastic supply (Central Valley, Inland Empire). MD (65.16 → -25.30) is a better structural comp: high appreciation, supply-constrained suburbs near a government center. Hawaii's supply constraint is more extreme than MD's, but its appreciation is also much higher.

**Prediction: -27.00**

---

### WI (Wisconsin)
**Features:** 22.65% appreciation, 4.69% UR, $36,047 income, 1.80% pop growth

Midwest manufacturing + agriculture state. The key comps are neighboring states:

- **MN** (24.94 → -21.83): Slightly higher appreciation, lower UR. Twin Cities drove MN's bubble with concentrated subprime lending and suburban construction.
- **MO** (18.82 → -10.97): Lower appreciation, similar UR. St. Louis had modest exposure.
- **IL** (25.87 → -21.81): Higher appreciation, Chicago-driven subprime concentration.

WI's appreciation (22.65%) falls between MO and MN. Its pop growth (1.80%) is low, suggesting less speculative construction. Milwaukee didn't experience the concentrated boom that Minneapolis or Chicago did. WI should fall meaningfully below MN/IL but above MO.

**Prediction: -15.00**

---

### NE (Nebraska)
**Features:** 11.88% appreciation, 3.04% UR, $35,718 income, 1.96% pop growth

Agricultural Great Plains state. Strikingly, NE has identical appreciation to CO (11.88%) but a much lower UR (3.04% vs 4.25%) and less metro concentration.

- **IA** (13.29 → 0.00): Neighboring ag state, slightly higher appreciation, 3.69% UR. No decline at all.
- **KS** (12.49 → -4.97): Neighboring state, similar appreciation, higher UR (4.42%).
- **ND** (22.30 → 0.00): Great Plains, much higher appreciation but oil-supported.

NE's combination of low appreciation, very low UR, and stable agricultural economy places it firmly in the resilient category. Between IA (0.00) and KS (-4.97), closer to IA given the lower UR.

**Prediction: -3.00**

---

### SD (South Dakota)
**Features:** 17.95% appreciation, 3.01% UR, $34,983 income, 2.53% pop growth

Another Great Plains agricultural state, neighboring ND (22.30 → 0.00) and IA (13.29 → 0.00). SD has the second-lowest UR in the held-out set. However, unlike ND, SD lacks the Bakken oil boom that provided an economic tailwind from 2006 onward.

Comps in the 15-20% appreciation range with low UR are scarce, but:
- **AL** (18.37, 4.01% UR → -9.90): Higher UR, similar appreciation.
- **KY** (14.25, 5.73% UR → -4.45): Lower appreciation, much higher UR.

SD's extremely low UR and ag economy should protect it, but the 17.95% appreciation is higher than IA/KS, and without ND's oil tailwind, some decline is likely. Modest.

**Prediction: -5.00**

---

### SC (South Carolina)
**Features:** 19.42% appreciation, 6.35% UR, $30,789 income, 5.00% pop growth

SC has a troubling combination: moderate appreciation, the second-highest UR in the held-out set (matching MS at 6.38), low income, and significant in-migration.

- **NC** (16.94, 4.73% UR → -13.06): Lower appreciation, lower UR, similar pop growth (5.87%). NC's Research Triangle anchored its economy.
- **MS** (16.40, 6.38% UR → -8.67): Similar UR but lower appreciation and much lower pop growth (1.28%).
- **GA** (15.17, 4.66% UR → -24.38): Lower appreciation but crushed by Atlanta subprime. SC doesn't have a comparable metro.

SC's coastal markets (Myrtle Beach, Hilton Head) had speculative investment, and the high UR + low income + moderate pop growth suggest vulnerability beyond what appreciation alone indicates. Worse than NC, but without GA's concentrated subprime exposure.

**Prediction: -15.00**

---

### TN (Tennessee)
**Features:** 17.18% appreciation, 5.22% UR, $32,878 income, 4.12% pop growth

Southern state with Nashville and Memphis metros. Moderate across all features.

- **AL** (18.37, 4.01% UR → -9.90): Slightly higher appreciation, lower UR.
- **NC** (16.94, 4.73% UR → -13.06): Nearly identical appreciation, slightly lower UR, higher pop growth.
- **MO** (18.82, 4.89% UR → -10.97): Similar appreciation and UR.
- **AR** (20.02, 5.23% UR → -6.70): Higher appreciation, nearly identical UR, but much lower pop growth.

TN's UR (5.22%) is higher than NC, AL, and MO, which adds vulnerability. But appreciation is moderate and pop growth isn't extreme. Nashville's diversifying economy provided some floor. Comparable to AL/MO range.

**Prediction: -10.00**

---

### NJ (New Jersey)
**Features:** 48.76% appreciation, 4.69% UR, $47,366 income, 0.70% pop growth

NJ sits in the upper-middle tier of appreciation. Key tension: high bubble + supply-constrained Northeast metro + significant subprime exposure in urban centers (Newark, Camden, Trenton).

- **NY** (40.29, 4.50% UR → -14.02): Lower appreciation, similar UR, negative pop growth. NYC's extreme supply constraint anchored NY.
- **DE** (45.63, 3.58% UR → -20.44): Similar appreciation, much lower UR.
- **VA** (53.63, 3.08% UR → -17.39): Higher appreciation, much lower UR, higher pop growth.
- **CT** (36.58, 4.42% UR → -18.76): Lower appreciation, similar UR.

NJ's very low pop growth (0.70%) should moderate overbuilding, similar to NY. But NJ's appreciation is significantly higher than NY's (48.76 vs 40.29), and NJ had concentrated subprime exposure in urban areas that NYC's Manhattan-anchored market didn't share. NJ's higher income provides some buffer but high property tax burden amplifies distress for underwater homeowners.

**Prediction: -23.00**

---

### VT (Vermont)
**Features:** 41.92% appreciation, 3.68% UR, $36,609 income, 0.81% pop growth

Rural New England state with high appreciation but minimal speculative construction.

- **NY** (40.29, 4.50% UR → -14.02): Nearly identical appreciation, higher UR, negative pop growth.
- **WA** (42.91, 4.99% UR → -25.19): Nearly identical appreciation, but much higher pop growth (4.37%) driving overbuilding.
- **ME** (34.89, 4.71% UR → -13.11): Lower appreciation, higher UR, rural New England peer.

The critical pattern: states with ~40-43% appreciation show wildly different outcomes depending on pop growth. WA/OR (high pop growth) crashed -25 to -26%. NY (negative pop growth) crashed only -14%. VT's 0.81% pop growth is much closer to NY's pattern, meaning the appreciation was more demand-driven than construction-driven. Rural character limits speculative building further.

**Prediction: -15.00**

---

### OK (Oklahoma)
**Features:** 14.28% appreciation, 3.91% UR, $34,650 income, 2.54% pop growth

Energy (oil and gas) and agriculture economy. Classic resilient profile.

- **TX** (11.68, 4.98% UR → -4.15): Fellow energy state, lower appreciation, higher UR.
- **KS** (12.49, 4.42% UR → -4.97): Neighboring state, lower appreciation, higher UR.
- **KY** (14.25, 5.73% UR → -4.45): Nearly identical appreciation, much higher UR.
- **LA** (22.89, 4.14% UR → -4.21): Energy state, higher appreciation.

All four comps cluster tightly around -4% to -5%. OK fits squarely in this group: energy-supported economy, low appreciation, low UR. No reason to deviate from the cluster.

**Prediction: -5.00**

---

### RI (Rhode Island)
**Features:** 48.54% appreciation, 5.26% UR, $38,719 income, -0.77% pop growth

RI has the most concerning combination in the held-out set: high appreciation, high unemployment, declining population. This is a bubble built on a weak economic foundation with eroding demand.

- **OR** (44.87, 5.39% UR → -25.98): Similar appreciation and UR, but OR had positive pop growth (3.48%) providing some demand support.
- **MA** (28.21, 4.69% UR → -17.56): Lower appreciation, lower UR, negative pop growth.
- **MI** (8.86, 6.87% UR → -29.40): Much lower appreciation but proves that economic weakness alone can drive severe crashes.

RI's bubble (48.54%) is larger than OR's (44.87%), and RI's declining population means no new demand to absorb distressed inventory. The high UR signals manufacturing decline and subprime vulnerability. Unlike NJ (similar appreciation but 0.70% positive pop growth and much higher income), RI has no buffers. This should be one of the worst-performing states in the held-out set.

**Prediction: -28.00**

---

### OH (Ohio)
**Features:** 9.43% appreciation, 5.43% UR, $33,976 income, 0.41% pop growth

Rust Belt state with minimal bubble but significant economic vulnerability. The question is whether OH follows IN (mild decline) or MI (catastrophic decline despite no bubble).

- **IN** (8.68, 5.02% UR → -7.30): Similar appreciation, slightly lower UR.
- **MI** (8.86, 6.87% UR → -29.40): Similar appreciation, much higher UR. MI's crash was driven by the auto industry collapse.

OH's UR (5.43%) sits between IN (5.02%) and MI (6.87%), much closer to IN. Ohio shared some of Michigan's manufacturing decline (Toledo, Akron) but wasn't ground zero for the auto collapse. Cleveland had significant subprime exposure, but Columbus was relatively resilient. Stagnant pop growth (0.41%) means weak demand but also minimal overbuilding.

OH should be worse than IN but far better than MI. The Cleveland subprime factor pushes it moderately above IN.

**Prediction: -12.00**

---

## Final Predictions

```json
[
  {"state": "HI", "predicted_crash_pct": -27.00},
  {"state": "WI", "predicted_crash_pct": -15.00},
  {"state": "NE", "predicted_crash_pct": -3.00},
  {"state": "SD", "predicted_crash_pct": -5.00},
  {"state": "SC", "predicted_crash_pct": -15.00},
  {"state": "TN", "predicted_crash_pct": -10.00},
  {"state": "NJ", "predicted_crash_pct": -23.00},
  {"state": "VT", "predicted_crash_pct": -15.00},
  {"state": "OK", "predicted_crash_pct": -5.00},
  {"state": "RI", "predicted_crash_pct": -28.00},
  {"state": "OH", "predicted_crash_pct": -12.00}
]
```
