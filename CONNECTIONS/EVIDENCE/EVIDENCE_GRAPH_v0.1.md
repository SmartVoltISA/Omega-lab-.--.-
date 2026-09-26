# EVIDENCE GRAPH v0.1 — Ω-LAB / ORISIK

Date: 2026-09-27
Parent registry: CONNECTIONS/INVENTORY/MASTER_EXPERIMENT_REGISTRY_v0.4.md

## 1. Evidence contract

Canonical chain:

FAMILY → EXPERIMENT → RUN → RESULT → AUDIT/CONTROL → REPLICATION → STATUS

Method gate:

PLANNED → CODED → EXECUTED → VALIDATED → REPRODUCED
Negative states: REJECTED / INVALIDATED.

Only EXECUTED results are experimental results. Only VALIDATED or REPRODUCED results are strong evidence for later conclusions.

## 2. High-confidence evidence anchors

| Family / block | Evidence state | What is actually supported |
|---|---|---|
| Ω-EMO-001A-R1 | VALIDATED | Tested CIE 1931 representation/control; independent numerical check agrees. No universal color ontology claim. |
| Ω-BASIS-002-R2 | REPRODUCED (numerical core) | Independent rerun reproduced numerical core; provenance/CI closure incomplete, so not foundation-level proof. |
| Ω-MEM-4 | NOT VALIDATED | Execution produced observations, but preregistered implementation defects prevent validation. |
| Ω-MEM-4R | EXECUTED / corrected replication | Corrected protocol executed; reported comparison is retained, but not treated as independently rerun beyond its recorded provenance. |
| Ω-INF-3 | EXECUTED / PARTIAL SUPPORT | 100-run reconstruction/compression test; effect is limited to tested reconstruction family. |
| Ω-INF-4 | EXECUTED / PARTIAL SUPPORT | 100-run trigram reconstruction; effect remains limited to tested setup. |
| Ω-INF-5 | EXECUTED / CORPUS-DEPENDENT | Effect changes sign/magnitude by corpus; no universal compression claim. |
| Ω-INF-8 | EXECUTED / FALSIFICATION | Deliberate break/control execution exists; supports corpus/policy dependence rather than a universal rule. |
| Ω-TEST-1 | EXECUTED | Reproducible analytic/geometric check. |
| Ω-TEST-2 | EXECUTED | Analytic + numerical geometric check. |
| Ω-TEST-3 | EXECUTED / EXPLORATORY | Numerical test only within its declared model. |
| Ω-TEST-4 | EXECUTED / EXPLORATORY | Numerical interaction test within declared model. |
| Ω-TEST-5 | EXECUTED after correction | Stability correction preserved; corrected lineage is accepted, prior defect not silently erased. |
| Ω-TEST-7 | EXECUTED / corrected blind rerun | First non-finite run invalidated; corrected 180-dataset blind rerun is the accepted lineage. |
| Ω-TEST-9 | EXECUTED | Matched-marginal counterfactual. |
| Ω-TEST-10 | EXECUTED / failed metric validation | Completed, but not accepted as a validated effect metric. |
| Ω-TEST-11 | EXECUTED / EXPLORATORY | Counterfactual test. |
| Ω-TEST-12 | EXECUTED / EXPLORATORY | Cross-family falsification test. |
| PHYS-ELECTRON-004 | EXECUTED / corrected | Corrected blinded held-out relations supersede affected interpretation of 003. |
| PHYS-ELECTRON-005 | EXECUTED / NEGATIVE pilot | Retrospective masked holdout pilot; negative/control result. |
| CICADA C1-002 | STRUCTURAL RESULT | Structural transformation established in its declared sense; interpretive meaning remains unknown. |
| Ω-RH | RESEARCH / AUDIT LINE | Multiple attacks/audits; no proof of RH and no counterexample established. |
| D/R/W/P foundation | EXECUTED / UNKNOWN | Neutral-machine observations pass local execution audit; minimal primitive mapping and D+R > W+P remain unproven. |
| E-ENERGY-0032R | REPLICATION CHECK / NEGATIVE | Exact numerical reproduction failed; therefore 0032 is not treated as reproduced. |
| E-ENERGY-0034 | COMPLETED / STRUCTURAL RESULT | Toy-model structural result only. |
| E-ENERGY-0036 | COMPLETED / NEGATIVE CONTROL | Negative control for color-free three-state emergence. |
| E-ENERGY-0037 | CONTROL / SYMMETRIC BIFURCATION | Symmetric toy-model control; not physical validation. |
| E-MAGNETIC-0001A | EXPERIMENT / CONTROL MODEL | Protocol/model object; validation still pending. |
| E-MAGNETIC-0001B | EXPLORATORY ENGINEERING | Environmental/lightning analog object; not evidence of real lightning-energy capture. |
| ORISIK EXP-0013…0018 | MIXED | Source/protocol/execution objects with different completion levels; each requires its own evidence chain. |
| ORISIK CL-SCALING-001 | PROTOCOL / EXECUTION PENDING in registry | Do not promote from registry name alone; primary execution artifacts must be reconciled before status upgrade. |
| ORISIK RELATIONAL-MEMORY-TEMPORAL-ORDER-001 | EXECUTED | Temporal-order PASS and mechanism-off null PASS; foundation promotion remains blocked. |

## 3. Explicit negative / rejected evidence

The following are retained as evidence of failure, not deleted:

- Ω-BASIS-002 original failed execution: REJECTED / no scientific result claim.
- Ω-MEM-4: methodological defects prevent validation.
- Ω-TEST-7 first run: non-finite output; invalidated before corrected blind rerun.
- REL-018 first metric-direction result: INVALID; corrected analysis retained separately.
- E-ENERGY-0032R: negative exact-numerical reproduction.
- PHYS-ELECTRON-003: superseded for the affected claim by corrected 004.
- RH attack routes with missing lemmas/domain bridges: NOT PROOF.

## 4. What is NOT evidence

The following are deliberately excluded from strong evidence:

- source code existing without execution record;
- result prose without executable provenance;
- historical chat statements without primary artifact;
- planned experiments;
- architecture specifications;
- application documents that merely reference a validated module;
- ORISIK registry entries whose execution evidence has not been reconciled;
- raw file count;
- duplicated/copy files;
- RH numbered files counted as independent experiments.

## 5. Current evidence tiers

### Tier A — validated / reproduced strong evidence
- Ω-EMO-001A-R1: validated within declared CIE 1931 control.
- Ω-BASIS-002-R2: reproduced numerical core, with explicit provenance limitations.

### Tier B — executed, controlled, or corrected but not promoted to general law
- Ω-INF-3/4/5/6/7/8
- Ω-TEST-1/2/3/4/5/7/9/10/11/12
- PHYS-ELECTRON-002/004/005
- Ω-TIME executed blocks where execution artifacts are present
- selected ENERGY blocks
- selected CICADA blocks
- corrected REL line records with primary execution artifacts.

### Tier C — exploratory / preliminary / lineage evidence
- early Ω-REL records whose original execution artifacts are not all recoverable
- most ENERGY chain results
- RH attack/audit sequence
- D/R/W/P mapping/search
- ORISIK mapped summaries and source trees.

### Tier D — planned / coded / architectural
- planned ENERGY 0001–0005
- unexecuted controls
- architecture/application specifications
- source-only ORISIK objects.

## 6. Identity rules

1. One experiment may have many files.
2. One file may describe a family, not a separate experiment.
3. A corrected rerun of the same protocol is attached to the original lineage.
4. A materially new protocol is a new block.
5. Replication is separate only when independently executed.
6. A source copy is not a new experiment.
7. A stale registry cannot override primary execution evidence.
8. An archive mention cannot create execution evidence.
9. Identifier collision is resolved at registry level without mutating historical files.

## 7. Current graph topology

Ω-Lab:

FAMILY
→ PROTOCOL
→ EXECUTION
→ RESULT
→ AUDIT/CONTROL
→ REPLICATION
→ STATUS

CONNECTIONS:

TOPOLOGY
→ STRUCTURE
→ DYNAMICS
→ EMERGENCE

Evidence layer crosses this graph but does not replace it.

ORISIK:

SOURCE
→ MAPPED SUMMARY
→ EXACT COPY
→ EXECUTION
→ RESULT
→ ACCEPTANCE
→ HISTORY

The SOURCE/MAPPED/EXACT distinction is mandatory.

## 8. Remaining audit queue

The remaining work is no longer conceptual. It is provenance closure:

1. attach exact protocol/run/result/audit paths to every one of the 146 registry objects;
2. assign one canonical status per object;
3. attach independent replication where it exists;
4. separate result-level status from hypothesis-level status;
5. reconcile ORISIK primary execution artifacts against its stale registry;
6. close historical REL provenance where source artifacts can still be recovered;
7. only then freeze a final evidence-status count.

Until that pass is complete, 146 remains a semantic registry count, not a final validated-experiment count.

## 9. Decision

The master registry is structurally complete enough to serve as the index.

The evidence graph is now the controlling layer for deciding what can be used as evidence.

No result is promoted merely because it exists in the repository.

No missing execution is invented.

No failed result is erased.

No family-level hypothesis is promoted from one local experiment.

## 10. Next pass

Build the per-object evidence ledger:

EXPERIMENT_ID | PROTOCOL | RUN | RESULT | CONTROL | AUDIT | REPLICATION | STATUS | CLAIM_ALLOWED

This is the last bookkeeping layer before scientific synthesis.
