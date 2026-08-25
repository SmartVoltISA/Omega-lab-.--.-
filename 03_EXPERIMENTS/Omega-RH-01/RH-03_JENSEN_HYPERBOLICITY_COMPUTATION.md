# Ω-RH-01 — RH-03 JENSEN HYPERBOLICITY COMPUTATION

**Date:** 2026-08-26  
**Status:** COMPUTATIONAL CHECK / NO PROOF CLAIM

## Objective

Test the Pólya–Jensen route directly on the central Taylor coefficients of the Riemann Xi function and identify where finite-degree hyperbolicity does or does not close toward RH.

The established equivalence is:

`RH ⇔ all relevant Jensen polynomials are hyperbolic.`

This is a theorem-level reformulation, not itself a solution.

## Computation

Using high-precision numerical differentiation of

`ξ(s) = 1/2 s(s-1) π^(-s/2) Γ(s/2) ζ(s)`

at `s = 1/2`, coefficients were reconstructed in the normalization

`Ξ(z) = ξ(1/2 + z) = Σ γ(n) z^(2n) / n!`.

The first coefficients obtained were approximately:

- γ(0) = 0.4971207781883141099
- γ(1) = 0.2725471035060672084
- γ(2) = 0.05968225697596591256
- γ(3) = 0.009309457581378690332
- γ(4) = 0.001215600621892661433
- γ(5) = 0.0001426443129524224073
- γ(6) = 0.00001560656580278186866
- γ(7) = 0.000001625928356594691616

For degree `d`, the tested Jensen polynomial was

`J^(d,n)(X) = Σ_{j=0}^d C(d,j) γ(n+j) X^j`.

## Observed finite tests

For shifts `n = 0,...,6`:

- degree `d=2`: numerically hyperbolic for every tested shift;
- degree `d=3`: numerically hyperbolic for every tested shift;
- degree `d=4`: numerical non-hyperbolicity appeared for shifts `n=1,...,6`.

This is **not evidence against RH**. It is an important normalization/definition checkpoint: the exact Pólya–Jensen construction and coefficient convention must be aligned before interpreting higher-degree tests. In particular, one must distinguish the Xi expansion convention, the derivative convention, and the exact Jensen family used in the published equivalence.

## Result

The computation confirms the expected low-degree behavior but exposes a critical reproducibility requirement: higher-degree results are sensitive to the exact normalization and indexing convention. Therefore no theorem-level inference is made from the raw `d=4` observation.

## Barrier

Finite verification, even for very large families of Jensen polynomials, cannot by itself prove RH. The known equivalence requires hyperbolicity for the complete infinite family.

## Next attack

1. Reconstruct the published Jensen-polynomial definition symbolically from the exact Xi Taylor coefficients.
2. Derive discriminants/Sturm certificates rather than relying on floating-point root classification.
3. Determine whether the Ω hierarchy can imply hyperbolicity of the complete family from a finite or structural invariant.
4. Search specifically for a theorem that converts an all-orders Laguerre/Turán hierarchy into Laguerre–Pólya membership under conditions satisfied by Xi.

## Evidence status

`COMPUTED → REPRODUCIBILITY CHECK REQUIRED → NO PROOF`

## Principle

A numerical pattern is a measurement. It becomes mathematics only after the normalization, assumptions, exact inequalities and proof of the implication are all explicit.
