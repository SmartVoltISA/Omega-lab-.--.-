# Ω-Space — Boundaries: Body / Skills / Tools / Market v1.0

**Status:** CORE / ARCHITECTURE  
**Date:** 2026-08-16

## 1. Why this separation exists

SPACE must not become a warehouse containing every experiment, tool and application ever created in Ω-Lab.

The architecture is therefore separated into four levels:

```text
                         SPACE
                    living organism
                           │
             ┌─────────────┼─────────────┐
             │             │             │
           BODY          SKILLS        EXTERNAL
             │             │          APPLICATIONS
             │             │             │
          organs       procedures      MARKET
             │             │
             └────── TOOLS ──────────────┘
```

The separation is functional, not merely organizational.

---

## 2. BODY — the organism itself

The SPACE body contains only mechanisms required for the organism to exist, perceive, remember, think, protect itself, communicate and act.

### Body organs

- structural backbone / spine;
- nervous system;
- brain / active core;
- memory;
- graph / relational structure;
- perception organs;
- communication organs;
- motor organs;
- resource circulation;
- recovery;
- immune / Guardian layer;
- audit / provenance;
- habitat interface.

The body should remain as stable and general-purpose as possible.

### Rule

> A body organ provides a basic physiological function. It does not contain a specific business workflow.

Example:

`vision` belongs to the body.  
`recognize this particular product for a Market strategy` belongs to a Skill/Application layer.

---

## 3. SKILL — the organism's learned procedure

A Skill is not a body organ and not a raw tool.

A Skill describes **how the organism uses what it has** to accomplish a repeatable task.

The practical model is:

```text
MEMORY / CONTEXT
      ↓
WHAT IS KNOWN?
      ↓
WHAT IS CONNECTED?
      ↓
WHERE WAS IT USED?
      ↓
WHAT WAS TRIED?
      ↓
WHAT HAPPENED?
      ↓
WHAT WORKED / FAILED?
      ↓
WHICH CAPABILITIES ARE REQUIRED?
      ↓
WHICH TOOLS ARE USED?
      ↓
PROCEDURE
      ↓
RESULT
      ↓
FEEDBACK
      ↓
MEMORY / GRAPH
```

This is the user's intended meaning of Skill: **the accumulated operational experience of the organism**, not merely a prompt or code file.

### Skill contains

- task class;
- required context;
- relevant memory/graph relations;
- prerequisite capabilities;
- tool sequence;
- procedure;
- expected result;
- verification method;
- known failure modes;
- previous successful cases;
- previous failures;
- provenance;
- feedback history;
- current readiness.

### Skill rule

> Skill remembers how an operation was performed, where it was useful, what happened and under which conditions it worked or failed.

A Skill can therefore be thought of as **the organism's practiced hand**.

---

## 4. TOOL — an instrument used by a Skill

A Tool is a concrete means of doing something.

Examples:

- calculator;
- browser/API client;
- camera interface;
- OCR;
- Python runner;
- CAD processor;
- database adapter;
- market-data adapter;
- image processor;
- file processor;
- terminal adapter;
- device controller.

A Tool does not decide the overall procedure.

```text
SKILL → selects/organizes → TOOL → performs operation
```

A tool can be used by many Skills.

### Tool rule

> Tool = instrument. Skill = learned way of using instruments.

This distinction prevents every new script from becoming an artificial "organ" of SPACE.

---

## 5. TOOL REPOSITORY — external instrument library

The planned public Tools repository is separate from the SPACE body.

Its purpose:

- collect reusable tools;
- expose useful implementations publicly;
- allow external contributions;
- receive issues and feedback;
- preserve provenance and versions;
- allow tools to mature independently from the organism core.

The repository should be open to discussion and reuse while maintaining clear safety and licensing boundaries.

### Promotion into SPACE

A public tool does not automatically become trusted by SPACE.

```text
PUBLIC TOOL
   ↓
INSPECT
   ↓
SANDBOX
   ↓
CAPABILITY REGISTRATION
   ↓
VERIFICATION
   ↓
GUARDIAN POLICY
   ↓
AVAILABLE TO SKILLS
```

The external repository is therefore an ecosystem, not an uncontrolled extension of the organism.

---

## 6. MARKET — an external application environment

Ω-MARKET is not a body organ.

It is an **application domain / economic environment** that uses the organism's capabilities, skills and tools for market research and potentially economic activity.

Existing Market architecture already contains its own state model, adaptive feedback ring, transition matrix, experiments and handoff documentation. fileciteturn74file0turn74file1turn74file4turn74file5

Therefore Market remains outside the SPACE body.

```text
SPACE
  ↓
SKILLS
  ↓
TOOLS / DATA
  ↓
Ω-MARKET
  ↓
RESULTS
  ↓
FEEDBACK
  ↓
SPACE MEMORY / KNOWLEDGE
```

Market can teach the organism through feedback, but Market's business logic must not become embedded in the organism's core.

### Market rule

> Market is a living application environment served by SPACE, not an organ inside SPACE.

---

## 7. LLM — processing organ, not the organism

The LLM is treated as a computational organ within the body/habitat boundary.

It can provide:

- language processing;
- synthesis;
- interpretation;
- candidate reasoning;
- transformation of information;
- planning proposals.

It does not automatically receive:

- unrestricted tool access;
- security authority;
- memory ownership;
- final execution authority.

The safe operational chain is:

```text
INPUT
 ↓
PERCEPTION
 ↓
MEMORY / CONTEXT
 ↓
LLM / PROCESSING
 ↓
PLAN / CANDIDATE ACTION
 ↓
GUARDIAN
 ↓
TOOL
 ↓
RESULT
 ↓
FEEDBACK
```

This preserves separation of cognition, authorization and execution.

---

## 8. Body / Skill / Tool / Application matrix

| Layer | Answers | Example |
|---|---|---|
| Body | What can the organism fundamentally perceive/process/do? | vision, memory, graph, communication |
| Capability | What operation is currently available? | OCR, speech-to-text, file read |
| Skill | How does the organism repeatedly accomplish a task? | inspect electrical panel and produce report |
| Tool | What concrete instrument performs a step? | Python, OCR engine, API client |
| Application | In which domain is the capability used? | Ω-MARKET |
| Environment | Where does the organism exist? | OS, CPU/GPU, RAM, network, devices |

---

## 9. The hand / finger model

The biological analogy is useful here:

```text
BODY
 ↓
ARM / MOTOR SYSTEM
 ↓
HAND
 ↓
FINGER
 ↓
TOOL
```

But operationally the hierarchy is:

```text
BODY ORGAN
 ↓
CAPABILITY
 ↓
SKILL
 ↓
TOOL
 ↓
ACTION
 ↓
RESULT
```

A particular tool is comparable to a finger/instrument at the action boundary. A Skill is the learned coordination that knows **which finger, which movement, in which order, for which purpose**.

---

## 10. Feedback crosses boundaries in both directions

The separation must not create isolation.

```text
BODY
 ↕
SKILL
 ↕
TOOL
 ↕
APPLICATION
```

Results travel upward as evidence and experience. Requirements travel downward as tasks and constraints.

Example:

```text
MARKET task
 ↓
Skill selects procedure
 ↓
Tool retrieves data
 ↓
Result
 ↓
Verification
 ↓
Skill update
 ↓
Memory / Graph
 ↓
Future Market decision
```

Thus separation is **modularity**, not disconnection.

---

## 11. What must never happen

1. Market logic must not become hard-coded into the Body.
2. A Tool must not become a Skill merely because it works once.
3. A Skill must not become a trusted capability without verification.
4. LLM output must not bypass Guardian.
5. Public tools must not receive implicit trust.
6. Memory must not be reduced to an undifferentiated log.
7. Application-specific state must not corrupt core organism state.

---

## 12. Target repository ecosystem

```text
Ω-LAB CORE REPOSITORY
│
├── 00_CORE
│   ├── foundation
│   ├── ontology
│   ├── memory
│   ├── graph
│   └── SPACE architecture
│
├── space/
│   ├── body / organs
│   ├── core
│   ├── guardian
│   ├── perception
│   ├── motor
│   └── habitat adapters
│
├── skills/                 ← learned procedures / operational knowledge
│
├── market/                 ← Ω-MARKET application environment
│
├── experiments/            ← research and experiments
│
└── history/                ← provenance

SEPARATE PUBLIC REPOSITORY
└── Ω-TOOLS                  ← reusable instruments and community feedback
```

The exact directory migration is a later implementation step. Historical material must not be deleted merely to make the tree look clean.

---

## 13. Final model

> **SPACE is the organism.**  
> **Body is what keeps it alive and connected.**  
> **Memory is what gives it history.**  
> **Skills are what it has learned to do.**  
> **Tools are what it uses to do it.**  
> **Market is an environment/application where those abilities are applied.**  
> **Habitat is where the organism physically/software-wise exists.**

This is the target separation for the next architecture stage.
