# Ω-RH-34 — RESOLVENT POSITIVITY SANITY CHECK
Date: 2026-08-26
Status: NAIVE FOURIER-CONE POSITIVITY FAILS / NO S1 CLAIM

## Objective
After RH-33 established compact resolvent for the finite-cutoff Fourier model, test whether the compact resolvent can simply inherit a Perron/Krein–Rutman argument from entrywise positivity in the Fourier basis.

## Test
Reconstruct the published `connes_exact_weil.py` matrix definition for QW_λ = A + Π − P, using the same Fourier basis V_n and the same archimedean, polar and prime terms. For finite N, choose c above the spectral lower bound and inspect

    R_c = (cI − QW_λ)^(-1).

If the standard positive orthant in Fourier coefficients were invariant in the required way, one would expect a nonnegative matrix representation of the resolvent (up to the precise cone convention).

## Result
For reconstructed finite matrices at λ² = 13, 23, 100 and 997 with N=10, R_c contains substantial negative entries even with c chosen safely above the bottom of the spectrum.

Representative result from the reconstruction:

    λ²=13:  min(R_c) ≈ −6.64×10^-3
    λ²=23:  min(R_c) ≈ −3.94×10^-3
    λ²=100: min(R_c) ≈ −6.44×10^-3
    λ²=997: min(R_c) ≈ −8.13×10^-3

The exact numerical values are only a sanity check because this is a finite reconstruction, not a continuum proof.

## Interpretation
The straightforward route

    compact resolvent + Fourier coefficient cone
        -> positivity improving
        -> Perron simplicity

is not available in this basis.

This does NOT show that the resolvent is not positivity preserving in another representation or with another cone. It only rejects the naive entrywise-positive Fourier implementation as the proof mechanism.

## Why this matters
RH-31 rejected compactness of P.
RH-33 restored compact resolvent of QW.
RH-34 now tests the next obvious shortcut and rejects it in the Fourier cone.

Therefore the remaining S1 problem is genuinely about the structure of the localized Weil form, not merely about finding a compact matrix and applying Perron–Frobenius mechanically.

## Next attack
1. Move to the physical/logarithmic representation of the localized Weil form.
2. Determine whether the quadratic form can be written as an irreducible Dirichlet form or positivity-improving semigroup there.
3. Compare this with the 2026 Suzuki screw-function formulation, which independently reports unconditional simplicity/evenness for sufficiently small intervals.
4. Determine whether that positivity mechanism extends to the λ-range relevant to the Siche cutoff model.

## Integrity
NAIVE FOURIER POSITIVITY ≠ POSITIVITY OF THE OPERATOR
FINITE MATRIX ≠ CONTINUUM THEOREM
NUMERICAL NEGATIVE ENTRY ≠ NO POSITIVE CONE EXISTS
COMPACT RESOLVENT ≠ SIMPLE GROUND STATE
