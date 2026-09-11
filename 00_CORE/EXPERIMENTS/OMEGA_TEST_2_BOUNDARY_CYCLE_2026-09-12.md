# Ω-Test-2 — Boundary / Internal–External / Opposing Helices / Cycle

**Experiment ID:** Ω-TEST-2-BOUNDARY-CYCLE-2026-09-12  
**Date:** 2026-09-12  
**Time:** 02:51 (UTC+05:00, project-local timestamp)  
**Status:** COMPLETED / ANALYTIC + NUMERIC GEOMETRIC CHECK  
**Class:** Boundary semantics / symmetry / closure

## Question

Can the proposed Ω structure consistently distinguish a trajectory from a boundary, while retaining a central reference `0`, internal/external separation, and opposing 3D spiral components?

## Model

Two transverse-opposed helices:

```text
r₊(t) = (cos t, sin t, a t)
r₋(t) = (cos(t+π), sin(t+π), a t)
```

Therefore in the transverse plane:

```text
r₋,xy(t) = −r₊,xy(t)
```

## Results

### 1. Opposing symmetry

Maximum measured transverse symmetry error:

```text
1.9767 × 10⁻¹⁵
```

This is numerical machine precision. The opposite pair is therefore implemented consistently with the intended central symmetry.

### 2. Constant radial reference

For the cylindrical helix, radial distance from the central axis remains constant to numerical precision:

```text
variation = 1.11022 × 10⁻¹⁶
```

This supports treating the axis as a stable reference in this idealized model.

### 3. Closure test

A circle sampled at exactly `θ=0` and `θ=2π` closes with numerical error:

```text
2.449 × 10⁻¹⁶
```

Therefore a closed curve can define a boundary in its plane.

### 4. Open helix ≠ boundary

The tested helix remains open over four turns; endpoint separation is approximately:

```text
3.76991
```

Therefore a trajectory/helix must not automatically be identified with a closed boundary.

### 5. Pitch independence of transverse opposition

A parameter sweep over multiple helix pitches retained machine-level transverse opposition because the phase offset is fixed at `π`.

This means the symmetry is structural within the model and does not depend on a particular pitch value.

## Interpretation

The experiment strengthens several Ω distinctions:

```text
trajectory ≠ boundary
projection ≠ whole configuration
symmetry ≠ universal physical law
0 as reference/boundary ≠ relation value 0
```

A closed boundary can support an internal/external distinction. An open spiral is a trajectory and does not by itself provide that partition.

## Important limitation

This is a mathematical consistency test. It does not establish that physical space is spiral, nor that DNA, galaxies, black holes, biological histories, and other systems share the same physical mechanism.

The stronger research target remains a **structural invariant of relations**, not visual spiral similarity.

## Next experiment

Construct a minimal abstract dynamical system containing:

```text
BOUNDARY
INTERNAL
EXTERNAL
+1 / −1 opposing processes
TIME
CYCLE
MEMORY / HISTORY
```

Then search for an invariant that survives changes in coordinate representation and scale. The invariant must be preregistered before cross-system comparison.

## Provenance / correction

The initial closure sampling used a non-exact endpoint grid and produced a small apparent closure error (`0.00471356`). This was corrected by sampling the exact endpoints `0` and `2π`; the corrected error is machine precision. The initial value is retained as a methodological failure, not as a scientific result.

**Rule:** failed measurements are preserved; corrected measurements supersede them explicitly and never silently.
