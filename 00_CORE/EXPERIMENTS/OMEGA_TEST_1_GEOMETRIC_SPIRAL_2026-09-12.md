# Ω-Test-1 — Geometric Spiral Schema

**Experiment ID:** Ω-TEST-1-GEO-SPIRAL-2026-09-12  
**Date:** 2026-09-12  
**Time:** 02:51 (UTC+05:00, project-local timestamp)  
**Status:** COMPLETED / REPRODUCIBLE ANALYTIC CHECK  
**Class:** Geometry / invariance / null-control

## 1. Research question

Does the proposed 3D spiral representation produce mathematically consistent projection behavior, and do selected dimensionless geometric quantities remain invariant under uniform scaling?

## 2. Canonical model

For a cylindrical helix:

```text
x(θ) = R cos(θ)
y(θ) = R sin(θ)
z(θ) = aθ
```

A side projection can produce a sinusoidal dependence, while the full object remains a 3D helix.

The opposing idealized component may be represented by:

```text
r₋(θ) = −r₊(θ)
```

This is a symmetry condition of the model, not a universal physical law.

## 3. Quantities tested

Curvature:

```text
κ = R / (R² + a²)
```

Torsion:

```text
τ = a / (R² + a²)
```

Arc length for angular span Δθ:

```text
L = √(R² + a²) Δθ
```

Candidate dimensionless quantities:

```text
κL
τL
τ/κ
```

## 4. Scale test

The same helix shape was tested under uniform coordinate scaling by ×1, ×3 and ×10, meaning both `R` and `a` were scaled by the same factor.

### Result

```text
maximum relative error = 4.1969474027865506 × 10⁻¹⁶
```

This is numerical machine-level error. Analytically the three quantities are exactly scale-invariant for geometrically similar helices.

## 5. Negative / limitation result

Changing the ratio `R/a` changes the geometry and therefore changes `κL`, `τL`, and `τ/κ`.

Therefore these are **dimensionless geometric descriptors**, not universal constants of Ω.

A spiral is also not automatically a boundary. An open spiral does not by itself create an internal/external partition. A boundary must be defined independently as a curve, surface, interface, or equivalent domain condition.

## 6. Projection result

The full 3D helix contains information absent from a 2D projection. For example, a projection of the cylindrical helix onto a plane containing the axial coordinate can appear sinusoidal.

Canonical distinction:

```text
3D structure
     ↓ projection
2D observation

projection ≠ whole configuration
```

This supports the Ω rule that observation/projection must not be silently identified with the underlying configuration.

## 7. Methodological correction recorded

An initial numerical differentiation run falsely indicated a large scale-invariance error (~80%). Investigation showed that the discrepancy was caused by boundary artifacts from numerical differentiation of an open curve.

The test was therefore repeated analytically.

The initial result is **REJECTED as a physical/mathematical finding** and retained only as a methodological failure record.

Canonical lesson:

```text
unexpected result
      ↓
check measurement / discretization / boundaries / normalization
      ↓
only then classify the result
```

## 8. Current conclusion

The experiment supports the following limited claims:

1. The proposed 3D spiral is a mathematically valid object.
2. A 2D sinusoidal appearance can be a projection of a 3D spiral.
3. Selected dimensionless geometric combinations are invariant under uniform scaling for similar helices.
4. Opposite spiral components can be represented by a precise symmetry relation.
5. Spiral geometry alone does not establish a universal physical law.
6. Spiral geometry alone does not establish an internal/external boundary.

## 9. Ω status

**SUPPORTED:** geometric consistency of the model and its projection interpretation.  
**NOT ESTABLISHED:** universality across physical systems.  
**NOT ESTABLISHED:** physical spiral geometry of space itself.  
**NEXT TEST:** boundary ↔ internal/external ↔ opposing processes ↔ time ↔ cycle, with preregistered invariants and independent datasets.

## 10. Files / provenance

Associated computational outputs from the experiment:

- `omega_test1_report_corrected.md`
- `omega_test1_scale_invariance_corrected.csv`
- earlier raw numerical output: `omega_test1_geometric_results.csv`

The corrected analytic result supersedes the initial numerical scale result.

---

**Research rule:** preserve failed and rejected states; do not silently overwrite them.  
**Canonical distinction:** research direction ≠ proven universal law.
