# EXP-C1-022 — Numeric Invariant / Cross-Layer Audit

**Date:** 2026-08-28
**Branch:** `research/cicada-3301`
**Status:** CORRECTED; strong recurrence of 1033, but node-label interpretation remains UNKNOWN

## Correction to previous version

The earlier version claimed an archived `X-Cicada: 1033` header. Primary/community material checked in the current audit instead shows a documented 2014 header `X-Cicada: 3301` on the fourth onion. Therefore the `X-Cicada: 1033` claim is REMOVED from the evidence set.

This correction is important: we do not promote a false edge merely because it supports the graph hypothesis.

## Provenance-controlled observations

1. The 2014 portrait exposes numeric columns whose sums are **1033** and **3301**.
2. The documented OpenPuff extraction password for `magicsquares.txt` is **33011033**.
3. The extracted artifact contains three magic squares with constants **3301, 1033, 1033**.
4. The 5×5/1033 matrix is reproduced in Liber Primus / P63-related material.
5. A separate documented 2012/2013 puzzle mechanism pauses a prime-number display at **1033 and 3301**, showing that both numbers were operationally highlighted before the 2014 magic-square stage.
6. The 2014 HTTP header evidence currently supports **`X-Cicada: 3301`**, not `1033`.
7. 2014 user-agent strings independently contain `CicaDOS 1.033` / `Cic/DOS/ 1.033`, but these are version-like identifiers and are not automatically equivalent to the 1033 magic constant.

## Structural graph after correction

`numeric source → 1033/3301 → ordered concatenation 33011033 → steganographic extraction → magic-square constraints → later Liber Primus representation`

Separately:

`prime display → explicit pauses at 1033 and 3301`

Separately:

`2014 HTTP stage → X-Cicada: 3301`

These are legitimate edges. We currently DO NOT connect `1033 → X-Cicada`.

## What is established

1033 is not an isolated number in the corpus. It appears as:

- a portrait-derived invariant;
- a magic-square constant;
- a repeated Liber Primus matrix invariant;
- an explicitly highlighted value in the earlier prime-number sequence;
- a version-like component in later `1.033` user-agent strings.

This is a strong recurrence across representation classes, but the occurrences may have different functions.

## What is NOT established

This experiment does not establish that:

- 1033 is a universal state variable;
- 1033 is a network node identifier;
- 1033 generates the P63 matrix;
- 1033 is cryptographic key material;
- 3301 and 1033 form a universal key pair;
- the authors consciously designed a graph architecture.

## New falsifiable prediction

If 1033 is a conserved operational state rather than a recurring thematic/structural constant, there should be another independently documented transition where changing or selecting 1033 changes the next object, route, key, or validation result.

A mere occurrence, version string, or numerical coincidence does not qualify.

## Controls

Use 3301 and other prominent constants as controls. Compare:

- frequency of appearance;
- operational use;
- role changes across stages;
- whether the value participates in a deterministic transition.

## Current verdict

**1033 recurrence: OBSERVED.**

**1033 as conserved state / bridge variable: PLAUSIBLE, NOT PROVED.**

**`X-Cicada: 1033`: REJECTED / REMOVED from evidence.**

The next experiment should prioritize operational uses of 1033 and 3301, especially places where either value selects, unlocks, indexes, validates, or routes to another object.