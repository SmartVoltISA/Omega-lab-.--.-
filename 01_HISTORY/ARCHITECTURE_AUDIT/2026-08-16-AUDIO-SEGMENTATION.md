# Ω-Audio Organ — temporal segmentation

## Implemented

Added a deterministic frame-based segmentation layer using short-time energy and zero-crossing behavior to expose candidate voiced/unvoiced regions.

## Invariant

Segmentation creates candidate temporal regions only. It does not assert phoneme identity and does not write to long-term/global memory.

## Next

Add transition features, consonant/burst cues and phoneme candidate nodes; validate them through Ω graph context.
