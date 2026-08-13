# E-ENERGY-0025 — Matched Memory, Capacity and Different Transition Barriers

**Date:** 2026-08-13  
**Direction:** ENERGY  
**Status:** COMPLETED / PRELIMINARY RESULT  
**Parent:** E-ENERGY-0024  
**Hypothesis:** H-ENERGY-09 — relational potential as a third observable

## 1. Question

Can two states be made equivalent with respect to:

- retained memory statistic;
- number of immediately available transitions;

while still differing in the structural barrier required to reach a target state?

If yes, then memory and transition capacity do not fully specify transition behaviour.

## 2. Construction

Prepare paired states A and B such that:

```text
M(A) = M(B)
T(A) = T(B)
```

but choose different intermediate paths to a common target:

```text
A → a1 → a2 → Target
B → b1 → b2 → Target
```

The paths are constrained to have different minimum bottleneck values.

## 3. Representative result

A matched pair was obtained:

```text
A: M = 2, T = 14, barrier = 10
B: M = 2, T = 14, barrier = 13
```

The immediate state descriptors therefore match on the two previously identified observables, while the path constraint differs.

## 4. What this establishes

The pair demonstrates that:

```text
memory statistic + transition capacity
```

is insufficient to determine the complete transition structure.

A third descriptor — path/barrier structure — is required for this model class.

## 5. Does the third descriptor equal energy?

No.

The barrier is a property of a selected transition path. It does not automatically define a conserved quantity, and it does not by itself transfer between subsystems.

Therefore:

```text
barrier ≠ energy
```

remains an explicit rule.

## 6. New observation

The system now naturally separates into:

```text
MEMORY
  = what history is retained

CAPACITY
  = how many next changes are available

BARRIER
  = how constrained a chosen change can become
```

A possible energy-like quantity would have to be a relation among these, or an additional invariant not reducible to any one of them.

## 7. Transfer implication

The next decisive test is no longer to find another local descriptor.

It is to ask whether the barrier/potential difference can be converted into a transferable quantity during a coupled transition.

Target:

```text
A_high potential + B_low potential
              ↓
          coupled change
              ↓
A_low potential + B_high potential
```

while preserving a total without explicitly imposing conservation.

## 8. Strong falsification path

If every observed transfer can be fully predicted from the graph transition rules and no additional conserved quantity is needed, the separate-energy hypothesis is weakened.

If a stable conserved quantity emerges from the coupled dynamics and is independent of the chosen representation of memory and barrier, the hypothesis gains substantial support.

## 9. Preliminary conclusion

**Result:** MATCHED STATES WITH DIFFERENT PATH BARRIERS FOUND.

This is another successful separation experiment.

It demonstrates that the current graph state cannot be summarized completely by memory content and immediate transition capacity.

It still does not establish an energy quantity.

## 10. Next experiment

### E-ENERGY-0026 — Coupled potential transfer

Build two matched subsystems with different target-path barriers and search for a coupled dynamics in which a measurable candidate quantity moves from one subsystem to the other while the combined quantity remains invariant.

The conservation must emerge from the coupled rules rather than being hard-coded as a balancing operation.

## 11. Research log

E-ENERGY-0025 followed E-ENERGY-0024 and successfully produced matched states on memory and immediate transition capacity while preserving a difference in path barriers.

This further narrows the search for an independent energetic observable.
