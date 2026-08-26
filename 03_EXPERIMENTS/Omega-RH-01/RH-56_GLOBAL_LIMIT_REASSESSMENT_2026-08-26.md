# RH-56 — GLOBAL LIMIT REASSESSMENT

Date: 2026-08-26

## Status

RH remains UNSOLVED. This is externally consistent with the Clay Mathematics Institute, which continues to list the Riemann Hypothesis among the unsolved Millennium Prize Problems.

## New audit result

The previous formulation "global limit is the universal bottleneck" was too broad.

Finite Weil compressions can already produce rigorous quantitative zero information without proving full Weil positivity. Therefore the correct distinction is:

finite compression -> finite-rank theorem -> quantitative zero information  [VERIFIED]

versus

finite/local positivity -> full Weil positivity  [OPEN]

## Shimizu route

The current v8 manuscript claims a self-adjoint Hilbert-Schmidt construction and a finite-window-to-limit identification with xi. The decisive audit is not self-adjointness itself and not the identity theorem. The decisive issue is whether the limiting transform identity is independently derived, rather than encoded in the counterterm/representative/limit construction.

Audit gates:
G1: existence and convergence of the limiting operator.
G2: convergence/continuity of the relevant pairings.
G3: exact identification of the limiting transform with xi'/xi, without circularity.

Current status: CLAIMED, not independently verified.

## Velez route

The current preprint claims nonnegative Weil quadratic form via positive spectral factorization of the completed arithmetic kernel. The decisive audit is whether the factorization is genuinely global on the full admissible test-function space, rather than a cutoff or restricted-class factorization.

Current status: CLAIMED, not independently verified.

## Verified external controls

1. Planat–Solé: second-level concavity of the Riemann Xi kernel is proved by two complementary methods with reproducible certificates. This is a verified intermediate result, not an RH proof.
2. Eureka/Suzuki: a positivity certificate reaches 0 < a <= 69/200 = 0.345, approximately 99.55% of (log 2)/2. This is a finite-range result, not RH.
3. Clay: RH remains an unsolved Millennium Prize Problem.

## Working conclusion

The correct common research target is not "prove a generic global limit". It is to independently establish the exact extension/factorization step that turns a verified finite/local construction into the full global Weil positivity or an equivalent all-zero statement.

Acceptance rule: no CLAIMED route is promoted to PROVEN without an independently checkable closure of its final extension/identification step.
