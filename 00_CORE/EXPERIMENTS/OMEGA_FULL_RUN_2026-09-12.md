# Ω FULL EXPERIMENT RUN — 2026-09-12

**Run timestamp:** 2026-09-12, 02:51 UTC+05:00  
**Scope:** T1–T6 local mathematical stress run  
**Status:** COMPLETED

## Summary

| Test | Status | Result |
|---|---|---|
| T1 — 3D spiral / 2D projection | PASS | top-radius RMS error `4.955e-17` |
| T2 — boundary vs trajectory | PASS | closed-loop error `2.449e-16`; open helix endpoint distance `3.769911` |
| T3 — dynamic boundary + memory | PASS (model) | path/amplitude `67.565649` |
| T4 — opposition-specific invariant | FAIL | `J_full=0.632159`, `J_null=0.710391`; statistic not specific |
| T5 — scale invariance for similar helices | PASS | max relative error `1.802e-16` |
| T6 — universality stress test | FAIL | normalized metric range `22.532866–90.291626` |

## T1 — 3D spiral / projection

The full object is a 3D helix. Its orthogonal projections can appear sinusoidal or circular. The ideal cylindrical top-view radius is constant to numerical precision.

**Conclusion:** 3D structure and 2D observation must remain distinct.

## T2 — boundary vs trajectory

A closed circular curve closes with error `2.449e-16`. The open helix has endpoint separation `3.769911`.

**Conclusion:**

```text
trajectory ≠ boundary
```

A trajectory does not automatically create an internal/external partition.

## T3 — dynamic boundary

A time-indexed abstract boundary `b(t)` with opposing drives and memory evolves continuously. Baseline normalized path/amplitude was `67.565649`.

**Conclusion:** a dynamic boundary is a valid model construction, but movement is not evidence of physical struggle.

## T4 — opposition invariant

The tested statistic failed to distinguish the full opposing model from the no-interaction null:

```text
J_full = 0.632159
J_null = 0.710391
```

**Conclusion:** the candidate is rejected as an opposition-specific invariant.

## T5 — scale invariance

For geometrically similar helices, the dimensionless combinations `κL`, `τL`, and `τ/κ` remain invariant under uniform scaling.

Maximum relative error in the analytic scale test: `1.802e-16`.

**Conclusion:** selected geometric descriptors are scale-invariant within the tested helix class, but are not universal constants.

## T6 — universality stress test

The dynamic normalized metric `path/amplitude` changed substantially across frequency and memory parameters:

```text
minimum = 22.532866
maximum = 90.291626
```

**Conclusion:** this metric cannot currently be promoted as a universal Ω invariant.

## Overall scientific status

The Ω construction survives internal mathematical consistency checks, but **no universal physical invariant has been established**.

### Survives

- 3D spiral vs 2D projection distinction;
- boundary vs trajectory distinction;
- time-indexed boundary as an abstract dynamical state;
- scale invariance of selected dimensionless descriptors for similar helices.

### Does not survive as universal evidence

- spiral shape as a universal invariant;
- boundary motion as proof of opposition;
- current opposition statistic;
- current normalized boundary-path metric.

## Epistemic boundary

These are synthetic mathematical experiments. They test internal consistency and falsifiability of the Ω construction. They do not establish that physical space is spiral or that unrelated physical systems obey one common law.

## Next target

**Ω-Test-5:** construct independent generative systems with interaction present/absent while matching marginal statistics, and preregister an interaction-sensitive statistic before inspecting outcomes.

## Provenance

The full-run report and CSV summary were generated locally and retained with this experiment record. Failed tests remain part of the permanent research history.
