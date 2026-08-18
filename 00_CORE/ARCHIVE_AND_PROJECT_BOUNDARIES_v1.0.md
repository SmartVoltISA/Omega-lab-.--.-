# Ω-Lab — ARCHIVE AND PROJECT BOUNDARIES v1.1

**Status:** CORE / ACTIVE  
**Date:** 2026-08-18

## Purpose

Preserve the complete historical path of work while keeping project scopes separated. No work is disposable merely because the active project changes.

## Project identities

- **PROJECT OMEGA** — umbrella research/foundation project: universal principles, shared protocols, cross-project architecture and general experiments.
- **SPACE** — operational organism/system project.
- **MARKET** — market-analysis/application project.

These identities remain distinct. A shared foundation does not merge the projects.

## Fundamental propagation rule

A mechanism that is proven to be **fundamental and universal** is not treated as belonging to only one project.

It becomes a common foundation and must be available across every project and every applicable organ:

```text
             OMEGA FOUNDATION
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
      SPACE       MARKET      OTHER
        │           │           │
      organs      organs      organs
```

Example: **MEMORY** is not merely a SPACE organ. If MEMORY is established as a fundamental Ω-Lab mechanism, its contract, principles and history belong to OMEGA and its operational implementation must be available to SPACE, MARKET and all other applicable organs.

The same rule applies to other mechanisms once they are demonstrated to be fundamental rather than merely useful in one project.

## Classification

Every significant artifact receives one of three scopes:

### 1. PROJECT-SPECIFIC

```text
SPACE-only  → SPACE
MARKET-only → MARKET
OMEGA-only  → OMEGA
```

It stays with its owning project.

### 2. SHARED / REUSABLE

A mechanism used by multiple projects but not yet established as fundamental:

```text
OMEGA shared definition
        ↓
project-specific implementations
```

### 3. FUNDAMENTAL / UNIVERSAL

A mechanism that is an architectural foundation for the organism as a whole:

```text
OMEGA canonical foundation
        ↓
SPACE
MARKET
ALL APPLICABLE ORGANS
```

The canonical definition is maintained in OMEGA; each project retains its own implementation state, tests, adapters and history. The same mechanism may therefore be recorded in OMEGA + SPACE + MARKET without duplication of meaning or loss of provenance.

## No silent relocation

Do not move a file merely because its idea originated elsewhere. If scope expands, create explicit references, synchronized contracts or project-specific adaptations while preserving the original record.

## History / archive

History is append-only in meaning:

```text
WORK → RESULT → VERIFICATION → DECISION → NEXT STATE
```

Changing active project does not erase the previous location, context, experiment, failure, rejected version, frozen state or branch.

A reconstruction must be labelled as reconstruction; it must never silently replace the historical record.

## Archive minimum

For every significant work cycle preserve:

- project scope;
- fundamental/shared/project-specific classification;
- work item / experiment ID;
- objective;
- source state;
- actions;
- files changed;
- commits / SHA;
- tests and CI status;
- result;
- limitations / failures;
- decision;
- next step;
- cross-project links;
- provenance.

## Environment is part of the organism

A software organ is not complete merely because its source exists. If the organ requires a server/runtime environment, the environment is part of the implementation boundary and must also be specified, versioned and verified.

```text
CODE
 ↓
RUNTIME / SERVER ENVIRONMENT
 ↓
EXECUTION
 ↓
RESULT
```

The environment itself must have provenance: OS/runtime versions, dependencies, configuration, services, storage, network assumptions, secrets boundary and verification procedure. Secrets must never be committed as plaintext.

Because the execution environment can serve multiple projects, its **general infrastructure contract** belongs to OMEGA, while project-specific deployment/configuration remains in SPACE, MARKET or the applicable project.

## Non-negotiable rule

> **Не смешивать проекты. Не терять историю. Фундаментальное — распространять. Специфическое — оставлять у владельца. Среду работы считать частью системы.**

The archive is structural memory, not a graveyard.
