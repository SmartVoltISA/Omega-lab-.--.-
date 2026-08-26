# Ω-RH-25 — MULTI-ROUTE RUN
Date: 2026-08-26
Status: CLOSED CHECKPOINT — NO RH PROOF

## Objective
Run several independent routes in parallel instead of iterating only on Viceré T3.

## Route A — Viceré exact stabilization
Target:
    Q_λ(f) = Q_W(f) for all λ >= λ0(f).

Result:
No independently derived exact remainder cancellation was obtained. The public preprint claims the stabilization theorem, but the accessible record is insufficient to certify every equality, domain condition, and cutoff/limit interchange.
Status: CANDIDATE / UNVERIFIED.

## Route B — Yang spectral-variational bridge
New exact result identified in the public preprint:
The truncated arithmetic potential
    V_X(u)=Σ_{n<=X} Λ(n)/sqrt(n) [δ(u-log n)+δ(u+log n)]
has Fourier transform equal, up to normalization, to the prime-side density entering the compressed Weil form.

This is a genuine exact prime-sector identification. However, the paper explicitly states that the full Hessian-Weil bridge is conditional: it assumes that the second variation of a rigorously defined spectral action equals a positive multiple of Weil's Hermitian form. That bridge is not proved.
Status: EXACT LOCAL IDENTITY / GLOBAL BRIDGE UNPROVED.

## Route C — finite Hankel positivity
The 2026 contour-Hankel construction gives an exact local finite-dimensional formulation: inertia detects off-line conjugate pairs once the matrix order resolves the coordinate nodes.

Result:
This converts RH locally into a finite Hankel-positivity statement, but the required positivity independently of the zero set remains unresolved.
Status: EXACT FINITE REFORMULATION / POSITIVITY UNPROVED.

## Route D — current unconditional zero-density progress
The August 2026 result proves at least two thirds of nontrivial zeros are simple and on the critical line, with a 0.6725 bound under the Montgomery–Taylor window. Lean formalisation is provided. This is a real unconditional advance, but it is not RH.
Status: VERIFIED PROGRESS / NOT RH.

## Cross-route result
All three proof-oriented routes reduce to the same missing bridge:

finite/local exact structure
        -> universal positivity / global control
        -> RH.

The new Yang identity is useful because it removes ambiguity in the prime-sector correspondence; it does not close the global bridge.

The Hankel route is useful because it makes the obstruction finite-dimensional, but it does not supply universal positivity.

Viceré remains the shortest claimed route if T3 is actually proved; however, we have not independently verified T3.

## Final status
RH remains OPEN.

## Next attack priorities
1. Use Yang's exact prime identity to replace the prime-sector bookkeeping in RH-24.
2. Test whether the Hessian-Weil proportionality can be derived rather than assumed.
3. Use the Hankel inertia formulation as a counterexample detector: any off-line pair must create a negative direction.
4. Return to Viceré only after these independent constraints are applied.

Acceptance rule remains unchanged: no claim of proof without a complete global positivity argument independent of RH.
