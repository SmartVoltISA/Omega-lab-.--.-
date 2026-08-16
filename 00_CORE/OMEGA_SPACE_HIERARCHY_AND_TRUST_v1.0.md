# Ω-Space — Hierarchy, Lineage and Trust v1.0

## Core distinction

> **PROVENANCE ≠ TRUST.**

A SPACE must be able to know who/what produced it, why it exists, what purpose it serves, and where it sits in the family of SPACE organisms. None of this grants automatic trust or authority.

## Hierarchy

The first SPACE is the **ROOT SPACE** and serves as the reference organism for the family. Later SPACE organisms may be specialized, derived, experimental or application-specific.

```text
ROOT SPACE
├── SPECIALIZED SPACE
│   ├── VISION SPACE
│   └── AUDIO SPACE
├── MARKET SPACE
└── EXPERIMENTAL SPACE
```

Every SPACE retains lineage metadata:

- identity;
- model identity/version;
- parent SPACE/model;
- derived-from relation;
- purpose;
- creation reason;
- role;
- version;
- visibility.

## Model versus organism

A model is not an organism.

One model may instantiate multiple independent SPACE organisms:

```text
MODEL-A → SPACE-001
        → SPACE-002
        → SPACE-003
```

Each SPACE has its own state, memory, graph, Guardian and Habitat.

A specialized model may itself produce another family of SPACE organisms.

## What a SPACE may know about another SPACE

By default, SPACE may know structural metadata:

- who the other SPACE is;
- what model it uses;
- where it came from;
- why it was created;
- what role it has;
- its version;
- its public/authorized capabilities;
- permitted relationship metadata.

Private memory, secrets, internal state and unrestricted tools are not exposed merely because of lineage.

## Dynamic trust

Trust is a separate, changing state derived from evidence and behaviour.

```text
IDENTITY
  ↓
PROVENANCE
  ↓
HISTORY
  ↓
EVIDENCE
  ↓
TRUST
  ↓
CAPABILITY SCOPE
  ↓
GUARDIAN DECISION
```

Trust may rise or fall. Every change is itself historical information.

```text
0.30 → evidence → 0.55 → successful interactions → 0.78
                                  ↓
                              violation
                                  ↓
                                0.21
```

The previous trust values are never silently erased.

## Guardian relationship

Guardian uses trust as one input to authorization. Trust is not itself permission.

```text
request + identity + capability + evidence + trust + freshness
                         ↓
                      GUARDIAN
                  ↙      ↓      ↘
               ALLOW   RESTRICT   BLOCK
```

A trusted SPACE can still be denied an operation outside its capability scope. A newly created SPACE can interact under narrow permissions before it has accumulated trust.

## Evolution and family memory

The family retains lineage even when models evolve.

A child may differ substantially from its parent while preserving:

```text
who → from whom → why → purpose → what changed → what resulted
```

This allows later SPACE organisms to understand family history without inheriting private memories by default.

## Fundamental protection

Lineage, identity, trust history, capability history and Guardian decisions are foundational information. They therefore require the same integrity, provenance and recovery protection as core memory and graph structure.
