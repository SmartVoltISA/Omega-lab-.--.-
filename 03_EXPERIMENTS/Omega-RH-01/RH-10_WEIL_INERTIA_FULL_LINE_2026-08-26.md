# Ω-RH-01 — RH-10: Full Weil/Inertia line audit
Date: 2026-08-26
Status: AUDIT RESULT / NO PROOF CLAIM

## Scope
Full pass over the proposed line:
Weil quadratic form -> finite Hermitian/Hankel compression -> Sylvester inertia -> exclusion of off-critical zeros -> RH.

## Result
The line is mathematically meaningful but does NOT currently close to RH.

## What survives
1. Weil's criterion is an exact equivalence: positivity of the Weil quadratic form for the admissible test-function class is equivalent to RH.
2. Finite-dimensional compressions can detect negative directions associated with off-critical zero configurations.
3. Sylvester inertia is a valid invariant: a negative eigenvalue/negative principal minor is an obstruction to positivity.
4. Numerical positivity of finite matrices can therefore provide strong necessary evidence.

## Load-bearing gap
The missing implication is the reverse global direction:

finite/selected compression positivity for tested subspaces
    => positivity of the Weil form on the entire admissible space.

Without a density/completeness theorem plus a uniform control of the limiting form, finite positivity does not establish global Weil positivity.

Equivalently, finding no negative direction in a finite family does not exclude an off-critical zero whose witness lies outside that family.

## Important distinction
If an off-critical quartet exists, Weil's criterion predicts a negative direction. This is useful for falsification. But constructing a witness for every possible off-critical quartet is not the same as proving that the tested finite family contains all such witnesses.

## Spectral variant
A self-adjoint operator would solve the localization problem if its spectrum were rigorously identified with the imaginary parts of ALL nontrivial zeros of the completed zeta function. Merely constructing a self-adjoint operator with the observed first zeros is insufficient.

## Current classification
WEIL POSITIVITY: exact criterion
FINITE INERTIA: valid diagnostic / partial obstruction
GLOBAL POSITIVITY: NOT PROVED
RH: NOT PROVED

## Next attack
Seek a canonical dense test-function basis for the Weil form and an exact monotone finite-section theorem. The required result would be: positivity of every finite principal compression in a dense nested basis + uniform form control => positivity on the full admissible space. Separately, derive an explicit off-critical witness map and determine whether it can be made universal rather than zero-dependent.
