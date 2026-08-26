# Ω-RH-38 — GALERKIN POSITIVITY / TAIL CLOSURE AUDIT
Date: 2026-08-26
Status: STRONG FINITE CERTIFICATION MECHANISM / GLOBAL CLOSURE STILL OPEN

## Objective
Determine whether the finite Galerkin results can be promoted to the full Weil positivity statement without assuming RH.

## Verified external structure
Groskin (arXiv:2607.02828) gives two exact finite statements for the truncated Weil quadratic form:

1. Every real even Galerkin vector v maps to an explicit band-limited Guinand–Weil test function g_v, with the finite quadratic value equal exactly to the corresponding zero-sum functional.
2. The omitted archimedean tail is a totally positive Cauchy–Stieltjes increment. Therefore a finite-cutoff positivity certificate implies positivity after restoring that particular positive tail. Conversely, a sufficiently negative finite eigenvalue, below the explicit tail budget, certifies a genuine negative full form.

## Consequence
For a fixed finite Galerkin family, the sign problem is now much cleaner:

    q_T(v) >= 0  =>  Q_W(g_v) >= 0

provided the exact truncation/tail hypotheses of the theorem are satisfied.

This removes one major source of ambiguity: the archimedean tail is not itself the obstruction.

## Remaining global step
The finite certification is not yet a proof of RH because RH requires

    Q_W(f) >= 0

for every admissible test function f, not merely every vector in one finite Galerkin dictionary.

The remaining closure problem can be stated precisely:

(A) Density: the union of the admissible finite Galerkin/source spaces must be dense in the relevant Weil form domain after the pole-neutral constraints.

(B) Uniform lower control: the finite forms must be uniformly lower bounded in a topology strong enough to pass positivity to the closure, or an equivalent closed-form argument must be supplied.

(C) Compatibility: the finite source quotient must preserve the exact pole constraints and the limiting Weil form under N -> infinity and cutoff removal.

## Important finding
The correct target is therefore NOT "prove numerical eigenvalues stay positive as N grows". The target is an analytic closure theorem of the form:

    D_fin dense in D(Q_W)
    and
    q|_{D_fin} >= 0
    ----------------------
             Q_W >= 0.

If this can be proved, RH follows by Weil's criterion.

## Counter-route
If a finite eigenvalue satisfies

    lambda_min < -B_T

with B_T the rigorous omitted-tail budget, then the corresponding explicit g_v is a genuine negative Weil witness and RH is false.

A negative eigenvalue in [-B_T,0) is inconclusive.

## Current status
FINITE EXACT DICTIONARY: VERIFIED BY SOURCE
TAIL POSITIVITY: VERIFIED BY SOURCE
GLOBAL DENSITY/CLOSED-FORM PASSAGE: NOT YET PROVED
NEGATIVE WITNESS: NONE ESTABLISHED
RH: UNRESOLVED

## Next attack
1. Write the pole-neutral finite source space explicitly.
2. Prove density in the Weil form domain (preferably via a standard Paley–Wiener/Schwartz approximation argument adapted to the constraints).
3. Prove lower semicontinuity/closedness of the Weil quadratic form under that approximation.
4. If any step fails, construct the precise obstruction rather than replacing it by numerical convergence.

## Integrity
FINITE CERTIFICATE != GLOBAL THEOREM
TAIL POSITIVITY != DENSITY
NUMERICAL CONVERGENCE != FORM CLOSURE
