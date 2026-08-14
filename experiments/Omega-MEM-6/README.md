# Ω-MEM-6 — Predictive Distinguishability → Choice

**Status:** PILOT / not final
**Date:** 2026-08-14
**Relation:** continuation of Ω-MEM-5.

## Question

If memory makes future transitions distinguishable, does that reduce uncertainty in the next transition and change the realized transition distribution?

Working chain:

`history → memory → distinguishable futures → next-transition distribution`

## Pilot design

Compare the same current observable state under:

1. relevant memory;
2. capacity-matched irrelevant/random memory;
3. no memory.

Primary metric:

`H(X_next | current_state, memory)`

Secondary metric:

`ΔH = H(X_next | current) - H(X_next | current, memory)`

The pilot intentionally does not claim agency, free will, or a universal law of choice.

## Important limitation

This pilot is a computational sanity check, not the final Ω-MEM-6 protocol. It uses deterministic toy generators and one fixed random seed for controls. A final run must use multiple seeds, matched capacities, confidence intervals, raw data, and an independent audit.
