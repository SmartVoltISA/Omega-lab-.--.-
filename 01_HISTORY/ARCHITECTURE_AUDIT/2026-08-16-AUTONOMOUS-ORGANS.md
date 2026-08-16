# Ω-Lab — Autonomous Organ Architecture

**Date:** 2026-08-16  
**Status:** Phase 1 implemented; CI verification pending

## Decision

SPACE organs are to become independent, self-sufficient modules. Each organ owns its local state and local memory. Cooperation occurs only through explicit message contracts and boundary authorization.

## Completed before this work

- Existing organ layer identified under `space/organs/`.
- Guardian remains the execution/security boundary.
- Capability and tool registries are already present.
- Cycle/graph/memory separation is enforced.
- Protected foundation is outside the operational graph.
- Compression clone experiment has a green canonical TAR.GZ lossless path.

## Implemented now

- Added `space/organs/autonomous_organ.py`.
- Added explicit `OrganMessage` envelope.
- Added local operation registration and local execution.
- Added local state and local memory ownership.
- Added lifecycle stop/start.
- Added snapshots for audit/recovery.
- Added tests for independence, contract rejection, message boundaries, failure isolation and non-shared memory.
- Added `space/SPACE_ORGAN_ARCHITECTURE_PLAN_v1.0.md` with the remaining phases.

## Non-goals

This phase does not connect organs to networks, external devices, arbitrary execution, shared global memory, or automatic capability transfer.

## Invariant

> **Самостоятельность внутри. Контракт снаружи. Контроль на границе.**

An inter-organ message is only a request envelope. It is not permission and does not execute another organ by itself.

## Next

Run the complete SPACE test suite. Then implement Guardian-mediated inter-organ communication, followed by failure isolation, stress tests and audit/replay checks.
