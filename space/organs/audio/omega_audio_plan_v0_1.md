# Ω-Audio Organ v0.1 — Plan

## Goal
Build a deterministic acoustic layer for the Ω-Language Organ. It converts waveform measurements into auditable acoustic features, candidates and relations; it does not pretend to solve speech recognition yet.

## Pipeline

waveform → segmentation → acoustic features → phoneme candidates → syllable/word candidates → Ω relations → language organ → memory

Reverse path:

meaning/word → phoneme sequence → acoustic parameter targets → synthesis/test signal

## Feature set

1. F0 / fundamental frequency
2. energy / amplitude envelope
3. duration
4. F1–F3 formant estimates where valid
5. harmonic/noise indicators
6. spectral/aperiodic indicators
7. pauses and segment boundaries
8. prosodic contour: pitch, duration and intensity

These are deliberately kept as explicit measurable features. Acoustic phonetics demonstrates that speech can be represented using a compact set of physical parameters including fundamental frequency, formants, amplitudes and noise components. Prosody is likewise commonly described through pitch, timing, rhythm and stress. The prototype must preserve uncertainty rather than forcing a single interpretation.

## Ω representation

Every observation becomes an auditable record:

feature → value → time span → confidence → candidate relation

Candidate words are alternatives, not confirmed memory. Graph validation may rank or reject candidates but may not silently rewrite long-term memory.

## Stages

A. deterministic waveform measurements
B. segmentation and candidate phonemes
C. prosody/accent representation
D. candidate word reconstruction
E. Ω-graph integration
F. memory retrieval benchmark
G. multilingual/accent dataset experiments
H. only then evaluate whether a learned model is useful

## Acceptance criteria

- deterministic results on identical input;
- explicit confidence/unknown state;
- no direct global-memory writes;
- no capability escalation;
- graph integrity preserved;
- auditable feature-to-candidate path;
- full CI suite green before closing v0.1.

## Reference basis

UCLA phonetics material documents F0, formants, amplitudes and noise as measurable speech parameters; VoiceSauce documents automated measurement of F0, F1–F4, energy, CPP and harmonic/noise measures. These references guide the feature inventory, not the implementation itself.
