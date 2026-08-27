# EXP-C1-009 — P20 selector recount

**Branch:** `research/cicada-3301`
**Status:** reproducible negative result / selector unresolved

## Objective
Determine where the reported 166-rune P20 stream comes from, without accepting the current tracker terminology as a definition.

## Primary source
P20 transcription from `Wulfic/Cicada3301-Liber_Primus/pages/page_20/runes.txt`.
The transcription contains **812 runes**. Gematria Primus maps 29 runes to indices 0–28 and to the first 29 primes.

## Independent counts
Using the repository transcription:

1. **0-based prime positions among the 812 runes:** 141 selected.
2. **1-based prime positions among the 812 runes:** 141 selected.
3. **Prime character positions including separators/newlines:** 138 (0-based), 140 (1-based).
4. **Prime character positions with newlines removed:** 133 (0-based), 141 (1-based).
5. **Runes whose Gematria INDEX is prime** (`2,3,5,7,11,13,17,19,23`): **237 selected**.
6. **Runes whose Gematria VALUE is prime:** all 812, because all 29 Gematria values are prime.

None of these natural definitions produces 166.

## Consequence
The published label `166-rune prime-stream` must NOT currently be interpreted as any of the following without further evidence:

- prime positions in the rune-only stream;
- prime positions in the raw text;
- prime Gematria indices;
- prime Gematria values.

The number **166 remains an observed/reported extraction, not a reproduced selector rule**.

## Important source inconsistency
The current community tracker reports a 166-rune P20 stream and an Old English result after a 2×83 rearrangement, while the P20 solver code itself explicitly tests several different interpretations and notes that all Gematria values are prime. This means the phrase `prime-position stream` is currently an operational label, not a sufficiently specified mathematical rule.

## Next experiment
Recover the exact historical extraction procedure that produced the 166 elements. Candidate sources to audit:

- an external position stream rather than local P20 positions;
- punctuation-aware indexing with a non-obvious origin/offset;
- a pre-filtered stream;
- a page/image coordinate order rather than transcription order;
- a manually selected prime-derived mask;
- interaction with P19's `REARRANGING THE PRIMES` instruction.

Do not attempt further 2×83/Deor decryption until the 166-element selector itself is reproducible.

## Status classification
- **PROVED:** P20 has 812 runes in the current transcription.
- **PROVED:** all 29 Gematria values are prime.
- **PROVED:** simple prime-position and prime-index definitions do not yield 166.
- **REPORTED:** a 166-rune extraction exists in the community tracker.
- **UNKNOWN:** exact selector producing 166.
- **REJECTED:** simple prime-position selector; simple prime-Gematria-index selector; literal prime-vs-nonprime Gematria-value split.
