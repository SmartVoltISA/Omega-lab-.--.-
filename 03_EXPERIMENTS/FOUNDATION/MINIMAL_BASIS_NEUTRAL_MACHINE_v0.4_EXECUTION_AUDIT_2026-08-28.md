# MINIMAL BASIS NEUTRAL MACHINE v0.4 — EXECUTION AUDIT

Date: 2026-08-28
Status: EXECUTED / bounded evidence / NOT CANONICAL

## Scope

The neutral machine was independently reconstructed from the repository source and executed locally after correcting the known issue that `dst` was declared but not applied to control state. The corrected transition is:

`(control_state, read_symbol) -> (new_control_state, write_symbol, move)`.

The search space contains 48 possible single rules and C(48,2)=1128 two-rule programs, for a total of 1176 programs.

Each program was executed from the fixed initial tape `(0,1,0,1)` for at most 12 transitions.

## Raw counts

- programs examined: 1176
- traces deterministic under identical input: YES
- replay fingerprint stable: YES
- traces showing tape difference: 276
- traces showing repeated full state `(tape, pc, control)`: 87
- traces terminating before the 12-transition bound: 1087
- traces visiting multiple positions: 364
- traces changing control state: 267

## Symmetry control

A binary alpha-renaming / complement transformation was applied simultaneously to tape symbols, read/write symbols and control-state labels. With the corrected initialization of the renamed control state, all 1176 programs passed the symmetry replay test.

Status: PASS.

## Important limitation

These observations demonstrate properties of the neutral machine's transition dynamics. They do NOT establish that D, R, W or P are fundamental primitives, because no primitive-to-machine encoding has yet been validated.

They also do not establish semantic capabilities such as choice, memory or will. Such labels must be supplied by a separate observer and tested against null/permutation controls.

## Earlier implementation correction

The earlier v0.4 source declared `dst` but did not use it in `step()`. This was a real implementation defect. The corrected local execution uses `dst` as the next control state. Therefore any prior result obtained from the defective implementation must be treated as superseded.

## Decision

EXECUTION VALID for the bounded neutral-machine test.

FUNDAMENTALITY CLAIM: UNKNOWN.

NEXT: implement a validated primitive-to-machine encoding and independent observer, then run the full D/R/W/P budget comparison with null, permutation, alpha-renaming and replay controls.
