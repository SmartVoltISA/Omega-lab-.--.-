# Ω-Lab — EXP-005 Spontaneous Boundary Without Predefined Modules — 2026-10-08

## Status

EXECUTED / NEGATIVE RESULT

## Question

Can a persistent boundary arise spontaneously from relational dynamics when no modules, groups, or boundary labels are supplied?

## Model

- 24 states
- initially homogeneous relation weights
- no predefined groups
- one stochastic trajectory
- local Hebbian reinforcement after each transition
- global slow decay
- 20,000 transitions
- 30 independent seeds
- boundary inferred only after dynamics from similarity of transition distributions using a spectral partition

## Results

Across 30 seeds:

- bootstrap stability of inferred partition: **0.905 ± 0.050**
- fraction of total relational weight inside inferred groups: **0.343 ± 0.114**
- fraction crossing inferred groups: **0.657 ± 0.114**

A row-permuted null produced mean cut conductance approximately **0.493 ± 0.022**, while the inferred partition had mean conductance **0.657 ± 0.114**.

## Interpretation

This is a negative result for the present mechanism.

The inferred partition can be stable under resampling, but stability alone does not make it a meaningful boundary. In this model the inferred split does not preferentially concentrate relational weight inside the proposed regions; in fact, the cut is worse than the row-permuted null on average.

Therefore:

> **No spontaneous meaningful boundary was demonstrated under this relational learning rule.**

This is important because it prevents us from confusing a mathematically stable partition with a physically/causally meaningful boundary.

## Decision

Do not promote spontaneous boundary emergence.

Do not add a boundary mechanism merely because a clustering algorithm always returns a partition.

## Next stronger experiment

Change the question from "can clustering find a boundary?" to:

> **Does a candidate boundary predict different responses to perturbations on its two sides?**

A boundary should earn its status only if intervention reveals a functional separation:
- perturb inside → primarily internal recovery;
- perturb outside → primarily external response;
- crossing the boundary → measurable change in predictive dynamics;
- candidate boundary should improve recovery/prediction over capacity-matched controls.

This becomes EXP-006.

