# Ω-Lab — RUNTIME ENVIRONMENT PLAN v1.0

**Status:** CORE / NEXT IMPLEMENTATION  
**Date:** 2026-08-18

## Why

The organism cannot be proven by source files alone. It needs a reproducible runtime environment in which organs can execute, communicate, persist state and be verified.

## Architecture

```text
                    Ω-LAB RUNTIME
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
      SPACE            MARKET          OTHER ORGANS
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                 SHARED SERVICES
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       storage        runtime        CI/test
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                    SERVER / HOST
```

## Minimum environment contract

1. Host/server identity and OS.
2. Runtime versions (Python/Node/etc.) actually required by organs.
3. Dependency lock files.
4. Environment configuration separated from secrets.
5. Persistent storage for MEMORY and provenance.
6. Network/service boundaries.
7. Process/service supervision.
8. Health checks.
9. Backup/recovery procedure.
10. Reproducible bootstrap procedure.
11. CI verification of the environment contract.
12. Project isolation: SPACE and MARKET must not silently share mutable state unless explicitly declared shared infrastructure.

## Separation

General infrastructure belongs to OMEGA as a common environment contract.

Project deployments remain scoped:

```text
OMEGA
  └── environment contract

SPACE
  └── SPACE runtime/config/data

MARKET
  └── MARKET runtime/config/data
```

Shared services may be physically shared while logical data/state remains isolated.

## Security boundary

No passwords, API keys, tokens or private credentials in Git. Use environment variables, secret stores or equivalent runtime injection.

## Verification target

The first environment proof is deliberately minimal:

```text
BOOTSTRAP
  ↓
HEALTH CHECK
  ↓
START ORGAN
  ↓
READ / WRITE TEST STATE
  ↓
VERIFY RESULT
  ↓
PERSIST PROVENANCE
```

Only after this passes should the environment be treated as an operational substrate for the organism.

## Next implementation

Create the smallest reproducible local/server environment, then attach SPACE first because SPACE is the active reconstruction target. MARKET receives the shared infrastructure contract without absorbing SPACE-specific state.
