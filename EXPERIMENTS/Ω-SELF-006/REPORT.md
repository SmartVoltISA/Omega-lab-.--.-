# Ω-SELF-006 — Useful-work objective and policy-selection stress test

**Status:** PILOT RUN EXECUTED LOCALLY — exploratory, diagnostic result  
**Date:** 2026-10-21  
**Branch:** `experiment/omega-self-006-useful-work`

## Question
When task progress is measured alongside survival and energy, does selecting a policy from a candidate pool improve useful output, or can the objective reward conservative behavior that does less work?

## Protocol
- Candidate policies: 24 threshold controllers, generated with fixed seed 20261022.
- Training: 20 seeds in each of three families (`rapid`, `slow`, `surprise`).
- Held-out test: 60 seeds in each of four families (240 episodes per primary condition), including `unseen_drift`, a gradual productivity-degradation family not used during candidate selection.
- Horizon: 250 steps.
- Primary conditions: fixed baseline; feedback heuristic; best of 24 candidates by training score; one random candidate from the same pool.
- Composite objective: 0.50 × (mean task progress / 250) + 0.30 × full-survival fraction + 0.20 × (mean energy / 100).
- Paired bootstrap: 3,000 resamples for task-progress differences.

## Results (held-out test set)

| Condition | Full survival | Mean task progress | Mean energy | Composite score |
|---|---:|---:|---:|---:|
| A — fixed baseline | 100% | 189.38 | 23.24 | 0.72524 |
| B — feedback heuristic | 100% | 185.37 | 31.85 | 0.73444 |
| C — best of 24 | 100% | 180.15 | 45.50 | 0.75132 |
| D — random candidate | 100% | 190.32 | 22.50 | 0.72564 |

Selected candidate: `candidate_13`, energy threshold 44.96, stress limit 18.70. Random candidate: `candidate_15`, energy threshold 15.42, stress limit 11.38.

### Paired bootstrap on task progress

| Comparison | Mean difference in progress | 95% bootstrap interval |
|---|---:|---:|
| C − A | −9.227 | [−9.433, −9.010] |
| C − D | −10.166 | [−10.387, −9.942] |
| B − A | −4.014 | [−4.175, −3.854] |

All primary conditions reached 100% survival, so survival did not distinguish them. The search-selected policy achieved the highest composite score, but its mean task progress was lower than both the fixed baseline and the random candidate. Its higher energy reserve compensated for the lost work under the chosen objective.

## Main finding
**The objective is vulnerable to a “do less, preserve resources” trade-off.** The optimizer did not discover a more productive strategy; it found a policy that rests more and retains more energy. This is a useful failure of the measurement design, not evidence that search creates intelligence.

The confidence intervals concern progress differences in this specific toy simulator; they do not establish generalization to real systems. The unseen family is one designed stress test, not broad out-of-distribution validation.

## Decision
Do not claim success based on the composite score. For Ω-SELF-007:
1. Make useful work a hard minimum or primary objective, with resource reserves acting as constraints rather than a large compensating reward.
2. Add explicit task completion and failure costs.
3. Tune difficulty on training environments only; freeze the held-out set.
4. Compare best-of-N against a randomly selected candidate and a compute-matched non-search controller.
5. Keep all metrics visible; do not let one composite score hide a drop in task progress.

## Reproducibility
The runner and its raw CSV, summaries, family breakdown, candidate distribution, metadata, and bootstrap intervals were generated in the local run. Treat the results as exploratory and rerun the committed script with the documented seed and parameters before treating them as a stable benchmark.
