# EXP-007 — Relation Endpoint Coalescence (reconstruction)

**Status:** EXECUTED / RECONSTRUCTED OPERATIONALIZATION  
**Date:** 2026-11-12  
**Historical source:** Ω-Lab Archive 013, section 2; related protocols in Archives 016 and 018.  
**Integrity warning:** the original source code, exact geometry, movement law, time horizon, random seeds and raw outputs were not preserved. This experiment is therefore **not an exact replication**. It is a transparent reconstruction inspired by the archived description.

## Question

Can a graph of relations form cycles and higher-order structure when endpoints move and are joined only when they approach within a distance threshold, without initializing graph vertices as primitives?

## Reconstructed model

- Start with 150 relations, represented as 300 free endpoints paired into edges.
- No graph vertices or clusters are initialized.
- Endpoints move by independent Gaussian displacements on a periodic 2D box (side 10).
- When two endpoint clusters approach closer than threshold, they are coalesced.
- The original 150 relations remain; their endpoint equivalence classes define the quotient multigraph.
- A vertex is therefore a derived endpoint-cluster, not a primitive object.

Parameters: 500 steps; movement standard deviation 0.08; 40 seeds per threshold; thresholds 0.05, 0.10, 0.20. For each spatial run, a matched null control performs the same number of random endpoint coalescences without using spatial proximity.

## Measurements

- number of derived vertices;
- connected components and giant-component fraction;
- cycle rank (first Betti number of the multigraph): E − V + C;
- self-loops;
- triangle count;
- mean degree.

The matched-random control is essential: it tests whether spatially selected endpoint collisions produce more organized topology than simply contracting the same number of endpoint pairs.

## Results

| Threshold | Derived vertices (mean) | Cycle rank (spatial) | Cycle rank (matched random) | Triangles spatial | Triangles random |
|---:|---:|---:|---:|---:|---:|
| 0.05 | 59.93 | 91.23 | 91.40 | 37.83 | 41.70 |
| 0.10 | 30.20 | 120.83 | 120.80 | 111.80 | 108.60 |
| 0.20 | 19.48 | 131.53 | 131.53 | 122.95 | 101.38 |

At threshold 0.10, the spatial rule and matched-random contractions are nearly indistinguishable on cycle rank, loops and triangle count. The spatial model does not show a reliable topology advantage.

At threshold 0.20, spatial contractions produce more triangles than the matched-random control (paired mean difference +21.58; 95% paired-bootstrap CI +9.47 to +32.98 in 40 seed pairs). However, the graph is already highly collapsed: approximately 19.5 derived vertices remain from 300 endpoints and the giant component contains essentially all vertices. This is a threshold-sensitive local clustering signal, not evidence of a robust general mechanism for meaningful node formation. Multiple metrics and thresholds were explored, so the isolated signal is exploratory.

At threshold 0.05, the spatial process does not outperform the matched-random control.

## Interpretation

1. **Emergent vertices are constructible:** endpoint equivalence classes can define vertices after relational endpoints coalesce; no vertex set is supplied at initialization.
2. **Cycles appear in the quotient graph:** the cycle rank rises as endpoints coalesce while the relation set remains fixed.
3. **But cycles alone are not evidence of organized emergence:** matched random contractions generate almost the same cycle rank.
4. **Spatial proximity may influence local clustering in a high-coalescence regime:** the triangle-count difference at threshold 0.20 is a candidate effect, but it occurs alongside near-total connectivity/collapse and lacks robustness at the archival threshold 0.10.
5. **No recursive emergence was tested:** this model does not allow derived vertices to create new relations and then form higher-level vertices.

## Sensitivity check

With threshold fixed at 0.10 and movement standard deviation varied (0.04, 0.08, 0.16; 20 seed pairs each), the spatial rule did not consistently exceed matched-random coalescence in triangle count. Thus the high-threshold triangle signal should not be generalized.

## Decision

**PARTIAL / NOT CONFIRMED.**

This reconstruction demonstrates a mathematical mechanism by which vertices and cycles can be derived from endpoint relations. It does **not** establish that spatial relations spontaneously create stable, meaningful nodes in a robust way. The crucial control shows that much of the apparent cycle formation is a generic consequence of endpoint contraction.

## Next experiment

Keep the relation-first representation, but add a preregistered mechanism for persistence/selection of endpoint clusters and test whether it creates reusable, perturbation-resistant modules beyond matched random contraction, without tuning thresholds after seeing results. Then test whether those modules can become relations at the next level.

## Reproducibility

Run:

`python EXP-007_RELATION_ENDPOINT_COALESCENCE_RECONSTRUCTION.py`

The script writes `EXP-007_RELATION_ENDPOINT_COALESCENCE_RESULTS.json` with per-seed raw outputs and aggregate summaries. The JSON is generated by the script and is not hand-entered.
