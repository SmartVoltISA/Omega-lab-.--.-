# Ω-MEM-8 — Pilot Results

**Status:** PRELIMINARY POSITIVE / PILOT ONLY
**Date:** 2026-08-14

## Design

Two histories converge on the same observable state `S`:

- `A → S → B → S`
- `X → S → Y → S`

At `S`, the path-derived memory is the immediately preceding node (`A` or `X`). The memory therefore records the preceding path state and does **not** contain a direct label for the next transition (`B` or `Y`).

A capacity-matched irrelevant memory is obtained by independently permuting the same memory values.

30 seeds, 5,000 blocks per seed.

## Results

Across 30 seeds:

| Metric | Path-trace memory | Irrelevant memory |
|---|---:|---:|
| `H(next | current)` | 1.9999 bits | 1.9999 bits |
| `H(next | current, memory)` | 0.4998 bits | 1.9991 bits |
| `I(next; memory | current)` | **1.5001 bits** | **0.0008 bits** |

The pilot therefore shows a strong difference between path-derived and permuted memory at matched nominal capacity.

## Interpretation limit

This is not yet a general result. The pilot uses a deliberately simple deterministic construction in which the preceding path branch determines the next branch. The purpose is to verify the architecture and the absence of direct next-label storage before moving to richer dynamics.

No causal intervention result is claimed from this pilot.
