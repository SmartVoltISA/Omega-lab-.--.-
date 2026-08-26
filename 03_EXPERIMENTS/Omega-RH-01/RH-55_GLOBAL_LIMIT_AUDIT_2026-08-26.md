# RH-55 — GLOBAL LIMIT AUDIT

Date: 2026-08-26
Status: ACTIVE / BLOCKED AT GLOBAL IDENTIFICATION

## Purpose
Audit the repeated finite/local -> global transition appearing in Shimizu, Velez, Suzuki and related Weil approaches to the Riemann Hypothesis.

## Current verified external controls
- Finite/truncated Weil functionals have rigorous computer-assisted positivity on explicit finite-dimensional families; this does NOT establish full Weil positivity.
- Planat–Solé prove second-level concavity of the Riemann Xi kernel by two complementary methods with reproducible certificates; they explicitly do not claim RH.
- Eureka reports a Suzuki localized Weil-positivity certificate through a=69/200=0.345, about 99.55% of (log 2)/2; finite range only.

## Candidate routes
### Shimizu v8
Claims a self-adjoint Hilbert–Schmidt determinant model and a finite-window comparison leading to identification with xi. The critical audit is not the identity theorem or self-adjointness, but the complete passage from finite-window/operator pairings to the exact number-theoretic xi functional without circularity.

Required checks:
G1: K_N -> K in the required operator topology.
G2: relevant pairings/measures converge and are continuous in that topology.
G3: limiting operator-side functional equals the classical xi explicit-formula functional independently of RH.

Status: CLAIMED, not independently verified.

### Velez v2
Claims Q_W(f) >= 0 for all admissible f through positive spectral factorization of the completed arithmetic Weil kernel.

Critical audit:
- Is the factorization defined on the full Weil test-function space?
- Is any cutoff/window restriction removed by a proved limit?
- Is positivity preserved in that limit?

Status: CLAIMED, not independently verified.

## Central conclusion
Finite positivity is real and useful, but finite positivity alone does not imply full Weil positivity. The common bottleneck is now formulated as an explicit global-extension/identification problem, not as a vague "limit issue".

RH status: NOT SOLVED.

## Protocol
Do not mark any candidate SOLVED from author claims. A branch becomes VERIFIED only after an independent replay of the critical implication. Failed branches remain archived with their first failed lemma.
