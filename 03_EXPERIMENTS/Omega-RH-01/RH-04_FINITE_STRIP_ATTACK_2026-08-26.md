# Ω-RH-01 — FINITE-STRIP ATTACK / AUDIT

**Date:** 2026-08-26
**Status:** OPEN / UNRESOLVED

## 1. Target

The Pólya–Jensen route reduces RH to hyperbolicity of the Jensen-polynomial family associated with

`Theta(z) = xi(1/2 + sqrt(z))`.

For the standard coefficients `gamma(n)`,

`J^(d,n)(X) = sum_{j=0}^d binom(d,j) gamma(n+j) X^j`.

The open region is not the whole `(d,n)` plane. Known results establish eventual hyperbolicity for every fixed degree and all degrees `d <= 8`. Recent 2026 work further proves an unconditional hyperbolicity wedge roughly of the form

`n^3 log^2(n+2) >= K d^5`,

and another analysis places the remaining difficulty in a finite strip approximately

`0 <= n < C d^4,  d >= 9`.

## 2. Independent numerical sanity check

Direct high-precision differentiation of

`xi(s) = 1/2 s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`

at `s=1/2` reproduces the first Taylor coefficients used by the Jensen construction. For example,

`gamma(0) = 0.4971207781883141099...`

`gamma(1) = 0.0250291646987266842...`

`gamma(2) = 0.0107641101791232119...`

The degree-2 Jensen polynomial at `n=0` is not hyperbolic, while the degree-2 polynomial at `n=1` is hyperbolic. This is a useful normalization/indexing check and agrees with the established distinction between finite shifts and eventual hyperbolicity.

## 3. Important correction to earlier Ω numerical work

A previous exploratory computation used an incorrectly normalized kernel expression for high moments. The resulting high-degree roots were therefore rejected and are **not evidence against RH**.

This file supersedes any interpretation of those roots as counterexamples.

Rule:

`numerical root failure != mathematical counterexample`

High-degree Jensen calculations must use independently validated moment data and certified precision/stability checks.

## 4. Current mathematical bottleneck

The current problem can be stated as:

`Disc(J^(d,n)) > 0` together with full hyperbolicity, throughout the remaining finite strip.

For a polynomial family, the boundary of the hyperbolic region is detected by a multiple real root, equivalently by

`J^(d,n)(x) = 0`

and

`d/dx J^(d,n)(x) = 0`.

Since the derivative is another Jensen polynomial up to a positive factor,

`(J^(d,n))' = d J^(d-1,n+1)`,

this creates a potentially useful recursive structure.

## 5. New attack directions

A. Build certified moment data rather than evaluating high derivatives of zeta directly.

B. Use the exact moment/Mellin representation and derive stable recurrence or saddle formulas for `gamma(n)`.

C. Search for a structural inequality on the quotient coordinates

`q_k = R_(k+1)^2 / (R_k R_(k+2))`,

where `R_j = gamma(n+j)/gamma(n)`.

D. Test whether the finite-strip obstruction can be converted into a single invariant inequality rather than checking every polynomial independently.

E. In parallel, test the de Bruijn–Newman heat-flow formulation and the Weil-positivity/spectral route. The known equality `Lambda = 0` is not itself RH, so any proposed implication must be proved rather than inferred.

## 6. Research result of this pass

No proof and no counterexample.

The search space has been narrowed to the finite-strip mechanism and, more specifically, to the missing structural inequality that would force hyperbolicity there.

The next computational objective is a certified recurrence/moment engine capable of producing `gamma(n)` through at least `n = 130` and then evaluating the degree-9+ finite strip with interval or arbitrary-precision certification.

## 7. Integrity rule

Proposed != tested.
Tested != proved.
Numerically stable != mathematically certified.
Unknown != false.
