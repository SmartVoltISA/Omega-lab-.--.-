# Ω-Audio Organ — Phoneme Candidate Layer v0.2

**Date:** 2026-08-16

## Completed

- Added a deterministic F1/F2 candidate layer.
- Added a small seed vowel inventory.
- Candidate ranking is explicit and deterministic.
- Ambiguity is preserved; no candidate is asserted as truth.
- Invalid measurements produce no candidate.
- Added unit tests for ranking, invalid input and ambiguity.

## Architectural invariant

`acoustic measurement -> candidate -> graph/context validation -> confirmed symbol`

The candidate layer does not write to long-term memory and does not mutate the global graph.

## Scientific boundary

F1/F2 are useful acoustic cues for vowel identity, but static target values vary by speaker and context. This implementation therefore uses broad anchors only and does not claim speaker-independent phoneme recognition.

## Next

Temporal segmentation, candidate transitions, consonant/noise cues, then Ω-node/edge representation.
