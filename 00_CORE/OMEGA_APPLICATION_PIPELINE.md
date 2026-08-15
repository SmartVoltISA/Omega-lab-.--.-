# Ω-Lab — APPLICATION PIPELINE

**Status:** CORE / ACTIVE
**Version:** Ω-Application 1.0
**Established:** 2026-08-16

## 1. Purpose

Ω-Lab research does not end when an observation or experimental result is obtained.

A confirmed result must be evaluated for practical use and assigned a controlled destination:

- `TOOL` — implement as an independent computational or operational instrument;
- `SKILL` — implement as a reusable capability of Space/AI/system agents;
- `CONTROL` — convert into a validation, negative-control, regression, or safety test;
- `DEFERRED` — preserve for future development when evidence or implementation readiness is insufficient.

The purpose of this layer is to prevent useful discoveries from remaining only as notes, while also preventing unproven ideas from being prematurely turned into system functionality.

---

## 2. Fundamental rule

> **A result is not automatically an application. Confirmation and usefulness are separate questions.**

The operational sequence is:

```text
RESEARCH
   ↓
RESULT
   ↓
VERIFY
   ↓
CLASSIFY
   ↓
APPLICATION DESIGN
   ↓
IMPLEMENT TOOL / SKILL / CONTROL
   │
   └── or DEFER
   ↓
APPLICATION TEST
   ↓
MEASURE BENEFIT
   ↓
FEEDBACK
   ↓
MEMORY / GRAPH / PROVENANCE
   ↺
```

No step may be silently skipped when the result is being promoted into the active system.

---

## 3. Epistemic gate

Before practical implementation, the result must have an explicit evidence state.

Recommended states:

| State | Meaning |
|---|---|
| `HYPOTHESIS` | Proposed but not sufficiently tested |
| `OBSERVED` | Pattern observed but not independently confirmed |
| `PARTIAL` | Some evidence supports the result, limitations remain |
| `CONFIRMED` | Repeated/controlled evidence supports the stated claim within defined scope |
| `REFINED` | Original claim changed after testing |
| `REJECTED` | Evidence contradicts the claim within tested scope |
| `OPEN` | Evidence remains insufficient |

Only `CONFIRMED` results should normally enter the implementation pipeline.

`PARTIAL` results may enter only as explicitly experimental prototypes, never as silently trusted production logic.

---

## 4. Classification gate

After verification, ask four questions:

1. **Can this be executed independently?**
2. **Can this be reused as a system capability?**
3. **Is its greatest value in detecting errors or preventing false conclusions?**
4. **Is implementation premature?**

The answers determine the destination.

```text
                    VERIFIED RESULT
                          │
          ┌───────────────┼───────────────┐
          │               │               │
       executable      capability      validation
          │               │               │
         TOOL           SKILL          CONTROL
          │               │               │
          └───────────────┼───────────────┘
                          │
                     if not ready
                          ↓
                      DEFERRED
```

A result may legitimately produce more than one artifact. For example, one research result may become both a `TOOL` and a `CONTROL`.

---

## 5. TOOL

### Definition

A `TOOL` is an explicit instrument that performs a bounded operation on data, structure, state, graph, memory, or another system object.

### Typical characteristics

- deterministic or sufficiently specified input/output;
- independently executable;
- measurable output;
- reusable across experiments or projects;
- can be tested without requiring the full reasoning context.

### Possible applications

- graph analysis;
- state-transition analysis;
- memory comparison;
- structural-distance calculation;
- anomaly detection;
- experiment auditing;
- market-state analysis;
- dependency analysis;
- provenance reconstruction;
- architecture diagnostics;
- data quality checks.

### Example

If a confirmed result establishes that a particular relation metric reliably exposes a structural transition, it can become:

`Relation Transition Analyzer`

Potential uses:

- Ω-Lab experiments;
- MARKET;
- Space architecture;
- network diagnostics;
- software dependency analysis.

### Acceptance requirement

A TOOL must have:

```text
INPUT
OUTPUT
ASSUMPTIONS
LIMITATIONS
TEST
EXPECTED BEHAVIOR
FAILURE MODES
VERSION
```

---

## 6. SKILL

### Definition

A `SKILL` is a reusable capability or procedure available to an intelligent system, agent, or Space component.

Unlike a TOOL, a Skill may require interpretation, selection, sequencing, or contextual judgment.

### Typical characteristics

- reusable reasoning or operational procedure;
- context-sensitive;
- may invoke one or more tools;
- produces an action, decision, classification, or structured result.

### Possible applications

- retrieve minimally sufficient memory;
- compare competing hypotheses;
- select an appropriate analysis tool;
- detect state transitions;
- construct experiment protocols;
- identify missing evidence;
- determine whether a result is ready for promotion;
- trace provenance;
- identify contradictions between branches;
- select the next experiment.

### Example

A confirmed memory result may produce:

`Relevant Context Retrieval`

The Skill could:

1. identify the current task state;
2. search candidate memories;
3. rank them by structural relevance;
4. return the minimum sufficient context;
5. record which memories influenced the decision.

### Acceptance requirement

A SKILL must specify:

```text
TRIGGER
INPUT CONTEXT
PROCEDURE
TOOLS USED
OUTPUT
DECISION RULES
FAILURE / ABSTENTION RULE
FEEDBACK
```

---

## 7. CONTROL

### Definition

A `CONTROL` is a mechanism whose primary purpose is to test, constrain, audit, or falsify system behavior.

Controls are first-class outputs of research.

### Possible applications

- negative controls;
- regression tests;
- counterexample tests;
- reproducibility checks;
- memory contamination tests;
- false-positive detection;
- provenance integrity checks;
- tool output validation;
- Guardian checks;
- safety gates.

### Principle

> **A discovery that tells us how a system can fail is also a useful discovery.**

A result does not need to increase capability directly to have operational value.

---

## 8. DEFERRED

A result is `DEFERRED` when:

- evidence is promising but incomplete;
- implementation cost is currently unjustified;
- the application is not yet clearly defined;
- required data or infrastructure is unavailable;
- another experiment has higher priority;
- implementation could contaminate an active experiment;
- the result is conceptually important but operationally immature.

Deferred does **not** mean rejected.

The original result, evidence, proposed applications, missing requirements, and reason for deferral must remain recoverable.

---

## 9. Application mapping

Every promoted result should receive an application record containing:

```text
RESULT-ID
CLAIM
EVIDENCE-STATUS
SOURCE-EXPERIMENTS
APPLICATION-CLASS
APPLICATION-NAME
PROBLEM-SOLVED
INPUTS
OUTPUTS
POSSIBLE-USE-CASES
EXPECTED-BENEFIT
LIMITATIONS
IMPLEMENTATION-STATUS
VALIDATION-STATUS
FEEDBACK
NEXT-ACTION
```

---

## 10. Use-case expansion

The first obvious application is not necessarily the best one.

For every candidate TOOL or SKILL, search at least three levels:

### Direct

What does it immediately do?

### Adjacent

Where else can the same mechanism solve a structurally similar problem?

### Cross-domain

Can the same relation, state, memory, or graph property be reused in another domain?

Example:

```text
RELATION ANALYSIS
       │
       ├── Direct: Ω-Lab graph
       ├── Adjacent: software dependencies
       ├── Adjacent: electrical architecture
       └── Cross-domain: market/network dynamics
```

The system must distinguish **demonstrated use** from **possible use**. Possible applications remain hypotheses until tested.

---

## 11. Benefit assessment

Every application must state its expected benefit.

Use a practical classification:

- `CAPABILITY` — enables something previously unavailable;
- `ACCURACY` — improves correctness;
- `EFFICIENCY` — reduces computation, time, or manual work;
- `ROBUSTNESS` — reduces failure or instability;
- `TRACEABILITY` — improves provenance and auditability;
- `SAFETY` — prevents harmful or invalid operation;
- `DISCOVERY` — makes new structure or hypotheses visible.

A benefit must be measurable where practical.

Example:

```text
Claim: relevant-memory selection improves reasoning.

Expected benefit:
- lower irrelevant-context load;
- improved retrieval precision;
- fewer contradictory memories;
- measurable change in task performance.
```

Do not claim benefit merely because an implementation exists.

---

## 12. Application validation

A Tool or Skill is not considered production-ready merely because it runs.

Minimum validation:

```text
UNIT / LOCAL TEST
      ↓
CONTROL / COUNTEREXAMPLE
      ↓
REPRODUCIBILITY
      ↓
REAL APPLICATION
      ↓
BENEFIT MEASUREMENT
      ↓
REGRESSION TEST
```

If the application fails validation, its status must be downgraded or the implementation revised.

No successful demonstration may erase a failed test.

---

## 13. Promotion states

Recommended lifecycle:

```text
CANDIDATE
   ↓
DESIGNED
   ↓
PROTOTYPE
   ↓
VALIDATED
   ↓
ACTIVE
   ↓
MONITORED
   ↓
REFINED / RETIRED
```

`ACTIVE` means the artifact is allowed to influence the operational system.

`MONITORED` means its performance remains subject to feedback and regression testing.

---

## 14. Relation to ORDER and provenance

Application artifacts must preserve origin.

```text
RESULT
  ↓
APPLICATION RECORD
  ↓
TOOL / SKILL / CONTROL
  ↓
APPLICATION TEST
  ↓
BENEFIT
  ↓
FEEDBACK
```

The application must therefore be traceable back to:

- observation;
- hypothesis;
- protocol;
- experiment;
- result;
- verification;
- implementation;
- validation.

This connects directly to the ORDER architecture: provenance is not optional metadata; it is part of system integrity.

---

## 15. Negative and failed results

Failed experiments must enter the application pipeline when they reveal operational constraints.

Examples:

```text
FAILED HYPOTHESIS
      ↓
LIMITATION IDENTIFIED
      ↓
CONTROL CREATED
```

or:

```text
FAILED METHOD
      ↓
KNOWN FAILURE MODE
      ↓
GUARD / ABSTENTION RULE
```

This prevents repeated failure and converts negative knowledge into system protection.

---

## 16. Core principle for Space

Space should not merely receive a list of tools.

It should know:

```text
WHAT exists
WHY it exists
WHERE it came from
WHEN it was validated
WHAT it can do
WHEN it should be used
WHEN it must NOT be used
WHAT evidence supports it
WHAT its limitations are
WHAT feedback it has received
```

Therefore the application layer becomes a bridge between Ω-Lab research and Space operational intelligence.

---

## 17. Mandatory research closeout

When an experiment or research branch reaches a meaningful result, the closeout must answer:

1. What did we find?
2. Is it confirmed?
3. What exactly is confirmed — and within what scope?
4. What contradicts or limits it?
5. Can it become a TOOL?
6. Can it become a SKILL?
7. Can it become a CONTROL?
8. What are the direct applications?
9. What are the adjacent applications?
10. What are the possible cross-domain applications?
11. What measurable benefit is expected?
12. What must be tested before implementation?
13. If not ready, why is it DEFERRED?
14. What is the next action?

A result without this assessment is considered **research-complete but application-incomplete**.

---

## 18. Status language

Use precise language:

- `CONFIRMED` — evidence supports the claim within defined scope;
- `APPLICABLE` — a plausible operational use has been identified;
- `IMPLEMENTED` — an artifact exists;
- `VALIDATED` — the artifact passed defined application tests;
- `ACTIVE` — approved for operational use;
- `DEFERRED` — preserved for future development;
- `REJECTED` — application was tested and failed or was shown to be invalid.

Do not collapse these states into a single word such as “done”.

---

## 19. Working principle

> **Find → verify → understand → classify → build → test → measure → feed back.**

And:

> **Do not build an instrument merely because an idea is interesting. Build it when evidence and utility justify it.**

Likewise:

> **Do not discard a result merely because it cannot yet be implemented. Preserve it with its evidence, limitations, and future application paths.**

---

## 20. Current status

`Ω-Application 1.0` is an active Ω-Lab architectural rule.

It establishes the application layer between research results and operational system capabilities.

The first implementation task is retrospective: apply this pipeline to existing confirmed Ω-Lab results and classify them into `TOOL`, `SKILL`, `CONTROL`, or `DEFERRED`, recording possible use cases and expected benefits without treating speculative applications as confirmed facts.
