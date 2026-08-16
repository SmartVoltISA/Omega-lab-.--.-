# Ω-Audio — Candidate Sequence Graph

**Date:** 2026-08-16
**Status:** implementation complete; CI acceptance pending

## Implemented

Added the first explicit graph representation of temporal sound/phoneme candidates.

Pipeline now has a structural target:

`audio -> measurements -> segments -> candidates -> candidate nodes -> NEXT relations`

## Invariants

- Candidate nodes are ordered by time.
- Temporal adjacency becomes an explicit `NEXT` relation.
- Confidence remains attached to each candidate.
- Candidates remain unconfirmed by default.
- Duplicate node IDs and invalid confidence values fail closed.
- This layer does not write to confirmed/global graph memory.

## Meaning

The audio path now begins to use the same architectural primitive as the rest of Ω-Space: different elements become a connected structure through explicit relations. Confirmation and semantic promotion remain later guarded operations.

## Next

Add acoustic transition/noise evidence, competing candidate paths, context scoring and guarded promotion into the linguistic graph only after CI acceptance.
