# RESULT-010 — DEPTH-SWEEP-1

## Status
Confirmed computational result on a controlled model family.

## Question
Can the measurement procedure recover a deliberately specified minimal history depth?

## Previous failure
The first DEPTH-SWEEP construction was invalid: its sequence construction caused the measurement to become sufficient at window 2 even for larger target depths. That run was explicitly rejected as evidence.

## Correction
The model was rebuilt so that for target depth N:
- the next symbol is a deterministic function of the complete N-symbol history;
- every shorter suffix is insufficient;
- the complete N-symbol history is sufficient.

The corrected code is `depth_sweep_link1.py`.

## Verification run
- Commit: `dbc39445ef206b4c68069790e748029e9d3d28f7`
- GitHub Actions run: `Ω-LINK-1 #53`
- Run ID: `31784115092`
- Conclusion: `success`
- Artifact: `omega-link-1-results`

## Result
For target depths N = 1..6, the minimum sufficient history window matched N:

| Target depth N | Minimum sufficient window |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |

For windows shorter than N, conditional entropy remained non-zero (1 bit in this controlled construction); at window N it became 0.

## Interpretation
The measurement procedure successfully recovered known minimal history depths from 1 through 6 in this controlled family.

## Boundary
This validates the measurement method and model construction. It does NOT establish that arbitrary real systems have finite memory depth, nor that any particular physical system has a specific depth.

## Research chain
Error → diagnosis → corrected construction → independent workflow run → artifact → result.

This result is a methodological support for subsequent experiments that attempt to infer minimal sufficient state from observed dynamics.