# Ω-Space — Autonomous Organs Check

**Date:** 2026-08-16

## Work completed

- Reviewed existing organ architecture and current `space/organs` inventory.
- Verified the minimal `AutonomousOrgan` contract and its existing tests.
- Added a deterministic organ test runner for CI.
- Added isolation stress tests: 8 organs × 100 local operations and a 16-organ failure-isolation check.
- Confirmed inter-organ messages are envelopes only; they do not execute themselves.
- Confirmed local memory is independently allocated per organ.

## Current CI state

The repository contains a `space-organism` workflow that discovers `space/test_*.py` tests. A dedicated autonomous-organ runner was added so the new contract can also be exercised deterministically.

**Important:** no new green CI result for the latest commits is claimed here until GitHub Actions reports it. The architecture is implemented; acceptance remains pending CI evidence.

## Acceptance criteria

1. Every autonomous organ passes local contract tests.
2. Unknown operations are rejected.
3. One organ can stop without stopping unrelated organs.
4. Local memory is not implicitly shared.
5. Inter-organ messages do not execute without a dispatcher/authorization boundary.
6. Stress repetition does not merge organ state or memory.
7. Only after these pass do we implement Guardian-mediated communication.

## Architectural invariant

> **Самостоятельность внутри. Контракт снаружи. Контроль на границе.**

No organ is granted network, graph, memory-sharing, capability-escalation, or execution authority merely by being an autonomous organ.
