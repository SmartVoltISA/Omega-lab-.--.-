# REL-71 — Automatic Dynamic Fingerprint Extraction from Raw Time Series

## Status
PREREGISTERED / METHODS EXTENSION

## Purpose
Move one step below the previous blind functional-equivalence tests: do not provide the classifier with labels such as `memory`, `hysteresis`, `delay`, or `multistability`. Extract candidate structural-dynamic properties directly from raw input/output trajectories.

## Core principle

`RAW INPUT/OUTPUT → OBSERVABLES → CANDIDATE FINGERPRINT → EQUIVALENCE TEST → PHYSICAL CORRESPONDENCE`

The system must not be told in advance that a trajectory is hysteretic or memory-bearing.

## Target fingerprint

`F = (I, T, Θ, H, B, R, S)`

where:
- `I` — state/identity persistence observables;
- `T` — transition topology inferred from trajectories;
- `Θ` — threshold / switching-point estimates;
- `H` — history dependence;
- `B` — basin / stability indicators;
- `R` — recovery and perturbation response;
- `S` — scaling / symmetry observables.

## Blind observables

1. Input-output mapping consistency.
2. Rising-vs-falling branch discrepancy at matched input values.
3. Loop area under quasi-static excitation.
4. Dependence of output on previous input beyond the instantaneous input.
5. Switching-point dispersion under repeated cycles.
6. Recovery after a controlled perturbation.
7. Relaxation time and persistence.
8. Number and stability of recurrent states/clusters.
9. Response under amplitude and rate changes.
10. Noise sensitivity and repeatability.

No observable is automatically named `hysteresis` or `memory` before the audit stage.

## Critical controls

### C1 — Pure phase delay
A linear dynamic system with a known lag must not be classified as hysteretic merely because rising and falling trajectories differ at finite frequency.

### C2 — Static nonlinearity
A memoryless nonlinear mapping must not be classified as memory-bearing.

### C3 — Saturation
A saturating system must not be classified as hysteretic without branch/history evidence.

### C4 — True hysteresis
A controlled bistable/hysteretic system is a positive control.

### C5 — Noise
Add controlled measurement noise and verify fingerprint stability within preregistered tolerances.

## Required excitation

Use at least:
- slow triangular / loading-unloading input;
- sinusoidal input at multiple rates;
- amplitude sweep;
- reversal tests;
- perturbation and recovery sequence.

The slow-input condition is essential because a finite-frequency phase lag can mimic a loop. Published identification literature explicitly distinguishes hysteresis from ordinary phase delay by persistence of the loop as excitation frequency approaches zero. citeturn0search1turn0search0

## Decision rule

A property may enter the fingerprint only if:

`effect size > noise floor`

and

`property reproduces across independent excitations`

and

`control systems do not produce the same signature at the selected resolution`.

Functional equivalence is declared only at the resolution of the frozen observable vector and tolerances. Systems may therefore be:

- `EQUIVALENT_AT_LEVEL_k`
- `DISTINCT_AT_LEVEL_j`

simultaneously.

## Expected negative result

The extractor may discover that some apparently distinct signatures are not identifiable from input/output data alone. This is a valid result. Internal state variables can be unmeasured in hysteretic systems, making identification intrinsically underdetermined in some cases. citeturn0search0

## Why this matters for Ω

This is the transition from manually described properties to machine-discovered properties:

`PHYSICS → RAW TRAJECTORY → STRUCTURAL-DYNAMIC SIGNATURE → CANDIDATE ENTITY`

The reverse direction remains:

`Ω STRUCTURE → PREDICTED SIGNATURE → PHYSICAL OBSERVATION`

The strongest validation remains bidirectional convergence:

`Ω → X ← PHYSICS`

## Non-claim

This experiment does not claim that the extracted fingerprint is fundamental, unique, or complete. It tests whether useful structural-dynamic distinctions can be recovered without supplying their names in advance.

## Fixation

If the blind extractor separates the positive and negative controls while preserving equivalence among deliberately different mechanisms with the same frozen observable fingerprint, record a positive methodological result. If not, record the failure mode and refine the observable set without rewriting previous anchors.
