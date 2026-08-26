# Ω-RH-40 — EXTERNAL THEORY SWEEP

Date: 2026-08-26

## Objective

Audit multiple current public approaches to RH rather than committing to one proof architecture.

## Routes checked

1. Completed arithmetic Weil-kernel / positive spectral factorization (Velez).
2. Hilbert–Schmidt determinant / compact-resolvent comparison model (Shimizu).
3. Pólya-kernel log-concavity route (Pavesi).
4. Weyl/KLM + finite-core Volterra route (Freedman).
5. Suzuki Weil-quadratic-form operator numerical realization.
6. Moving-contour Hankel/inertia formulation.

## Status after audit

### Velez
The public record explicitly claims a proof by positive spectral factorization of the completed arithmetic kernel. It is a preprint. Our Ω audit must therefore verify the factorization and especially the exact stabilization/limit bridge rather than accepting the claim.

### Shimizu
The public Zenodo record contains an explicit disclaimer that an earlier manuscript had fatal errors. The current architecture claims a self-adjoint Hilbert–Schmidt determinant model and an identity with ξ. This is a high-value route to audit because the decisive statement is the target identity F_K = ξ; that identity cannot be accepted merely from local equality unless all comparison constants, domains, and analytic continuation hypotheses are independently closed.

### Pavesi / Pólya kernel
The claim is that log-concavity of Ω(e^v) follows from a weighted theta-series inequality, and then Pólya's theorem gives real zeros. This is structurally attractive because it attacks the zero location directly. The critical point to verify is the global inequality x(S4 S0 − S2^2) ≤ S2 S0 on all x>0. The manuscript uses asymptotic regimes plus a finite computational core; the finite core must have a rigorous certificate and the regime interfaces must be explicit. Until independently certified, status remains candidate.

### Freedman / Volterra
This is unusually useful because the manuscript explicitly separates proved identities from numerical evidence and external bridge requirements. It states that the normalized Volterra/Weyl quotient Schur certificate is closed, while quotient-to-original Weyl lift, uniform omega coverage, and KLM/de Branges bridge remain open. Therefore it is not a complete RH proof yet, but it supplies concrete subproblems for Ω.

### Suzuki numerical operator
The numerical realization is explicitly described as a candidate/operator realization rather than a completed proof. Useful for testing spectral laws and possible operator structures, not sufficient for RH.

### Hankel/inertia
The contour Hankel formulation gives a finite-dimensional detector: negative inertia can encode off-line zero pairs. However, the independent positivity of the Hankel matrices is still unresolved. Thus this route is primarily a falsification/detection tool unless a zero-independent positivity theorem is found.

## Cross-route conclusion

No audited route currently supplies a complete independently verified proof of RH.

The strongest reusable mechanisms are:

- exact Weil-form representations;
- self-adjoint/compact-resolvent spectral constructions;
- positive-factorization candidates;
- rigorous finite-to-continuum closure problems;
- direct global kernel inequalities;
- finite-dimensional negative-witness detection.

The recurring failure mode is the same: a local, finite, numerical, or normalized positivity result is obtained, but the final universal bridge is not closed.

## Ω decision

Do NOT declare RH solved from any one public preprint.

Use the routes as independent generators of lemmas and as cross-checks against one another. Prioritize intersections where two routes require the same missing statement. In particular:

A. Weil positive factorization ↔ Volterra/Schur factorization.
B. Pólya global log-concavity ↔ direct kernel positivity.
C. Hilbert–Schmidt determinant identity ↔ compact-resolvent model.
D. Hankel negative inertia ↔ Weil-form negative witness.

## Current status

`OPEN — MULTI-ROUTE AUDIT`

`NO RH CLAIM`
