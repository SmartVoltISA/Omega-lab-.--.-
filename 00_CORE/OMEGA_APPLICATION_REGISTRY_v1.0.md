# Ω-Lab — Application Registry v1.0

## Purpose

Retrospective application mapping of research results into TOOL, SKILL, CONTROL or DEFERRED.

This registry is deliberately conservative. Discovery of a result is not sufficient for promotion. Every application keeps its evidence status and provenance.

## Current candidates

| Result / branch | Evidence status | Destination | Candidate artifact | Demonstrated use | Possible use | Benefit | Next validation |
|---|---|---|---|---|---|---|---|
| Ω-LINK-1 structural relation results | CONFIRMED within tested scope / broader generalization OPEN | TOOL + CONTROL | `Relation Influence Analyzer` | Research graph analysis | Space graph, software dependency graphs, network diagnostics, architecture analysis | DISCOVERY, TRACEABILITY, ROBUSTNESS | Implement bounded analyzer; test on known graph topologies and counterexamples |
| Ω-MEM-4R | REFINED / PARTIAL | CONTROL + DEFERRED | `Memory Expressiveness Counterexample Suite` | Research validation | Regression tests for memory representations and hypothesis claims | ROBUSTNESS, SAFETY | Automate the counterexample set and verify against prior claims |
| Ω-MEM-5 | PARTIAL / PROMISING | SKILL candidate + CONTROL | `Relevant Context Retrieval` | Research prediction task | Space context selection, memory ranking, minimal sufficient context | ACCURACY, EFFICIENCY | Remove oracle dependence; compare against IID and independent generators; measure benefit |
| Graph-first memory protocol | ARCHITECTURE / not a single empirical claim | SKILL + TOOL | `Graph Memory Inspector` | Ω-Lab architecture | Space memory provenance, relation inspection, conflict tracing | TRACEABILITY, DISCOVERY | Build read-only prototype against existing graph schema |
| Ω-ORDER architecture | OPEN hypothesis | DEFERRED + CONTROL | `Provenance Branch Inspector` | Architectural proposal only | Research history reconstruction, Space provenance | TRACEABILITY, DISCOVERY | Apply retrospectively to one nontrivial memory branch and compare inspection quality |
| Ω-REL-009 conflict-memory branch | RESULT EXISTS / application requires result-level audit | CONTROL candidate | `Conflict Memory Test` | Research experiment | Memory conflict detection and regression testing | ROBUSTNESS, SAFETY | Verify exact result and controls before promotion |
| ENERGY branch | Result-by-result audit required | DEFERRED | Energy/transition analysis tools | Research branch | Smart energy systems, control, optimization | CAPABILITY, EFFICIENCY | Audit individual experiment results before any application claim |

## Rules

### 1. Confirmed result does not mean production-ready

`CONFIRMED` only means the stated claim is supported within its tested scope.

### 2. Application status is independent

Use:

`CANDIDATE → DESIGNED → PROTOTYPE → VALIDATED → ACTIVE`

No candidate in this document is automatically ACTIVE.

### 3. Speculative applications remain hypotheses

Direct, adjacent and cross-domain uses are useful discovery paths, but they must not be described as demonstrated benefits until tested.

### 4. Controls are first-class outputs

Counterexamples, negative results and failure modes can become valuable controls even when the original hypothesis is rejected or refined.

## First implementation batch

### A. Relation Influence Analyzer — TOOL

Purpose: calculate bounded structural effects of relation/edge changes on a supplied graph.

Inputs:
- graph;
- selected edge/relation;
- perturbation operation;
- structural metric.

Outputs:
- before/after metrics;
- affected nodes/paths;
- influence summary;
- provenance.

Must not claim universal predictive power.

### B. Memory Expressiveness Counterexample Suite — CONTROL

Purpose: prevent overgeneralization of memory hypotheses by preserving known counterexamples and expected failure boundaries.

### C. Relevant Context Retrieval — SKILL candidate

Purpose: select context that materially affects a task while preserving provenance and uncertainty.

Hard requirement: no oracle leakage. The Skill is not promoted until independent evaluation exists.

### D. Graph Memory Inspector — TOOL

Purpose: inspect node identity, relations, provenance, state, confidence and conflicts without modifying memory.

This is a low-risk implementation target because it is observational rather than generative.

## Application discovery levels

For each confirmed result:

1. **Direct** — same problem/domain.
2. **Adjacent** — structurally similar problem.
3. **Cross-domain** — same mechanism in another domain.

Each level remains separately labelled as demonstrated or hypothetical.

## Current priority

1. Build Graph Memory Inspector.
2. Build Relation Influence Analyzer.
3. Build Memory Counterexample Control Suite.
4. Re-audit Ω-MEM-5 before implementing Relevant Context Retrieval.
5. Audit Ω-REL-009 and ENERGY results individually.

## Provenance requirement

Every artifact created from this registry must reference:

`hypothesis → protocol → experiment → result → verification → application → application test → benefit`

No orphan Tools or Skills.

## Status

**ACTIVE REGISTRY / APPLICATION WORK IN PROGRESS**

This registry is the bridge from Ω-Lab research to operational Space capabilities.
