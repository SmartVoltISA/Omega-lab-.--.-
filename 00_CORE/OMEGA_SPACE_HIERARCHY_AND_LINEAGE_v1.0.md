# Ω-Space — Hierarchy & Lineage v1.0

## Purpose

The first complete SPACE is the **root/foundation organism**. Future SPACE instances are not copies without history: they are registered as models/instances with explicit identity, purpose, parent, derivation reason and version.

The hierarchy answers:

- who came from whom;
- why a SPACE was created;
- what purpose it serves;
- which model it belongs to;
- which SPACE are ancestors, descendants, siblings or peers;
- what structural information can be shared without exposing private memory.

## Hierarchy

```text
Ω-SPACE ROOT
│
├── SPACE-A  (specialist model)
│   ├── SPACE-A1
│   └── SPACE-A2
│
├── SPACE-B  (specialist model)
│
└── SPACE-C  (independent/peer model)
```

The root is the reference organism. Children may specialize, experiment, operate in a different habitat, or become independent branches.

## Model vs instance

A **model** is the reusable design/behavioral family.

A **SPACE instance** is a living execution of that model with its own state, memory, graph, Guardian and habitat.

Therefore:

```text
MODEL
  ↓ instantiates
SPACE INSTANCE
  ↓ lives in
HABITAT
```

Two instances of the same model are peers unless an explicit lineage relationship exists.

## Lineage is not ownership

`parent_space_id` records origin/derivation, not unrestricted control.

A child SPACE does not automatically inherit the parent's private memory, credentials, resources or permissions.

Origin is visible as structural metadata; private state remains local unless explicitly shared through Guardian-authorized protocols.

## What a SPACE can know about another SPACE

Default visibility is **METADATA**:

- identity;
- model identity;
- version;
- role;
- purpose;
- parent/ancestor relation;
- creation reason;
- declared capabilities/skills where public;
- health/status where explicitly exposed.

Private memory, secrets, internal state and restricted tools require explicit authorization.

## Relationship semantics

The hierarchy distinguishes:

- `PARENT_OF`;
- `CHILD_OF`;
- `ANCESTOR_OF`;
- `DESCENDANT_OF`;
- `SIBLING_OR_PEER`.

A future relation layer may additionally record:

- `SPECIALIZED_FROM`;
- `EXPERIMENTAL_FORK_OF`;
- `MERGED_FROM`;
- `COLLABORATES_WITH`;
- `REPLACED_BY`;
- `DEPLOYED_FOR`.

These are relations, not assumptions.

## Why / purpose / history

Every derived SPACE should retain:

```text
parent
+ model
+ purpose
+ reason for creation
+ derived_from
+ version
+ creation event
```

This lets the organism answer not only **what another SPACE is**, but **why it exists and how it came to exist**.

## Memory rule

Lineage metadata becomes part of the historical record. A model can be deprecated or replaced without erasing the lineage of the organisms derived from it.

## Guardian rule

Hierarchy does not bypass Guardian.

A parent cannot silently control a child merely because it is a parent. A child cannot silently access a parent's private memory merely because it was derived from it. Cross-SPACE interaction follows the normal bidirectional Guardian boundary and SPACE-to-SPACE transport.

## Root principle

> **The first SPACE is the reference organism, not the ruler of all later SPACE.**

It provides the initial architecture, standards and lineage root. Future SPACE may specialize and evolve while remaining traceably connected to their origin.

## Organism-level view

```text
ROOT SPACE
   │
   ├── shared architecture
   ├── lineage knowledge
   ├── public model metadata
   │
   └── independent instances
          │
          ├── own memory
          ├── own state
          ├── own graph
          ├── own Guardian
          └── own habitat
```

This makes SPACE an ecosystem rather than one monolithic process.
