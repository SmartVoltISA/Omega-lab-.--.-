# Ω-Space — Hardware Integration Roadmap v1.0

## Goal

Bring the logical organism from a software prototype to a hardware-aware organism without coupling the brain to a particular machine.

## Phase H0 — resource model

- CPU/RAM/GPU/VRAM/storage classes
- resource claims
- release
- capacity and availability
- health events

Status: foundation model added.

## Phase H1 — local telemetry

Implement read-only adapters for:

- CPU load/frequency/temperature where available;
- RAM usage;
- storage capacity/health;
- GPU utilization/memory/temperature where available;
- process/service health.

Telemetry is observation, not permission.

## Phase H2 — secure external I/O

Implement Guardian-gated adapters for:

- Wi-Fi/Ethernet;
- Bluetooth;
- USB devices;
- camera;
- microphone;
- display;
- speaker;
- other OS/device interfaces.

No direct device calls from Brain.

## Phase H3 — processing fabric

Introduce a resource-aware planner:

```text
Task
 ↓
Skill
 ↓
Tool
 ↓
Resource requirements
 ↓
CPU / RAM / GPU / VRAM allocation
 ↓
Execution
 ↓
Result + telemetry
 ↓
Feedback
```

## Phase H4 — persistent habitat

Add durable stores for:

- memory;
- graph;
- audit;
- skill artifacts;
- models;
- tool metadata;
- configuration.

Durability must preserve provenance and versioning.

## Phase H5 — SPACE federation

Implement authenticated SPACE-to-SPACE messaging with:

- identity;
- capability;
- freshness;
- correlation;
- result;
- feedback;
- failure/recovery.

## Phase H6 — embodied I/O

Connect real visual/audio input and display/audio output through the same boundary.

## H7 — autonomous habitat management

Only after H0–H6 are stable:

- resource scheduling;
- thermal/load awareness;
- service restart;
- degraded mode;
- migration to another host;
- multi-SPACE cooperation.

## Non-negotiable boundaries

1. CPU is processing capacity, not authority.
2. GPU is acceleration, not authority.
3. RAM/VRAM are working memory, not identity.
4. Storage is persistence, not truth by itself.
5. Network connectivity is not trust.
6. Wi-Fi/Bluetooth/USB are external interfaces and cross Guardian.
7. Sensor data is untrusted observation until validated.
8. Tools cannot bypass Guardian.
9. Skills cannot grant permissions by themselves.
10. Another SPACE cannot grant trust merely by being another SPACE.
