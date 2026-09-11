# Ω-Test-3 — Dynamic Boundary / Opposition / Memory

**Experiment ID:** Ω-TEST-3-DYNAMIC-BOUNDARY-2026-09-12  
**Date:** 2026-09-12  
**Time:** 02:51 (UTC+05:00, experiment run timestamp)  
**Status:** COMPLETED / EXPLORATORY NUMERICAL TEST

## Research question

Can a minimal abstract boundary/front `b(t)` evolve from opposing processes, and can memory alter that trajectory?

## Model

```text
db/dt = k(I-E) - γb - μm

dm/dt = |db/dt| - λm
```

`b(t)` is an abstract boundary state, not physical space. `I` and `E` are opposing drives; `m` is a memory variable.

## Results

Drive scales 0.5, 1, 2 and 5 produced proportional boundary amplitudes and path lengths. The normalized quantity

```text
path_per_amplitude = total boundary path / amplitude
```

remained constant at approximately **8.875949** across those scales.

This is consistent with scale normalization for this particular linear model.

## Null control

A matched one-sided model was also tested:

```text
db/dt = I - γb
```

It also produced a moving boundary trajectory.

Null result:

> Boundary motion alone does not establish opposition.

The null model had `path_per_amplitude ≈ 8.712439`, close enough to demonstrate that the normalized path metric alone cannot identify the presence of opposing interaction.

## Interpretation

Supported:

1. A boundary/front can be represented as a time-indexed state `b(t)`.
2. Opposing processes can be represented explicitly through `I-E`.
3. Memory can modify dynamics without being identical to the instantaneous boundary state.
4. A path can be represented as the ordered history of boundary/state changes.

Not established:

1. Boundary movement proves physical struggle.
2. The model is a universal law.
3. A scalar boundary captures real multidimensional systems.

## Important negative result

The experiment rejects the naive criterion:

```text
moving boundary ⇒ opposition
```

because the one-sided null also moves.

Therefore Ω needs an observable specifically sensitive to **interaction between opposing components**, rather than merely to motion, path length, or amplitude.

## Next experiment

Compare the full opposing model with a statistically matched null preserving the marginal properties of each drive. Pre-register an interaction-sensitive statistic and use permutation/bootstrap testing.

## Provenance

The computational run and result file were produced locally and retained separately. The experiment record preserves the model, result, null control, limitation, and next test.

**Canonical status:** research result, not universal physical law.
