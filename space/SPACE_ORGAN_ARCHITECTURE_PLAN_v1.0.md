# Ω-Space — Autonomous Organ Architecture Plan v1.0

**Date:** 2026-08-16  
**Status:** IN PROGRESS

## Goal

Turn every SPACE organ into a self-contained module that can operate independently while communicating with other organs only through explicit contracts and Guardian-controlled boundaries.

## Completed foundations

- Organ directory already exists with sensory, nervous, motor, circulatory, digestive, immune and habitat components.
- Guardian is the execution/security boundary.
- Capability and tool registries already exist.
- Cycle/graph/memory separation has been established: the cycle cannot be materialized into the operational graph.
- Protected foundation remains outside the operational graph.
- Compression experiment is closed with a green canonical TAR.GZ lossless path.

## Work plan

### Phase 1 — Organ contract
- Define a minimal autonomous-organ interface.
- Give each organ its own identity, local state, local memory reference and lifecycle.
- Require explicit inbound/outbound message contracts.
- No direct cross-organ object access.

### Phase 2 — Boundary enforcement
- Guardian authorizes inter-organ requests.
- Capability is scoped to an operation and target organ.
- An organ cannot silently grant another organ new capabilities.
- Default cross-organ access is deny.

### Phase 3 — Failure isolation
- Organ failure must not terminate unrelated organs.
- Guardian can quarantine one organ without destroying its local state.
- Recovery preserves provenance.

### Phase 4 — Communication
- Add a bounded organ message envelope.
- Support request/response and event notification.
- Keep local memory local unless an explicit contract permits a shared result.

### Phase 5 — Integration tests
- Independent operation of every organ.
- Authorized communication.
- Unauthorized communication rejection.
- Capability non-escalation.
- Failure and quarantine isolation.
- No cycle→graph materialization through organ communication.

### Phase 6 — Stress and audit
- Repeated inter-organ requests.
- Message storms.
- Organ failure during communication.
- Recovery after quarantine.
- Audit completeness and deterministic replay.

## Architectural invariant

> **Самостоятельность внутри. Контракт снаружи. Контроль на границе.**

An organ may be powerful within its own domain. Cooperation is possible, but cooperation does not imply fusion of internal state, memory, graph, cycle or authority domains.

## Next checkpoint

Complete Phase 1 with a concrete organ contract and its tests before expanding external tools or network capabilities.
