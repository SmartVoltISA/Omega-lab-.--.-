# SPACE Measurement Quarantine — v1.0

## Purpose

A dedicated quarantine zone for measurements, probes, stress tests, experiments and diagnostic inputs that must not silently become part of the trusted organism state.

## Principle

**Measure first. Trust later.**

Anything entering quarantine is treated as untrusted experimental data until validation completes.

## Boundary

```text
EXTERNAL / EXPERIMENTAL INPUT
        ↓
   QUARANTINE
        ↓
 validation / normalization
        ↓
 Guardian review
        ↓
 trusted state / memory
```

The quarantine boundary applies to:

- measurements;
- sensor samples;
- downloaded media;
- test payloads;
- stress-test inputs;
- tool outputs under evaluation;
- unknown or malformed data;
- experimental observations.

## Required metadata

Every quarantined measurement should carry:

- measurement_id;
- source;
- timestamp;
- tool/capability used;
- input hash when applicable;
- units and dimensions;
- raw value;
- normalized value, if any;
- validation status;
- Guardian decision;
- related node/edge/graph identifiers;
- experiment/test identifier;
- final disposition.

## Dispositions

- `ACCEPTED` — validated and eligible for trusted state.
- `REJECTED` — invalid, unsafe, malformed or inconsistent.
- `ISOLATED` — retained for analysis but excluded from trusted state.
- `PENDING` — requires further validation.
- `EXPIRED` — no longer valid for the active context.

## Memory rule

Quarantine does **not** delete history. Rejected or isolated measurements remain available as historical evidence with provenance.

## Guardian rule

Quarantine is a boundary, not a permission system. Guardian decides whether data may cross from experimental/untrusted state into trusted system state.

## Graph rule

A quarantined observation may be represented as a graph node/edge, but its trust state must remain explicit. Experimental relations must not be silently promoted to trusted relations.

## Stress-test rule

Stress tests operate on quarantined inputs by default. A stress test must not mutate production/trusted state unless an explicit controlled transition is recorded.

## Goal

Provide SPACE with an analogue of a biological quarantine/measurement chamber: isolate, observe, measure, validate, record, then either admit or reject — without losing the history of what was observed.

## Status

Architecture defined. Runtime enforcement and automated CI coverage are next implementation targets.
