# Ω-RH-41 — Theory Sweep and Acceptance Gate — 2026-08-26

## Objective
Audit all currently active proof architectures against one acceptance condition:

> Prove RH by establishing Weil positivity for the full admissible test-function class, or produce a rigorously verified off-line zero / negative Weil witness.

## Current external status

The Clay Mathematics Institute still lists the Riemann Hypothesis among the unsolved Millennium Prize Problems. A number of 2026 preprints claim proofs, but a preprint claim is not accepted as a theorem until its critical bridges survive independent verification.

## Routes audited

### 1. Completed arithmetic Weil-kernel factorization (Velez)
Claimed mechanism:

    Q_W(f) = ||T f||² >= 0.

Acceptance gate:
- exact identity with the full Weil form;
- positivity of the factorization operator on its full domain;
- no hidden cutoff/stabilization assumption;
- correct passage from the completed kernel to RH.

Status: CLAIMED IN PREPRINT; NOT YET INDEPENDENTLY VERIFIED.

### 2. Local curvature / jet route
Claimed mechanism: an assumed off-line quartet produces a local second-order defect proportional to -δ², while other sectors have zero second-order projection.

Acceptance gate:
- prove the local projection statement for the full admissible class;
- prove that the constructed test function isolates the defect without an uncontrolled remainder;
- derive contradiction with the global Weil positivity criterion.

Status: PROMISING BUT REQUIRES FULL GLOBAL-TO-LOCAL BRIDGE.

### 3. Pólya / global log-concavity route
Target:

    (log Ω(e^v))'' <= 0 for all v

with the exact hypotheses required by the relevant Pólya theorem.

Acceptance gate:
- global, not sampled, inequality;
- all asymptotic regions controlled;
- exact identification of Ω with the Riemann xi kernel;
- theorem hypotheses checked.

Status: OPEN.

### 4. Volterra / Schur route
Target: construct a positive or contractive operator whose spectral lift gives the Weil form.

Acceptance gate:
- exact Weyl lift;
- uniform parameter control;
- identification with the zeta/xi spectral object;
- no finite-dimensional-only conclusion.

Status: OPEN.

### 5. Ω-Siche route
Established in the working audit:
- the prime shift operator itself is noncompact;
- the Fourier-cutoff Weil operator has a plausible/established compact-resolvent framework at fixed cutoff;
- naive Fourier-cone Perron positivity fails.

Therefore:

    P_lambda noncompact != QW_lambda noncompact
    compact resolvent != simple ground state
    finite lambda != RH

Status: SIMPLE-GROUND-STATE AND LIMIT BRIDGES OPEN.

### 6. Finite Weil/Hankel route
Finite vectors can be mapped exactly to corresponding Weil test functions. A finite negative eigenvalue is only a genuine RH counter-witness if it exceeds the rigorously bounded truncation/tail error.

Acceptance gate:

    lambda_min < - tail_budget

for a rigorously certified computation.

Status: NO CERTIFIED NEGATIVE WITNESS FOUND.

## Critical conclusion

All audited routes currently reduce to one of two genuine mathematical closure mechanisms:

A. Global positive factorization:

    Q_W = B* B.

B. Closed-form limit:

    q_n >= 0 for a dense core,
    q_n -> Q_W,
    with a valid lower-semicontinuity/closed-form argument.

A third outcome remains possible:

C. Negative witness:

    exists f such that Q_W(f) < 0.

No numerical convergence, finite matrix sign, or preprint claim is counted as A/B/C.

## Current result

RH remains OPEN after this audit. The research is narrowed, not solved.

## Next execution target

Run A/B/C in parallel:
1. symbolically reconstruct every claimed positive factorization;
2. prove or break the global Pólya inequality;
3. derive the Volterra-to-Weil bridge;
4. search finite witnesses with rigorous tail certification;
5. audit the local-curvature argument for a hidden remainder.

## Integrity rule

A solution is accepted only when the complete chain reaches

    Q_W(f) >= 0 for every admissible f
    => RH

or a rigorously verified off-line zero / negative Weil witness is produced.
