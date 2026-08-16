# Ω-Space — Hardware Habitat Architecture v1.0

## Core rule

Hardware is not the organism itself. Hardware is the **habitat and resource substrate** in which SPACE lives.

SPACE must never treat CPU, GPU, RAM, VRAM, Wi-Fi, Bluetooth, storage, display, camera, microphone or external devices as trusted organs by default.

They are capabilities exposed by the habitat through controlled adapters.

## Resource organs

| Habitat resource | Organ analogue | Primary role |
|---|---|---|
| CPU | central processing metabolism | control, orchestration, deterministic computation |
| RAM | working circulation | active context, buffers, temporary state |
| Storage | long-term tissue/memory substrate | persistent memory, models, artifacts, audit |
| GPU / accelerator | high-throughput processing organ | tensor/model/media workloads |
| VRAM / accelerator memory | high-speed working memory | model/context buffers and accelerator state |
| Network | external circulation | remote services and communication |
| Wi-Fi | wireless external interface | network access through Guardian |
| Bluetooth | short-range device interface | peripherals/devices through Guardian |
| Camera | eye sensor | visual perception |
| Microphone | ear/sound sensor | audio perception |
| Speaker/display | motor/output organs | external expression |
| USB/PCIe/etc. | attachment interfaces | hardware expansion through adapters |

## CPU ↔ RAM ↔ GPU/VRAM

The normal processing path is:

```text
Task
  ↓
Brain / Planner
  ↓
Skill selection
  ↓
Tool selection
  ↓
Resource Planner
  ├── CPU for control / ordinary computation
  ├── RAM for active context / buffers
  ├── GPU for parallel model/media computation
  └── VRAM for accelerator-local working state
  ↓
Result
  ↓
Feedback
  ↓
Memory + Graph + Skill update
```

The GPU is an accelerator, not a second brain. VRAM is accelerator working memory, not long-term memory.

## Resource allocation

Every non-trivial workload should expose:

- requested resource class;
- estimated capacity;
- actual consumption;
- timeout/deadline;
- cancellation state;
- result/provenance;
- release state.

Resource exhaustion must become an observable system event and must not silently degrade into uncontrolled execution.

## Network and device security

All external I/O crosses the Guardian boundary.

```text
SPACE organ
   ↓
Tool / Adapter
   ↓
Guardian authorization
   ↓
Habitat interface
   ↓
Wi-Fi / Ethernet / Bluetooth / USB / device
   ↓
External world
```

The reverse path is identical in principle:

```text
External world
   ↓
Interface adapter
   ↓
Guardian verification
   ↓
Nervous/Event layer
   ↓
Sensor organ / Brain
```

No organ may directly open an uncontrolled network socket or device channel merely because the OS exposes it.

## Local SPACE-to-SPACE communication

SPACE instances communicate as organisms, not as arbitrary processes.

Every inter-SPACE message must carry:

- sender identity;
- receiver identity;
- message/correlation ID;
- capability/action class;
- timestamp/freshness information;
- payload/provenance;
- requested operation;
- authorization evidence;
- response/feedback linkage.

Path:

```text
SPACE A
  ↓
Nervous/Event layer
  ↓
Guardian
  ↓
Transport
  ↓
Guardian
  ↓
Nervous/Event layer
  ↓
SPACE B
```

## Trust model

Local does not mean trusted.

Same-host communication is still subject to identity, capability, freshness and policy checks when it crosses an organ/security boundary.

## Hardware abstraction rule

The core SPACE organism depends on interfaces, not specific hardware vendors.

A laptop, workstation, server, edge computer or future robotic platform may provide different habitat implementations while exposing the same logical resource contracts.

## Required future adapters

1. CPU telemetry adapter
2. RAM telemetry adapter
3. GPU/VRAM telemetry adapter
4. persistent storage adapter
5. network adapter
6. Wi-Fi adapter
7. Bluetooth adapter
8. camera adapter
9. microphone/audio adapter
10. display adapter
11. speaker adapter
12. USB/device adapter
13. process/service supervisor
14. hardware health adapter

These adapters remain outside the core brain and are controlled through the same capability + Guardian boundary.
