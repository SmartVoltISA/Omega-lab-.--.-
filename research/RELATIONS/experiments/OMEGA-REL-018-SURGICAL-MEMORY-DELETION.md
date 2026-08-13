# Ω-REL-018 — Surgical Memory Deletion

## Question

If memory is the carrier of the boundary, does deleting ONLY the stored memory immediately before a reversal remove the delay?

## Purpose

Direct causal test of the Ω hypothesis under investigation:

> memory → boundary/resistance to the next transition

The test does not appeal to external scientific recognition. It tests the mechanism inside the experimental model and records both valid and invalid measurements.

## Experimental design

- Runs: 300 paired runs
- Steps per run: 600
- Target reversal: step 160
- Memory strength: 1.05
- Same external force history within each pair
- Same noise history within each pair
- Same initial state
- Control: memory retained
- Intervention: ONLY the stored memory is erased immediately before the target reversal

The simulation itself is identical between the paired conditions except for the memory deletion intervention.

## Measurement error discovered

The first REL-018 analysis used the wrong target direction for the reversal. The simulation was unchanged, but the metric was wrong.

Therefore the first numerical result is **INVALID and discarded**.

The metric was corrected and the complete analysis was rerun.

## Corrected execution result

| Condition | Mean delay | SD | Fraction delayed > 1 step |
|---|---:|---:|---:|
| Memory retained | 2.626667 | 2.088499 | 0.623333 |
| Memory erased | 1.000000 | 0.000000 | 0.000000 |

Paired difference (erased − retained): **−1.626667 steps**.

## Plain-language result

When the previous state is retained as memory, the next reversal is delayed.

When ONLY that memory is removed, the transition occurs immediately in every run.

In this model:

```text
previous result
      ↓
   memory
      ↓
 resistance to change
      ↓
 delayed next transition
```

Delete the memory:

```text
memory removed
      ↓
 resistance disappears
      ↓
 immediate transition
```

## Interpretation

The corrected experiment supports the narrower causal statement:

> **In this model, the stored historical state is the mechanism carrying resistance to the next transition.**

This is stronger than a simple correlation because the stored memory was directly intervened on while the external input was held paired.

It does **not** establish a universal law that every form of memory is identical to prohibition. The next falsification step is to test whether the same causal structure survives different memory implementations and different transition rules.

## Status

**Execution verified.**

**First REL-018 metric: INVALID — discarded.**

**Corrected REL-018 metric: retained.**

This file records the full history so the invalid result is not silently erased.
