# Ω-TEST-5 — INTERVENTION / INTERACTION TEST

**Date:** 2026-09-12  
**Status:** COMPLETED after numerical-stability correction.

## Purpose

Test whether interaction between opposing components can be detected by intervention rather than by correlation alone.

## Model

Independent external drives `I(t)` and `E(t)` are generated first.

Intact system uses bounded symmetric coupling:

`x(t)=0.55x(t-1)+0.5I(t-1)+c tanh(y(t-1))+noise`

`y(t)=0.55y(t-1)+0.5E(t-1)+c tanh(x(t-1))+noise`

Intervention sets the coupling channel to zero while retaining the same external-drive processes.

## Primary results (`c=0.35`)

Lagged correlation:

- null: `0.029244`
- intact: `0.601587`
- intervention: `0.029244`

Incremental prediction gain of `y` from previous `x`:

- null: `0.000000`
- intact: `0.002236`
- intervention: `0.000000`

100 shuffled surrogates of the intact `x` sequence:

- surrogate mean: `0.000010`
- surrogate SD: `0.000012`
- z-score: `186.586826`
- empirical one-sided p: `0.009901`

## Interpretation

The intervention removes the coupling mechanism while preserving the external-drive process. This gives the statistic a stronger causal interpretation than the correlation-only statistic tested in Ω-Test-4.

However, this is still a synthetic system with known coupling. It demonstrates detectability of interaction in this model class, not a universal law of nature.

## Ω classification

**PROMISING / CONDITIONAL PASS.**

Not foundational. Promotion requires survival across independent generative families, nonlinearities, noise levels, sampling schemes, and matched-marginal nulls.

## Methodological result

`correlation → intervention → response difference`

is a stronger route for testing the Ω interaction claim than visual similarity or raw correlation.

## Next experiment

Ω-Test-6: multiple independent generative families with matched marginals, hidden model identity, and a preregistered interaction-sensitive statistic. Test whether the interaction signal generalizes beyond the equations used to generate it.
