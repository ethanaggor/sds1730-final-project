## Approach

I'll identify the most comparable training states for each held-out state across all four features, then use the crash outcomes of those comps, weighted by similarity, to form predictions. I'll also apply economic reasoning about bubble dynamics, labor market vulnerability, and income resilience.

### Key patterns in the training data

Before diving in, a few observations about the training set:

1. **Income is the clearest signal.** Low-income states (<$32K) average roughly -20% crash; high-income states (>$40K) average roughly -12%.
2. **Appreciation is surprisingly noisy.** The biggest bubble states (NV, FL, HI at 74-81% appreciation) had mild crashes (-4 to -7%), while low-appreciation states like KY (14%) and SD (18%) had severe ones (-45%, -28%). Bubble size alone is not predictive here.
3. **Pop growth among high-appreciation states matters.** NV (12.2% pop, -4.5%), FL (6.8% pop, -7.3%), and CA (2.2% pop, -21.8%) suggest that demand fundamentals (migration) cushioned bubble markets, while CA's lower growth left it more exposed.
4. **Three extreme outliers** (ME -55.7, KY -44.7, UT -41.0) share low income but otherwise vary widely, suggesting unobserved local factors.

---

## State-by-State Reasoning

### AR (Arkansas)
**Features:** appr 20.0, ur 5.23, pcpi $29,376, pop 3.56

Arkansas is a low-income Southern state with moderate appreciation and above-average unemployment. Closest comps:
- **TN** (appr 17.2, ur 5.22, pcpi $32,878, pop 4.12): -13.1 -- nearly identical UR and similar appreciation/pop growth
- **AL** (appr 18.4, ur 4.01, pcpi $31,264, pop 2.79): -11.0 -- similar appreciation and income, lower UR
- **MS** (appr 16.4, ur 6.38, pcpi $27,827, pop 1.28): -9.4 -- similar low income tier

AR has the lowest income in the test set, which is a risk factor, but its features cluster tightly with TN and AL. KY (-44.7) is a potential comp by income/UR but appears to be a severe outlier.

**Prediction: -12.0**

---

### MN (Minnesota)
**Features:** appr 24.9, ur 4.06, pcpi $39,362, pop 2.18

A Midwest state with moderate appreciation, solid income, and below-average unemployment. Comps:
- **WI** (appr 22.7, ur 4.69, pcpi $36,047, pop 1.80): 0.0 -- similar Midwest state, MN has lower UR and higher income
- **IL** (appr 25.9, ur 4.62, pcpi $40,021, pop 0.70): -15.7 -- nearly identical appreciation and income
- **ND** (appr 22.3, ur 3.12, pcpi $33,120, pop 1.66): -10.1 -- similar appreciation, lower income

MN sits between WI's resilience and IL's moderate crash. Its better unemployment rate relative to IL and higher income relative to ND and WI suggest it would land in the middle of this cluster.

**Prediction: -10.0**

---

### NH (New Hampshire)
**Features:** appr 31.8, ur 3.52, pcpi $42,866, pop 2.23

A wealthy New England state with moderate appreciation and low unemployment. Comps:
- **MA** (appr 28.2, ur 4.69, pcpi $47,311, pop -0.19): 0.0 -- neighboring, slightly lower appreciation, higher income
- **VT** (appr 41.9, ur 3.68, pcpi $36,609, pop 0.81): -10.1 -- neighboring, higher appreciation, lower income
- **PA** (appr 34.1, ur 4.73, pcpi $37,803, pop 1.10): -11.8 -- similar appreciation, lower income

NH's income ($42.9K) is well above VT ($36.6K) and PA ($37.8K), approaching MA territory. Its low UR reinforces resilience. ME (-55.7) is geographically close but appears to be an extreme outlier unrelated to fundamentals. NH should land between MA and VT.

**Prediction: -7.0**

---

### KS (Kansas)
**Features:** appr 12.5, ur 4.42, pcpi $35,411, pop 1.47

A Great Plains state with very low appreciation and moderate economics. Comps:
- **OK** (appr 14.3, ur 3.91, pcpi $34,650, pop 2.54): 0.0 -- neighboring, very similar features
- **NE** (appr 11.9, ur 3.04, pcpi $35,718, pop 1.96): -3.6 -- nearly identical appreciation and income
- **TX** (appr 11.7, ur 4.98, pcpi $35,422, pop 6.03): -2.9 -- similar appreciation and income
- **IA** (appr 13.3, ur 3.69, pcpi $34,197, pop 1.38): -13.0 -- similar features but much worse outcome

KS clusters most tightly with OK and NE, both of which had minimal crashes. Its slightly higher UR than OK/NE pulls it somewhat worse. IA is a cautionary comp, but the central tendency of KS's nearest neighbors is mild.

**Prediction: -6.0**

---

### CT (Connecticut)
**Features:** appr 36.6, ur 4.42, pcpi $53,224, pop 0.95

A very wealthy Northeast state with moderate-high appreciation. Comps:
- **MA** (appr 28.2, ur 4.69, pcpi $47,311, pop -0.19): 0.0
- **NJ** (appr 48.8, ur 4.69, pcpi $47,366, pop 0.70): -7.3
- **NY** (appr 40.3, ur 4.50, pcpi $43,760, pop -0.37): -9.9
- **DC** (appr 70.2, ur 5.83, pcpi $55,384, pop 0.38): -4.2

CT has the second-highest income in the combined dataset, behind only DC. Its appreciation (36.6%) is between MA (28.2%) and NY (40.3%). Among the high-income Northeast cluster, the crash range is 0 to -10. CT's very high income and moderate UR suggest it should land in the milder part of this range.

**Prediction: -7.0**

---

### AZ (Arizona)
**Features:** appr 73.4, ur 4.27, pcpi $34,460, pop 9.41

A classic sand-state bubble with very high appreciation and very high population growth. Comps:
- **FL** (appr 74.4, ur 3.28, pcpi $38,009, pop 6.84): -7.3 -- nearly identical appreciation, high pop growth
- **NV** (appr 79.7, ur 4.17, pcpi $39,437, pop 12.18): -4.5 -- similar UR and very high pop growth
- **CA** (appr 74.0, ur 4.89, pcpi $41,454, pop 2.18): -21.8 -- same appreciation but much lower pop growth

The critical pattern among high-appreciation states: pop growth appears to cushion the crash (NV > FL > CA in pop growth; NV < FL < CA in crash severity). AZ's 9.4% pop growth slots between FL and NV, pointing toward -5 to -7. However, AZ's income ($34.5K) is notably below FL ($38K), NV ($39.4K), and CA ($41.5K), adding vulnerability. This lower-income penalty pushes the prediction a few points worse.

**Prediction: -10.0**

---

### WY (Wyoming)
**Features:** appr 34.9, ur 3.07, pcpi $43,805, pop 3.82

A high-income, low-unemployment energy state with moderate appreciation. Comps:
- **MT** (appr 36.6, ur 3.37, pcpi $31,870, pop 3.60): -17.6 -- very similar appreciation and pop growth, much lower income
- **VT** (appr 41.9, ur 3.68, pcpi $36,609, pop 0.81): -10.1 -- similar appreciation, lower income
- **NM** (appr 32.6, ur 4.23, pcpi $30,433, pop 4.50): -8.9 -- similar appreciation and pop growth, much lower income
- **CO** (appr 11.9, ur 4.25, pcpi $39,869, pop 4.23): -18.5 -- similar income, much lower appreciation

WY has far higher income ($43.8K) than its closest appreciation/pop comps (MT $31.9K, NM $30.4K). In the training data, income acts as a buffer. MT at -17.6 is the most structurally similar, but WY's $12K income advantage should meaningfully reduce severity. Energy-dependent economies also tended to be insulated during the housing bust (high commodity prices through 2008).

**Prediction: -11.0**

---

### OR (Oregon)
**Features:** appr 44.9, ur 5.39, pcpi $34,488, pop 3.48

A Pacific Northwest state with moderate-high appreciation but weaker labor market and income than its neighbor. Comps:
- **WA** (appr 42.9, ur 4.99, pcpi $39,744, pop 4.37): -13.1 -- neighboring state, very similar appreciation, lower UR, higher income
- **MT** (appr 36.6, ur 3.37, pcpi $31,870, pop 3.60): -17.6 -- similar pop growth, lower appreciation
- **VT** (appr 41.9, ur 3.68, pcpi $36,609, pop 0.81): -10.1 -- similar appreciation, lower UR

WA is the natural anchor. OR has materially worse UR (5.39 vs 4.99) and substantially lower income ($34.5K vs $39.7K). Both factors push OR several points worse than WA's -13.1.

**Prediction: -15.0**

---

### AK (Alaska)
**Features:** appr 36.1, ur 6.62, pcpi $41,013, pop 4.15

A unique state: very high unemployment (second-highest in the full dataset), but also high income and moderate appreciation. The oil-dependent economy operates largely independently of the lower-48 housing cycle. Comps:
- **NY** (appr 40.3, ur 4.50, pcpi $43,760, pop -0.37): -9.9 -- similar appreciation and income, much lower UR
- **WA** (appr 42.9, ur 4.99, pcpi $39,744, pop 4.37): -13.1 -- similar appreciation, income, and pop growth
- **SC** (appr 19.4, ur 6.35, pcpi $30,789, pop 5.00): -22.1 -- similar UR but much lower income

AK's high income resembles NY/WA, but its UR of 6.62 is far above either. The UR penalty relative to the WA/NY baseline (~-11.5 average) adds roughly 3-4 points of severity.

**Prediction: -14.0**

---

### MI (Michigan)
**Features:** appr 8.9, ur 6.87, pcpi $33,563, pop -0.05

Michigan has the worst labor market in the combined dataset (highest UR, only state with negative pop growth besides LA). The auto industry collapse made MI's housing crash fundamentally demand-driven rather than speculation-driven. Comps:
- **IN** (appr 8.7, ur 5.02, pcpi $32,905, pop 2.20): -17.4 -- neighboring Rust Belt, nearly identical appreciation and income, much lower UR
- **MO** (appr 18.8, ur 4.89, pcpi $33,860, pop 2.33): -21.9 -- similar income, lower UR
- **IL** (appr 25.9, ur 4.62, pcpi $40,021, pop 0.70): -15.7 -- similar region, higher income and appreciation

IN at -17.4 is the natural anchor. MI's UR is nearly 2 full points higher (6.87 vs 5.02), and its pop growth is negative (people leaving) vs IN's positive 2.2%. These are severely worse fundamentals. The -17 to -22 range captures the Rust Belt cluster (IN, MO, WV), and MI's labor market distress places it at the worse end.

**Prediction: -20.0**

---

### OH (Ohio)
**Features:** appr 9.4, ur 5.43, pcpi $33,976, pop 0.41

Another Rust Belt manufacturing state, with very low appreciation and elevated unemployment. Comps:
- **IN** (appr 8.7, ur 5.02, pcpi $32,905, pop 2.20): -17.4 -- nearly identical appreciation and income, similar UR
- **MO** (appr 18.8, ur 4.89, pcpi $33,860, pop 2.33): -21.9 -- similar income
- **IA** (appr 13.3, ur 3.69, pcpi $34,197, pop 1.38): -13.0 -- similar income, lower UR

OH is very close to IN, with slightly higher UR (5.43 vs 5.02) and much lower pop growth (0.41 vs 2.20). These differences push OH slightly worse than IN's -17.4, but OH doesn't have MI's extreme labor distress.

**Prediction: -18.5**

---

## Final Predictions

```json
[
  {"state": "AR", "predicted_crash_pct": -12.00},
  {"state": "MN", "predicted_crash_pct": -10.00},
  {"state": "NH", "predicted_crash_pct": -7.00},
  {"state": "KS", "predicted_crash_pct": -6.00},
  {"state": "CT", "predicted_crash_pct": -7.00},
  {"state": "AZ", "predicted_crash_pct": -10.00},
  {"state": "WY", "predicted_crash_pct": -11.00},
  {"state": "OR", "predicted_crash_pct": -15.00},
  {"state": "AK", "predicted_crash_pct": -14.00},
  {"state": "MI", "predicted_crash_pct": -20.00},
  {"state": "OH", "predicted_crash_pct": -18.50}
]
```
