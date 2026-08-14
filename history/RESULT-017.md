# RESULT-017 — Hidden vs Explicit State Equivalence Control: Methodological Limitation

## Status
Executed successfully, but NOT accepted as a substantive Ω result.

## Experiment
`explicit_state_equivalence_link1.py`

## Run
Ω-LINK-1 Run #89

## Purpose
Attempt to test whether delayed distinguishability is caused by hidden observability rather than by the transition mechanism itself, by comparing a hidden-history representation with an explicitly augmented state representation.

## What was actually tested
The experiment compared future output signatures of finite-memory systems with future signatures of the full augmented history state. The selected pairs shared the immediately visible output but differed in older history.

## Observed outcome
For the concrete control construction, the hidden output divergence occurred at H=1 for the reported witnesses, and the explicitly augmented state also differed at H=1.

## Methodological limitation
This does not provide the intended control of delayed distinguishability. The experiment did not constrain the selected pair to have identical hidden outputs for H=1..d and first diverge at H=d+1. Therefore it cannot establish or refute the proposed relationship between hidden observability and delayed emergence of distinguishability.

The explicit state necessarily contains the hidden history, so immediate state-level difference is expected and is not by itself evidence against the delayed-output phenomenon.

## Decision
Do not use RESULT-017 as evidence for or against an Ω law.
Record it as a methodological control and retain the limitation explicitly.

## Next requirement
Construct a corrected control in which the same physical finite-memory process is represented as hidden current output versus full augmented state, while selecting pairs whose hidden output histories remain identical through the intended delay H=1..d and diverge first at H=d+1. Only then compare the two representations.
