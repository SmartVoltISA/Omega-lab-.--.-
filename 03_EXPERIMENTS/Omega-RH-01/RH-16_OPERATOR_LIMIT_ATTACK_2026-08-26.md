# Ω-RH-16 — Operator-limit attack

Date: 2026-08-26
Status: OPEN / NO PROOF CLAIMED

## Objective
Attack the remaining bridge in the Weil/Hilbert-Pólya route:

    A_a -> A_infinity
    Spec(A_infinity) = {gamma_n}

without assuming RH.

## Required proof obligations

1. Define a common Hilbert space and domains for A_a.
2. Prove a genuine convergence notion (e.g. strong resolvent or norm-resolvent convergence), not pointwise convergence of matrix entries.
3. Establish self-adjointness of the limit independently of the zero set.
4. Identify the limiting spectral measure/operator with the completed xi function through an exact explicit-formula identity.
5. Prove that no off-critical zero can survive the limit.
6. Check every domain, interchange of limit/integral/sum, and uniform bound for circularity.

## Current result

No complete closure found in this pass. Finite positivity and finite self-adjoint compressions are insufficient by themselves. The load-bearing issue remains the RH-independent identification of the global limit with xi/Weil data.

## Falsification rules

- Numerical spectral convergence is not operator convergence.
- Self-adjoint finite truncations do not imply the required global spectrum.
- Any use of zero locations in proving the operator limit is circular.
- Agreement with known zeros is validation, not proof.

## Next attack

Search for an exact quadratic-form construction whose closed Friedrichs operator is defined directly from the arithmetic explicit formula, then prove that its spectral determinant is xi up to an explicit nonvanishing factor. This would bypass the uncontrolled A_a -> A_infinity identification if successful.

## Status

UNKNOWN / OPEN. No proof claim.
