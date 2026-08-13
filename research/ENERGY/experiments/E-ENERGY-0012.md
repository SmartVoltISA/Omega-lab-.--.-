# E-ENERGY-0012 — Binding / Destruction Symmetry

**Date:** 2026-08-13  
**Status:** COMPLETED / FALSIFICATION PRESSURE  
**Parent hypothesis:** H-ENERGY-04 — structural potential

## 1. Question

Does creating a relation and destroying a relation produce a consistent energetic-like asymmetry in the minimal relational model?

Target intuition:

```text
A + B → A—B
```

may require an input, while

```text
A—B → A + B
```

may release something.

The model must determine whether such a distinction emerges structurally rather than being programmed.

## 2. Model

Use four labeled nodes and a common local relation graph.

Two initial subsystems:

```text
0—1     2—3
```

A binding transition adds a cross-relation:

```text
0—1     2—3
  \     /
   1—2
```

The structural observable is the same transition-capacity score used in the preceding experiments.

No energy variable is introduced.

## 3. Structural result

For the disconnected two-pair configuration, the number of single-edge toggles available under the degree constraint is **6**.

For the bound three-edge configuration, the number is also **6** when disconnected intermediate states are allowed.

Therefore the raw toggle-count observable does **not** distinguish binding from destruction by itself.

Under the additional constraint that the system must remain connected at every step, the bound state becomes locally constrained: removing its bridge would disconnect the system. The apparent asymmetry then comes from the connectivity constraint, not from an independently emerging energy quantity.

## 4. Reverse process

The binding operation is directly reversible as a graph edit if disconnected states are permitted:

```text
(0—1, 2—3) → add (1,2) → (0—1, 2—3, 1—2)
```

and:

```text
(0—1, 2—3, 1—2) → remove (1,2) → (0—1, 2—3)
```

No intrinsic directionality appears.

This is an important negative result.

## 5. Interpretation

The simple relation graph does **not** spontaneously produce the expected statement:

> binding requires energy / destruction releases energy.

Instead, the directionality appears only after additional constraints are imposed.

This means that **structural potential alone is insufficient to derive energetic directionality in this model class.**

## 6. Falsification result

H-ENERGY-04 is **not falsified completely**, because the hypothesis was broader than this specific graph score.

However, the following stronger version is rejected for the tested model:

> "The number of accessible relational changes by itself determines an energy-like cost of binding or release."

That formulation does not survive the symmetry test.

## 7. What this tells us

There are at least three distinct ingredients that may need to be separated:

```text
STRUCTURE
   ↓
AVAILABLE TRANSITIONS
```

is one thing.

```text
TRANSITION
   ↓
DIRECTION / COST
```

is another.

And:

```text
COST / RELEASE
   ↓
CONSERVATION / TRANSFER
```

is a third.

The first experiment demonstrated structural potential-like variation.

The second demonstrated conditional redistribution.

This experiment shows that neither is sufficient by itself to generate physical energetic asymmetry.

## 8. New hypothesis generated

### H-ENERGY-05 — Structure + transition rule

A possible energy-like quantity may require not only the structure but also a **non-symmetric transition rule** or an additional state variable that distinguishes accessible change from the cost of change.

Candidate architecture:

```text
STRUCTURE
   ↓
POTENTIAL
   ↓
TRANSITION RULE
   ↓
COST / RELEASE
   ↓
TRANSFER
```

This is an open hypothesis, not a conclusion.

## 9. Important methodological result

This experiment demonstrates why Ω-Lab must test reverse processes.

A forward-only experiment could have produced an attractive narrative about "stored energy". The reverse test shows that the minimal relation model itself is symmetric unless additional structure is supplied.

That negative result is valuable and must be preserved.

## 10. Next experiment

The next step should not immediately add classical energy equations.

Instead test whether a **state-dependent relation weight** or **history-dependent structural state** can produce a genuine cost/release asymmetry while remaining minimal.

Candidate next experiment:

`E-ENERGY-0014 — Transition Cost from State`.

Question:

> Can a cost-like quantity emerge from the difference between two structural states and their allowed transition paths, rather than from an arbitrary assigned edge weight?

## 11. Preliminary conclusion

**Result:** NEGATIVE for the simplest model; PRODUCTIVE for the research direction.

The current evidence supports:

> Structure can constrain possible change.

It does not yet support:

> Structure alone determines energetic cost or release.

The missing ingredient may be the **transition relation itself** — how one structure becomes another — rather than structure alone.
