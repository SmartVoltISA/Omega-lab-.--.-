# Ω-Audio Organ v0.1 — Acoustic Layer

**Date:** 2026-08-16
**Status:** implementation committed; CI acceptance pending.

## Implemented

- Deterministic acoustic feature extractor.
- Duration and sample-rate metadata.
- RMS and peak amplitude.
- Zero-crossing rate.
- Autocorrelation-based F0 estimate with explicit bounds.
- Voiced/unvoiced decision derived from the F0 estimator.
- Unit tests for empty, constant, deterministic sine and basic measurement cases.

## Architectural rule

No neural network is used. Measurements remain explicit and auditable so that later stages can map them to Ω nodes, relations and graph candidates.

## Next

1. Windowed/spectral representation.
2. Formant candidates F1–F3.
3. Segment boundaries and phoneme candidates.
4. Prosody: stress, pitch contour and pauses.
5. Map acoustic candidates into Ω relations without auto-promoting guesses to facts.
