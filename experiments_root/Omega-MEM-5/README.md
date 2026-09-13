# Ω-MEM-5 — Memory → Predictive Choice

**Status:** OPEN / protocol definition only  
**Date:** 2026-08-14  
**Relation:** continuation of Ω-MEM-2 → Ω-MEM-4 → Ω-MEM-4R and the `006-MEMORY-PREDICTION-GRAPH` line.

## Why this experiment exists

The previous memory experiments asked whether a memory representation can improve prediction. The audited Ω-MEM-4 showed that this question cannot be answered cleanly by raw state count alone: several implementations had capacity and structural-matching defects, while some robust observations survived the audit.

The present branch asks a narrower question:

> **Does memory matter because it increases the number of stored states, or because it makes different future transitions distinguishable?**

This is directly connected to the current Ω discussion of:

**state → history → memory → distinguishable future transitions → choice**

and to the working observation from the lightning/spectral discussion that a continuous process may be represented at different resolutions while the underlying transition structure remains the object of interest.

## Working hypothesis

Let `S` be the currently observed state and `M` the retained memory/history representation.

Define the predictive choice set:

`C(S,M) = set of distinguishable next transitions available/predictable from (S,M)`.

Working hypothesis:

> **Functional memory is not adequately characterized by the number of memory states. It is characterized by how strongly the memory representation partitions the future into distinguishable predictive alternatives.**

This is a hypothesis, not a conclusion.

## Minimal model

For two histories `H1` and `H2` that arrive at the same current observation `S`:

`H1 → S`  
`H2 → S`

we test whether:

`C(S,M1) ≠ C(S,M2)`

and whether the difference improves prediction of the next transition.

## Core distinction

Two systems can have the same:

- number of memory states;
- current observed state;
- parameter/state budget;

while differing in how those states partition future transitions.

Therefore Ω-MEM-5 separates:

1. **memory capacity** — how many internal states can be represented;
2. **memory content** — which histories are retained;
3. **predictive partition** — which future transitions those histories distinguish;
4. **choice/prediction quality** — how accurately the next transition can be selected.

## Relation to Ω-MEM-4R

Ω-MEM-4R found useful but model-specific evidence for capacity thresholds and predictive memory, while explicitly rejecting a universal structural-match law. It also identified implementation defects that prevent stronger conclusions.

Ω-MEM-5 therefore does **not** reuse the invalid comparisons. It turns the surviving question into an explicit observable quantity: the predictive partition induced by memory.

## Relation to physical analogy

The lightning/spectral discussion is used only as a conceptual analogy, not as experimental evidence for this computational hypothesis.

A physical process may be observed at coarse or fine resolution, producing different numbers of distinguishable states. The question for Ω-MEM-5 is whether the invariant object is better described by the **structure of distinguishable transitions** than by the raw number of nodes used to represent them.

## Falsification targets

The hypothesis is weakened or falsified if, under equal capacity and controlled current state:

- different histories do not change the predictive transition partition;
- additional memory states improve prediction only through capacity, with no history-specific predictive effect;
- predictive partition size is unrelated to prediction quality across controlled systems;
- a memory representation that preserves no relevant historical distinction performs equivalently to one that does preserve it.

## Non-claims

Ω-MEM-5 does **not** claim that:

- memory is a universal primitive;
- choice is fundamental;
- physical systems literally implement this graph;
- more choices mean more information;
- state count equals information volume;
- the model establishes anything about consciousness or agency.

Those questions remain outside this experiment.
