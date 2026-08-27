# EXP-C1-008 — P20 166-rune provenance audit

Date: 2026-08-28
Status: ACTIVE / correction

## Finding

The current Wulfic master tracker reports a 166-rune P20 "prime-position stream" and a 646-rune remainder. It also reports a value-based separation into prime-valued vs non-prime-valued runes.

However, the same repository's P20 README explicitly records the earlier "Prime-Valued Runes vs Non-Primes" split as a FAILED ATTACK (IoC 1.11), and the canonical Gematria table maps all 29 runes to prime values. Therefore the phrase "prime/non-prime" cannot be interpreted naively as primality of Gematria values.

A second simple interpretation—1-based prime positions in the ~812-rune P20 text—does not produce 166 selected positions. Therefore the provenance of the 166-element stream is not established by the current evidence.

## Consequence

The previous Ω-CICADA hypothesis that "166 = prime-index selection" is withdrawn from PROVED/OBSERVED status and marked UNKNOWN pending reconstruction of the exact selector used to obtain 166 elements.

## Required reconstruction

Recover the exact transformation that maps the canonical P20 transcription to:

812 total runes -> 166 selected + 646 remainder.

Candidate selectors must be tested explicitly:
- rune-value predicates;
- 0-based vs 1-based position predicates;
- prime ordinal predicates;
- punctuation-aware indexing;
- page/image coordinate-derived ordering;
- combinations only where independently motivated.

## Acceptance criteria

A selector becomes a support only if:
1. it reproduces exactly 166 selected elements from the canonical transcription;
2. it reproduces the published P20 partial Old English result without using the published selected stream as an input;
3. the same selector is not tuned specifically to P20;
4. a shuffled/null control fails to produce equivalent language scores;
5. the full reversible procedure is recorded.

## Current status

- P19 plaintext clue: PROVED.
- Gematria Primus = 29 prime values: PROVED.
- P20 total transcription ~812: PROVED.
- 166-element stream reported by current tracker: REPORTED, provenance UNKNOWN.
- "prime-valued vs non-prime-valued" literal interpretation: REJECTED.
- 1-based prime-position interpretation: REJECTED as an explanation for 166.
- Full P20 solution: UNKNOWN.

This correction supersedes earlier Ω-CICADA notes that treated the 166-element selection as established.
