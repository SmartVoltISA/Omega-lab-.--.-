# EXP-C1-024 — Role-Control Matrix

**Date:** 2026-08-28  
**Branch:** `research/cicada-3301`  
**Status:** CONTROL DESIGN / NO GLOBAL-ROLE CLAIM

## Objective
Test whether 3301/1033 are unusually persistent *operational* markers rather than merely salient numbers.

## Existing evidence
C1-023 establishes repeated operational roles for 3301 and 1033 across 2013–2014, but explicitly notes that recurrence alone is insufficient and that 3301 is a matched control. See `EXP-C1-023-1033-OPERATIONAL-RECURRENCE.md`.

## Control values
Use the same role taxonomy for other salient values already present in the corpus: 761, 313, 353, 757, 1039. Do not select controls after seeing their apparent success.

## Role taxonomy
For every occurrence, classify only if the value performs an operation:

1. STREAM_STOP / STATE_MARKER — changes execution or timing of a process.
2. COMMAND_SELECTOR — appears as an input selecting a response/object.
3. ADDRESS_SELECTOR — identifies or routes to an external object/endpoint.
4. PHYSICAL_ENDPOINT — used in a phone/poster or other physical access path.
5. STRUCTURAL_INVARIANT — defines a matrix/square/geometry constraint.
6. AUTH_MARKER — appears as part of signature/authentication identity.
7. EXTRACTION_KEY — demonstrably used to unlock/extract another artifact.
8. VERSION_LABEL — version/user-agent only; weak evidence unless linked to an operation.

## Scoring rule
Do not count raw textual appearances. For each value, count distinct stages and distinct role classes, with provenance links. A role counts only when the source demonstrates an operation or constraint.

Primary comparison:

`R(v) = number of distinct operational role classes`

Secondary:

`S(v) = number of distinct stages with operational evidence`

A candidate persistent routing marker must outperform matched controls on both R and S, and at least one repeated role must occur in two different representation spaces.

## Falsification
The hypothesis is weakened/rejected if:

- controls show equal or greater role diversity;
- apparent roles collapse into the same source artifact;
- occurrences are mostly labels/version strings;
- no deterministic transition can be demonstrated from the marker to a selected object.

## Current conclusion
No statistical conclusion is claimed yet. C1-023 provides a strong recurrence observation for 3301/1033 but not a universal semantic role. This experiment converts the next step into a controlled comparison rather than further confirmation hunting.

## Key research question
If 3301/1033 are routing markers, what deterministic operation connects the marker to the next selected object?

Until that edge is reproduced independently, the graph interpretation remains **compatible but unproven**.
