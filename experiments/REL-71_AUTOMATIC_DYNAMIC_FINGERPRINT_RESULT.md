# REL-71 — Automatic Dynamic Fingerprint Extraction Result

**Status:** pilot result / exploratory computational test  
**Date:** 2026-09-17  
**Layer:** Ω-Lab / relational-dynamics experiments

## Question

Can a black-box procedure extract useful dynamic distinctions from raw input/output trajectories without being told the physical labels in advance?

## Blind systems

Six anonymous synthetic systems were generated from the same multi-frequency input:

- A — direct response
- B — fixed input/output delay
- C — static nonlinear transformation
- D — saturation
- E — leaky internal-state response
- F — thresholded, history-dependent response

The analysis did **not** use the semantic names during feature extraction.

## Extracted observables

For each anonymous system the pilot calculated:

1. instantaneous input/output correlation;
2. correlation after fixed lag;
3. residual autocorrelation after removing the contemporaneous linear component;
4. signed/absolute input-output loop area;
5. rise/fall asymmetry;
6. output scale.

A second pass varied excitation period across 20, 40, 80 and 160 samples.

## Result

The blind observables separated several mechanisms that have similar static input/output appearance:

- direct response A produced near-zero loop area and near-zero residual memory;
- delayed response B produced a large loop area that decreased as excitation period increased;
- static nonlinear C and saturation D retained near-zero loop area compared with dynamic systems;
- leaky-state E retained substantial residual temporal dependence and a nonzero loop area over a broad period range;
- threshold/history-dependent F showed state-dependent behaviour, but the present toy construction did **not** produce a clean monotonic hysteresis signature across all periods.

Representative absolute loop-area values by excitation period:

| system | 20 | 40 | 80 | 160 |
|---|---:|---:|---:|---:|
| A | 0.048 | 0.012 | 0.003 | 0.001 |
| B | 13.541 | 12.143 | 6.979 | 3.629 |
| C | 0.085 | 0.024 | 0.006 | 0.002 |
| D | 0.067 | 0.017 | 0.004 | 0.001 |
| E | 4.795 | 6.864 | 6.336 | 4.047 |
| F | 0.237 | 0.080 | 0.004 | 0.015 |

## Interpretation

### Positive methodological result

Raw trajectories contain enough information to distinguish at least three broad classes without giving the classifier their physical names:

**memoryless → delayed/dynamic → state/history-dependent**.

Static nonlinearity and saturation can be separated from temporal-state effects when the analysis includes lag structure and excitation-period dependence.

### Important negative result

Loop area alone is **not** a valid universal memory/hysteresis detector.

A pure delay can generate a large input-output loop even though the system has no hysteretic internal state. Therefore:

> loop ≠ hysteresis
> 
> lag ≠ memory
> 
> nonlinearity ≠ hysteresis

This is consistent with the broader system-identification literature, where hysteresis is treated as a dynamic nonlinearity and identification requires more than a single geometric observable. See Noël et al. (2017), *A nonlinear state-space approach to hysteresis identification*.

## New requirement for REL-72

The fingerprint must become a **trajectory-response fingerprint**, not a collection of isolated scalar features.

Required tests:

1. multiple excitation frequencies;
2. amplitude sweep;
3. forward/reverse sweep comparison;
4. reversal-point dependence;
5. return-point/recovery test;
6. repeated-cycle convergence;
7. perturbation and recovery;
8. noise robustness;
9. separation of pure delay from internal-state memory;
10. model-free clustering only after feature extraction is locked.

The next experiment should explicitly include paired controls:

**delay control ↔ genuine hysteresis control**

under matched low-frequency loop geometry.

## Decision

**REL-71 PASS as a methodological pilot, NOT as a physical-discovery claim.**

The experiment supports the narrower statement that blind black-box trajectory features can expose structural/dynamic distinctions that static topology or instantaneous input/output mapping cannot.

It does not establish that the extracted clusters correspond to fundamental physical entities.

## Ω anchor

The current working representation is therefore upgraded from

`Entity = (Graph, Invariant, Transition, Control, Response)`

to an observational form:

`Fingerprint = (Structure-independent Observables, Transition, Lag, Reversal, Retention, Recovery, Scaling)`

with physical labels applied only **after** the fingerprint is frozen.

## External methodological correspondence

Black-box nonlinear state-space identification is an established approach to hysteresis identification; the cited literature explicitly treats hysteresis as a dynamic nonlinearity and discusses validation under different excitation conditions.

Reference: J.-P. Noël, A. F. Esfahani, G. Kerschen, J. Schoukens, 2017, *A nonlinear state-space approach to hysteresis identification*, Mechanical Systems and Signal Processing.

## Reproducibility note

The pilot used a fixed random seed (71), deterministic synthetic trajectories, and a fixed feature-extraction procedure. This is a computational pilot and should be rerun with preregistered tolerances before any stronger claim is made.
