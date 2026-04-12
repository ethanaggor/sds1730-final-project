## Approach

I'll build a mental model from the training data by identifying how each feature relates to crash severity, then apply it state by state.

### Key Patterns in Training Data

**1. Appreciation is the strongest single predictor, but not sufficient alone.**
The four extreme crashes (NV -55.7, AZ -46.0, FL -44.7, CA -41.0) all had appreciation >70%. But HI (80.7% appreciation) crashed only -18.5%, and DC (70.2%) only -11.9%. Something else modulates the relationship.

**2. Population growth amplifies bubbles into crashes.**
High appreciation + high pop growth = catastrophic crash. This combination signals speculative overbuilding, not just price inflation:
- NV: 79.7% appreciation + 12.2% pop growth → -55.7%
- AZ: 73.4% + 9.4% → -46.0%
- FL: 74.4% + 6.8% → -44.7%

Low/negative pop growth moderates even very high appreciation:
- DC: 70.2% appreciation + 0.4% pop → -11.9%
- PA: 34.1% + 1.1% → -9.4%

**3. Economic anchors (government, oil, supply constraints) provide floors.**
- DC: government employment → -11.9% despite 70% appreciation
- AK: oil economy → 0.0% despite 36% appreciation
- HI: island supply constraint → -18.5% despite 81% appreciation

**4. Industrial distress causes crashes without bubbles.**
- MI: only 8.9% appreciation but -29.4% crash (auto industry collapse)
- GA: only 15.2% appreciation but -24.4% crash (Atlanta subprime concentration + overbuilding)

**5. Plains/Midwest stability.** SD (0.0%), IA (0.0%), NE (-2.9%) show that low-appreciation, stable-population, agricultural-economy states weathered the crisis.

---

## State-by-State Predictions

### ID (Idaho)
- Appreciation: 39.45%, UR: 3.39%, PCPI: $31,244, Pop growth: 7.72%

**Key comps:**
- UT (23.4% appreciation, 7.0% pop → -21.9%): Similar high pop growth pattern, but ID has much higher appreciation
- OR (44.9%, 3.5% → -26.0%): Similar appreciation, but ID has double the pop growth
- WA (42.9%, 4.4% → -25.2%): Similar appreciation, but ID has higher pop growth and lower income

Idaho's Boise metro was a textbook speculative-growth market: rapid in-migration, construction boom, low-income residents stretching to buy into rising prices. The combination of 39.5% appreciation with 7.7% pop growth (third highest after NV and AZ in the training set) and low income ($31,244) creates a profile worse than UT but less extreme than the Sun Belt bubble states. Higher pop growth than OR/WA offsets the slightly lower appreciation.

**Prediction: -27.0%**

---

### MA (Massachusetts)
- Appreciation: 28.21%, UR: 4.69%, PCPI: $47,311, Pop growth: -0.19%

**Key comps:**
- CT (36.6%, 0.95% pop, $53K → -18.8%): Higher appreciation, similar low pop growth
- NH (31.8%, 2.2% → -20.0%): Similar appreciation but higher pop growth
- NJ (48.8%, 0.7%, $47K → -22.1%): Much higher appreciation, similar income

MA's appreciation (28.2%) is the lowest among comparable Northeast states. The very high income ($47,311) and negative pop growth are strongly protective. Boston's market is supply-constrained with strong fundamentals (education, healthcare, biotech). However, outer suburbs and former mill towns (Lawrence, New Bedford) had genuine subprime exposure, pulling the statewide figure down.

Lower appreciation than all Northeast comps, combined with negative pop growth and high income, suggests MA should fare better than CT/NH/NJ.

**Prediction: -15.0%**

---

### VT (Vermont)
- Appreciation: 41.92%, UR: 3.68%, PCPI: $36,609, Pop growth: 0.81%

**Key comps:**
- ME (34.9%, 1.3% → -13.1%): Similar rural New England profile, lower appreciation
- WY (34.9%, 3.8% → -7.7%): Similar appreciation but much higher income ($43,805)
- OR (44.9%, 3.5% → -26.0%): Similar appreciation but much higher pop growth

VT's 41.9% appreciation is high, matching WA/OR territory. Every training state above 40% appreciation crashed at least -11.9% (DC). But VT's very low pop growth (0.81%) is a powerful moderating force: it means minimal speculative overbuilding. The market is small and rural, with appreciation partly driven by second homes (ski areas) rather than broad speculation. Second homes add volatility in downturns (discretionary purchases get cut), but the lack of overbuilding limits supply overhang.

VT sits between ME (lower appreciation, similar dynamics → -13.1%) and the more urbanized Northeast states. Higher appreciation than ME pushes it worse; lower pop growth than NH (-20.0%) pulls it back.

**Prediction: -15.0%**

---

### VA (Virginia)
- Appreciation: 53.63%, UR: 3.08%, PCPI: $42,164, Pop growth: 4.16%

**Key comps:**
- MD (65.2%, 2.4% → -25.3%): Higher appreciation, lower pop growth, both DC corridor
- DC (70.2%, 0.4% → -11.9%): Government anchor effect
- NJ (48.8%, 0.7% → -22.1%): Lower appreciation, much lower pop growth

VA's 53.6% appreciation is very high, sitting between NJ (48.8%) and MD (65.2%). The Northern Virginia bubble (Loudoun, Prince William counties) was driven by DC corridor spillover and speculation. Pop growth of 4.16% is significantly higher than MD's 2.39%, which offsets the lower appreciation.

The government/defense employment anchor provides some floor (like DC), but Virginia is a much more diverse state than DC. Hampton Roads (military) adds stability, but the statewide figure includes heavily exposed suburban markets. VA should crash somewhat less than MD (lower appreciation) but more than NJ (higher pop growth offsets slightly higher NJ appreciation).

**Prediction: -24.0%**

---

### NM (New Mexico)
- Appreciation: 32.57%, UR: 4.23%, PCPI: $30,433, Pop growth: 4.50%

**Key comps:**
- MN (24.9%, 2.2% → -21.8%): Lower appreciation but Midwest subprime exposure
- NC (16.9%, 5.9% → -13.1%): Lower appreciation, higher pop growth
- ME (34.9%, 1.3% → -13.1%): Similar appreciation, lower pop growth
- NH (31.8%, 2.2% → -20.0%): Similar appreciation, lower pop growth

NM has moderate appreciation with moderate pop growth and the second-lowest income in the held-out set. The Albuquerque market had meaningful subprime exposure, and the low income base ($30,433) means households were more stretched. The Santa Fe luxury market is a different dynamic (second homes, amenity buyers) that adds some volatility.

Higher pop growth than ME/NH but lower appreciation than the severe crash states. Low income adds vulnerability relative to wealthier states with similar appreciation.

**Prediction: -18.0%**

---

### IL (Illinois)
- Appreciation: 25.87%, UR: 4.62%, PCPI: $40,021, Pop growth: 0.70%

**Key comps:**
- MN (24.9%, 2.2% → -21.8%): Very similar appreciation, higher pop growth
- WI (22.7%, 1.8% → -11.8%): Similar appreciation, similar pop growth
- MO (18.8%, 2.3% → -11.0%): Lower appreciation

IL is anchored by Chicago, where the south and west suburbs had severe subprime concentration. The MN vs. WI divergence (-21.8% vs -11.8% with very similar appreciation) demonstrates that local subprime exposure and economic structure dominate at moderate appreciation levels.

IL's very low pop growth (0.70%) is a strong moderating factor, but Chicago's manufacturing decline and subprime pockets in Harvey, Park Forest, and other south suburbs push the crash higher. The statewide figure is moderated by the more stable downstate markets. IL falls between WI and MN: worse than WI due to Chicago's subprime issues, better than MN due to lower pop growth.

**Prediction: -17.0%**

---

### WV (West Virginia)
- Appreciation: 25.64%, UR: 4.77%, PCPI: $28,528, Pop growth: 0.86%

**Key comps:**
- KY (14.3%, 2.5% → -4.5%): Similar economic profile, lower appreciation
- MS (16.4%, 1.3% → -8.7%): Similar poor-state dynamics
- AR (20.0%, 3.6% → -6.7%): Similar appreciation range
- PA (34.1%, 1.1% → -9.4%): Higher appreciation, similar pop growth

WV is the lowest-income state in either dataset. The 25.6% appreciation is somewhat surprising for such a poor state, but this reflects the low price base (small absolute dollar increases produce large percentage gains). Very low pop growth means no overbuilding. The housing market is small, illiquid, and largely non-speculative.

The low income increases household vulnerability to economic stress, but the minimal speculation limits the crash mechanism. WV fits between the mild-crash Appalachian/Southern states (KY, AR) and the moderate PA figure.

**Prediction: -9.0%**

---

### ND (North Dakota)
- Appreciation: 22.30%, UR: 3.12%, PCPI: $33,120, Pop growth: 1.66%

**Key comps:**
- SD (18.0%, 2.5% → 0.0%): Very similar Plains state, lower appreciation
- IA (13.3%, 1.4% → 0.0%): Midwest stability benchmark
- AK (36.1%, 4.2% → 0.0%): Energy economy buffer
- NE (11.9%, 2.0% → -2.9%): Plains baseline

ND's critical differentiator is the Bakken oil boom, which accelerated sharply from 2008 to 2012, precisely during the national housing downturn. This created a massive surge in housing demand (oil field workers) that supported or increased prices while the rest of the country declined. This is directly analogous to AK's oil economy buffer.

SD, a neighboring Plains state without the oil boom, showed 0.0% decline at 18.0% appreciation. ND's higher appreciation (22.3%) creates some vulnerability, but the oil boom more than compensates. Very low UR (3.12%) and stable Plains economy add resilience.

**Prediction: -2.0%**

---

### NY (New York)
- Appreciation: 40.29%, UR: 4.50%, PCPI: $43,760, Pop growth: -0.37%

**Key comps:**
- NJ (48.8%, 0.7% → -22.1%): Higher appreciation, similar corridor state
- CT (36.6%, 0.95% → -18.8%): Lower appreciation, similar dynamics
- RI (48.5%, -0.8% → -27.6%): Higher appreciation, similar negative pop growth

NY is dominated by the NYC metro area. Manhattan is one of the most supply-constrained housing markets in the world, which limits downside. But the state also includes Long Island (severe subprime exposure, significant crash), Westchester (expensive suburban decline), and upstate markets (economically weak, moderate declines).

The negative pop growth and very high income are protective. NY's 40.3% appreciation is between CT (36.6% → -18.8%) and NJ (48.8% → -22.1%). The negative pop growth and NYC anchor should produce a better outcome than the simple appreciation level suggests.

**Prediction: -16.0%**

---

### DE (Delaware)
- Appreciation: 45.63%, UR: 3.58%, PCPI: $40,736, Pop growth: 5.04%

**Key comps:**
- OR (44.9%, 3.5% → -26.0%): Nearly identical appreciation, lower pop growth
- WA (42.9%, 4.4% → -25.2%): Similar appreciation, slightly lower pop growth
- MD (65.2%, 2.4% → -25.3%): Much higher appreciation, lower pop growth
- NJ (48.8%, 0.7% → -22.1%): Similar appreciation, much lower pop growth

DE's 45.6% appreciation with 5.0% pop growth is a concerning combination. Delaware's beach communities (Rehoboth, Dewey) saw significant speculation, and the Wilmington suburbs tracked the broader Philadelphia/DC corridor bubble. The pop growth is higher than any comparable state at this appreciation level (OR 3.5%, WA 4.4%).

OR crashed -26.0% with nearly identical appreciation and 1.5 percentage points less pop growth. DE's higher pop growth and beach market speculation suggest at least as severe a correction as OR.

**Prediction: -26.0%**

---

### MT (Montana)
- Appreciation: 36.61%, UR: 3.37%, PCPI: $31,870, Pop growth: 3.60%

**Key comps:**
- WY (34.9%, 3.8% → -7.7%): Most similar; both rural Western resource states
- ME (34.9%, 1.3% → -13.1%): Same appreciation, lower pop growth, different region
- AK (36.1%, 4.2% → 0.0%): Similar appreciation, but oil economy outlier

MT and WY share a profile: rural Western states, similar appreciation (~35-37%), similar pop growth (~3.6-3.8%), low UR. The critical difference is income: WY at $43,805 has a much stronger economic floor from energy/mining revenue than MT at $31,870.

MT's lower income means less economic resilience and more household vulnerability. Markets like Bozeman and Missoula attracted amenity migrants, creating localized bubbles. MT should crash more than WY (-7.7%) due to the weaker economic base, but the rural market structure and moderate pop growth limit the severity. ME at -13.1% provides an upper bound for states with this appreciation level and low-moderate pop growth.

**Prediction: -12.0%**

---

## Final Predictions

```json
[
  {"state": "ID", "predicted_crash_pct": -27.00},
  {"state": "MA", "predicted_crash_pct": -15.00},
  {"state": "VT", "predicted_crash_pct": -15.00},
  {"state": "VA", "predicted_crash_pct": -24.00},
  {"state": "NM", "predicted_crash_pct": -18.00},
  {"state": "IL", "predicted_crash_pct": -17.00},
  {"state": "WV", "predicted_crash_pct": -9.00},
  {"state": "ND", "predicted_crash_pct": -2.00},
  {"state": "NY", "predicted_crash_pct": -16.00},
  {"state": "DE", "predicted_crash_pct": -26.00},
  {"state": "MT", "predicted_crash_pct": -12.00}
]
```
