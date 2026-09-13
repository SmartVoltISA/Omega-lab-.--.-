# Ω-MEM-2 — Prediction Advantage of Memory

Date: 2026-08-10

## Status
RAW ARCHIVE — not yet re-analyzed or normalized.

## Hypothesis
H-MEM-2: «Память даёт системе преимущество в предсказании будущего».

## Protocol
- Generator: Markov order-2, alphabet X/Y
- P(repeat | context) = 0.9
- length = 1000, burn-in = 100
- 50 seeds (0–49)
- Models: M0, M2, M4, M8 structured; R2, R4, R8 random
- Prediction: frequency-based state→next-symbol mapping; train 500 / test 500
- Intervention: reset state to 0 at test step 250
- Null: independent random X/Y generator

## Recorded results
### Same-seed
M0 0.5135
M2 0.4980, advantage -0.0155
M4 0.5128, advantage -0.0007
M8 0.4988, advantage -0.0147
R2 0.5680, advantage +0.0545
R4 0.6649, advantage +0.1514
R8 0.6813, advantage +0.1678

### Cross-seed
Train seeds 0–24, test seeds 25–49.
M0 0.5003
M2 0.5004, advantage +0.0001
M4 0.4980, advantage -0.0023
M8 0.5034, advantage +0.0031
R2 0.5516, advantage +0.0513
R4 0.6339, advantage +0.1336
R8 0.6920, advantage +0.1917

### Periodic XXYY
M0 0.5010
M2/M4/M8 0.7495

### Context memory
State = last input. Recorded accuracy ≈ 0.90 and advantage ≈ +0.39 in the original run; a later pasted console output reports 0.8198 ± 0.0207 and +0.2607. Both records are preserved pending reproducibility check.

### Important discrepancy to investigate
Two Ω-MEM-2c records were supplied:
- Earlier report: reset caused accuracy 0.75 → 0.50 (drop +0.25).
- Later direct console output from the supplied `intervention_prediction()` code: normal 0.7495, before 0.7520, after 0.7470, drop +0.005.

This discrepancy is deliberately NOT resolved in the archive. It must be reproduced from the exact code before any hypothesis status is finalized.

## Interpretation supplied with the experiment
The original interpretation proposed that memory is useful when its update structure matches the structure of the input pattern. This is archived as a claim to be checked, not as an established fact.

## Reproducibility
See `omega_mem2.py`. The code is archived as supplied in the conversation. Any later corrections must be committed as new versions; the original is not to be deleted.
