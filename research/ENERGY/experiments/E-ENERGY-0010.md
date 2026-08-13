# E-ENERGY-0010 — Structural Potential

**Date:** 2026-08-13  
**Status:** COMPLETED — TOY MODEL / FIRST PASS  
**Parent:** H-ENERGY-04 — Structural potential hypothesis

## 1. Question

Can a static relational structure possess a measurable difference in its **capacity for future transformation**, before any transformation occurs?

This is the first direct test of the new "accumulator" intuition.

Important: the experiment does **not** assume that this capacity is physical energy.

---

## 2. Minimal model

Five identical nodes are used.

Each structure contains four undirected relations (edges), so the number of elements and the number of relations are held constant.

Three structurally different trees are compared:

```text
PATH
0—1—2—3—4

STAR
  1
  |
2—0—3
  |
  4

BRANCHED TREE
  3
  |
1—0—2
|
4
```

The exact labels are irrelevant; only topology matters.

No variable named energy is present in the primitive state.

---

## 3. Local transformation rule

One elementary transformation is defined as:

1. remove one existing relation;
2. add one absent relation;
3. reject the transformation if the resulting graph becomes disconnected;
4. reject the transformation if any node exceeds degree 3.

This is deliberately an artificial rule. It is a laboratory control, not a claim about physical dynamics.

---

## 4. Candidate structural-potential observable

Define:

> **P(S) = number of legal one-step transformations available from structure S.**

This quantity measures the structure's immediate **transformation capacity**.

It is NOT yet called energy.

The hypothesis predicts that different configurations can have different P values even while the system is static.

---

## 5. Result

Computed first-pass values:

| Structure | P(S): legal one-step transformations |
|---|---:|
| Path | 17 |
| Star | 12 |
| Branched tree | 14 |

All three systems have:

- 5 identical nodes;
- 4 relations;
- no motion;
- no primitive energy variable.

Yet the number of permitted future transformations differs.

---

## 6. Release / transition check

For each starting structure, one legal transformation was performed and P(S') was recalculated.

Observed ranges:

| Initial structure | Initial P | P after one legal change |
|---|---:|---:|
| Path | 17 | 14–17 |
| Star | 12 | 14 |
| Branched tree | 14 | 14–17 |

Thus a structural transition can change the measured transformation capacity.

---

## 7. Observation

The experiment demonstrates, within this toy rule system:

> A static relational configuration can carry a measurable difference in its capacity for future change.

The quantity is determined by the structure and the allowed transformation rules, not by current motion.

This is the first concrete support for the weaker form of the structural-potential hypothesis.

---

## 8. What the experiment does NOT demonstrate

It does NOT demonstrate that P(S) is physical energy.

P(S) is dependent on the chosen rewrite rules. A different rule set can produce a different P.

Therefore:

```text
structural potential ≠ demonstrated physical energy
```

and:

```text
P(S) ≠ automatically energy
```

This distinction is mandatory.

---

## 9. Important result for the original hypothesis

The original formulation was:

> Energy is a consequence of a change in relation in space.

The experiment suggests a possible refinement:

> A relational structure can possess a measurable **potential for change before the change occurs**.

If this survives more rigorous models, energy may need to be treated not simply as a product of change but as a quantity associated with the configuration's relation to its possible transformations.

This remains OPEN.

---

## 10. Falsification status

### Supported

- Structural configuration can affect future transformation capacity in the toy model.
- The difference exists while the structure is static.
- A transformation can alter that capacity.

### Not supported / not tested

- Physical energy has been derived.
- Conservation of P has been demonstrated.
- P is independent of the chosen rewrite rules.
- P corresponds quantitatively to work or energy transfer.
- Space itself is necessary.

### Next decisive tests

1. Find a rule-independent candidate or identify the invariance class under changes of representation.
2. Test whether a candidate quantity behaves additively under composition of independent subsystems.
3. Test whether a transition redistributes a conserved total rather than merely changing an arbitrary graph statistic.
4. Compare reversible and irreversible transformations.
5. Only then compare with classical potential energy.

---

## 11. Interpretation

The strongest outcome of E-ENERGY-0010 is not "we found energy".

It is:

> **The idea of a stored structural potential is computationally coherent: a static structure can differ in its capacity for future change.**

That is a legitimate new experimental foothold.

---

## 12. Next experiment

**E-ENERGY-0011 — Release test**

The next question is stronger:

> When structural potential changes, can the difference be represented as a quantity transferred into another component while preserving a total invariant?

If not, the current quantity is merely a measure of graph flexibility and should not be promoted toward energy.

**Status:** NEXT.
