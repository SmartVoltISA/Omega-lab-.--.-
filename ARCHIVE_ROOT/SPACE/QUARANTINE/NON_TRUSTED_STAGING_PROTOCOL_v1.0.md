# Non-Trusted Staging Protocol v1.0

## Purpose

Experimental measurements and CI/test results must remain available for inspection without being promoted into trusted organism memory.

## Flow

`external/test -> quarantine staging -> inspect -> Guardian decision -> optional promotion -> trusted memory`

Staging is not trusted memory. Reading staged data does not grant it authority. Promotion is a separate operation and must be explicitly authorized.

## Guarantees

- staged measurements carry source and deterministic payload hash;
- staged records are inspectable later;
- staging code has no trusted-memory write interface;
- rejected/unknown data remains available for forensic analysis;
- promotion is deliberately outside this component.

## Rule

**Do not block inspection merely because data is not trusted. Block authority, not visibility.**
