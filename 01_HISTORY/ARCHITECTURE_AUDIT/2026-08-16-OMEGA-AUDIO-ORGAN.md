# Ω-Audio Organ — Architecture History

**Date:** 2026-08-16
**Status:** plan initialized; implementation pending

## Decision

Create a separate Ω-Audio Organ rather than embedding a full speech/LLM model into the language organ.

## Rationale

The acoustic layer should expose measurable intermediate representations so that sound can be connected to Ω nodes, relations, graph context and memory without hiding the path inside a black box.

## Initial representation

waveform → acoustic features → candidate phonemes → candidate words → Ω relations → meaning

Reverse:

meaning → word/phonemes → acoustic targets → test/synthesis signal

## Important invariant

Prediction is a candidate, not a memory mutation. A guessed word or phoneme must carry uncertainty and cannot silently modify long-term memory.

## Evidence reviewed

UCLA phonetics resources describe F0, formants, amplitude and noise as useful acoustic parameters. Prosody is represented through pitch, duration/intensity, rhythm and stress. VoiceSauce demonstrates automated extraction of F0, formants, energy, CPP and harmonic/noise measures.

## Next step

Implement deterministic measurements and tests first; only after the measurable layer is stable evaluate learned components.
