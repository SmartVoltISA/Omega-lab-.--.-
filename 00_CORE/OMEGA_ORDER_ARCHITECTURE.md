# Ω-Lab — ORDER Architecture

**Status:** CORE / ACTIVE / OPEN RESEARCH DIRECTION  
**Version:** Ω-Order 1.0  
**Established:** 2026-08-10

## 1. Purpose

This document introduces `ORDER` as a structural layer of Ω-Lab.

The purpose is not to declare that physical time is fundamental, nor to replace the existing relation-first graph protocol. The purpose is to represent the **order of changes and provenance of states** while preserving the possibility that multiple research branches emerge, split, reconnect, and form higher-level structures.

The central working idea is:

> **ORDER is the root of provenance: it records how a state, observation, hypothesis, experiment, or node came to exist and in what order changes occurred.**

`TIME` is treated as one possible representation or interpretation of order, not as an assumption built into the architecture.

---

## 2. Core distinction

Ω-Lab now separates two complementary structures:

### Provenance tree

Answers:

> **Where did this come from?**

```text
ORDER
  ↓
EVENT / CHANGE
  ↓
OBSERVATION
  ↓
INTERPRETATION
  ↓
HYPOTHESIS
  ↓
PROTOCOL
  ↓
EXPERIMENT
  ↓
RESULT
  ↓
NEXT QUESTION
```

This structure may branch whenever a result produces several different next questions.

### Research graph

Answers:

> **What is this connected to?**

```text
DIRECTION
   ↕
RELATION
   ↕
DIRECTION
   ↓
stable intersection
   ↓
NODE
```

The graph is allowed to cross branches of the provenance tree.

---

## 3. Combined architecture

The intended structure is therefore neither a simple tree nor a flat graph.

It is:

```text
                 ORDER / PROVENANCE
                        │
          ┌─────────────┼─────────────┐
          │             │             │
       branch A      branch B      branch C
          │             │             │
          └──────┐  ┌───┘             │
                 │  │                 │
              RELATIONS ──────────────┘
                 │
              INTERSECTION
                 │
                NODE
                 │
          new directions
                 │
          new experiments
                 │
              new branches
```

Thus:

> **The tree preserves origin. The graph preserves connection. Their intersections describe the growing research environment.**

---

## 4. Why ORDER instead of immediately using TIME?

The distinction is deliberate.

A sequence of computational updates can establish an order of states without establishing physical time.

For example:

```text
state A → update → state B → update → state C
```

demonstrates an ordering relation.

It does not by itself demonstrate:

```text
physical time = computational update count
```

Therefore Ω-Lab uses the more conservative abstraction `ORDER`.

Possible future branches may investigate whether particular forms of order correspond to:

- temporal order;
- causal order;
- irreversible order;
- computational time;
- memory order;
- observer-dependent ordering.

These are separate questions.

---

## 5. Relation to Ω-0

Ω-0 provides an important motivation for this architecture.

The existing experiments investigate whether an updating trace can preserve enough information to reconstruct internal order.

That result should be represented as evidence for an **internal-order relation**, not as proof that physical time has been derived.

Therefore the current relation is:

```text
EXP-Ω-0
   │
   └── supports → internal-order reconstruction
                       │
                       └── relates_to → ORDER
```

The relation between ORDER and physical TIME remains OPEN.

---

## 6. Branching

A branch is created when one state or result produces multiple structurally distinct continuations.

Example:

```text
RESULT R
 ├── interpretation A
 │     └── hypothesis H-A
 │            └── experiment E-A
 │
 └── interpretation B
       └── hypothesis H-B
              └── experiment E-B
```

Branches must not be collapsed merely because one becomes more successful.

Rejected branches remain part of the provenance history.

---

## 7. Reconnection

Different branches may later converge:

```text
branch A ───────┐
                ├── NODE-X
branch B ───────┘
```

A reconnection is meaningful when independent branches establish a persistent relation.

This follows the existing Ω-Lab node-formation rule: stable nodes should emerge from repeated meaningful intersections rather than being imposed in advance.

---

## 8. What the architecture makes visible

The combined structure should make it possible to inspect, at any point:

- what is known;
- what was observed;
- what is interpreted;
- what is hypothesized;
- what has been tested;
- what failed;
- what was corrected;
- what remains unresolved;
- which branches are active;
- which branches are dormant;
- where independent branches intersect;
- where the next useful experiment is located.

This is the intended operational value of the architecture.

---

## 9. Epistemic state is separate from provenance

An item has both:

1. **provenance** — where it came from;
2. **epistemic status** — how strongly it is currently supported.

For example:

```text
H-MEM-2.3
  provenance: Ω-MEM-4
  status: OPEN
  evidence: partial
  counterevidence: present
  next test: Ω-MEM-4R
```

A later result may change the status without deleting the provenance path.

---

## 10. No retroactive rewriting

When a hypothesis is refined or rejected:

```text
old hypothesis
      ↓
experiment
      ↓
contradiction
      ↓
refined hypothesis
```

The old state remains historically valid as a record of what was believed or tested at that point.

The current graph may mark it as `REFINED`, `REJECTED`, or another appropriate state, but the causal/provenance path must remain recoverable.

---

## 11. Proposed identifiers

For the ORDER layer, use:

```text
D-ORDER-01       direction
H-ORDER-01       hypothesis
E-ORDER-xxx      experiment
EVT-xxx          event/change
OBS-xxx          observation
NODE-xxx         emergent node
```

Existing Ω identifiers remain unchanged.

This is an extension, not a migration of historical identifiers.

---

## 12. Initial hypothesis

### H-ORDER-01 — Order as the provenance root

**Formulation:**

> A research system can be represented more completely by combining an ordered provenance structure of state changes with a relation graph whose edges may cross provenance branches; this combined structure exposes both origin and connectivity of the evolving system.

**Status:** OPEN

**Current evidence:**

- existing Ω-Lab graph protocol requires preserving relations and their changing epistemic states;
- Ω-0 investigates reconstruction of internal order from updating traces;
- current research already contains branching hypotheses and experiments that cross-connect conceptually distinct directions.

**Counterevidence / risks:**

- ORDER may duplicate ordinary chronology without adding explanatory value;
- branch structure may become an unnecessary metadata layer;
- apparent graph intersections may be artifacts of categorization rather than real structural relations.

**Required test:**

Apply the architecture retrospectively to a nontrivial Ω-Lab branch and determine whether it reveals missing provenance, contradictions, dependencies, or useful cross-branch relations that the existing graph representation does not expose clearly.

---

## 13. First validation target

The first validation should use the memory branch because it already contains:

```text
Ω-0
  ↓
Ω-MEM-1a–1d
  ↓
Ω-MEM-2
  ↓
Ω-MEM-3
  ↓
Ω-MEM-4
  ↓
Ω-MEM-4R
  ↓
Ω-MEM-5
```

The purpose is not to force this sequence into a simple timeline. The purpose is to show:

- where Ω-MEM-3 broke the previous formulation;
- where Ω-MEM-4 refined the hypothesis;
- why Ω-MEM-4R became necessary;
- how the same experiments connect to memory, structure, expressiveness, and order;
- where the next branch begins.

If the representation improves inspection and experiment selection, that is evidence for the usefulness of ORDER as an architectural layer.

---

## 14. Working principle

> **Do not use the tree to replace the graph. Do not use the graph to replace the tree.**
>
> **Use the tree to preserve origin and the graph to preserve relation.**

The growing Ω-Lab structure should therefore be understood as a **network of branching histories**.

---

## 15. Current status

This architecture is a proposed Ω-Lab core extension.

It is **not** a confirmed theory of time, causality, space, or physical reality.

It is an architectural hypothesis about how a growing research system can preserve its own structure while remaining falsifiable.

**Next action:** validate H-ORDER-01 against the existing DIR-1 / memory branch and record whether the combined tree + graph representation produces measurable practical benefit.
