# Ω-Space — Autonomous Organ Contract v1.0

**Status:** Phase 1 — contract defined

## Invariant

> **Самостоятельность внутри. Контракт снаружи. Контроль на границе.**

Each organ owns its local state and local memory. Cross-organ communication is explicit and target-bound. Message existence is not permission to execute; authorization remains a separate Guardian responsibility.

## Required properties

- unique `organ_id`;
- independent lifecycle;
- local state;
- local memory boundary;
- explicit operation allow-list;
- typed message envelope with source, target and operation;
- rejection of target mismatch and unknown operations;
- no implicit shared memory;
- no direct peer object access.

## Non-goals

This contract does not create a graph of all organs, merge their memories, or grant network/self-deployment capabilities. Those concerns remain outside the organ contract and require explicit higher-level policy.
