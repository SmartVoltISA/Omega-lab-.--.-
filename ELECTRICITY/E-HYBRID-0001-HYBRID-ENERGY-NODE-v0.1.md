# E-HYBRID-0001 — Hybrid Energy Node v0.1

Date: 2026-08-23
Status: virtual prototype / benchmark model

## Objective

Build a common energy node that accepts heterogeneous ambient sources, conditions them independently, stores energy, and supplies a controlled low-power load.

## Architecture

```text
PV ─────────┐
TEG ────────┤
VIBRATION ──┤→ SOURCE CONDITIONING → ENERGY BUS → STORAGE → REGULATED LOAD
MAGNETIC ───┤                         ↑             │
RF / OTHER ─┘                         └── GUARDIAN ─┘
```

The magnetic input is intentionally a slot in v0.1. It must be measured rather than assigned an invented power value.

## Literature benchmark

A 2026 experimentally validated hybrid PV+TEG+PZT system reports:
- PV: 8.1 mW peak at 600 W/m²;
- TEG: 3.6 mW at ΔT = 10°C;
- PZT: 1.9 mW at 60 Hz, 0.3 g;
- reported hybrid peak: 12.8 mW;
- reported operational uptime: 93% under the stated test conditions.

The source reports adaptive source switching, MPPT, storage, DC-DC conversion and load management. These values are benchmarks, not predictions for our hardware.

## First-order power budget

Nominal component peak sum from the reported source values:

8.1 + 3.6 + 1.9 = 13.6 mW.

Reported integrated peak = 12.8 mW.

Difference from simple sum = 0.8 mW, approximately 5.9% of the component-sum benchmark. This is NOT a universal efficiency figure because the component maxima need not occur simultaneously and the integrated test has its own operating conditions.

If a hypothetical 80% end-to-end conversion/storage/load efficiency were imposed only as a sensitivity scenario:

12.8 mW × 0.80 = 10.24 mW useful output.

This 80% number is a modeling assumption, not a measured result.

## Energy scale

At 10.24 mW continuous useful output:
- 1 hour ≈ 10.24 mWh;
- 24 hours ≈ 245.8 mWh;
- 30 days ≈ 7.37 Wh.

These are conditional calculations assuming continuous average output, not the published 93% uptime or peak power.

For a 1 F supercapacitor charged from 0 to 3.3 V:

E = 1/2 C V² = 5.445 J ≈ 1.51 mWh.

At 10.24 mW, the idealized charge time from empty to 3.3 V would be about 532 s (8.9 min), before accounting for voltage-dependent converter efficiency and source intermittency.

## Control strategy

The node must not simply sum all source voltages. Each source requires an appropriate interface and operating point. The controller estimates:

- source voltage/current;
- instantaneous or estimated input power;
- source availability;
- storage state;
- load demand;
- conversion losses;
- safety limits.

A basic policy is:

1. harvest any source whose net delivered power is positive;
2. prioritize the source with the highest net useful power when sources compete for one converter;
3. store surplus;
4. shed or defer non-critical loads when storage falls below threshold;
5. preserve a reserve for sensing/communication;
6. log source contributions and losses.

## Guardian layer

Future version: optimize source arbitration using state and history rather than instantaneous power only.

State vector candidate:

X(t) = [P_PV, P_TEG, P_VIB, P_MAG, SOC, P_LOAD, LOSS, STATE, MEMORY]

Decision:

u(t) = source selection + storage/load allocation.

Objective:

maximize useful delivered energy while maintaining safety and minimum reserve.

## Proposed physical prototype

Target application: self-powered SmartVolt/industrial sensor node.

Minimum instrumentation:
- source voltage/current measurement for each input;
- supercapacitor voltage;
- load voltage/current;
- temperature;
- vibration/acceleration;
- magnetic field sensor if magnetic harvesting is included;
- time-stamped logging.

Initial source set:
1. small PV cell;
2. TEG across a controlled temperature difference;
3. electromagnetic vibration harvester;
4. magnetic-field harvester as a separate experimental channel.

## Critical control experiment

Compare:

A. single-source harvester;
B. fixed-priority hybrid harvester;
C. adaptive hybrid harvester.

Keep the available environmental inputs the same.

Measure:
- harvested joules;
- useful delivered joules;
- losses;
- uptime;
- storage state;
- source utilization;
- number of load interruptions.

The hypothesis is not that energy is created. The hypothesis is that topology + adaptive source arbitration can increase useful delivery/reliability relative to a poorly coordinated hybrid system under the same external energy conditions.

## Important boundary

Existing literature already demonstrates hybrid harvesting of multiple sources and adaptive power management. Therefore the novelty question is NOT whether hybrid harvesting works. It is whether our relational/Guardian architecture provides a measurable improvement in efficiency, uptime, resilience, maintenance or cost.

## Next experiment

Construct a numerical simulation with time-varying PV, ΔT and vibration inputs, then add a measured or literature-grounded magnetic input. Compare fixed versus adaptive allocation under identical input traces.
