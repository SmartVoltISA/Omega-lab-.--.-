# Ω-Space — Organism Architecture v1.0

## Operational status

SPACE now has an integrated organism-level core rather than isolated prototypes.

## Organs

| Organ | Responsibility |
|---|---|
| Input / Perception | `SpaceOrganism.observe()` receives observations |
| State | `SpaceState` holds current state and revisions |
| Memory | `DistributedMemory` preserves local and cycle history |
| Graph | `GraphCore` stores nodes and relations/edges |
| Context | memory retrieval supplies a bounded active context |
| Planner | `Planner` converts intent into a bounded plan |
| Capability Registry | declares available and verified capabilities |
| Tool Registry | exposes bounded executable tools |
| Guardian | authorizes or restricts execution |
| Execution | registered tool handlers only; no arbitrary execution |
| Feedback | results update state, memory and graph |
| Event Bus | publishes observations, results, recovery and guard events |
| Audit | records provenance of operational decisions/results |
| Loop Guard | detects repeated semantic cycles without progress |
| Recovery | enters controlled recovery mode while preserving state |

## Complete organism cycle

```text
OBSERVE
  ↓
STATE
  ↓
MEMORY / CONTEXT
  ↓
GRAPH
  ↓
PLAN
  ↓
CAPABILITY
  ↓
GUARDIAN
  ↓
EXECUTION
  ↓
RESULT
  ↓
FEEDBACK
  ├── STATE
  ├── MEMORY
  ├── GRAPH
  ├── EVENTS
  └── AUDIT
       ↓
  LOOP GUARD
       ↓
  NEXT CYCLE / REPLAN / RECOVERY
```

## Safety boundary

SPACE never equates tool registration with permission to execute. The tool requires a capability, the capability must be verified, and Guardian evidence must authorize the action. Guardian remains the security boundary.

## Memory boundary

Memory is not only a log. It is used as context for the next action and receives the result of the current action. This closes the memory ↔ feedback relationship.

## Graph boundary

Every operational cycle produces a provenance-bearing graph event. The graph is therefore updated by execution and can later be used to reconstruct system state and relations.

## Loop boundary

A repeated semantic state/action/output without evidence or strategy change eventually produces `STOP_REPLAN`. The system must then change strategy rather than continue emitting equivalent progress.

## Recovery boundary

Faults do not erase state. Recovery is an explicit state transition with preserved provenance.

## Current implementation layer

The organism core is intentionally deterministic and dependency-light. External models, devices, networks and persistent databases can be attached as organs through the existing bounded interfaces rather than being embedded into the core.
