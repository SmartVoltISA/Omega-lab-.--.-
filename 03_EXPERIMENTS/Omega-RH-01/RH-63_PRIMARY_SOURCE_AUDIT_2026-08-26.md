# RH-63 — PRIMARY-SOURCE AUDIT — 2026-08-26

## Result
No independent closure of RH was obtained in this pass.

## Fresh primary-source observations
1. Shimizu v8 is the latest listed version (posted 2026-07-03) and is explicitly marked not peer-reviewed.
2. Its public abstract states the chain: finite-window comparison -> self-adjoint Hilbert–Schmidt operator -> determinant F_K -> two transform identities -> local equality with xi -> identity theorem -> RH.
3. The abstract identifies the technically decisive steps as the finite-window scalar-coefficient/cyclic-contraction/finite-rank/Hilbert–Schmidt-limit passage on the operator side and the finite-window Guinand–Weil residue identification on the classical side.
4. A prior PREreview of v2 explicitly noted gaps in that earlier version. This is historical evidence only; it is not proof that v8 retains those gaps. Therefore v8 must be audited from its current full text, not rejected merely from the old review.
5. Velez v2 is a Zenodo preprint claiming non-negativity of the Weil quadratic form by positive spectral factorization of the completed arithmetic kernel. The record labels it as a preprint.

## Critical correction
We cannot honestly claim a line-by-line proof audit from the current web metadata alone: the accessible Shimizu v8 page exposes the abstract/metadata, not the complete proof body. Therefore the correct status is CLAIMED, not FAILED and not PROVEN.

## Exact next mathematical test
For Shimizu:
  A_N -> A in the stated topology;
  continuity of the determinant/trace functional under that convergence;
  equality of the operator-side and classical-side limits;
  no counterterm or representative choice may encode the target equality.

For Velez:
  prove the factorization on the complete admissible test-function domain;
  prove that cutoff/restricted forms converge exactly to the full Weil form;
  check that positivity is not only a property of a finite/cutoff subspace.

## Status
Shimizu: CLAIMED / requires full-text lemma audit.
Velez: CLAIMED / requires full-domain factorization audit.
RH: NOT INDEPENDENTLY VERIFIED.

This anchor supersedes no earlier RH anchor; it records the methodological correction that we must not infer a proof gap from an abstract, nor infer a proof merely from an author's claim.
