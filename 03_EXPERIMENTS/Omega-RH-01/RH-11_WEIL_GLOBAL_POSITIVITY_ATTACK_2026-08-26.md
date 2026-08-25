# Ω-RH-11 — Weil global positivity attack

Date: 2026-08-26
Status: OPEN / NO PROOF CLAIMED

## Objective

Test whether finite-dimensional positivity checks for Weil's quadratic form can be upgraded to global positivity, which would imply the Riemann Hypothesis.

## Established mathematical status

Weil's positivity criterion is an equivalence: RH is equivalent to positivity of the corresponding explicit-formula quadratic form on an appropriate test-function class.

Therefore finite positive Gram/Hankel matrices are evidence only unless a density/completeness theorem and a uniform limiting argument are supplied.

## Current attack

For an increasing family of finite-dimensional spaces V_N, let Q_N be the compressed Weil form. The desired implication is:

  Q_N >= 0 for every N
      + density(union_N V_N)
      + continuity / lower-semicontinuity of Q
      => Q(f) >= 0 for every admissible f.

The difficult point is not finite positivity. It is obtaining a rigorous bound uniform in N that controls the passage to the closure.

## Failure modes checked

1. Positive principal minors for tested N do not by themselves imply positivity of the infinite form.
2. Numerical convergence of the smallest eigenvalue is not a proof of non-negativity of the limiting operator.
3. A finite test basis can miss an off-subspace negative direction.
4. A spectral realization is not sufficient unless self-adjointness/domain/completeness and the exact explicit-formula correspondence are proved.

## New research direction

Use the explicit formula to define the quadratic form directly on a dense test class and seek an intrinsic coercive/closed-form estimate that is preserved under completion. The target is a theorem of the form

  Q(f) >= c ||P f||^2 - R(f)

with R controlled uniformly and vanishing under an admissible exhaustion, or an equivalent reproducing-kernel / Gram representation proving positive semidefiniteness directly.

## Independent cross-check

Current literature continues to describe Weil positivity as an equivalent criterion rather than a solved problem. A July 2026 numerical realization of a Suzuki Weil-quadratic-form operator explicitly states that it does not prove RH. See: arXiv:2607.24830.

## Result

NO PROOF YET.

The finite-to-infinite passage remains the load-bearing gap. This is now the primary Ω-RH target; finite numerical enlargement alone is not accepted as progress toward a proof unless accompanied by a rigorous uniform theorem.

## Rule

PROPOSED != TESTED
TESTED != PROVEN
NUMERICAL != GLOBAL
UNKNOWN != FALSE
