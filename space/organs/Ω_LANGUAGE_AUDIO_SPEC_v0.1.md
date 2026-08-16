# Ω-Language Organ — Audio / Prosody Extension v0.1

## Purpose
Extend the language organ from text-only semantics to speech-aware semantics without turning audio into a monolithic model.

## Representation layers

1. **Waveform layer** — raw audio/time samples; kept at the boundary.
2. **Acoustic feature layer** — fundamental frequency (F0), formants, amplitude/energy, noise/burst characteristics and timing.
3. **Phonetic layer** — phonemes/allophones and pronunciation candidates.
4. **Prosody layer** — stress/accent, pitch contour, duration, pauses, speaking rate and emphasis.
5. **Linguistic layer** — words/morphemes and semantic relations.
6. **Ω layer** — nodes, typed relations, state and graph-local context.

Speech acoustics can be represented with a compact set of physical parameters: vocal-fold vibration corresponds to fundamental frequency, while vocal-tract resonances correspond to formants; noise and burst components also carry information. See UCLA phonetics reference.

## Core invariant

Audio is evidence for interpretation, not permission to mutate the global graph. The language organ proposes structured candidates; existing graph-integrity checks and Guardian authorization decide whether a candidate is accepted.

## Prediction

The organ may predict missing/next phonetic or lexical candidates, but predictions remain candidates with confidence. It must not silently delete or rewrite confirmed structure. Any correction is an explicit transformation with an auditable reason.

## Pronunciation memory

Store pronunciation entries as reusable mappings:

`language + word/form + context -> phoneme sequence + stress/accent + optional variants + confidence/source`

Multiple pronunciations are first-class variants rather than overwritten values. This matches established pronunciation-lexicon practice (PLS).

## Processing loop

`audio -> acoustic features -> phonetic candidates -> language/context graph -> semantic candidates -> memory lookup -> validated interpretation -> text/voice output`

## Tests to add

- same word, different accent/context;
- same phoneme sequence, different lexical meaning;
- noisy audio and uncertain phoneme candidates;
- missing word prediction from graph context;
- pronunciation variant preservation;
- prosody changes without semantic change;
- semantic change signalled by prosody/context;
- graph integrity remains unchanged until Guardian-approved commit.

## Research boundary

Use external speech/phonetics resources as references and datasets, not as architectural dependencies. First implement deterministic feature/lexicon structures and benchmarks; only then evaluate a learned acoustic component.
