# Ω-Space — Multimodal Sensor Fusion & Capability Matrix v1.0

**Status:** CORE / HABITAT / IMPLEMENTATION BASELINE

## Principle

One physical resource may expose multiple independent capabilities. A capability is not the same as a device, permission, or conclusion.

```text
physical resource
  ↓
capability discovery
  ↓
Guardian policy
  ↓
signal acquisition
  ↓
local fusion
  ↓
semantic inference
  ↓
Memory + Graph + Feedback
```

## Capability separation

A user permission must authorize a specific capability or bounded capability set. Granting one capability must not silently grant unrelated capabilities.

Examples:

- Wi-Fi communication != Wi-Fi sensing
- camera capture != camera-based identity inference
- microphone capture != speech recognition
- Bluetooth communication != proximity inference
- location access != arbitrary movement history
- display output != external action authority

## Sensor classes

### Motion / position

- accelerometer
- gyroscope
- magnetometer
- rotation vector
- gravity / linear acceleration
- barometer
- GNSS/location where available

### Audio

- microphone input
- speaker output
- acoustic echo features where hardware/software permits
- speech/audio inference only after explicit capability authorization

### Vision

- camera frames
- motion / optical-flow features
- depth where available
- OCR / object inference as separate capabilities

### Radio / wireless

- Wi-Fi network communication
- Wi-Fi scan observations
- RSSI / signal observations where exposed
- CSI / PHY sensing only where the device, firmware and driver actually expose it
- Wi-Fi Aware nearby-device discovery where supported
- Bluetooth communication and discovery where supported
- Bluetooth proximity inference only as a separate inferred capability

### Environment

- light
- temperature
- pressure
- humidity where available
- other platform-exposed environmental sensors

## Fusion law

No consequential inference should depend unnecessarily on one noisy signal when independent signals are available at acceptable cost.

```text
raw signals
  ↓
normalization
  ↓
time alignment
  ↓
quality checks
  ↓
correlation / fusion
  ↓
state hypothesis
  ↓
confidence + uncertainty
  ↓
Guardian / policy
  ↓
semantic event
```

The system must preserve the provenance of contributing signals and must be able to explain which signals supported or contradicted an inference.

## Example: phone fall

Do not define `FALL` as a single accelerometer threshold.

Possible evidence:

```text
accelerometer spike
+ gyroscope rotation
+ orientation change
+ acoustic impact feature (if authorized/available)
+ subsequent stillness
+ optional camera confirmation
```

The result is a hypothesis with confidence, not an automatic fact.

## Example: spatial perception

The phone can combine:

```text
IMU          → motion continuity
Wi-Fi        → radio environment / possible ranging or sensing
microphone   → acoustic environment
camera       → visual geometry
barometer    → relative pressure/height changes
magnetometer → magnetic orientation cues
```

Different sensors have different error models. Fusion should exploit complementary strengths rather than assume identical reliability.

## Wi-Fi sensing boundary

Wi-Fi sensing is a real research/engineering capability, but availability is hardware- and driver-dependent. Standard Android application APIs do not universally expose PHY-layer CSI. Therefore `CSI_SENSE`, `PRESENCE_INFER`, `MOTION_INFER`, and similar capabilities must be discovered at runtime and marked unavailable when the platform cannot provide the required data.

Wi-Fi may also provide nearby-device discovery through supported platform mechanisms such as Wi-Fi Aware. Discovery is not equivalent to permission to communicate or disclose information.

## Energy-aware sensing

The sensor system must minimize resource use.

Priority order:

1. use already-available low-cost events;
2. use low-power sensors for coarse detection;
3. wake higher-cost sensors only when uncertainty requires them;
4. fuse locally before invoking an expensive model or external service;
5. stop sampling when the relevant state is stable;
6. record actual resource consumption and sensor duty cycle.

Example:

```text
low-power IMU event
      ↓
possible motion
      ↓
short high-rate IMU window
      ↓
uncertainty remains?
   ↙          ↘
 no            yes
 ↓              ↓
finish      activate next modality
```

## User control

The user remains the authority over consequential external access. Guardian must enforce:

- capability scope;
- duration / expiration;
- purpose where required;
- destination / audience;
- data minimization;
- revocation;
- auditability.

A capability may be used internally without external transmission when the policy permits local processing only.

## Core rule

> **Hardware provides signals. Fusion builds hypotheses. Memory preserves provenance. Guardian controls capabilities. SPACE does not silently turn a sensor reading into authority or fact.**
