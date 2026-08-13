# E-ENERGY-0013 — Transition Asymmetry / No-Go Test

**Date:** 2026-08-13  
**Direction:** ENERGY  
**Status:** COMPLETED / NEGATIVE RESULT  
**Parent:** E-ENERGY-0012  
**Hypothesis:** H-ENERGY-05 — energetic behaviour may arise from the relation between state and transition

## 1. Question

Can a direction-dependent transition cost emerge from structure alone when the underlying relation rule is symmetric and reversible?

Target:

```text
S1 → S2  : cost ?
S2 → S1  : cost ?
```

The desired energetic interpretation would require a principled difference between the two directions, without manually assigning a direction-dependent cost.

## 2. Minimal model

Use finite relation graphs with:

- identical node set;
- identical edge set size;
- connectivity constraint;
- maximum degree constraint;
- reversible local rewiring rule.

A transition is represented by a sequence of elementary rewrites.

A natural structural transition measure is the minimum number of elementary rewrites required to reach the target configuration.

## 3. Result

Under a reversible rule set, the shortest-path distance between two configurations is symmetric:

```text
D(S1,S2) = D(S2,S1)
```

For every tested pair, reversing the sequence of rewrites gives a path of identical length in the opposite direction.

Therefore no intrinsic directional "cost" appears from the static relational structure alone under symmetric reversible rules.

## 4. Strong negative result

This gives a useful boundary condition:

> **A purely relational graph plus symmetric reversible transformations does not by itself generate directional energetic asymmetry.**

If we want:

```text
S1 → S2  ≠  S2 → S1
```

then an additional asymmetry must enter the model.

Possible sources are deliberately left open:

1. state-dependent constraints;
2. an environment / external subsystem;
3. irreversible transition rules;
4. hidden internal states;
5. a directional ordering variable;
6. a non-symmetric relation between configurations.

None is accepted yet.

## 5. Consequence for H-ENERGY-05

H-ENERGY-05 in its strongest form is weakened:

> Structure + symmetric reversible transition rule is insufficient to produce directional transition cost.

This does **not** reject the broader energy hypothesis.

It tells us that if energy has a directional "release / expenditure" character, that character cannot come solely from an undirected static relation graph with reversible rules.

## 6. Important connection to the accumulator idea

The accumulator analogy now becomes more precise.

A static structure may encode a space of possible transitions, but an accumulator-like interpretation requires more than possibility count.

It requires something like:

```text
STATE
  ↓
AVAILABLE TRANSITIONS
  ↓
CONSTRAINT / BARRIER
  ↓
TRANSITION
```

The missing candidate is therefore not simply "how many changes are possible", but possibly **how the present state constrains the path to a future state**.

This suggests a new research target:

> **transition barrier / path structure**

rather than raw transition count.

## 7. New hypothesis generated

### H-ENERGY-06 — Transition-barrier hypothesis

A structure may possess an energetic potential not merely because it has possible future states, but because reaching those states requires crossing a structural barrier represented by intermediate configurations.

Conceptual form:

```text
S_low
  │
  │ barrier
  ↓
S_high
```

or:

```text
stored structural state
        ↓
required intermediate states
        ↓
transition
```

This is OPEN and unconfirmed.

## 8. Why this matters

The hypothesis now separates three quantities that were previously mixed:

### Capacity

How many transformations are available?

### Barrier

How difficult is it to reach a particular transformation under the model's constraints?

### Release

Does crossing the transition change a conserved quantity shared between subsystems?

The Ω-Lab ENERGY branch should not collapse these into one number prematurely.

## 9. Next experiment

### E-ENERGY-0020 — Barrier / constrained transition

Introduce the smallest possible **state-dependent structural constraint** while keeping the rule itself explicit and identical across experiments.

Test whether:

```text
S1 → S2
```

requires traversing a higher structural barrier than:

```text
S2 → S1
```

and whether the difference is transferable/conservable when two subsystems interact.

The constraint must not be called "energy" or "work".

## 10. Preliminary conclusion

**Negative result, high value.**

The experiment rules out a tempting but overly simple route:

> energy-like directional behaviour does not emerge automatically from an undirected relation graph plus reversible local rewrites.

The research direction is therefore narrowed toward:

```text
RELATION
   ↓
STRUCTURE
   ↓
CONSTRAINT
   ↓
TRANSITION BARRIER
   ↓
RELEASE / TRANSFER ?
```

This is the next clean experimental target.
