# Ω-RH-18 — Global proof audit

Date: 2026-08-26

## Result

The current candidate proofs do not yet establish RH.

### Velez
Velez v2 (Zenodo 10.5281/zenodo.21172964) claims nonnegativity of the Weil quadratic form by positive spectral factorization. It is explicitly a preprint. The claim must be independently verified at the factorization and full-domain extension steps before acceptance.

### Zhou — Overdetermined Weil Systems
Zhou claims that off-critical zero-pairs produce functions f_k(n), and that linear independence forces their absence.

Critical audit point: the displayed contradiction is immediate only for a finite collection of off-critical pairs M. The actual zero set is infinite, so replacing the infinite sum by a finite sum requires an additional convergence/truncation argument strong enough to preserve the linear-independence contradiction. The abstract does not establish that step. In particular, finite linear independence of {f_k}_{k=1}^M does not by itself imply that an infinite convergent series of such functions cannot vanish identically.

Therefore the Zhou route is not accepted as a complete proof without an independent infinite-series theorem.

## Current load-bearing problem

The recurring obstruction is now sharply identified:

finite/local positivity or finite linear constraints
    -> uniform control over the infinite zero set
    -> global Weil positivity

Any claimed proof must explicitly close this infinite passage without assuming RH.

## Ω status

STATUS: OPEN

No proof or counterexample accepted.
