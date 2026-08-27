# EXP-C1-010 — Audit of the 2025 “Complete Solution” Claim

**Status:** INDEPENDENTLY UNVERIFIED
**Branch:** `research/cicada-3301`
**Date:** 2026-08-28

## Question

A repository by `nexon33/cicada3301` published a document dated 2025-10-28 claiming a near-complete Liber Primus solution based on Page 57-derived master indices, a dual Fibonacci/Lucas pattern, key generation by `index % 29`, and independently generated skip positions.

## Evidence inspected

The repository's `FINAL_COMPLETE_SOLUTION.md` claims:

- 1,543 candidate indices extracted from Page 57;
- 11 Welcome-page master indices;
- 8 indices directly observed and 3 derived;
- a Fibonacci/Lucas construction for the derived indices;
- key = master_index % 29;
- skip positions generated independently from a seed plus Fibonacci-related gaps;
- perfect reconstruction on five already-solved pages.

Its `VERIFICATION_REPORT.md` reports that its scripts pass self-tests and labels the extraction and mathematical relationships verified.

## Critical distinction

Passing the author's own scripts is **not independent verification of the proposed cipher mechanism**.

The report itself says community verification is still awaiting independent reproduction. Therefore the claim must not be promoted to PROVED merely because the package's internal tests pass.

## Strong observations

1. The eight directly observed indices are explicitly documented.
2. Several derived arithmetic relations are exact:
   - 217 = 102 + 115
   - 218 = 333 - 115
   - 566 = 333 + 233
   - 689 = 566 + 123
3. The claimed Fibonacci/Lucas relations are mathematically exact once those selected indices are accepted.
4. The repository reports reconstruction on five solved pages.

## Weak points requiring independent reproduction

1. Whether the 1,543 candidate index set is uniquely extracted from the original Page 57 image.
2. Whether the selection rule is uniquely determined rather than selected after observing the desired 11 indices.
3. Whether the Fibonacci/Lucas relations are predictive on held-out pages rather than descriptive of the already selected Welcome indices.
4. Whether `index % 29` predicts keys on pages not used to construct the hypothesis.
5. Whether skip positions can be generated for an unseen page without manual choices.
6. Whether the complete method decrypts an independently chosen unsolved page without parameter tuning.

## Anti-overfitting test required

Before accepting the claim, reproduce the method on a held-out page using only rules fixed before seeing that page's plaintext.

Minimum test:

`Page 57 extraction -> deterministic selector -> key -> deterministic skip generator -> decrypt held-out solved page`

Then apply the exact frozen algorithm to an unsolved page.

Success must be measured by:

- exact plaintext match on held-out solved pages;
- no manually selected seed/gap parameters;
- no post-hoc crib fitting;
- negative-control permutation/randomization test;
- reproducible output from a clean implementation.

## Current classification

- Page 57 candidate extraction: **REPORTED**
- Eight observed indices: **REPORTED / PLAUSIBLE**
- Three derived indices: **PLAUSIBLE**
- Fibonacci/Lucas relationships: **PROVED as arithmetic identities, not as author-intent/cipher law**
- `index % 29` key mechanism: **UNVERIFIED**
- independent skip generator: **UNVERIFIED**
- complete Liber Primus solution: **UNKNOWN**

## Important consequence for Ω-CICADA

This claim is valuable experimental material and should be tested, not dismissed. It is currently the strongest concrete alternative to the P20 prime-stream line.

The next experiment is therefore not another blind cipher search. It is a **frozen-algorithm replication test** of the Nexon/Adrian mechanism, followed by application to an unseen page.
