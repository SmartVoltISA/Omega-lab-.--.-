# RESULT-014 — Exhaustive Minimal Future Horizon Control

## Status
Confirmed computational result.

## Experiment
`exhaustive_horizon_link1.py`

## Run
Ω-LINK-1 Run #74

## Purpose
Test whether minimal future horizon observed in hand-built examples is a general feature of small deterministic systems or an artifact of the chosen examples.

## Construction
- Binary state space: 2 states.
- All deterministic transition rules for the selected 4-entry rule representation were enumerated.
- All distinct initial state/memory pairs were compared.
- Horizons H=1..4 were checked.

## Observed result
- Total rules: 16.
- Pair checks: 96.
- First divergence:
  - H=1: 48 cases.
  - H=2: 16 cases.
  - H=3: 0 cases.
  - H=4: 0 cases.
- No divergence within H<=4: 32 cases.

## Finding
For this bounded two-state construction, the maximum observed minimal divergence horizon was H=2. No pair required H>=3.

## Interpretation
This constrains, rather than proves, the general behavior of the minimal-horizon concept. Earlier hand-built examples demonstrated that the measurement method can detect deliberately constructed delayed divergence. The exhaustive two-state control shows that the available state/rule space itself can impose a bound on the horizon.

Therefore the next question is not to increase history depth alone, but to increase the state-space size and test whether the attainable minimal horizon changes.

## Rule
Do not promote this result to a universal law. It is a confirmed property of the tested bounded construction.
