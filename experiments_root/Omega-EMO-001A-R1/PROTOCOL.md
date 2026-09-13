# Ω-EMO-001A-R1 — Physical Color Basis Control, Corrected Replication

Status at registration: **PLANNED**

## Why this is a new experiment

The original `Omega-EMO-001A` protocol required both CIE 1931 XYZ and CIE 2006 LMS datasets. During execution, the downloaded CIE LMS file failed the checksum published on the CIE dataset page. Under Ω-Lab's no-retrospective-repair rule, the failed run is preserved and is not silently repaired. This file defines a new corrected replication using only the CIE 1931 dataset whose published checksum was verified.

Original failure: LMS published checksum `27c74cc0f98edecadc02fc71f540b116`; downloaded file checksum observed during the failed execution: `dba2e9d1f5e6667575aa069832159510`. No LMS result is claimed from that run.

## Question

For the verified CIE 1931 2° standard-observer colour-matching-function dataset, what is the smallest linear basis dimension required to represent the sampled full XYZ response vectors without exact loss? As a representation control, what is the intrinsic dimension after explicit chromaticity normalization and centering?

## Data

Official CIE 1931 dataset:
https://cie.co.at/datatable/cie-1931-colour-matching-functions-2-degree-observer
File: `CIE_xyz_1931_2deg.csv`
Published MD5: `17cca777db64b17170f06f67ce9d3ab7`

## Primary analysis

1. Verify the exact file MD5.
2. Load wavelength and three response columns.
3. Record row count and wavelength range.
4. Compute numerical matrix rank with NumPy default `matrix_rank` tolerance.
5. Compute singular values and normalized ratios.
6. Compute best rank-1, rank-2 and rank-3 SVD reconstructions and relative Frobenius error.
7. Perform leave-one-column-out linear reconstruction as a diagnostic.
8. Normalize each XYZ row by X+Y+Z, center the resulting points, and compute the intrinsic affine dimension by ordinary linear rank/SVD.

## Minimality criterion

A basis dimension is a candidate minimum only if all lower dimensions fail exact reconstruction for the specified representation. This is representation-specific and is not a claim about a universal Ω basis.

## Checks

- input checksum must pass;
- all loaded values must be finite;
- rank-3 full XYZ and rank-2 centered chromaticity must pass the preregistered invariants;
- rank-2 full XYZ reconstruction must have non-zero error;
- run the same exact code twice and compare machine-readable outputs byte-for-byte;
- independently recompute rank/SVD metrics outside the experiment script.

## Interpretation boundary

This is a physical color control only. It cannot establish that three is a universal basis of information, emotion, energy, or reality, and it does not identify three "fundamental colors". It tests dimensionality of one published response representation.

## Stop condition

If checksum or execution evidence fails, no experimental result is claimed and the issue is preserved for a new corrected replication.
