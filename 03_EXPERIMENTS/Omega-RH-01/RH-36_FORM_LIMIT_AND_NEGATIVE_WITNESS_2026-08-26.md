# Ω-RH-36 — FORM LIMIT + NEGATIVE WITNESS SWEEP
Date: 2026-08-26
Status: ACTIVE / NO RH CLAIM

## Objective
Attack the remaining bridge without relying on operator-norm convergence:
finite Weil forms q_{lambda,N} >= 0 -> cutoff-free Weil form Q_W >= 0 -> RH.
Simultaneously search for a certified negative witness if the bridge fails.

## Control
The finite Galerkin construction has an exact dictionary: each finite vector determines a band-limited Guinand-Weil test function and the finite quadratic value equals the corresponding zero-sum exactly. The archimedean tail has an explicit two-sided certification budget (Groskin, arXiv:2607.02828).

## Required distinction
Do not infer q_N >= 0 for many N implies Q_W >= 0. A uniform form-domain theorem, lower-semicontinuity/closed-form convergence, or a complete tail certification over a dense class is required.

## Routes
A. Direct form closure: prove Q_W(f)=lim q_N(f_N) with liminf control on the full Weil form domain.
B. Explicit tail certification: use the positive archimedean tail budget. A finite eigenvalue below -B_T certifies a genuine negative Weil value; values in [-B_T,0) are inconclusive.
C. Negative witness: search systematically for lambda_min < -B_T.

## External controls
Suzuki 2026 treats the limiting self-adjoint operator as a conjectural bridge, not an RH proof (arXiv:2606.09096). The numerical realization also explicitly states it does not prove RH (arXiv:2607.24830).

## Status
Finite exact dictionary: verified in the cited construction.
Positive tail budget: established for that truncation.
Full infinite-dimensional positivity: NOT CLOSED.
RH: OPEN.

## Next hard target
Either prove the density + lower-semicontinuity bridge for the entire Weil test-function space, or find a certified negative witness outside the tail budget.

## Integrity
EXACT FINITE IDENTITY != INFINITE THEOREM
TAIL BOUND != GLOBAL DENSITY
NUMERICAL POSITIVITY != RH
NEGATIVE VALUE INSIDE BUDGET != COUNTEREXAMPLE
NEGATIVE VALUE OUTSIDE BUDGET = CERTIFIED COUNTEREXAMPLE
