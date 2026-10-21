# Ω-SELF-004 — Bounded strategy search and held-out evaluation

**Status:** PILOT / NEEDS REPLICATION  
**Date:** 2026-10-21

## Question
Can bounded search over candidate policies improve performance on held-out environment seeds? This tests parameter search, not spontaneous invention of an algorithm, consciousness, or general intelligence.

## Completed protocol
- 20 candidate policies, each defined by an energy threshold and a rest threshold.
- 40 training environments (10 per synthetic family); 400 held-out test environments (100 per family), disjoint seeds.
- 400 steps per episode; 1,600 held-out agent-runs across four conditions.
- Search score = 75% survival fraction + 25% normalized mean energy.
- Conditions: fixed baseline; hand-coded feedback adaptation; best policy by training score; one randomly generated candidate control.

A larger planned run (48 candidates, 120 training environments, 1,000 test seeds, 600 steps) timed out before producing a completed dataset. It is excluded from all reported results.

## Selected policy
Energy threshold 32.0747; rest threshold 29.7485; training score 0.85583.

## Held-out results

| Condition | Full-horizon survival | Mean survival steps | Mean energy | Mean final energy | Mean score |
|---|---:|---:|---:|---:|---:|
| A — fixed baseline | 70.0% | 336.15 | 35.25 | 25.64 | 0.71841 |
| B — hand-coded feedback | 96.25% | 389.31 | 38.45 | 37.25 | 0.82607 |
| C — training-selected policy | 100.0% | 400.00 | 41.79 | 42.27 | 0.85447 |
| D — one random candidate | 99.0% | 397.68 | 39.48 | 39.38 | 0.84434 |

Paired-seed bootstrap 95% percentile intervals for survival-rate differences (10,000 resamples):
- C minus A: +30.0 percentage points; CI [+25.5, +34.5].
- C minus B: +3.75 points; CI [+2.0, +5.75].
- C minus D: +1.0 point; CI [+0.25, +2.0].
- B minus A: +26.25 points; CI [+22.0, +30.75].

## Survival by environment family

| Family | Fixed baseline | Hand-coded feedback | Search-selected | Random candidate |
|---|---:|---:|---:|---:|
| Rapid changes | 65% | 98% | 100% | 100% |
| Slow changes | 87% | 98% | 100% | 100% |
| Surprise shift | 38% | 89% | 100% | 96% |
| Stable | 90% | 100% | 100% | 100% |

## Interpretation and limits
1. The selected policy beat the fixed baseline and the hand-coded feedback policy on these held-out seeds.
2. The random candidate also performed very well (99% survival); the improvement over one random candidate was small. This is weak evidence for the value of selection itself.
3. Search-selected survival reached a ceiling, suggesting this environment may be too easy to distinguish strong policies.
4. Training and test seeds differ, but environment families and the policy search space are shared. This is seed generalization, not generalization to unseen environment types.
5. Compute budgets are not fully matched: candidate search uses extra training episodes.
6. The experimenter wrote the random-search algorithm; the agent did not invent its own learning algorithm or architecture.

**Decision:** Keep as a pilot, not confirmation. Next compare the selected policy against the full distribution of random candidates, a tuned reactive baseline, sham selection, more difficult environments, and unseen environment families. Report search cost alongside task performance.

## Reproduction
```bash
python run_experiment.py --seeds 400 --train-seeds 40 --candidates 20 --horizon 400 --out results.csv
```
Requires Python, NumPy, and pandas. Outputs per-run CSV, summary CSV, family CSV, and metadata JSON.
