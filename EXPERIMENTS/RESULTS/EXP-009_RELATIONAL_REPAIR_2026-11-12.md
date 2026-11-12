# EXP-009 — Relational repair after perturbation

**Date:** 2026-11-12 · **Status:** exploratory pilot · **Seeds:** 100 · **Runs:** 400

## Design
100 vertices; initial random graph with 160 edges; add 240 relations by local triadic closure or degree-product null; delete a random 20% of edges; repair by adding the same number of new edges using either mechanism. Full factorial: 2 growth × 2 repair × 100 seeds. No planted modules, hidden labels, or replay of deleted edges. Partition NMI compares each damaged/repaired graph to the intact pre-damage graph's greedy-modularity partition.

## Results

| Growth | Repair | Damage transitivity | Repaired transitivity | Damage clustering | Repaired clustering | Damage NMI | Repaired NMI |
|---|---|---:|---:|---:|---:|---:|---:|
| closure | closure | 0.2388 | 0.2785 | 0.3500 | 0.4247 | 0.5489 | 0.4991 |
| closure | degree null | 0.2388 | 0.2111 | 0.3500 | 0.2823 | 0.5489 | 0.4564 |
| degree null | closure | 0.0974 | 0.1749 | 0.0907 | 0.2486 | 0.3534 | 0.2993 |
| degree null | degree null | 0.0974 | 0.1249 | 0.0907 | 0.1197 | 0.3534 | 0.2785 |

Closure repair minus degree-null repair, paired by seed; bootstrap 95% CI (10,000 resamples):

| Growth background | Metric | Delta | 95% CI |
|---|---|---:|---:|
| closure | transitivity | +0.0674 | [0.0655, 0.0694] |
| closure | avg clustering | +0.1424 | [0.1378, 0.1470] |
| closure | giant fraction | -0.0118 | [-0.0143, -0.0094] |
| closure | component count | +1.11 | [0.89, 1.34] |
| closure | efficiency | -0.0148 | [-0.0161, -0.0135] |
| closure | partition NMI | +0.0427 | [0.0244, 0.0604] |
| degree null | transitivity | +0.0500 | [0.0479, 0.0520] |
| degree null | avg clustering | +0.1289 | [0.1244, 0.1333] |
| degree null | giant fraction | -0.0068 | [-0.0084, -0.0053] |
| degree null | component count | +0.68 | [0.53, 0.84] |
| degree null | efficiency | -0.0073 | [-0.0084, -0.0063] |
| degree null | partition NMI | +0.0208 | [0.0066, 0.0352] |

## Interpretation
- **Supported:** triadic closure rebuilds local clustering more strongly than degree-product edge addition.
- **Not supported:** restoration of the original organization. In closure-grown graphs, NMI falls from 0.5489 after damage to 0.4991 after closure repair.
- Closure repair also yields slightly lower global efficiency and a smaller giant component than the degree-null repair. More triangles do not imply better global connectivity.
- Thus local structural rebuilding and recovery of the prior organization are separate outcomes.

## Limitations
The null is degree-product sampling, not exact degree-preserving rewiring. Greedy modularity is a heuristic, not ground truth. Only random 20% deletion was tested. Vertices are primitive in this model; emergence of vertices from relations is not tested. This is exploratory, not preregistered, and does not establish universal autonomy.

## Decision
**Partial support:** local generation of new relations restores local clustering after random damage.  
**Not supported:** recovery of the original community organization, full structural restoration, or autonomous node identity.

## Next
Add exact degree-preserving edge-swap controls, 10/20/40% damage sweep, targeted high-betweenness deletion, and planted-module positive control. Preserve the negative result: clustering recovery ≠ organizational recovery.
