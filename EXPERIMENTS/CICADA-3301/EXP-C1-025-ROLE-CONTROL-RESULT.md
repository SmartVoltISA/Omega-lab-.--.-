# EXP-C1-025 — Role-Control Result

**Date:** 2026-08-28  
**Branch:** `research/cicada-3301`  
**Status:** CONTROLLED COMPARISON / PARTIAL CORPUS

## Objective
Apply the C1-024 role taxonomy to 3301, 1033 and the preselected controls 761, 313, 353, 757, 1039.

## Evidence basis
Primary/near-primary archived material was checked for operational use, not raw occurrence.

### 3301
Observed operational roles:
- STREAM_STOP / STATE_MARKER: prime stream terminates at 3301; `prime_echo` treats it as a special point.
- COMMAND_SELECTOR: 2013 onion exposes `get 3301`.
- PHYSICAL_ENDPOINT: 2013 physical-stage numbers include 3301 suffix.
- STRUCTURAL_INVARIANT: 2014 magic-square constant 3301.
- AUTH_MARKER: authentic PGP messages are signed/signed off with 3301 identity marker.
- EXTRACTION_KEY: part of documented `33011033` OpenPuff password reconstruction.

Provisional role diversity R(3301)=6.

### 1033
Observed operational roles:
- STREAM_STOP / STATE_MARKER: 2013 prime stream has a special pause at 1033.
- COMMAND_SELECTOR: 2013 onion exposes `get 1033`.
- PHYSICAL_ENDPOINT: physical-stage numbers include 1033 suffix.
- STRUCTURAL_INVARIANT: 2014 magic-square constant 1033; same 5x5 matrix later occurs in Liber Primus material.
- EXTRACTION_KEY: participates in documented `33011033` OpenPuff password reconstruction.

Provisional role diversity R(1033)=5.

### 761
Observed:
- COMMAND/DATA VALUE: `count the instar emergence` returns 761+ in 2013.
- IDENTIFIER/DATA: 761 appears in 2013 artifact/cookie material.

No demonstrated multi-stage routing/extraction/structural role found in the checked corpus.

Provisional R(761)=1 strong operational class; stage diversity S(761)=1–2 depending whether cookie is counted as a distinct stage. Cookie evidence is not treated as a routing operation.

### 313, 353, 757
These occur prominently in the 2013 missing-primes list, but the checked source does not demonstrate that each value independently performs a command selection, endpoint selection, extraction, or structural operation. Therefore raw occurrence is not scored as an operational role.

Provisional R=0 under the strict C1-024 criterion.

### 1039
Observed as a Gematria sum for `THE TOTIENT FUNCTION IS SACRED` in Liber Primus decoded material. This is a derived textual value, not by itself an operational selector or extraction key. It is therefore not scored as a routing role.

Provisional R(1039)=0.

## Result
The controlled comparison does NOT reject the persistent-marker hypothesis. In the checked corpus, 3301 and 1033 have substantially greater operational-role diversity than the selected controls.

However, this is not a statistical proof because:
1. the corpus is not yet exhaustive;
2. 3301/1033 were selected because of prior evidence, while controls were selected from salient corpus values;
3. role classification remains partly dependent on provenance interpretation;
4. the decisive deterministic edge `marker -> selected object` has not yet been reproduced as one common function.

## Important correction
The strongest candidate is now the **pair (3301,1033)**, not 1033 alone. 3301 has the larger role profile in the checked material.

The evidence therefore supports:

`3301/1033 -> persistent operational markers`

more strongly than:

`1033 -> universal state variable`.

## Graph implication
A graph-compatible interpretation remains plausible:

`value -> operation -> next object`

But no claim is made that the creators intentionally used graph theory. The next decisive experiment must reconstruct at least two independent transitions where the same marker pair determines or validates the next object.

## Verdict
**CONTROL RESULT: SUPPORTIVE, NOT CONCLUSIVE.**

The hypothesis survives the first matched-control test. The next target is deterministic transition reconstruction, not further frequency counting.
