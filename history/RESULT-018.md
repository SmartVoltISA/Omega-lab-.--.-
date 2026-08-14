# RESULT-018 — Corrected Hidden-vs-Explicit Delayed Control

## Status
Executed successfully. Negative methodological control; not evidence for a universal hidden-output delay law.

## Run
Ω-LINK-1 Run #91 / workflow dispatch #92 on commit `8151b9dd27b901a5cb17ab2741768bc9a8be13ea`.

## Result
The corrected control searched for pairs satisfying the strict condition that observable outputs remain identical through H=1..d and first diverge at H=d+1.

Observed:
- DEPTH 1: witness_found = False
- DEPTH 2: witness_found = False
- DEPTH 3: witness_found = False

No witness satisfying the strict hidden-output condition was found for depths 1–3.

## Interpretation
The earlier exhaustive results remain valid as computational observations:
- 1-memory binary systems: maximum observed minimal horizon = 2
- 2-memory binary systems: maximum observed minimal horizon = 3
- 3-memory binary systems: maximum observed minimal horizon = 4

However, these results must NOT be interpreted automatically as a universal rule that hidden information physically remains invisible for d steps and then emerges at d+1. The corrected hidden-vs-explicit control did not find such a witness under its strict construction.

Therefore the current evidence separates two claims:

1. Predictive distinguishability can require a finite horizon that grows with the memory depth in the tested constructions.
2. The stronger claim that this horizon is universally caused by hidden-state observability is NOT established by the current control.

## Decision
Keep RESULT-018 as a negative/control result. Do not promote it to an Ω law.

## Next research direction
Use the validated distinction as a practical forecasting architecture: compare long-horizon context/state with the smallest observable horizon, and test whether changes in the minimal predictive horizon carry information about regime transitions. Financial-market application must begin as an offline/backtest research experiment with explicit costs, slippage, leakage controls, and out-of-sample validation; no live-money claim is implied.
