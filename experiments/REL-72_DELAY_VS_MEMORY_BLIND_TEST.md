# REL-72 — Delay vs Memory: Blind Discrimination Test

## Status
PILOT / METHODOLOGICAL

## Question
Can a black-box observer distinguish a system with ordinary dynamical lag from a system with retained internal state when both produce similar input-output loops under periodic excitation?

## Blind rule
The observer receives only input/output trajectories. Mechanism labels are hidden until the fingerprint is frozen.

## Candidate mechanisms
- D: first-order lag / low-pass dynamics
- M: persistent internal state with hysteretic switching and retention
- N: static nonlinear saturation control
- Q: lag + nonlinear response control

Labels are hidden during extraction.

## Protocol
1. Apply identical slow and fast ramps.
2. Reverse the input before and after apparent state transitions.
3. Return input to a previously visited value.
4. Hold input fixed and observe whether output retains a branch/state distinction.
5. Repeat the same input sequence after a reset.
6. Repeat with multiple amplitudes and frequencies.
7. Extract features without using mechanism names.
8. Freeze the fingerprint.
9. Only then reveal labels and audit correspondence.

## Blind features
- forward/reverse discrepancy
- loop area
- phase lag
- reversal-point dependence
- return-point dependence
- retention after input hold
- recovery/reset dependence
- cycle-to-cycle convergence
- amplitude scaling
- frequency scaling
- state separability at equal input
- repeatability after identical history

## Critical discriminator
At equal instantaneous input x, compare y after different histories H1/H2.

A persistent state candidate requires a history-dependent output difference that survives sufficiently long after the input is returned to the same value, while a pure lag candidate should lose that difference according to its relaxation dynamics.

This is not sufficient by itself: the test must compare retention time, reversal dependence, reset response, and scaling across frequencies.

## Controls
- Pure delay/lag control
- Static nonlinearity control
- Noise-only control
- Synthetic memory-positive control

## Null hypothesis
Observed loop/hysteresis-like geometry can be explained by instantaneous nonlinearity and/or finite dynamical lag without a retained state variable.

## Positive methodological result criterion
The blind pipeline separates persistent-history behavior from ordinary lag with stable feature differences across perturbation scales, without labels entering feature extraction.

## Failure criterion
If lag and retained-state systems remain indistinguishable under the preregistered observables and tolerances, report NON-SEPARABLE-AT-THIS-RESOLUTION rather than forcing a distinction.

## Interpretation rule
No claim of physical memory is permitted from this synthetic test alone. A successful separation validates the measurement protocol, not a new physical law.

## Next step
Apply the same blind extractor to digitized or directly recorded physical systems with unknown labels, then perform Ω ↔ Physics bidirectional correspondence.
