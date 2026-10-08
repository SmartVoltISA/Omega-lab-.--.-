# Ω-Lab — Geometry Foundation Experimental Results — 2026-10-08

## EXP-002 — Recurrent topology vs state return

**Status:** EXECUTED / TOY RESULT

### Setup
- 12-state directed ring.
- 300 transitions.
- Same relational topology throughout.
- Retained trace updated at every visit.
- 30 seeds; deterministic dynamics, so seeds do not change topology/result.

### Result
- Topology edges: 12.
- Mean absolute trace difference between equivalent positions separated by one full cycle: **9.44954329**.
- Minimum observed difference: **1.9275**.
- Maximum observed difference: **11.79362628**.

### Interpretation
The same closed relational form recurs, while the retained trace is different.

This supports the *toy-model distinction*:

**closure of relational form ≠ return of historical state.**

It does not prove anything about physical time, memory, or nature in general.

---

## EXP-003 — Boundary as dynamical separation

**Status:** EXECUTED / NEGATIVE FOR CURRENT LEARNED-BOUNDARY METHOD

### Setup
- 12 states.
- Ground-truth internal module: states 0–5.
- External module: states 6–11.
- Internal transition retention: 92%.
- External transition retention: 65%.
- 5,000 transitions per run.
- 50 independent seeds.
- Compared:
  1. spectral/Fiedler learned cut;
  2. simple transition-retention threshold.

### Results
Spectral learned boundary:
- mean cut conductance: **0.2090**
- SD: **0.1353**
- mean F1 against planted boundary: **0.52**
- SD: **0.50**

Retention-threshold boundary:
- mean cut conductance: **0.07918**
- SD: **0.00414**
- mean F1: **1.00**
- SD: ~0

### Interpretation
The current spectral method failed to reliably recover the planted boundary in this toy system.

The simple retention threshold recovered the planted boundary perfectly because the data-generating process itself explicitly made internal retention the distinguishing feature.

Therefore this experiment does **not** demonstrate that a general dynamical boundary has been discovered.

It demonstrates a useful negative result:

> The proposed learned-boundary method is not yet adequate, and a boundary definition can accidentally encode the answer through the chosen statistic.

### Decision
Do not promote the spectral boundary mechanism.

Next boundary experiment must:
- avoid using the planted boundary's defining statistic directly;
- compare against capacity-matched controls;
- test intervention/recovery, not only boundary classification;
- use held-out perturbations.

---

## Independent geometry/memory rerun

A fresh 30-seed toy implementation of the memory/growth idea was also executed.

Mean prediction accuracy:
- flat: **0.006125 ± 0.001343**
- fixed memory: **0.884300 ± 0.017064**
- growing representation: **0.903320 ± 0.004978**

This is an independent implementation/run, **not** a replacement of the previously logged experiment because the implementation differs.

The qualitative result is consistent:
- memory strongly outperforms flat one-step history;
- growth gives a smaller additional gain;
- these are toy-model results only.

