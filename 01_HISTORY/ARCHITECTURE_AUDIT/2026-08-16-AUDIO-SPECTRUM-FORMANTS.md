# Ω-Audio Organ — Spectrum/Formant Layer

Date: 2026-08-16

## Implemented

- Added deterministic DFT-based spectral feature extraction.
- Added dominant-frequency candidate.
- Added spectral centroid.
- Added first three spectral peak candidates as provisional F1/F2/F3 fields.
- Added tests for silence, a 500 Hz reference tone, and candidate semantics.

## Scientific boundary

Spectral peaks are not automatically formants. True formant tracking requires temporal context and vocal-tract/acoustic constraints; therefore these values remain candidates. F1/F2/F3 are standard formant labels, while F0 is the fundamental frequency and not a formant.

## Next

Add windowed/time-local analysis, temporal transitions, phoneme candidate records, and Ω-graph edges. Do not promote an acoustic candidate to a linguistic fact without contextual validation.
