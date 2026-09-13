# Ω-MEM-1a–1d — Repeatability / Strict Intervention

**Status:** raw archival record; analysis intentionally deferred.

**Date:** 2026-08-10

## Fixed parameters

- history length: 15
- intervention step: 5
- seeds: 0–99 (100 independent seeds)
- memory sizes: S = 1, 2, 4, 8, 16
- input alphabet: X, Y
- output alphabet: A, B
- post-intervention comparison window: 10 outputs

## Predefined criteria

1. Causal effect: after intervention, with identical subsequent inputs, at least one output differs.
2. Δtrajectory: number of differing outputs after intervention.
3. Functional memory: different histories can produce different outputs for the same input.

## Reported Ω-MEM-1a result

| Model | Success rate | Mean Δ / 10 | State at reset = 0 | First diff = 0 | Reconvergence |
|---|---:|---:|---:|---:|---:|
| M0 (S=1) | 0% | 0.00 | 100/100 | 0/100 | 100% |
| M2 (S=2) | 54% | 5.40 | 46/100 | 54/100 | 46% |
| M4 (S=4) | 54% | 5.40 | 10/100 | 54/100 | 46% |
| M8 (S=8) | 54% | 5.40 | 1/100 | 54/100 | 46% |
| M16 (S=16) | 54% | 5.40 | 1/100 | 54/100 | 46% |

95% CI reported for the 54% success rate: approximately [0.442, 0.638].

## Important archival note

These are the results supplied from the original run. They are **not treated as final confirmation**. In particular, the 54% value and the relationship between `state_at_reset`, intervention, and reconvergence must be reproduced from the archived code before assigning a final hypothesis status.

## History rule

No result is deleted when later work disagrees with it. Later experiments may mark this record as `SUPERSEDED`, `REJECTED`, `CORRECTED`, or `NEEDS RETEST`, while preserving the original protocol, code, and output.
