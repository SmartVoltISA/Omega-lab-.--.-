# Ω-Lab Core — Graph, Relation, Node and External Memory Protocol

**Status:** CORE / ACTIVE
**Version:** Ω-Core 1.0
**Established:** 2026-08-10

## 1. Purpose

This document defines the operating protocol by which Ω-Lab is maintained as a growing structure of **directions, relations, and nodes** rather than as a chronological archive of conversations.

The repository is an external memory and structural map for the Ω-Lab research process.

The goal is not to predefine the final graph. The graph must be allowed to emerge from repeatedly recorded relations between research directions.

---

## 2. Fundamental rule

> **Do not build the final structure in advance. Record meaningful directions and their verified or proposed relations; allow stable intersections to become nodes.**

The repository therefore represents an evolving graph:

```text
Direction → Relation → Direction
                         ↓
                      Relation
                         ↓
                      Direction
                         ↓
                 stable intersection
                         ↓
                       NODE
```

A node is not merely a topic label. A node is a region of the research graph where multiple independent directions acquire persistent, meaningful connections.

---

## 3. Core entities

### 3.1 Direction

A **direction** is a meaningful research vector: a question, hypothesis line, mechanism, phenomenon, method, or experimental branch that can develop further.

Examples:

- memory;
- time;
- symmetry;
- asymmetry;
- comparison;
- trace;
- emergence;
- internal dynamics.

A direction does not have to be correct.

It only has to be sufficiently meaningful to deserve continued investigation.

### 3.2 Relation

A **relation** records a meaningful connection between two or more directions.

Examples:

```text
memory ↔ time
symmetry ↔ frozen trace
asymmetry ↔ directional distinction
trace → memory
memory → temporal order
```

A relation may be:

- proposed;
- observed;
- experimentally supported;
- contradicted;
- rejected;
- unresolved.

The status must be explicit.

### 3.3 Node

A **node** emerges when several directions and relations repeatedly intersect and form a stable research structure.

A node should not be declared merely because a topic sounds important.

Prefer evidence such as:

- multiple independent relations converge on it;
- it connects previously separate branches;
- it survives experiments or critical review;
- it repeatedly appears across experiments;
- it becomes useful as a reusable abstraction.

Node formation is therefore a conclusion of the graph, not an assumption imposed before the graph exists.

---

## 4. Repository as external memory

The repository serves as the persistent external memory of Ω-Lab.

Chat conversations are transient working space.

GitHub is the durable project state.

Important research state should therefore be transferred into the repository when it becomes structurally meaningful.

However, the repository must not become a dump of every conversation.

The criterion is **structural relevance**, not volume.

---

## 5. No forced chronology

The graph must not be organized primarily as:

```text
conversation 1 → conversation 2 → conversation 3
```

Chronology may be retained as metadata where useful, but chronology is not the primary structure.

The primary structure is:

```text
direction → relation → direction → intersection → node
```

This allows the project to be revisited by structure rather than by remembering which conversation contained an idea.

---

## 6. Recording a new direction

When a new meaningful research direction appears:

1. identify it;
2. give it a stable identifier;
3. describe the question or hypothesis without overstating certainty;
4. connect it to existing directions only where a meaningful relation exists;
5. do not invent connections merely to make the graph look complete.

Suggested identifier style:

```text
D-xxx
H-xxx
EXP-xxx
NODE-xxx
```

The exact naming may evolve, but identifiers should remain stable once published.

---

## 7. Recording a relation

For every significant relation, record:

```text
Source
Target
Relation type / description
Status
Evidence
Counter-evidence
Next test
```

Example:

```text
Source: memory
Target: temporal order
Relation: an updated trace may make prior states distinguishable
Status: OPEN
Evidence: Ω-0 M2
Counter-evidence: not yet tested independently
Next test: Ω-TM
```

Do not silently convert an interpretation into a fact.

---

## 8. Node formation protocol

A node may be promoted from a cluster of directions when at least one of the following is true:

- three or more meaningful relations converge;
- independent experiments point toward the same structure;
- a relation repeatedly survives attempts to falsify it;
- the cluster provides a useful reusable abstraction;
- previously separate branches become structurally connected.

Promotion remains provisional unless supported by evidence.

Use statuses such as:

```text
CANDIDATE NODE
PROVISIONAL NODE
SUPPORTED NODE
REJECTED NODE
```

A node can be split, merged, renamed, or rejected as the graph develops.

---

## 9. Evidence discipline

Ω-Lab must maintain a strict distinction between:

### Data
What was actually supplied or measured.

### Observation
What the procedure directly produced.

### Relation
A connection inferred between observations or directions.

### Interpretation
A proposed meaning of that relation.

### Hypothesis
A statement requiring further testing.

### Confirmed result
A result that survived defined controls and has sufficient reproducibility for the stated claim.

The strength of a node must never be inferred merely from how often it is discussed.

---

## 10. Experimental discipline

Every important experimental relation should, where practical, preserve:

- model version;
- code;
- parameters;
- initial conditions;
- random seeds;
- raw results;
- analysis procedure;
- controls;
- null models;
- negative results;
- known artifacts;
- interpretation status.

A failed experiment is part of the graph.

A rejected relation is part of the graph.

An artifact that destroys an apparent effect is particularly valuable because it prevents the graph from stabilizing around a false node.

---

## 11. Do not protect nodes

No node, hypothesis, or relation is protected because it is central to the project's philosophy.

If evidence contradicts it:

1. record the contradiction;
2. identify the affected relations;
3. downgrade or reject the node if appropriate;
4. preserve the history of why it changed.

Ω-Lab must optimize for explanatory and experimental value, not for preserving its original narrative.

---

## 12. Use of the graph during reasoning

When working on a new problem, the assistant should conceptually perform:

```text
new observation
      ↓
identify relevant direction(s)
      ↓
search existing graph
      ↓
find related directions / nodes
      ↓
compare evidence
      ↓
identify contradictions and gaps
      ↓
propose next relation or experiment
      ↓
record if structurally meaningful
```

The assistant should not assume that the newest conversation contains the full state of the project.

The repository should be consulted when the task depends on prior Ω-Lab structure, experiments, hypotheses, or decisions.

---

## 13. Avoiding graph pollution

Do not create a permanent node for:

- a passing thought;
- an untestable metaphor;
- a duplicate of an existing direction;
- a claim with no meaningful connection to the project;
- a result that exists only because of a known coding artifact.

Temporary ideas may remain in experiment notes without becoming structural nodes.

The graph should grow **sparsely and meaningfully**.

---

## 14. Relations can change

A relation is not permanent merely because it was recorded.

Its status may evolve:

```text
PROPOSED
   ↓
TESTED
   ↓
SUPPORTED / INCONCLUSIVE / CONTRADICTED
   ↓
RETESTED
   ↓
STABLE / REJECTED
```

The graph therefore represents not only connectivity but also the current epistemic status of that connectivity.

---

## 15. Cycles are important

When the graph develops a closed structure such as:

```text
A → B → C → A
```

record it explicitly.

Cycles may indicate:

- feedback;
- self-maintenance;
- mutual constraint;
- recurrent explanation;
- possible emergent node formation.

Do not assume every cycle is meaningful. Test whether it corresponds to an actual dependency or merely to the way the documents were written.

---

## 16. Memory principle of Ω-Lab

The repository is not only an archive of conclusions.

It is a memory of:

- what was considered;
- what was connected;
- what was tested;
- what survived;
- what failed;
- what remains open.

The memory must preserve **differences**, not merely final states.

This principle is especially important for Ω-TM research.

---

## 17. Relation to current Ω-TM research

Current directions include:

```text
memory
   ↕
time
   ↕
symmetry
   ↕
asymmetry
   ↕
trace
   ↕
comparison
```

These are currently directions and hypotheses, not a completed theoretical node.

The project must allow future experiments to determine whether some of these directions converge into a stable node.

In particular:

> **Symmetry as a frozen memory imprint and asymmetry as recoverable temporal direction is currently an OPEN hypothesis (H-TM-01), not a confirmed result.**

---

## 18. Core operational rule

When deciding what to add to Ω-Lab, use this question:

> **Does this create, strengthen, weaken, test, or clarify a meaningful relation in the project's emerging structure?**

If yes, record it at the appropriate level.

If no, do not force it into the graph.

---

## 19. Final principle

> **Ω-Lab is not a collection of answers. It is a growing structure of directions, relations, and emergent nodes whose state is preserved externally so that the research can return to, compare, challenge, and reorganize itself over time.**

The structure must emerge from the relations.

The memory must preserve the structure.

The structure must remain falsifiable.

---

**This document is a core operating protocol. Changes to it should be deliberate and explicitly versioned.**
