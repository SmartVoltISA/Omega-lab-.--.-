# Ω-Lab — Graph State Snapshot

**Date:** 2026-08-10

The graph is maintained as a research graph, not merely a file index.

## Core relation types

- `contains`
- `tests`
- `supports`
- `contradicts`
- `refines`
- `supersedes`
- `depends_on`
- `requires_retest`

## Direction → hypothesis → experiment structure

```text
DIR-1
  ├── H-MEM-2
  │     └── H-MEM-2.1
  │            └── EXP-Ω-MEM-3
  │                   ├── supports → H-MEM-2.1 (P1/P2/P4)
  │                   ├── contradicts → H-MEM-2.1 (P3 counterexample)
  │                   └── refines → H-MEM-2.2
  │
  └── H-MEM-2.2
         └── EXP-Ω-MEM-4
                ├── supports → capacity effects (exploratory)
                ├── refines → H-MEM-2.2
                ├── requires_retest → H-MEM-2.2
                └── supports candidate → H-MEM-2.3 (OPEN)
                       └── requires_retest → EXP-Ω-MEM-4R
```

## Ω-MEM-4 audit branch

```text
EXP-Ω-MEM-4
  ├── exploratory observations
  │    ├── Periodic-4 threshold at Counter S=4
  │    ├── Thue-Morse parity tracker fails
  │    ├── context representations predict Thue-Morse better
  │    ├── random FSM accuracy increases with S
  │    └── Random-iid remains near baseline
  │
  └── AUDIT_MEM4_2026-08-10
       ├── Context-2 implementation defect
       ├── P3 Matched capacity not swept
       ├── P3 Matched not true position/carry match
       ├── unequal-S Random vs Matched comparison
       ├── intervention inconsistency
       └── missing protocol artifacts
              ↓
         requires_retest → EXP-Ω-MEM-4R
```

## Ω-0 / memory branch

```text
H-0.2
  └── EXP-Ω-0
         └── supports → internal-order reconstruction

H-0.3
  ├── EXP-Ω-0
  └── EXP-Ω-MEM-1a–1d
         └── supports → functional/causal memory in tested architectures

H-0.4
  └── EXP-Ω-MEM-1a–1d
         └── requires_retest → universal minimality claim
```

## Ω-B branch

```text
Ω-B hypothesis
  ├── B1 internal dynamics vs noise
  ├── B2 diffusion-rule control
  │      └── contradicts → naive self-will interpretation
  ├── B3 null model
  ├── B4 fair comparison
  └── B5 spatial shuffle
```

## Ω-C branch

```text
H-Ω-C
  └── critical connectivity
       ├── algebraic connectivity λ2
       ├── spectral gap
       ├── percolation threshold
       └── resilience
```

## Status snapshot

- H-0.1 OPEN
- H-0.2 PARTIALLY_CONFIRMED
- H-0.3 PARTIALLY_CONFIRMED
- H-0.4 NEEDS_RETEST
- H-0.5 REJECTED
- H-0.6 OPEN
- H-0.7 OPEN
- H-MEM-2 PARTIALLY_CONFIRMED
- H-MEM-2.1 REFINED
- H-MEM-2.2 REFINED / NEEDS_RETEST
- H-MEM-2.3 OPEN

## Historical graph rule

A contradiction does not delete an earlier edge. The graph must preserve the path that produced the contradiction. A refined hypothesis is a new node or status transition linked to the experiment that caused refinement.

## Current frontier

`EXP-Ω-MEM-4` is preserved as an exploratory result. The active methodological frontier is now **Ω-MEM-4R**, whose purpose is to test expressive capacity and structural match under equal-capacity, correctly implemented controls.

After Ω-MEM-4R, and only if the representation problem is cleanly characterized, the project can proceed to Ω-MEM-5: adaptive discovery of predictive-state representations.
