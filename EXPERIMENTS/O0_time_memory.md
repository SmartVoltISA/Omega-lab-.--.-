# Ω-0 — Minimal Reconstruction of Time and Memory

**Status:** preliminary reported result; reproducibility pending archived source code and seeds.

## Question

Before attempting Ω-0.6 (a minimal comparison-only system), test whether sequence/order and functional memory can be reconstructed without explicitly supplying a physical time coordinate.

The experiment deliberately avoids interpreting the result as a claim that physical time does not exist.

## Minimal models

### M0 — No memory

- No persistent state is carried forward.
- Repeated acts are externally ordered but internally indistinguishable.
- Diversity: 1.
- Internal order: absent.

### M1 — Static trace

- A persistent trace exists.
- The trace is read-only and does not update.
- The trace therefore cannot encode a changing sequence.
- Diversity: 1.
- Internal order: absent.

### M2 — Updating trace

- A trace exists.
- The trace is updated by each act.
- The updated trace influences the next act.
- Diversity: 2 in the reported demonstration.
- An internal before/after distinction becomes observable.

## Reported result

A 20-step demonstration was reported with the following qualitative behavior:

| Model | Memory | Update | Reported behavior | Internal order |
|---|---|---|---|---|
| M0 | none | none | identical marks | no |
| M1 | static | none | identical marks | no |
| M2 | updating | yes | alternating distinct phases | yes |

The reported minimal dependency is:

```text
ACT → TRACE → UPDATE
```

Removing any one of these prevents the demonstrated internal ordering mechanism.

## Interpretation — deliberately limited

The experiment supports a **formal reconstruction of order**, not a physical theory of time.

A safer statement is:

> An external physical time coordinate is not required to represent a minimal internal order if acts leave an updating trace that influences subsequent acts.

This does **not** establish that physical time is emergent, nor that physical time is absent.

The experiment only identifies a candidate minimal mechanism for internally distinguishable sequence.

## Three questions

### 1. Can sequence exist without memory?

Yes, as an externally observed sequence. But in M0 the acts are internally indistinguishable, so the system has no demonstrated internal mechanism for distinguishing earlier from later.

### 2. Can functional memory exist without sequence?

Not in the tested construction. M1 contains a trace, but because it never changes it cannot encode changing history or affect a later phase.

### 3. Can before/after be represented without physical time?

Yes, in the limited formal sense demonstrated by M2: an updating state creates distinguishable phases and a dependency from one act to the next. This is an internal order relation, not yet a physical time variable.

## What this does NOT prove

- It does not prove that physical time is unreal.
- It does not prove that memory is fundamental or emergent in nature.
- It does not prove that `ACT → TRACE → UPDATE` is the unique possible minimal construction.
- It does not establish Ω-0.6 or any hypothesis about will.

## Reproducibility requirement

The reported result came from an AI-assisted experiment. The exact implementation, parameters, random seeds (if any), and raw output must be archived before treating the result as fully reproducible.

The next implementation should be deterministic where possible and should explicitly define:

- what constitutes an act;
- the representation of a trace;
- the update operator;
- the observation function;
- the criterion for internal order.

## Next step: memory

The next research branch is **Ω-MEM**: determine the minimum functional memory required for a system to retain information that can alter future comparisons.

The key distinction will be:

```text
recording ≠ memory
memory = retained state that can causally affect a later act
```

Candidate controls should compare:

1. no retained state;
2. read-only retained state;
3. one-symbol / one-bit mutable state;
4. minimal mutable state with overwrite;
5. minimal mutable state with accumulation.

The goal is not to maximize memory. It is to find the smallest memory structure that produces a measurable effect on future behavior.
