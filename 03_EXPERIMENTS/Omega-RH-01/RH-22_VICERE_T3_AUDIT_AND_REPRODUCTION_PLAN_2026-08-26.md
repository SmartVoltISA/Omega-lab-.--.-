# Ω-RH-22 — Viceré T3 Audit and Reproduction Plan
Date: 2026-08-26
Status: ACTIVE AUDIT — NOT A PROOF

## Purpose

Continue the RH line by treating Viceré's T3 (form stability) as a candidate theorem, not as an accepted proof.

The source claims positivity of the Weil quadratic form for all admissible smooth compactly supported test functions and presents T3 as the key new step in a semilocal spectral descent. The public record currently identifies the work as a preprint. Independent confirmation is therefore required before assigning proof status.

## Exact claim to verify

For each admissible fixed test function f, establish whether there exists a finite lambda_0(f) such that

    Q_lambda(f) = Q_W(f)    for all lambda >= lambda_0(f),

or whether the actual result is only asymptotic,

    Q_lambda(f) = Q_W(f) + R_lambda(f),   R_lambda(f) -> 0.

The distinction is load-bearing.

## Acceptance conditions

T3 can be accepted only if all of the following are demonstrated without assuming RH:

1. Precise definition of Q_lambda and Q_W on the same test-function domain.
2. Construction of the finite/semi-local spectral operator and proof of its required self-adjointness/positivity.
3. A finite threshold lambda_0(f), or an equivalent theorem that is sufficient for the stated stabilization.
4. Exact control of every lambda-dependent remainder.
5. Explicit proof that the stabilized form is exactly the Weil form, including prime, archimedean, zero, and boundary terms.
6. No step uses the location of zeta zeros on Re(s)=1/2.
7. The passage from the admissible test class to the full Weil criterion is stated and proved.

## Failure certificates

Any one of the following is sufficient to reject T3 as currently stated:

- only convergence is proved, not eventual equality;
- lambda_0 is asserted but not shown finite;
- a remainder tends to zero but is not identically zero after a finite cutoff;
- spectral reality is obtained only by assuming the desired zero location;
- equality with the Weil form is established only on a restricted class that is not shown sufficient;
- an interchange of infinite sums, limits, traces, or distributions lacks a uniform/dominating estimate;
- the argument changes the test space between the spectral and Weil forms without proving equivalence.

## Current external status

Viceré's Zenodo record is a preprint claiming a proof via Weil positivity and semilocal spectral descent. The claim itself is not treated here as established mathematics.

Independent recent work on Suzuki's operator likewise describes the operator realization as a candidate and explicitly states that the numerical realization does not prove RH. This is useful as a control against confusing numerical spectral agreement with a theorem.

## Reproducibility protocol

For selected compactly supported test functions f:

A. Compute Q_lambda(f) over a sequence of increasing cutoffs.
B. Measure delta_lambda = Q_lambda(f)-Q_reference(f).
C. Test whether delta_lambda becomes exactly zero in an exact/arbitrary-precision representation, rather than merely becoming numerically small.
D. Repeat with multiple test functions, including functions deliberately chosen near spectral transitions.
E. Separately compare Q_lambda with the explicit Weil expression, term by term.
F. Record any dependence of the required cutoff on f.

Numerical agreement alone is not acceptance. It is only a diagnostic.

## Current verdict

T3 remains a serious candidate mechanism. It is NOT yet promoted to PROOF.

Next decisive operation: obtain and parse the complete T3 proof, then audit every lemma and limit in order. If the exact stabilization theorem survives, reconstruct the T1-T5 chain independently. If it fails, record the first failing equation as a negative result.
