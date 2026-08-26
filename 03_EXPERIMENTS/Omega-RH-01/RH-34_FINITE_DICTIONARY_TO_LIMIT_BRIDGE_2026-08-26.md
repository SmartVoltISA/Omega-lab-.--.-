# Ω-RH-34 — FINITE DICTIONARY → LIMIT BRIDGE
Date: 2026-08-26
Status: NEW BRIDGE / NOT A RH CLAIM

## Trigger
The compact-resolvent route (RH-33) gives a legitimate discrete spectral framework for the stated fixed-λ Fourier-cutoff model. Independently, Groskin 2026 gives an exact finite Guinand–Weil dictionary and an explicit positive archimedean tail rule for the same Galerkin objects.

## Exact finite fact
For every finite Galerkin vector v, the truncated matrix value is exactly the Weil form of an induced band-limited test function. Therefore finite matrix calculations are not merely numerical analogies: they correspond to actual Weil test functions.

## Tail fact
The omitted archimedean tail is a positive Cauchy–Stieltjes Gram increment. Consequently a finite-cutoff positive matrix can certify positivity of the corresponding cutoff-free matrix, while a sufficiently negative eigenvalue certifies a genuine negative value. A small negative value inside the explicit tail budget is inconclusive.

## New bridge target
The remaining problem is now sharply separated into two limits:

    N -> infinity  (Galerkin/source-space closure)
    λ -> infinity  (arithmetic cutoff / spectral descent)

A valid bridge would establish, for a dense core D,

    q_N[f] -> Q_λ[f]

with a lower-semicontinuity or monotone-form argument strong enough that

    q_N >= 0 for every N  =>  Q_λ >= 0 on D,

and then a separate λ-limit theorem would give

    Q_λ[f] -> Q_W[f].

Compact resolvent can support the first passage by providing a canonical spectral basis, but it does NOT automatically imply positivity survives the N-limit or the λ-limit.

## Important consequence
The finite dictionary removes one ambiguity from previous work: finite Galerkin positivity is mathematically attached to genuine Weil test functions. The unresolved issue is no longer “does the finite matrix represent the Weil form?” It does. The unresolved issue is whether positivity can be made uniform/closed under the two required limits.

## Candidate theorem to prove
For each fixed λ and every f in the pole-neutral core,

    QW_λ[f] = lim_{N→∞} q_{λ,N}[f]

and, if q_{λ,N} >= 0 for all N,

    QW_λ[f] >= 0.

Then prove for every fixed f,

    lim_{λ→∞} QW_λ[f] = Q_W[f].

If both statements are established with no hidden RH-dependent assumption, Weil positivity follows.

## Failure test
If the Galerkin sequence is not form-convergent, or if positivity is lost in the limit, record the exact defect rather than replacing it with numerical convergence.

## Current verdict

FINITE DICTIONARY: ESTABLISHED EXTERNAL RESULT
ARCHIMEDEAN TAIL CONTROL: ESTABLISHED EXTERNAL RESULT
FIXED-λ FORM CLOSURE: OPEN TARGET
λ→∞ WEIL CLOSURE: OPEN TARGET
RH: UNRESOLVED

## Next attack
1. Prove form convergence of the Galerkin matrices to the fixed-λ operator on a dense core.
2. Test whether the pole-neutral subspace is preserved under the limit.
3. Derive a λ-uniform lower bound or monotone structure.
4. Combine with RH-33 compact resolvent only where logically valid.
