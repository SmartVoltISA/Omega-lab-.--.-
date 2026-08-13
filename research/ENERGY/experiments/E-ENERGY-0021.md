# E-ENERGY-0021 — Consumed Internal Resource

**Date:** 2026-08-13  
**Direction:** ENERGY  
**Status:** COMPLETED / PRELIMINARY RESULT  
**Hypothesis:** H-ENERGY-06 — transition barrier; extension toward stored/released potential

## 1. Question

Can a minimal internal state, distinct from the relation graph itself, create a directional transition while remaining measurable before and after the transition?

The internal state is called `R` (resource state). It is deliberately not called energy.

## 2. Minimal model

Each subsystem has:

```text
G = relation structure
R = internal resource state
```

Allowed transitions depend on both `G` and `R`.

A transition can consume one unit of `R` when a constrained structural transformation is executed.

No energy variable or physical energy equation is used.

## 3. Accumulation phase

A reversible loading operation increases `R`:

```text
R = 0 → 1 → 2 → 3
```

The structural graph can remain unchanged while `R` changes.

This is important because it creates a candidate analogue of a stored quantity: a system can have different future transition capabilities while its visible relational structure is identical.

## 4. Release / expenditure phase

A constrained transformation is executed:

```text
(G0, R=3)
      ↓ transition
(G1, R=2)
```

A second identical transformation gives:

```text
(G1, R=2)
      ↓ transition
(G2, R=1)
```

The transition is therefore directional in the augmented state space because the internal resource changes.

## 5. Result

The experiment successfully separates two cases that the previous pure-graph model could not distinguish:

### Case A — same graph, different internal state

```text
(G0, R=1)
(G0, R=3)
```

The relation structure is identical, but the allowed transition budget differs.

### Case B — transition consumes resource

```text
R_before > R_after
```

The resource state is measurable before and after each transition.

Therefore the model now contains a genuine **stored state that can be depleted by a process**.

## 6. Transfer test

A two-subsystem version gives:

```text
A: R=3     B: R=1
       ↓ transfer
A: R=2     B: R=2
```

Total resource remains:

```text
3 + 1 = 2 + 2 = 4
```

This is a controlled transfer, not destruction.

## 7. Critical caveat

The resource conservation is still a rule of the constructed model. We have not derived it from the relation graph.

Therefore we have demonstrated:

> A minimal system can contain a stored internal quantity that changes during structural transitions and can be transferred between subsystems.

We have NOT demonstrated:

> This quantity is physical energy.

The distinction remains explicit.

## 8. New structural insight

The experiment suggests that the earlier binary picture may be incomplete.

Instead of:

```text
energy = structure OR release
```

we now have a three-layer candidate architecture:

```text
STRUCTURE
    ↓
INTERNAL STORED STATE
    ↓
TRANSITION
    ↓
NEW STRUCTURE
```

The stored state can remain present while the structure is static.

The transition changes both the structure and the stored state.

## 9. Relation to the accumulator intuition

The model now reproduces the abstract logic of an accumulator:

```text
LOAD
  ↓
R increases
  ↓
HOLD
  ↓
R remains available
  ↓
RELEASE / USE
  ↓
R decreases
```

This is structurally analogous to the user's accumulator intuition, but it is still only a computational analogy.

## 10. Strongest remaining question

We introduced `R` as a primitive resource state.

That means we have not yet explained where the stored quantity comes from.

The next question is therefore deeper:

> **Can the stored state R itself emerge from relations and their history, instead of being inserted as a primitive?**

This is now the critical test.

## 11. Falsification path

The current hypothesis is weakened if `R` must always be manually assigned.

A stronger result would occur if repeated relational operations naturally create an internal state equivalent to `R`, with no explicit resource variable.

Then the hierarchy could become:

```text
RELATION
   ↓
HISTORY OF CHANGE
   ↓
STORED STATE
   ↓
TRANSITION
   ↓
RELEASE
```

That would connect ENERGY directly to the existing Ω-Lab work on memory and information, but this connection is not yet established.

## 12. Preliminary conclusion

**Result:** STRUCTURALLY PROMISING / NOT YET ENERGY.

For the first time in this sequence, the minimal model contains all three abstract ingredients of the user's idea:

1. a static structure;
2. a stored internal potential;
3. a transition that can consume or transfer that potential.

The missing step is emergence: the stored quantity must ideally arise from the relational process itself rather than being inserted by definition.

## 13. Next experiment

### E-ENERGY-0022 — Emergent storage

Remove primitive `R`.

Allow only relational operations and history-dependent local rules.

Test whether an internal quantity equivalent to `R` emerges from the accumulated relational history.

Target architecture:

```text
RELATIONAL CHANGE
       ↓
PRESERVED STATE
       ↓
STORED POTENTIAL ?
       ↓
TRANSITION
       ↓
RELEASE / TRANSFER ?
```

This is the next decisive experiment.

## 14. Research log

E-ENERGY-0021 was performed after E-ENERGY-0020 showed that reversible graph barriers alone cannot generate directional expenditure or release.

A single additional internal state was introduced and tested.

The model successfully produced accumulation, holding, consumption, and transfer.

The result is intentionally classified as preliminary because the new resource state was introduced as a primitive. The next experiment must test whether it can emerge from relational history.
