# MINIMAL BASIS NEUTRAL MACHINE v0.4 — EXECUTION

Date: 2026-08-28
Status: EXECUTED LOCALLY / PRELIMINARY EVIDENCE / NOT CANONICAL

## Implementation under test

`MINIMAL_BASIS_NEUTRAL_MACHINE_v0.4_FIXED.py`

The previous v0.4 implementation was rejected because `dst` was unused and control state was conflated with tape position. The FIXED implementation separates `control` and `head` and applies `dst` to the next control state.

## Exhaustive run

Rule universe:
- 2 control states
- binary read symbols
- binary write symbols
- 3 head moves (-1,0,+1)
- rule tables of size 1 and 2
- fixed initial tape `(0,1,0,1)`
- execution bound: 12 transitions

Total machines evaluated: **1176**.

## Observed signatures

| Signature | Count |
|---|---:|
| difference | 276 |
| repeat_state | 87 |
| termination | 1087 |
| multiple_positions | 364 |
| multiple_control | 267 |

Counts are not probabilities of a capability. A single machine may satisfy several signatures.

## Important limitation

This run validates the corrected neutral machine implementation and its raw observational signatures. It does **not** yet establish a minimal primitive basis for D/R/W/P because the primitive budget has not been coupled to the machine semantics without semantic leakage.

## Reproducibility

The evaluator is deterministic. The exact implementation is stored in the repository. The raw aggregate above was reproduced by executing the same corrected transition semantics locally.

## Decision

- v0.4 original: REJECTED.
- v0.4 FIXED implementation: execution successful.
- Minimal-basis conclusion: UNKNOWN.
- No canonical foundation change.

## Next experiment

Bind primitive budgets to neutral machine parameters through a mechanically checkable encoding, then run alpha-renaming, permutation, null, and replay controls. Only after those controls pass may capability classification be compared across budgets.
