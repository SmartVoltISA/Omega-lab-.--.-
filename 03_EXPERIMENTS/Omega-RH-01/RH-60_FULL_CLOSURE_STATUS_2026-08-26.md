# RH-60 — FULL CLOSURE STATUS — 2026-08-26

## Scope
Audit the current strongest public RH proof claims, especially Shimizu v8 and Velez v5, and determine whether the available evidence permits classifying RH as solved.

## Verified external facts
- Shimizu v8 is posted July 3, 2026 and is explicitly marked not peer-reviewed. It claims a self-adjoint Hilbert–Schmidt determinant model, finite-window comparison, and final identification with xi.
- Velez v5 is a Zenodo preprint. It claims non-negativity of the Weil quadratic form using Connes' semilocal trace formula, with exact stabilization from cutoff form to the full Weil form.
- These are proof claims, not independently verified solutions.

## Shimizu audit
The claimed chain is:
K = K* -> F_K -> (log F_K)' = (log xi)' near 0 -> F_K = xi -> RH.
The standard final identity-theorem and self-adjoint-spectrum steps are not the principal bottleneck. The critical audit target remains the independent derivation of the operator-side transform and its exact identification with xi'/xi, including all finite-window limits, pairing continuity, residual/counterterm handling, and absence of circular use of zero data.

Status: CLAIMED, NOT INDEPENDENTLY VERIFIED.

## Velez audit
The claimed chain is:
cutoff Weil form -> Hilbert-space norm via semilocal trace formula -> exact stabilization -> full Weil positivity -> Weil criterion -> RH.
The critical audit target is exact stabilization: the cutoff factorization must recover the full Weil quadratic form on the complete admissible test-function space, not merely on a restricted/cutoff class. The available source is a preprint and does not constitute independent verification.

Status: CLAIMED, NOT INDEPENDENTLY VERIFIED.

## Important correction
Earlier notes treated “global limit” as one universal obstruction. That is too coarse. Finite Weil compressions can already yield rigorous quantitative information about zeros. The unresolved issue is the stronger extension from finite/restricted positivity to the full infinite-dimensional Weil criterion, or an independently verified spectral identification with xi.

## Current verdict
RH is NOT classified as solved by this audit.

Classification:
- Shimizu: CLAIMED
- Velez: CLAIMED
- Finite Weil machinery: VERIFIED for its stated finite conclusions
- Full RH: NOT SOLVED / NOT INDEPENDENTLY VERIFIED

## Research frontier
1. Independently derive Shimizu's final target-identification equality.
2. Independently verify Velez exact stabilization and full-domain factorization.
3. If either closes without hidden RH assumptions, reconstruct the complete proof line-by-line and seek independent formal/numerical checks.

This record supersedes no earlier anchor; it is a new checkpoint and preserves prior RH-55 through RH-59 states.
