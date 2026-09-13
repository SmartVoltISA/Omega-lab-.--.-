# Ω-MEM-1a–1d — Control experiments on minimal functional memory

**Status:** preliminary AI-assisted result; reproducibility pending archival source code, seeds and raw outputs.

## Question

What is the minimum memory state space that can have a causal effect on future outputs, and does memory size or update structure matter more?

## Fixed models

M0: S=1
M2: S=2
M4: S=4
M8: S=8
M16: S=16

The experiments were run with parameters fixed before execution. The reported intervention is a same-history causal intervention: two otherwise identical instances are compared, with memory reset in one instance at the intervention point.

## Ω-MEM-1a — Repeatability, 100 seeds

| Model | Success rate | Mean Δ | State=0 at reset |
|---|---:|---:|---:|
| M0 | 0% | 0.00 | 100/100 |
| M2 | 54% | 5.40 | 46/100 |
| M4 | 54% | 5.40 | 10/100 |
| M8 | 54% | 5.40 | 1/100 |
| M16 | 54% | 5.40 | 1/100 |

The apparent 54% rate is explained by the intervention state. When `state_at_reset = 0`, resetting produces no effective change. When `state_at_reset != 0`, the intervention produces full divergence in the tested architecture.

## Ω-MEM-1b — Strict causal intervention

One history, two identical instances, then reset memory in one instance.

- M0: state at reset = 0 → 0/10 causal divergence; immediate reconvergence.
- M2–M16: state at reset != 0 → 10/10 divergence; first difference at the intervention; no reconvergence in the tested horizon.

This is the cleanest causal result in the series, but it remains architecture-specific.

## Ω-MEM-1c — Size vs structure

| Model | Structured | Random null | Difference |
|---|---:|---:|---:|
| M2 | 54%, Δ=5.40 | 32%, Δ=0.75 | +22% success |
| M4 | 54%, Δ=5.40 | 61%, Δ=1.80 | −7% success |
| M8 | 54%, Δ=5.40 | 81%, Δ=2.74 | −27% success |
| M16 | 54%, Δ=5.40 | 89%, Δ=4.04 | −35% success |

There is no simple claim that structured memory is always superior. In this test, random memory has higher intervention success at larger state spaces, while structured memory produces stronger divergence when it is causally active.

This suggests a **frequency-vs-strength trade-off**, not a universal size or structure advantage.

## Ω-MEM-1d — Minimality

- S=1: causal memory is structurally impossible in this architecture because the state space contains only one state; reset is the identity transformation.
- S=2: causal memory is possible. A concrete counterexample exists: a history such as `[X,Y,Y]` reaches a non-zero memory state, and resetting it changes the subsequent output for the same input.

This establishes minimality **for the tested architecture**, not a universal theorem about memory.

## What was corrected

The earlier claim `S>=2 → causal effect always` was too strong. The controlled experiments show:

> **S=1: causal effect is impossible in this architecture.**
>
> **S>=2: causal effect is possible, but depends on the actual memory state at intervention.**

Also rejected:

- structured memory is always better than random memory;
- larger memory necessarily produces stronger causal influence.

## Current interpretation

The strongest defensible result is not that “more memory is better”. It is that a memory mechanism needs at least two distinguishable internal states to permit a non-trivial reset intervention, and that the causal effect depends on whether the intervention changes an actually occupied functional state.

The next experiments should separate:

1. state-space size;
2. reachable-state fraction;
3. transition structure;
4. intervention location;
5. strength and duration of causal influence.

## Reproducibility requirements

Before treating this as a confirmed result, archive:

- exact source code;
- all parameters;
- all 100 seeds;
- raw trajectories;
- intervention protocol;
- output definition;
- null-model generation procedure;
- software/runtime version.

Then rerun independently.

## Principle

A successful attempt to break a previous result is itself a result and must remain in the project history.
