# Ω REL-009 — Conflict → Selection → Memory

Date: 2026-08-13
Status: EXECUTED / EXPLORATORY RESULT

## Question

Does retaining the outcome of relation competition create path dependence, compared with the same competition without retained memory?

## Models

- M0 — competition without memory: winner affects current strength but leaves no persistent memory trace.
- M1 — competition with memory: winner leaves a persistent trace that biases subsequent selection.

Common parameters:

- 8 competing alternatives;
- 500 steps per run;
- 100 independent runs per model;
- competition = 1.0;
- memory rate = 0.12 in M1;
- fixed random-seed scheme.

## Executed results

### M0 — no memory

- winner persistence: **0.5968 ± 0.1139**
- winner changes: **201.20 ± 56.84**
- winner entropy: **1.2385 ± 0.2709**
- distinct winners: **8.00 ± 0.00**

### M1 — memory

- winner persistence: **0.7423 ± 0.0872**
- winner changes: **128.58 ± 43.53**
- winner entropy: **0.8946 ± 0.2527**
- distinct winners: **8.00 ± 0.00**

## Direct observation

Adding the retained winner trace increased persistence and reduced switching/diversity of the sequence of winners in this model.

Observed changes:

- persistence: +0.1455 absolute;
- winner changes: −72.62 per 499 transitions on average;
- entropy: −0.3439.

All 8 alternatives remained reachable at least once in the aggregate per-run metric, so this run does NOT demonstrate complete elimination of alternatives.

## Interpretation

The executed model supports the narrower statement:

> **When the result of a competition is retained and fed back into later selection, the future sequence becomes path-dependent and more persistent than in the matched no-memory model.**

This is consistent with the hypothesis that memory can act as a constraint on future choices.

It does NOT establish:

- that conflict is universally necessary for memory;
- that memory is universally identical to a boundary;
- that the mechanism is fundamental to Ω;
- that this toy mechanism reproduces the historical edge-only experiment;
- that the result is physical.

## Important methodological limitation

M0 and M1 used independent seed ranges. The next robustness check should use matched random streams / common-random-number controls so that the external perturbations are identical between the paired models.

The present result is therefore an exploratory positive result, not a final confirmation.

## Required next test

Repeat with matched perturbation sequences for M0/M1, then vary memory rate and run additional seeds. Test whether the persistence difference remains when the external random drive is exactly paired.

## Honesty rule

This file records an actual executed run. It must not be upgraded to CONFIRMED without the matched-seed control and further checks.
