# Ω-RH-01 — RH-08: Spectral-tail audit

Date: 2026-08-26
Status: AUDIT RESULT / NO CLAIM OF SOLUTION

## Objective
Test the load-bearing tail step in the Gershon v1 claim: whether a bound on the Hadamard spectral remainder is sufficient to establish the global positivity needed for D_r(n)>0.

## Finding
The published/preprint argument identifies a spectral-gap reduction using the first two known zeros and a geometric tail. However, a numerical ratio observed in the first finite set of terms is not, by itself, a uniform bound for every subsequent zero. To make the argument unconditional one needs an explicit theorem controlling the entire remaining zero sequence and its contributions to the logarithmic derivatives/remainder.

The statement that the first two zeros supply a global dominant-pole separation therefore remains a proof obligation, not an established consequence of the finite zero data.

## Important distinction
Known zeros on the critical line may be used as certified input data. They cannot be used to assume that all remaining zeros lie on that line. Any estimate whose derivation requires real ordinates for the full zero set would be circular.

## Current verdict
- No counterexample to RH found.
- No independent proof of the required uniform spectral-tail inequality found.
- Gershon's Lambda=0 claim remains unverified.
- The finite numerical evidence does not close the infinite tail.

## New attack target
Replace empirical tail ratios with a zero-free/zero-density estimate that is unconditional and uniform in the index. Track separately:
1. modulus of each Hadamard factor;
2. contribution of off-line conjugate pairs;
3. convergence and differentiation of the remainder;
4. constants required by the D_r(n) positivity inequality.

A successful closure must not assume RH or any equivalent PF_infinity statement.
