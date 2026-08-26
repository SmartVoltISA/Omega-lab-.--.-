# RH-45 — Shimizu Proof Dependency Audit

Date: 2026-08-26
Status: BLOCKED / CRITICAL ASSUMPTION FOUND

## Finding
The latest Shimizu v8 preprint presents a self-adjoint Hilbert–Schmidt determinant construction and claims a global identity F_K = xi. The decisive chain passes through Proposition 5.23 / Proposition 5.24 and Lemma 6.148.

## Critical point
Version 4 explicitly states Proposition 5.23 with an assumption named **Explicit-formula preservation**: after calibrating the Archimedean term, the total finite-window variation is assumed to be preserved as the sum of the prime-power contribution and the residual contribution. This is then used to identify the effective residual with the K_R component.

Version 8 subsequently states Lemma 6.148 as a finite-window equality between the operator-side residual functional and the explicit-formula residual functional, but its proof invokes Proposition 5.24. In the displayed proof, the equality follows algebraically once Proposition 5.24 is granted.

This is therefore the first item that must be independently proved, not merely reused as a decomposition.

## Consequence
The later chain

finite-window equality -> central convergence -> pairing equality -> local logarithmic derivative equality -> F_K = xi -> self-adjoint spectral localization -> RH

is valid only if the finite-window comparison identity is independently established from the classical explicit formula and the constructed operator data.

The current text does not yet provide an independent proof of that bridge sufficient for acceptance. The phrase 'Explicit-formula preservation' in the earlier proposition is a critical dependency.

## Decision
Shimizu is NOT accepted as a solved proof.

This does not show the theorem is false. It identifies a concrete proof obligation:

1. Prove explicit-formula preservation from first principles;
2. prove that the operator residual functional equals the classical residual independently;
3. only then retain Lemma 6.148 and the determinant identity.

## Sources checked
- Shimizu, Proof of the Riemann Hypothesis v8, Preprints.org, 3 July 2026.
- Shimizu v6 text, especially Proposition 5.23, Definition 6.9, Lemma 6.148, Theorem 6.150, Lemma 6.152 and Theorem 6.154.

## Important
This is an audit finding, not a disproof of RH and not a claim that the author's construction cannot be repaired.