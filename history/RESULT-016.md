# RESULT-016 — Memory Depth / Future-Horizon Sequence

## Status
Confirmed computational result.

## Purpose
Determine whether the maximum minimal future-divergence horizon changes systematically with internal memory depth.

## Exhaustive controls
- Memory depth 1, binary system: H_max = 2.
- Memory depth 2, binary system: H_max = 3.
- Memory depth 3, binary system: H_max = 4.

For memory depth 3:
- deterministic rules: 65,536
- initial histories: 16
- pair checks: 7,864,320
- first divergence counts:
  - H=1: 3,932,160
  - H=2: 1,835,008
  - H=3: 770,048
  - H=4: 227,328
  - H=5..7: 0
- no divergence within H<=7: 1,099,776

## Finding
Within the tested binary deterministic finite-memory model family, the observed maximum minimal future-divergence horizon follows:

memory depth d = 1 -> H_max = 2
memory depth d = 2 -> H_max = 3
memory depth d = 3 -> H_max = 4

Thus the sequence is consistent with H_max = d + 1 for d = 1..3.

## Interpretation
This is a computationally confirmed pattern within the tested model family, not yet a universal law. The important next step is to determine the mechanism that produces the +1 relation rather than merely extending the table.

## Constraint
Do not promote H_max = d + 1 to an Ω law until the mechanism is independently derived or further model classes confirm it.
