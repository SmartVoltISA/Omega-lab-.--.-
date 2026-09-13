# Ω-LINK-1 — RESULT-004

**Status:** OBSERVED RESULT / not a universal law
**Run:** 31779369021
**Commit:** d07624b939071c86579610acec11a62dd39601b3

## Observation

Adding one edge produced a local gain of exactly one immediate transition in every tested case, but global reachability gain depended on the existing topology.

- `NEW`: local gain = 1, global gain = 1
- `REDUNDANT`: local gain = 1, global gain = 0
- `ALTERNATIVE`: local gain = 1, global gain = 0
- `PARTIAL`: local gain = 1, global gain = 0

## Combined structural observation

Together with RESULT-003, the experiments show a symmetric distinction between local relation change and global possibility change:

- Removing one edge always removes its immediate local transition, but global reachability may remain unchanged through alternative paths.
- Adding one edge always introduces a local transition, but global reachability may remain unchanged when the destination was already globally reachable.

## Interpretation

A single relation is therefore not equivalent to a unique global possibility. Global possibility is a property of the surrounding relational structure, including alternative paths.

## Interpretation boundary

These are observations from small deterministic graph constructions. They do not yet establish a universal ontology of relations.

## Next question

Test whether the same local/global distinction persists when relation direction, path length, cycles, and graph size are varied independently.
