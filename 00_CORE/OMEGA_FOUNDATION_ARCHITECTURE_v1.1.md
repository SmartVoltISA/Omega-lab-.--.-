# Ω-Lab — FOUNDATION ARCHITECTURE v1.1

**Status:** CORE / ACTIVE  
**Date:** 2026-08-16

## 1. Two foundations

The foundation consists of two inseparable mechanisms:

1. **MEMORY** — persistence of state, history, context, relations and differences.
2. **BIDIRECTIONAL TRANSFORMATION** — the system transforms different parts into a whole and the whole back into differentiated parts.

Core form:

```text
РАЗНОЕ → СВЯЗИ → ЦЕЛОЕ → ОБРАТНАЯ СВЯЗЬ → РАЗНОЕ
   ↑                                      ↓
   └────────────── ПАМЯТЬ ────────────────┘
```

## 2. Structural construction

The working structural sequence is:

```text
ОПОРА → УЗЕЛ → СВЯЗЬ → РЕБРО → ГРАФ → ЦЕЛОЕ
```

The reverse transformation is equally fundamental:

```text
ЦЕЛОЕ → FEEDBACK → ГРАФ/РЁБРА → СВЯЗИ → УЗЛЫ → ОБНОВЛЁННЫЕ СОСТОЯНИЯ
```

A complete organism requires both directions.

## 3. Parts → whole

Different elements become a coherent whole through meaningful relations and their organization:

```text
parts + relations → edges → graph → whole_state
```

The whole is not merely a list of parts. It is the current organized state of their relations.

## 4. Whole → parts

The current whole state must be capable of producing feedback that returns to the participating elements:

```text
whole_state → feedback → local constraints / updates → parts'
```

The updated parts then participate in the next assembly:

```text
parts' + relations → graph' → whole_state'
```

Thus:

```text
S₀ → W₀ → S₁ → W₁ → S₂ → W₂ → …
```

## 5. Memory is structural

Memory is not only an archive located outside the system.

A node without memory loses its history and context. A relation without memory loses the history of interaction. A graph without memory cannot preserve transitions between states.

Therefore memory is attached to the structural levels:

```text
NODE + MEMORY
RELATION + MEMORY
EDGE + MEMORY
GRAPH + MEMORY
WHOLE + MEMORY
```

Memory preserves, where applicable:

- prior state;
- change between states;
- provenance;
- relation history;
- context;
- outcomes;
- failed and rejected states;
- recoverability of previous structure.

## 6. Distributed memory

Memory is distributed across the system rather than being reduced to one undifferentiated store.

Local memory can be aggregated upward:

```text
local memories → relations → graph memory → whole memory
```

Whole-system state can return downward:

```text
whole memory/state → feedback → local memories/state
```

This gives memory continuity across scales.

A central durable repository may exist, but it does not replace structural/local memory.

## 7. Feedback is functional, not logging

A feedback path is functional only when information from the whole can influence a subsequent local state, relation, decision or action.

Required chain:

```text
RESULT → FEEDBACK → STATE UPDATE → NEXT ACTION/RELATION → NEW RESULT
```

A returned log that cannot affect the next cycle is not functional feedback.

## 8. Memory + feedback

Memory without feedback is passive storage.

Feedback without memory is a reaction without durable history.

Together:

```text
MEMORY → CONTEXT
FEEDBACK → CHANGE
CONTEXT + CHANGE → NEW STATE
```

This is the minimum architectural mechanism for a system that accumulates history while remaining dynamically responsive.

## 9. Graph as active structure

The graph is both representation and operating structure. It carries relations, aggregates local state into global state, and provides the route through which global state returns to local elements.

```text
ELEMENTS
  ↓
RELATIONS
  ↓
EDGES
  ↓
GRAPH
  ↓
WHOLE STATE
  ↓
FEEDBACK
  ↓
LOCAL STATE
  ↺
```

## 10. Multi-scale recursion

A whole at one scale may be a node at the next scale. A node may itself contain a subgraph.

Therefore the same architecture can repeat:

```text
parts → relations → whole
whole → feedback → parts
```

at local, subsystem and system levels.

## 11. Operational organism

The architecture implies the following functional organs for SPACE:

- **Perception/Input** — receives observations, requests and environment state;
- **State** — maintains the current system state;
- **Memory** — stores durable history and local/relational traces;
- **Graph** — organizes nodes, relations and edges;
- **Context/Activation** — retrieves the minimally sufficient active subgraph;
- **Reasoning/Planning** — converts state and context into candidate actions;
- **Tool/Skill layer** — provides bounded capabilities;
- **Guardian** — authorizes actions and enforces security policy;
- **Execution** — performs only authorized operations;
- **Feedback** — returns results to state, graph and memory;
- **Loop Guard** — stops unproductive repetition and forces re-planning;
- **Provenance/Audit** — preserves why, from where and under which state an action/result occurred;
- **Recovery** — moves the organism into a controlled degraded/recovery state after faults.

No single organ substitutes for the others.

## 12. Complete cycle

The intended SPACE organism cycle is:

```text
INPUT
  ↓
OBSERVE / STATE
  ↓
MEMORY + CONTEXT ACTIVATION
  ↓
GRAPH / RELATIONS
  ↓
REASON / PLAN
  ↓
GUARDIAN
  ↓
AUTHORIZED EXECUTION
  ↓
RESULT
  ↓
FEEDBACK
  ├──→ STATE UPDATE
  ├──→ GRAPH UPDATE
  ├──→ MEMORY UPDATE
  └──→ PROVENANCE / AUDIT
           ↓
      LOOP / NEXT CYCLE
```

The loop guard interrupts cycles that repeat without new information, state change or strategy change.

## 13. Fundamental interpretation

This architecture permits the system to be treated as an organism-like information structure without requiring that any particular philosophical claim about consciousness be assumed in advance.

The architecture itself is the object being built and tested.

## 14. Relation to existing Ω architecture

This document extends the existing relations-first, graph-memory and whole↔different foundations. It does not erase historical formulations. It adds the explicit requirement that memory and bidirectional feedback participate in the operational architecture itself.

Existing Ω-Lab principles remain the source of structural rules; this document provides their integrated organism-level form.

## 15. Core formula

> **Память сохраняет. Связь соединяет. Граф собирает. Целое возвращает состояние. Feedback изменяет части. Память сохраняет изменение. Новый цикл собирает новое целое.**

This is the foundation of the next SPACE implementation stage.
