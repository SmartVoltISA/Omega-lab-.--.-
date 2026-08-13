# E-ENERGY-0029 — Directionality from State Ordering

**Date:** 2026-08-13  
**Direction:** ENERGY  
**Status:** COMPLETED / CRITICAL NEGATIVE RESULT  
**Parent:** E-ENERGY-0028

## 1. Question

Can a minimal ordering of states generate a preferred direction of transition — a computational analogue of release — without introducing energy or an explicit arrow of time?

Target:

```text
high state → low state
```

while the reverse requires an additional condition.

## 2. Minimal ordered model

Use a binary local state:

```text
x ∈ {0,1}
```

with an externally declared order:

```text
0 < 1
```

The conserved quantity remains:

```text
Q = A + B
```

The question is whether the ordering itself can determine which transition occurs.

## 3. Test A — reversible dynamics

Allow both transitions:

```text
1 → 0
0 → 1
```

The ordering exists, but the dynamics remain symmetric.

Result:

> An ordering relation by itself does not generate directionality.

## 4. Test B — descending-only local rule

Allow:

```text
1 → 0
```

but forbid:

```text
0 → 1
```

Now a preferred direction appears.

However, the direction was explicitly inserted into the transition rule.

Therefore this is not an emergent result.

## 5. Test C — reversible global state-space dynamics

Require the complete closed system to have reversible transitions while attempting to recover an effective local preference for descending transitions.

A purely reversible finite-state system cannot produce a genuine one-way loss of accessible states without storing the missing information/state somewhere else.

If the apparent direction is present locally, the full system must contain a compensating degree of freedom.

## 6. Major result

The experiment establishes an important constraint:

> **State ordering is not sufficient to generate energetic release.**

A preferred direction must arise from either:

- an explicitly directional rule;
- an additional state/resource that records the transition;
- coupling to an environment/reservoir;
- coarse-graining that hides compensating degrees of freedom;
- or another mechanism not yet represented in the model.

## 7. Consequence for the accumulator hypothesis

The desired architecture:

```text
stored potential
      ↓
release
      ↓
lower state
```

cannot be obtained from conservation + barrier + state ordering alone.

Something must distinguish the complete system from the local subsystem in which release is observed.

## 8. New important distinction: closed vs open system

This creates a possible fundamental split.

### Closed description

The full state transition remains reversible and information-preserving.

### Local/open description

A subsystem can appear to release or dissipate a stored quantity because another part of the system absorbs the compensating state.

Conceptual form:

```text
SUBSYSTEM A
high → low
    ↓
release
    ↓
ENVIRONMENT / SUBSYSTEM B
low → high / absorbs change
```

This is not yet a physical thermodynamic derivation. It is a structural possibility that must now be tested.

## 9. New hypothesis

### H-ENERGY-10 — Apparent release as redistribution in a larger closed system

> What appears locally as energy release may be a redistribution of a conserved structural quantity into degrees of freedom outside the observed subsystem.

**Status:** OPEN / TESTABLE.

This hypothesis is deliberately compatible with the accumulator intuition while avoiding an unexplained one-way rule.

## 10. Next experiment

### E-ENERGY-0030 — Reservoir / Hidden-Degree Transfer

Build the smallest closed system containing:

```text
A = observed subsystem
B = reservoir
```

Search for dynamics where:

```text
A: high → low
B: low → higher
```

while:

```text
Q_total = constant
```

and the full transition remains reversible.

The decisive question is whether **local release and global conservation can coexist without a directional primitive**.

## 11. Preliminary conclusion

**Result:** STATE ORDERING ALONE FAILS TO GENERATE RELEASE DIRECTION.

This is a critical negative result.

The research now has a strong constraint:

> **A closed reversible system cannot simply lose a locally stored quantity without the corresponding state appearing elsewhere.**

This moves the ENERGY investigation toward the relation between local release, global conservation, and hidden/environmental degrees of freedom.

## 12. Research log

E-ENERGY-0029 followed E-ENERGY-0028, where conservation and barrier were successfully combined but remained directionally symmetric.

State ordering was tested as the smallest possible source of directionality.

The result shows that ordering alone is insufficient. Directionality must either be encoded, emerge from additional state, or arise from a local description of a larger closed system.
