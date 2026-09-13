# Ω-EMO-001A-R1 — Results

Date: 2026-08-13
Status: **VALIDATED** for the tested CIE 1931 control only.

## 1. Execution provenance

Protocol commit before execution: `9765c172c532335b01c1def44a08cdf0c3e67eaf`

Code commit before execution: `d3416c4803627727d29790d20ec84171762a4d7d`

Code Git blob SHA: `c8005d3bf81e5bf0ea9c8d899d2ff893803d9b3b`

Runtime:
- Python 3.13.5
- NumPy 2.3.5
- pandas 2.2.3

Input:
- `CIE_xyz_1931_2deg.csv`
- MD5 `17cca777db64b17170f06f67ce9d3ab7`
- 471 rows, 360–830 nm

Command used for both runs:

`python run_xyz_basis_control.py --xyz CIE_xyz_1931_2deg.csv --output RESULTS.json`

## 2. Repeated execution

The exact same source code and exact same input file were run twice.

Run 1 output SHA-256:
`e9039bd9f4fd2fd3bc128343a459e64b6d529bf0a1c3686629da7e50439d4cc6`

Run 2 output SHA-256:
`e9039bd9f4fd2fd3bc128343a459e64b6d529bf0a1c3686629da7e50439d4cc6`

Byte-for-byte comparison: **PASS**.

## 3. Independent recomputation

A separate direct NumPy calculation, outside the experiment script, reproduced:

- full XYZ numerical rank = **3**;
- best rank-2 relative Frobenius error = **0.23881758083691765**;
- best rank-3 relative Frobenius error = **4.1159049975648407e-16**;
- centered chromaticity numerical rank = **2**;
- centered chromaticity rank-2 relative Frobenius error = **1.2158890770368865e-15**.

Independent recomputation therefore agrees with the archived execution.

## 4. Main observations

### FACT

The verified CIE 1931 XYZ response matrix has numerical rank 3 under the preregistered linear-rank/SVD procedure.

The singular values were:

`12.680500379283586, 10.594816825599407, 4.063830073876259`

Normalized to the first singular value:

`1.0, 0.8355204060329033, 0.32047868398911356`

### FACT

A best rank-2 reconstruction does not reproduce the full XYZ matrix exactly. Its relative Frobenius error is approximately **0.2388**.

A rank-3 reconstruction reaches numerical machine precision, approximately **4.12×10^-16** relative Frobenius error.

### FACT

The leave-one-column-out diagnostics also show substantial residuals. Relative residuals for reconstructing each dropped XYZ column from the other two were approximately:

- X from Y,Z: **0.62025**;
- Y from X,Z: **0.63929**;
- Z from X,Y: **0.95145**.

This supports the non-redundancy of the three published XYZ coordinates in this representation, while the coordinate-wise test itself is not the primary coordinate-invariant criterion.

### FACT

After explicit chromaticity normalization `XYZ/(X+Y+Z)` and centering, the intrinsic affine dimension is **2**. The third singular value was approximately **4.59×10^-15**, while the first two were approximately **9.73** and **5.29**.

A rank-2 reconstruction of centered chromaticity had relative error approximately **1.22×10^-15**.

## 5. What this does NOT show

It does not show that there are "three fundamental colors".

It does not show that the Ω information spectrum has three components.

It does not show that emotions have three components.

It does not show that XYZ, LMS, RGB, opponent channels, or perceptual unique hues are the same layer.

It does show something narrower: **for the tested full CIE 1931 XYZ representation, three linear degrees of freedom are required for exact reconstruction of the sampled response matrix; after an explicit intensity-normalizing operation that removes one degree of freedom, the chromaticity representation has intrinsic affine dimension two.**

## 6. Methodological consequence

The first result is not "the number is three" in a universal sense.

The result is:

> **the minimum basis depends on exactly what state information is required to preserve.**

Full XYZ response: 3 dimensions.

Chromaticity after removing overall scale: 2 dimensions.

This is a useful constraint for the next Ω experiment: before searching for a universal basis, we must define the state-preservation criterion and the transformation allowed to remove information.

## 7. Status against Ω-01-style checks

- execution evidence: **PASS**;
- reproducibility by exact rerun: **PASS**;
- method-independent direct recomputation: **PASS**;
- model-independence: **NOT TESTED**;
- adversarial destruction across alternative datasets/models: **NOT YET TESTED**.

Therefore this is **VALIDATED within the tested CIE 1931 control**, not a universal confirmation of the spectrum hypothesis.

## 8. Next scientific boundary

The next step should not be to declare three as the Ω basis.

The next step is to test whether the same minimality criterion survives a genuinely different representation/model, and only then move from the color control to the abstract state-space problem.
