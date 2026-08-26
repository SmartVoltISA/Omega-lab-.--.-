# Ω-RH-35 — LIMIT BRIDGE STATUS
Date: 2026-08-26
Status: CRITICAL LIMIT OBSTRUCTION IDENTIFIED / NO RH CLAIM

## Objective
Test whether the finite-cutoff/Galerkin positivity route can be promoted to the continuum Weil positivity needed for RH.

## Key external control
Groskin's 2026 truncated-Weil computation reports extremely high-precision convergence of selected ground-state quantities and recovery of initial zeros, but explicitly states that whether the truncated objects converge to the Riemann zeros as the cutoff tends to infinity remains open. It also reports negative-sign eigenvalues in the raw finite matrices at increasing Fourier dimensions. Therefore numerical convergence of selected modes cannot be promoted to continuum positivity.

## Main conclusion
The compact-resolvent result at fixed lambda is useful, but it does NOT close the lambda -> infinity bridge.

The required implication is:

    QW_{lambda,N} >= 0 for all relevant N
        => limit_N QW_{lambda,N} >= 0
        => QW_lambda >= 0
        => limit_{lambda->infty} QW_lambda = Q_W >= 0.

Each arrow requires a theorem in the correct topology.

## Important distinction
A sequence of finite matrices can have a selected positive ground-state eigenvalue and simultaneously contain negative eigenvalues elsewhere. Thus tracking the lowest positive/even branch is not equivalent to proving positivity of the entire quadratic form.

## Stronger attack
The next viable route is not to demand operator-norm convergence if it is unavailable. Prove convergence of closed quadratic forms in the sense of Mosco/Kato (or an equivalent form convergence theorem), together with a uniform lower bound. Then positivity of every approximant would pass to the limit.

Candidate theorem structure:

1. Define closed forms q_{lambda,N} on a common dense core.
2. Prove q_{lambda,N}(f) -> q_lambda(f) for every core vector f.
3. Establish a lambda,N-uniform lower bound q_{lambda,N}(f) >= -epsilon_{lambda,N} ||f||^2 with epsilon -> 0, OR exact nonnegativity if available.
4. Prove liminf stability of the closed forms.
5. Pass N -> infinity and then lambda -> infinity.
6. Identify the resulting form exactly with the Weil form Q_W.

## Potential failure mode
If the lower bound cannot be made uniform, finite-dimensional positivity does not imply continuum positivity. This is the current principal obstruction.

## Current status
COMPACT RESOLVENT AT FIXED lambda: ESTABLISHED FOR THE STATED FOURIER-CUTOFF MODEL.
FINITE-MATRIX APPROXIMATION: USEFUL BUT NOT A CONTINUUM PROOF.
UNIFORM LOWER BOUND: OPEN.
N -> infinity FORM CONVERGENCE: OPEN.
lambda -> infinity IDENTIFICATION WITH Q_W: OPEN.
RH: UNRESOLVED.

## Next attack
Build explicit quadratic-form estimates on the common test-function core and try to prove a uniform lower bound plus Mosco/Kato convergence. In parallel, search for a direct negative witness if uniform positivity fails.

## Integrity
NUMERICAL CONVERGENCE != THEOREM.
SELECTED EIGENBRANCH != GLOBAL POSITIVITY.
FIXED-lambda SPECTRAL THEORY != lambda->infinity LIMIT.
NO RH CLAIM.
