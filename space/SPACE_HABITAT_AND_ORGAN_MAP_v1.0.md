# Ω-Space — Habitat & Organ Map v1.0

## The distinction

SPACE is the organism. The hardware, operating system, network, displays, audio devices, sensors and external services are its **habitat**.

Hardware is therefore not the organism's skeleton. It is the environment in which the organism lives and through which its organs obtain input and perform authorized output.

## Functional anatomy

```text
                         ┌───────────────┐
                         │     BRAIN     │
                         │ State/Graph/  │
                         │ Memory/Plan   │
                         └───────┬───────┘
                                 │
                 ┌───────────────┼───────────────┐
                 │               │               │
          NERVOUS SYSTEM   CIRCULATORY      IMMUNE SYSTEM
          signals/events   resources/health anomaly/quarantine
                 │               │               │
       ┌─────────┴──────┐        │        ┌──────┴──────┐
       │                │        │        │             │
   SENSORY          DIGESTIVE   │      GUARDIAN     RECOVERY
   INPUT             LLM        │      security      repair
       │             processing │
       └──────────────┬─────────┘
                      │
                 MOTOR SYSTEM
                 authorized output
                      │
               ┌──────┴──────┐
               │   HABITAT   │
               │ OS / HW /   │
               │ network /   │
               │ displays /  │
               │ audio / I/O │
               └─────────────┘
```

## Organs and responsibilities

### Brain / active core

State, graph, memory, context activation, planner, capabilities, tools and the operational loop. This is where integration and active processing happen.

### Guardian / passive protective phase

Guardian is deliberately not the thinking center. It evaluates evidence and policy at the boundary before execution. It can allow, restrict or block. The architecture must not let the active core bypass this boundary.

### Nervous system

Carries signals between organs. It provides priority, routing and dispatch. It should not contain business logic for every organ.

### Circulatory system

Carries operational resources and health pulses: compute budget, queue pressure, service availability, model budget, memory pressure and other measurable resources. It is the future home of scheduling/resource arbitration.

### Sensory system

Normalizes input from text, microphone, camera, files, network events, system telemetry, monitors and other external sources. Raw devices remain outside the core behind adapters.

### Digestive system

Processes complex input through an LLM boundary. The LLM is a processing organ: it interprets, summarizes, transforms and proposes. It does not receive security authority merely because it generated a proposal.

### Motor system

Produces output through controlled actuators: display, audio, keyboard/mouse automation, APIs, files, device controls and future robotics. Execution requires authorization.

### Immune system

Detects anomalies, records evidence and can quarantine a component. It complements Guardian: Guardian protects the action boundary; Immune detects abnormal behavior over time.

### Recovery

Preserves state and moves the organism into controlled recovery rather than silently continuing after faults.

### Habitat

Describes the actual runtime environment: machine/VM/container, OS, CPU/GPU, memory, storage, network, displays, audio, cameras, microphones and external devices/services.

## Information flow

```text
HABITAT → SENSE → NERVOUS → BRAIN
                       ↓
                 DIGEST / PLAN
                       ↓
                    GUARDIAN
                       ↓
                  MOTOR / TOOL
                       ↓
                   HABITAT
                       ↓
                   FEEDBACK
                       ↺
```

## What is still missing before physical deployment

1. persistent storage backend;
2. real sensory adapters;
3. real actuator adapters;
4. LLM backend adapter;
5. host resource telemetry;
6. network/service adapters;
7. hardware/device identity binding;
8. process supervisor / service lifecycle;
9. secrets and credential vault boundary;
10. durable event transport for multi-process operation;
11. end-to-end integration tests against a sandbox habitat;
12. deployment package for the target host.

These are implementation organs, not changes to the foundation.
