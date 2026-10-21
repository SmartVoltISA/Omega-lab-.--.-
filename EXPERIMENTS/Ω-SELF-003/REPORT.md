# Ω-SELF-003 — Feedback-driven adaptation vs sham self-modification

**Status:** PILOT RESULT / REQUIRES INDEPENDENT REPLICATION  
**Date:** 2026-10-21

## Question
Does feedback-driven bounded policy change generalize across varied environment dynamics, or is the apparent benefit from Ω-SELF-002 explained by merely changing parameters?

## Design
Five conditions were run on 1,000 shared environment seeds (5,000 agent-runs), 600 steps each. Each seed selects one of four environment families, 250 seeds each: rapid regime transitions, slower transitions, one surprise regime shift, or no regime shift. Conditions share observation noise, forage noise, rest noise, conserve noise, and cues within each seed. Initial energy and high/low forage yields vary by family.

- **A — reactive/noisy:** uses noisy current-energy observation.
- **B — fixed self-model:** maintains an estimated energy state but does not change its policy.
- **C — feedback self-modification:** adjusts policy thresholds based on observed energy outcomes and current state.
- **D — sham self-modification:** changes thresholds on a schedule unrelated to observed outcomes.
- **E — oracle state:** sees true energy; diagnostic upper bound.

Primary metric: survival through all 600 steps. All policy rules are explicitly hand-coded.

## Results

| Condition | Full-horizon survival | Mean survival steps |
|---|---:|---:|
| A — reactive/noisy | 49.8% | 431.2 |
| B — fixed self-model | 43.2% | 401.9 |
| C — feedback self-modification | 94.7% | 578.7 |
| D — sham self-modification | 22.2% | 304.4 |
| E — oracle state | 99.7% | 599.0 |

Paired-seed bootstrap 95% percentile intervals (10,000 resamples) for full-horizon survival-rate differences:
- **C minus A:** +44.9 percentage points; 95% CI [+41.8, +48.1].
- **B minus A:** −6.6 points; 95% CI [−9.9, −3.5].
- **D minus A:** −27.6 points; 95% CI [−30.8, −24.4].
- **C minus D:** +72.5 points; 95% CI [+69.7, +75.3].

## Across environment families

| Family | A reactive | B fixed model | C feedback adaptation | D sham changes | E oracle |
|---|---:|---:|---:|---:|---:|
| Rapid changes | 45.6% | 34.8% | 95.2% | 9.2% | 100.0% |
| Slow changes | 62.4% | 54.0% | 96.4% | 22.8% | 100.0% |
| One surprise shift | 13.2% | 9.2% | 87.2% | 0.4% | 98.8% |
| No shift | 78.0% | 74.8% | 100.0% | 56.4% | 100.0% |

## Interpretation
1. A persistent state estimate alone again underperformed the reactive baseline.
2. Feedback-driven policy adaptation substantially outperformed both the reactive baseline and a sham condition whose parameters changed without reference to outcomes.
3. The result is consistent across four synthetic families, including surprise shifts, but these are closely related toy environments rather than independent real-world domains.
4. This does not show that the agent autonomously invented the update rule. The update rule was designed by the experimenter.
5. Sham changes were harmful, suggesting change by itself is not sufficient; the connection between feedback and the direction of adaptation mattered in this setup.

## Limitations
- One model family with hand-designed dynamics and policies.
- Environment families are synthetic and selected by the experimenter.
- Feedback adaptation uses hand-coded rules; it is not open-ended architecture evolution.
- No reproduction, inheritance, multi-agent ecology, or subjective consciousness was tested.
- Bootstrap intervals are conditional on this simulation and do not establish a universal law.

## Decision
Record as evidence for **feedback-driven adaptation in this specific toy control problem**, not as evidence that a self-model or consciousness is necessary. Next: compare feedback adaptation with a tuned reactive baseline, random-search policy tuning, and learned adaptation on environments not used during rule design.

## Reproduction
```bash
python run_experiment.py --seeds 1000 --horizon 600 --out results.csv
```
Requires Python, NumPy, and pandas.
