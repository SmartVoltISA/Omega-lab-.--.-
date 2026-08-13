# Ω REL-011/012 — Memory as Boundary

Date: 2026-08-13
Status: EXPERIMENTAL RESULT / MODEL-SCOPED

## Question

Can memory be operationally identified with a boundary on future transitions?

The target is not a claim about conventional computer memory. The Ω hypothesis under test is narrower:

> A retained result becomes memory, in the operational sense relevant to Ω, when it changes the set of future transitions that remain available.

## REL-011 — first hard-boundary attempt

A first implementation made the previous winner the only allowed next state. This produced near-total locking and therefore was degenerate: the boundary itself forced the result. It was useful as a failure/control of model design, but not as a clean test of the hypothesis.

REL-011 results were therefore NOT used as confirmation.

## REL-012 — non-degenerate transition test

Models:

- M0 — no memory; all 9 non-self transitions remain available.
- M1 — memory is stored but does not affect transition availability (control).
- M2 — memory creates a temporary boundary: every used directed transition i→j is forbidden for K=5 subsequent steps.

Conditions:

- N = 10 states;
- 200 runs;
- 600 steps per run;
- same initial state, external score stream and random draw stream within each comparison;
- no self-transition;
- boundary intervention: M2 boundary OFF for the middle third, then ON again.

## Results

M0:

- mean available transitions = 9.0000 ± 0.0000
- state changes = 600.00 ± 0.00
- unique states = 10.00 ± 0.00

M1 (memory stored, no prohibition):

- mean available transitions = 9.0000 ± 0.0000
- state changes = 600.00 ± 0.00
- unique states = 10.00 ± 0.00

M2 (memory as boundary):

- mean available transitions = 8.7181 ± 0.0154
- state changes = 600.00 ± 0.00
- unique states = 10.00 ± 0.00

Intervention on M2:

- boundary ON before removal: 8.7202 ± 0.0273 available transitions;
- boundary OFF: 9.0000 ± 0.0000;
- boundary ON after restoration: 8.7181 ± 0.0286.

## Direct observation

The stored record by itself did nothing (M1 = M0).

When the stored record was used as a prohibition on future transitions, the accessible transition space became smaller (M2 < M0).

When the prohibition was removed, the accessible transition space returned to the unrestricted value.

When the prohibition was restored, the restriction returned.

This is a direct intervention result, not merely a correlation.

## What survived the attempt to break

The simplest non-degenerate implementation supports the following model-scoped statement:

> In this Ω transition model, memory has no behavioral effect merely by existing as stored information; it becomes causally relevant when the stored result acts as a boundary on future transitions.

Therefore the operational Ω relation

`memory → boundary on future possibilities`

survived the direct removal/reinstatement test.

## What did NOT survive / what remains open

We cannot yet claim the universal identity `memory = prohibition` for every possible system.

A stored record that does not affect transitions is a counterexample to the broader statement that every form of memory is automatically a prohibition. This means the Ω definition must remain operational rather than linguistic:

> Memory, in the Ω sense under test, is a retained difference that changes the future transition space.

The next stronger test should vary N, K, initial conditions and transition topology, and test whether the same relation survives without relying on the particular implementation used here.

## Status decision

This is strong enough to use `memory-as-boundary` as a WORKING Ω PRINCIPLE for subsequent experiments, but not yet as a universal law.

If later experiments produce a reproducible memory effect without any change in future transition space, this principle must be revised.

## Honesty rule

Execution verified for REL-011 and REL-012.

REL-011 was rejected as a degenerate implementation.
REL-012 produced the positive controlled result described above.

No claim is made beyond the tested model.
