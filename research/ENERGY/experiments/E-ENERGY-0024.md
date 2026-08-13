# E-ENERGY-0024 — Memory vs Transition Potential Discrimination

**Date:** 2026-08-13  
**Direction:** ENERGY  
**Status:** COMPLETED / PRELIMINARY RESULT  
**Parent:** E-ENERGY-0023  
**Hypothesis:** H-ENERGY-08 — dual-role conserved state

## 1. Question

Can the stored state produced by relational history be distinguished from memory/information itself?

The test deliberately separates:

```text
WHAT THE SYSTEM REMEMBERS
```

from

```text
WHAT THE SYSTEM CAN DO NEXT
```

If these can vary independently, a distinct energy-like variable may be possible.

## 2. Minimal construction

Four history classes are prepared:

- H1: same history length, different content;
- H2: different history length, same compressed memory statistic;
- H3: same current graph, different historical constraints;
- H4: different current graph, matched transition capacity.

For each state we measure two independent observables:

`M` = retained history information under the chosen encoding.

`T` = number/structure of admissible future transitions.

Neither `M` nor `T` is called energy.

## 3. Result A — same memory statistic, different transition capacity

Two states can have the same coarse memory statistic `M` while having different transition sets.

Representative pattern:

```text
State A: M = 2, T = 17
State B: M = 2, T = 12
```

Thus the chosen memory statistic is insufficient to determine future transition capacity.

This is a useful separation result, but it does not prove that the difference is energy.

## 4. Result B — different memory histories, same transition capacity

Different histories can produce states with the same transition capacity:

```text
State C: M = 3, T = 14
State D: M = 5, T = 14
```

Therefore transition capacity is not equivalent to the selected memory statistic.

## 5. Result C — no unique scalar yet

Although `M` and `T` can vary independently under the chosen encoding, neither is a universal conserved scalar.

Different configurations can share the same `T` while having different transition-path structures.

Therefore the experiment does not yet isolate a unique energy-like quantity.

## 6. Major result

The experiment successfully breaks the simplest identification:

```text
stored state = memory statistic = transition potential
```

At least under the tested encoding, these are not identical observables.

This is important because the previous E-ENERGY-0023 result could otherwise have been dismissed entirely as memory bookkeeping.

## 7. What remains unresolved

There are now at least three distinct layers:

```text
MEMORY
  ↓
what previous changes can be reconstructed

TRANSITION CAPACITY
  ↓
what changes are currently accessible

TRANSITION BARRIER / PATH
  ↓
what constraints are encountered while changing
```

The missing quantity, if one exists, would have to connect these layers without being reducible to any one of them.

## 8. New hypothesis

### H-ENERGY-09 — Relational potential as a third observable

> A distinct potential-like quantity may be associated with the relation between stored state, current structure, and allowed transitions, rather than with memory or transition capacity alone.

**Status:** OPEN / SPECULATIVE.

## 9. Decisive next experiment

Construct states that are matched in:

- memory content;
- current transition capacity;

but differ in the **minimum transition barrier** required to reach a target state.

Then test whether a third quantity emerges that predicts the difference.

This is the next controlled separation:

```text
same memory
same capacity
different barrier
       ↓
? potential
```

## 10. Falsification

If barrier, capacity, and memory together fully determine all observed transition behaviour, no independent energy-like scalar is required by this model.

If a stable additional quantity is required to predict transfer/release across the controlled cases, the energy hypothesis gains support.

## 11. Preliminary conclusion

**Result:** MEMORY AND TRANSITION CAPACITY ARE NOT IDENTICAL; ENERGY STILL UNCONFIRMED.

The experiment has narrowed the problem.

We no longer ask whether stored history exists — it does in the model.

We ask whether there is an additional invariant or potential associated with the **relationship between history, structure, and transition path**.

## 12. Research log

E-ENERGY-0024 was designed as a deliberate anti-confirmation test after E-ENERGY-0023.

The result rejects the simplest claim that the observed stored state is equivalent to a single coarse memory statistic or transition capacity.

The next experiment will hold memory and capacity fixed while varying transition barriers.
