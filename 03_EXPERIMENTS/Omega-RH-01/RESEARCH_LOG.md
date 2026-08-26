# Ω-RH-01 — RESEARCH LOG

Public append-oriented working record for the Riemann Hypothesis investigation.

## 2026-08-26 — INIT

### Trigger

The Riemann Hypothesis was introduced as a possible mathematical problem to investigate through the Ω-Lab research process.

### Initial decision

Do not assume that the Ω-Lab Foundation solves RH. First reconstruct RH independently, then test whether a non-superficial mathematical correspondence exists.

### Initial target

`ζ(ρ)=0, 0<Re(ρ)<1  ⇒  Re(ρ)=1/2`

### Initial research architecture

```text
KNOWN MATHEMATICS
       ↓
EXACT RH FORMULATION
       ↓
KNOWN EQUIVALENCES / BARRIERS
       ↓
Ω-FOUNDATION COMPARISON
       ↓
MINIMAL MATHEMATICAL CONSTRUCTION
       ↓
COMPUTATIONAL / SYMBOLIC TESTS
       ↓
FALSIFICATION
       ↓
THEOREM CANDIDATE
       ↓
PROOF ATTEMPT
       ↓
INDEPENDENT AUDIT
```

### Important separation

The Ω-Foundation contains structural ideas such as distinction, relation, state, cycle, memory, prohibition, possibility and choice. Similar language alone is not mathematical evidence. A connection is accepted only when it can be expressed as a precise mathematical statement and checked.

### First external check

Independent public RH research repositories demonstrate that many apparently promising approaches have already encountered precise barriers. One useful model is the explicit preservation of failed approaches and no-go results. This supports using a permanent failure ledger in Ω-RH rather than repeatedly rediscovering dead ends.

### Status

`OPEN — BASELINE / NO CLAIM OF SOLUTION`

## 2026-08-26 — RH-31

### Siche / Krein–Rutman compactness attack

The continuum prime operator in the audited construction is a finite positive sum of truncated translations after the logarithmic change of variables. A finite sum of translations on an interval is not automatically compact merely because the interval is compact.

A stronger analytic obstruction was recorded: choose a sufficiently small interior support whose finitely many translated copies are disjoint, and use normalized oscillatory functions on that support. The sequence is bounded and weakly null, while the translated output retains a uniform positive L² norm. This contradicts the defining compactness property.

### Status

`KREIN–RUTMAN COMPACTNESS GATE: REJECTED FOR THE STATED SHIFT OPERATOR`

This is not an RH counterexample and does not disprove the spectral claim. It only removes the supplied compact-operator justification for simplicity.

### Next action

Find whether the correct spectral object is instead a compact resolvent, compact quadratic-form embedding, or another smoothing transform, and independently attack simplicity without assuming compactness of the prime shift operator.
