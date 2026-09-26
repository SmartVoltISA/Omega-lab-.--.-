# EVIDENCE LEDGER v0.1
Date: 2026-09-27
Parent: EVIDENCE_CLOSURE_AUDIT_v0.2

Legend: A=strong validated/reproduced; B=executed with restricted scope; C=preliminary/incomplete provenance; D=source/protocol only; E=rejected/invalidated/superseded; U=unresolved provenance.

## A — strong evidence

| ID | Protocol/Run | Result | Control/Audit | Replication | Status | Claim allowed |
|---|---|---|---|---|---|---|
| Ω-EMO-001A-R1 | archived protocol + exact code | RESULTS.md | independent NumPy recomputation | exact same input/code twice | A / VALIDATED | CIE 1931 XYZ representation has tested rank-3 requirement; centered chromaticity rank 2 |
| Ω-BASIS-002-R2 | protocol commit 6d2936… + run_r2.py | RESULTS.md | audit 2026-08-13 | independent numerical rerun | A/B / REPRODUCED CORE | numerical regime-information effect in declared model class; not ontology of time |

## B — execution-backed, restricted claims

| ID/family | Evidence | Status | Allowed claim |
|---|---|---|---|
| Ω-INF-3 | 100-run reconstruction/compression | B | tested reconstruction can alter compression relative to original |
| Ω-INF-4 | 100-run trigram reconstruction | B | same, for tested trigram family |
| Ω-INF-5 | independent corpora | B | effect is corpus-dependent |
| Ω-INF-6 | sampling-policy control | B | sampling policy is a relevant control variable |
| Ω-INF-7 | robustness test | B | reported robustness only within tested setup |
| Ω-INF-8 | deliberate falsification/break test | B | universal compression claim not established |
| Ω-MEM-4R | corrected protocol/execution record | B | corrected matched-context comparison within declared processes |
| Ω-TEST-1 | analytic/geometric execution | B | declared geometric property verified |
| Ω-TEST-2 | analytic + numerical execution | B | declared geometric property verified numerically |
| Ω-TEST-3 | numerical exploratory | B | model-scoped observation |
| Ω-TEST-4 | interaction test | B | model-scoped interaction observation |
| Ω-TEST-5 | corrected numerical stability run | B | corrected model-scoped observation |
| Ω-TEST-7 | corrected 180-dataset blind rerun | B | corrected blind result; first run invalid |
| Ω-TEST-9 | matched-marginal counterfactual | B | counterfactual result in tested setup |
| Ω-TEST-10 | completed metric test | B/E | metric did not validate as intended |
| Ω-TEST-11 | counterfactual | B | exploratory counterfactual result |
| Ω-TEST-12 | cross-family falsification | B | exploratory falsification result |
| PHYS-ELECTRON-002 | relation-level test | B | declared relation structure in tested data |
| PHYS-ELECTRON-002A | verification | B | verification of 002 |
| PHYS-ELECTRON-004 | corrected blinded held-out relations | B | corrected relation-only clustering result |
| PHYS-ELECTRON-005 | masked holdout pilot | B/E | negative control/pilot result |
| CICADA C1-002 | exact grid transformation | B | structural transformation; interpretation unresolved |
| CICADA C1-015 | state-invariant audit | B | declared invariant observation |
| CICADA C1-016 | execution/result | B | declared structural observation |
| CICADA C1-017 | matrix-type invariants | B | declared invariant observation |
| CICADA C1-018 | Fibonacci spiral invariant | B | declared positional structure |
| CICADA C1-019 | M3 Fibonacci/spiral control | B | strong/reproduced positional structure; endpoint unknown |
| E-ENERGY-0034 | hysteresis state-color model | B | history dependence can be encoded by state |
| E-ENERGY-0036 | negative three-state emergence control | B/E | simple scalar memory did not produce 3 stable attractors |
| E-ENERGY-0037 | symmetric bifurcation control | B | symmetric instability can produce two complementary populations |
| E-ENERGY-0032R | independent replication attempt | E | original 0032 exact numbers remain unverified |
| E-MAGNETIC-0001A | magnet/coil control model | D/C | model/protocol only; no physical validation |
| E-MAGNETIC-0001B | environmental/lightning analog | C | exploratory engineering mechanism only |

## E — failed, invalidated or superseded

| ID | Status | Correct handling |
|---|---|---|
| Ω-BASIS-002 original | E / REJECTED | retain failure; do not use result |
| Ω-MEM-4 | E / NOT VALIDATED | methodological defects block validation |
| Ω-TEST-7 first run | E / INVALIDATED | attach to corrected TEST-7 lineage |
| Ω-REL-018 first metric result | E / INVALIDATED | corrected run is separate accepted lineage |
| PHYS-ELECTRON-003 | E / SUPERSEDED | corrected 004 controls affected interpretation |
| E-ENERGY-0032 numerical values | U | exact provenance not independently verified |

## C — research lines

| Line | Status | Rule |
|---|---|---|
| Ω-RH-01…64 | C/U | one attack/audit lineage; no RH proof |
| D/R/W/P | C/U | neutral-machine observations do not prove primitive basis or D+R superiority |
| early Ω-REL | C/U | 18 semantic blocks; historical provenance incomplete for some records |
| REL-066…073 | B/C | separate blind/black-box line; claim scope remains record-specific |
| Ω-ENERGY | C/U | branch hypothesis remains open; individual controls/results retain own status |
| ORISIK registry | D/C/U | registry membership never substitutes for execution evidence |

## D — source/protocol only or planned

- E-ENERGY-0001…0005: planned/blocked; not executed.
- ORISIK source-only mapped objects: not promoted without execution evidence.
- Architecture/application specifications: not experiments.
- Repository copies and history files: provenance only.

## 146-object closure rule

The 146-object master registry remains the denominator.
For objects not explicitly resolved above, the ledger status is `U — PROVENANCE CLOSURE REQUIRED`, never an inferred execution status.
This preserves the distinction between 'not proven' and 'false'.

## Claim gate

CLAIM_ALLOWED = function(STATUS, CONTROL, REPLICATION, PROVENANCE)

A claim can only be promoted when the evidence chain supports it. Family-level or ontological claims are never promoted from a single local result.

## Closure decision

The ledger is now the controlling evidence index. The remaining unresolved entries are explicitly marked rather than silently upgraded.