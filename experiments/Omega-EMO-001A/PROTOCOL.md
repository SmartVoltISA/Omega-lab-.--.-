# Ω-EMO-001A — Physical Color Basis Control

Status at registration: **PLANNED**

## Purpose

Test the first, narrow empirical control for the Ω spectrum hypothesis using published CIE color-response datasets. This experiment does **not** test whether information or emotion has the same basis. It only tests whether the chosen color-response spaces require three independent linear channels under an explicitly defined representation.

## Governing Ω-Lab rules

This experiment follows `METHOD.md` and `EXPERIMENTS/README.md`:

- no fact without evidence;
- no result without execution;
- separate FACT / OBSERVATION / INTERPRETATION / HYPOTHESIS / UNKNOWN;
- preserve source data identity, checksums, code revision, execution record and raw output;
- attempt an adversarial check before extending the hypothesis;
- do not silently repair a completed experiment.

## Question

For a finite, published color-response dataset, what is the smallest linear basis dimension required to represent the sampled response vectors without exact loss?

## Models / controls

1. **CIE 1931 XYZ 2° standard observer** — 471 wavelength samples, three published colour-matching functions.
2. **CIE 2006 LMS 2° cone fundamentals, energy basis** — published LMS cone fundamentals. The source contains missing values; following the CIE dataset guidance, missing table entries are converted to zero for computational analysis and the count is recorded.
3. **Chromaticity-only control** — CIE 1931 XYZ rows normalized by X+Y+Z. Because normalization removes one degree of freedom, the intrinsic affine dimension is tested after centering the normalized points.

## Primary analysis

For each dataset:

1. verify the downloaded file checksum against the published CIE checksum;
2. load the three response columns;
3. record row count and wavelength range;
4. compute numerical matrix rank;
5. compute singular values and normalized singular-value ratios;
6. compute best rank-1, rank-2 and rank-3 SVD reconstructions and their relative Frobenius error;
7. perform leave-one-column-out linear reconstruction as a diagnostic, not as the primary coordinate-invariant test;
8. for chromaticity-only data, center the normalized 3-column points and repeat the rank/SVD test.

Numerical rank uses NumPy's default `matrix_rank` tolerance. No post-hoc threshold selection is permitted.

## Minimality criterion

A basis dimension is a candidate minimum only if all lower dimensions fail exact reconstruction under the primary representation. The result is representation-specific; it is not a claim about a universal basis of nature.

## Adversarial / robustness checks

- repeat the complete analysis from the same exact source files;
- rerun the same program twice and compare machine-readable outputs byte-for-byte;
- verify input checksums before each run;
- verify that the chromaticity control changes the dimensional question as predicted by its explicit normalization operation;
- do not infer "three fundamental colors" from a three-dimensional result.

## Data provenance

Official CIE 1931 dataset:
https://cie.co.at/datatable/cie-1931-colour-matching-functions-2-degree-observer
File: `CIE_xyz_1931_2deg.csv`
Published MD5: `17cca777db64b17170f06f67ce9d3ab7`

Official CIE 2006 LMS dataset:
https://cie.co.at/datatable/cie-2006-lms-cone-fundamentals-2-field-size-terms-energy
File: `CIE_lms_cf_2deg.csv`
Published MD5: `27c74cc0f98edecadc02fc71f540b116`

## Interpretation boundary

A successful three-dimensional color control can establish only that the tested full color-response representations have three independent linear degrees of freedom. It does not establish that three is a universal Ω basis, that the basis components are "colors", or that emotional/information states have the same dimensionality.

## Stop condition

If the exact source file, checksum, code revision or execution evidence cannot be verified, the experiment remains PLANNED/CODED and no experimental result is claimed.
