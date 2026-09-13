# Ω-B5 — Spatial shuffle control

## Purpose

Determine whether the difference between internal chaos and matched white noise depends on spatial organization, temporal correlation, or both.

## Hypothesis

If the internal dynamics remain temporally correlated but their spatial arrangement is destroyed by permutation, then a large reduction in domain size/lifetime would indicate that spatial correlation is an important part of the mechanism.

## Design

Compare:

### A — Original internal dynamics

Use the original `v(i,t)` field.

### B — Spatially shuffled internal dynamics

At every time step, randomly permute `v` across spatial locations while preserving:

- the time index;
- the marginal distribution of `v` at each step;
- mean;
- variance;
- temporal sequence of the field as a whole.

The permutation should destroy spatial correlation without replacing the process by independent white noise.

## Metrics

Pre-register:

1. number of domains;
2. mean domain lifetime;
3. mean domain size;
4. birth rate;
5. death rate;
6. spatial autocorrelation of `v`;
7. temporal autocorrelation of `v`;
8. correlation length;
9. distribution of `u`;
10. distribution of `|∇u|`.

## Replication

Run at least 100 independent seeds per condition if computationally feasible.

Report:

- mean;
- standard deviation;
- confidence interval;
- effect size;
- distribution across seeds.

## Interpretation

If original ≠ spatial shuffle while both retain similar temporal statistics, spatial organization is implicated.

If original ≈ spatial shuffle but both differ from white noise, temporal correlation is a stronger candidate explanation.

If original ≈ spatial shuffle ≈ white noise, the previously observed distinction may be explained by marginal statistics or implementation details.

## Status

**Proposed next experiment. Results pending.**
