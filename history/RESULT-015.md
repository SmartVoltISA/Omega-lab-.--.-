# RESULT-015 — Memory Depth and Minimal Future Horizon

## Status
Confirmed computational result.

## Experiment
`exhaustive_horizon_2memory_binary_link1.py`

## Run
Ω-LINK-1 Run #80

## Purpose
Test whether increasing internal memory depth can increase the maximum attainable minimal horizon of future divergence.

## Construction
- Binary state space: 2 states.
- Transition rule depends on `(current, memory1, memory2)`.
- All 2^8 = 256 deterministic rules were enumerated.
- All 8 possible initial triples were compared pairwise.
- Horizons H=1..6 were checked.

## Observed result
- Total rules: 256.
- Pair checks: 7168.
- First divergence:
  - H=1: 3584 cases.
  - H=2: 1536 cases.
  - H=3: 448 cases.
  - H=4: 0 cases.
  - H=5: 0 cases.
  - H=6: 0 cases.
- No divergence within H<=6: 1600 cases.
- Maximum observed minimal horizon: H=3.

## Comparison
Previous exhaustive controls:
- One-step memory, binary: H_max = 2.
- One-step memory, 3-state: H_max = 2.

Current control:
- Two-step memory, binary: H_max = 3.

## Finding
Increasing the internal memory depth from one previous element to two previous elements increased the maximum observed minimal future-divergence horizon from 2 to 3 in the tested exhaustive binary construction.

## Interpretation
This is evidence for a relationship between memory depth and attainable prediction horizon in this model family. It is not yet a universal law. The next test should examine three-step memory and determine whether the pattern H_max = memory_depth + 1 continues or breaks.

## Rule
Do not promote the sequence to a general Ω law until the next memory-depth control has been executed and independently checked.
