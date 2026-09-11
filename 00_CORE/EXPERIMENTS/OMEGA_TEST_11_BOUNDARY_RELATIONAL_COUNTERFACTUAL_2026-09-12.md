# Ω-Test-11 — Boundary–Relational Counterfactual

**Experiment ID:** Ω-TEST-11-BOUNDARY-RELATIONAL-COUNTERFACTUAL-2026-09-12  
**Status:** COMPLETED / EXPLORATORY NUMERICAL TEST  
**Purpose:** test whether a boundary-relevant relational property disappears when an interaction is cut and returns when the interaction is restored.

## Model

Three synthetic families were tested:
- linear coupled dynamics
- bounded nonlinear (`tanh`) coupling
- asymmetric nonlinear coupling

The active phase used bidirectional coupling `c=0.35`. During the middle phase (`t=2000..3999`) the coupling was cut to zero, while external drives remained present. It was then restored.

Controls:
- `none`: no direct interaction
- `shared`: correlated external drives but no direct interaction

## Candidate observable

For each direction, one-step predictive gain was measured from adding the other component to an autoregressive baseline:

`G(A→B) = 1 - Var(residual_full)/Var(residual_base)`

The boundary-relational score was the mean suppression of bidirectional predictive gain:

`S_∂ = mean(G_pre - G_cut)`

and recovery was:

`R_∂ = mean(G_post - G_cut)`.

This is deliberately a relational observable: it asks whether the cross-component influence disappears under edge-cut intervention and returns after restoration.

## Results

Negative controls were used to set a pre-registered-style threshold at their 99th percentile:

`threshold = 0.00163662`

Classification on 450 datasets:
- TP = 150
- FN = 0
- FP = 3
- TN = 297
- sensitivity = 1.000
- specificity = 0.990

Mean suppression / recovery by family:

| family | condition | suppression | recovery |
|---|---|---:|---:|
| asym | direct | 0.092910 | 0.094097 |
| asym | none | 0.000024 | -0.000029 |
| asym | shared | 0.000021 | 0.000109 |
| linear | direct | 0.174889 | 0.175844 |
| linear | none | 0.000024 | -0.000029 |
| linear | shared | 0.000021 | 0.000109 |
| tanh | direct | 0.090191 | 0.091016 |
| tanh | none | 0.000024 | -0.000029 |
| tanh | shared | 0.000021 | 0.000109 |

## Interpretation

The direct-interaction condition shows a clear `high → low → high` pattern in the relational observable across all three tested model families, while the no-interaction and shared-drive controls remain near zero.

This is substantially stronger than Tests 4, 8, 9 and 10 for the specific question of whether a relation itself changes the reachable/predictive state of the other component.

However, this does **not** establish a universal physical Ω invariant. The observable is a statistical/causal signature for these synthetic dynamical families.

## Scientific status

**CONDITIONAL PASS — strong candidate relational property, not foundational.**

What is supported:
`active relation → cross-component influence`  
`cut relation → influence collapses`  
`restore relation → influence returns`

What is not established:
- universal physical law
- unique definition of `0`
- causality in arbitrary physical systems
- physical interpretation of predictive gain as energy, force, or time

## Ω interpretation

A useful operational form is:

`A ↔ 0 ↔ B`

where `0` denotes the boundary/interface reference.

The test supports the more precise statement:

> A boundary can carry a relational signature that changes under intervention on the relation crossing it.

This is stronger and safer than saying that boundary motion itself proves “struggle”.

## Next falsification

Repeat with:
1. graph diffusion / network dynamics,
2. coupled oscillators,
3. an independently generated system where the boundary is defined geometrically rather than from the same predictive statistic.

Require the same `high → low → high` signature without reusing the generating equations in the observable.

**Canonical rule:** RESULT ≠ TRUTH.

**Local provenance:** `omega_test11_boundary_counterfactual_report.md`, `omega_test11_boundary_counterfactual_results.csv`.
