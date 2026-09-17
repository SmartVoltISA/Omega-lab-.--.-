# REL-70 — Black-Box Dynamics Fingerprint

**Date:** 2026-09-17  
**Layer:** Ω-Lab  
**Status:** PILOT / CONTROLLED METHODOLOGY

## FACT

Public nonlinear-system benchmarks provide input-output datasets for systems including Bouc-Wen hysteresis, Wiener-Hammerstein systems, cascaded tanks, and other nonlinear dynamics. The Bouc-Wen benchmark is explicitly designed as a blind identification problem from synthetic input-output data. citeturn0search0turn0search9

Hysteresis identification is difficult because the relevant memory state can be internal and unmeasured; black-box nonlinear state-space identification is therefore an established approach. citeturn0search1

## OBJECTIVE

Construct an Ω fingerprint without using the physical/model name and without assuming a particular model family.

Input:

`u(t), y(t)`

Output fingerprint:

`F = {response, reversibility, threshold, memory, retention, recovery, scaling, basin}`

## PRE-REGISTERED TEST LOGIC

### 1. Response

Measure whether output follows input, lags input, amplifies it, saturates, or changes regime.

### 2. Reversal

Run the same input trajectory forward and with controlled reversal. Compare output paths.

A persistent loop under slow/quasi-static reversal is evidence for hysteretic behavior; ordinary phase lag alone must not be classified as hysteresis. The benchmark literature uses persistence of the input-output loop as the defining behavioral signature of hysteresis. citeturn0search1turn0search7

### 3. Threshold

Estimate transition regions independently for increasing and decreasing input.

### 4. Memory test

At approximately the same instantaneous input value, compare outputs following different histories.

`same input + different history -> different state`

is required for a history-dependent classification.

### 5. Retention test

Remove or hold the external drive and measure whether the state persists.

This separates transient lag from persistent internal state.

### 6. Recovery test

Apply a standardized perturbation, return to nominal input, and measure return to the previous state/basin.

### 7. Scaling

Repeat with amplitude/frequency changes to distinguish genuine state dependence from an artifact of one excitation regime.

## NEGATIVE CONTROLS

At minimum include:

- linear lag system;
- low-pass filter;
- nonlinear saturation without memory;
- noisy threshold system;
- hysteretic system;
- system with hidden internal state but no hysteresis.

The classifier must not infer hysteresis merely from correlation, phase lag, saturation, or noise.

## BLINDNESS RULE

During fingerprint extraction and clustering:

- physical name hidden;
- model family hidden;
- mechanism label hidden;
- benchmark identity hidden;
- only input-output observations available.

Names are revealed only after the fingerprint and cluster assignments are frozen.

## DECISION RULE

Do not output `HYSTERESIS = TRUE` from one statistic.

Use a conjunction of independent behavioral checks:

`H = loop persistence + history dependence + reversal asymmetry + retention/return-path evidence`

with thresholds preregistered before evaluation.

If the evidence is incomplete, output `CANDIDATE` rather than `TRUE`.

## EXPECTED Ω OUTPUT

The system should produce two layers:

### Mechanism-agnostic behavioral class

Examples:

`LAGGED_RESPONSE`

`NONLINEAR_MEMORY`

`HYSTERETIC_MEMORY`

`MULTISTABLE_SWITCHING`

`CONTINUOUS_MEMORY`

### Physical correspondence

Only after reveal:

`KNOWN CORRESPONDENCE`
`PARTIAL CORRESPONDENCE`
`CANDIDATE`
`NEW HYPOTHESIS`

## CHECK

This design directly addresses the failure discovered in REL-69: ordinary delay can imitate memory in a limited observation window.

The new test requires history comparison, reversal, retention, and perturbation recovery. This makes the fingerprint dependent on behavior under controlled transformations rather than on static statistics.

## RESULT

**Methodological result:** Ω can now distinguish the question “does the output lag?” from the stronger question “does the system retain state information that changes its response under the same instantaneous input?”

This does not yet constitute experimental physical validation. The next implementation should run on public benchmark data without using benchmark names during extraction.

## NEXT

Run the same pipeline on at least three classes:

1. hysteretic benchmark;
2. non-hysteretic nonlinear benchmark;
3. linear/dynamic control.

Then add noise and reduced observation windows.

The decisive metric is not classification accuracy alone. It is **false-positive resistance**: whether non-memory systems remain outside the hysteretic-memory class under changes of excitation and noise.

## FIXATION

REL-70 supersedes no previous anchor. It extends REL-69.

Core chain:

`OBSERVATION → CONTROLLED PERTURBATION → TRAJECTORY → DYNAMIC INVARIANTS → FINGERPRINT → FUNCTIONAL CLASS → PHYSICAL CORRESPONDENCE`
