# Ω-MEM-9 — Convergent Paths

**Status:** OPEN / protocol definition only
**Date:** 2026-08-14
**Relation:** continuation of Ω-MEM-8.

## Question

Can a path-dependent internal trace remain causally relevant after different histories converge to the same current observable state?

## Core construction

Create multiple histories that converge on the same observable state:

```text
A ─┐
   ├→ S₁ ─┐
B ─┘      │
          ├→ S₂ → {X,Y}
C ────────┘
```

At the observation point, `S₂` must be identical across histories. The internal memory may retain only a trace of the preceding path and must not contain a direct label for `X` or `Y`.

## Primary test

Compare future-transition statistics conditioned on:

1. current observable state only;
2. current observable state + path trace;
3. current observable state + capacity-matched irrelevant memory.

Then reset only the internal memory while holding the observable state fixed.

## Measurements

- `H(next | current)`;
- `H(next | current, memory)`;
- `I(next; memory | current)`;
- empirical transition distributions for convergent histories;
- divergence between those distributions;
- intervention effect after memory reset;
- persistence/decay of the history effect after additional convergent transitions.

## Critical controls

- Identical current observable state across history classes.
- Equal memory capacity.
- Equal sequence lengths and seed counts.
- No future-transition label in memory.
- Irrelevant-memory permutation control.
- Memory reset must not alter the observable state.
- Verify that the generator itself does not leak history labels through the observable state.

## Falsification

The hypothesis is weakened if convergent histories become statistically indistinguishable once current observable state is controlled, or if memory reset has no effect where the model predicts retained history dependence.

## Non-claims

This experiment does not test consciousness, agency, free will, or whether choice is fundamental. It tests only whether a path-derived internal trace can preserve causal predictive relevance through convergence of observable states.

## Freeze rule

This protocol is frozen before implementation. Any correction must be recorded as an amendment and must not silently alter the primary test.
