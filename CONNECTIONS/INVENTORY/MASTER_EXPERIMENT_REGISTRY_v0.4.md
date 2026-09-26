# MASTER EXPERIMENT REGISTRY v0.4 — FINAL RECONCILIATION PASS

Date: 2026-09-27
Repository: SmartVoltISA/Omega-lab-.--.-
Purpose: reconcile Ω-Lab / ORISIK into semantic research blocks rather than raw files.

## 1. Counting rule

A raw file is NOT automatically an experiment. Count one canonical research block when a named protocol/experiment lineage asks one defined question. Result files, code files, audits, copies, corrections and history attach to that lineage.

raw files != experiments

The 629-file inventory remains a source inventory, not an experiment count.

## 2. Final reconciliation of the three blockers

### A. Ω-REL

The repository contains two different REL layers.

Early REL line: REL-001…045-era research line, represented by archival records and REL-018 primary material. Several old numbered records are not currently recoverable as standalone files from the present tree/search index; therefore they must not be fabricated as independently executed experiments.

Reconciled semantic count for the early line: 18 research blocks:

REL-001; REL-002A; REL-003; REL-004A; REL-004B; REL-005/006 combined; REL-007; REL-009; REL-010; REL-011/012 combined; REL-016; REL-018; REL-024; REL-029; REL-036; REL-041; REL-043; REL-045.

This is a lineage count, not a claim that every historical record has a currently retrievable standalone execution artifact.

Blind/black-box REL line: REL-066…073 is a separate later family. Primary artifacts include extraction/result and blind-test/result records. Count: 8 named research blocks.

Therefore REL is registered as 26 semantic research blocks, with provenance quality differing by record.

No missing historical REL execution is upgraded merely because an archive mentions it.

### B. E-ENERGY

Actual numbered ENERGY blocks: E-ENERGY-0010, 0011, 0012, 0013; E-ENERGY-0020 through 0037 inclusive; E-ENERGY-0032R.

This is 23 numbered blocks (4 + 18 + 1).

Additional named computational research blocks: E-ENERGY-HYSTERESIS-BALANCE-001 and E-ENERGY-PREISACH-001.

Therefore the reconciled ENERGY research branch contains 25 named blocks.

The README E-ENERGY-0001…0005 are explicitly PLANNED/BLOCKED and are NOT counted as executed experiments.

The branch remains OPEN / HYPOTHESIS / NOT CONFIRMED. Individual completed computational results retain their own evidence status.

E-ENERGY-0032R is a replication check with a negative exact-numerical-reproduction result; it is not merged with 0032.

### C. E-MAGNETIC-0001 collision

Two materially different research objects use the same identifier:

1. ELECTRICITY/E-MAGNETIC-0001-MAGNET-COIL-FLUX-CYCLE.md — magnet + coil / flux / motion / energy cycle; experiment/control model.
2. 02_EXPERIMENTS/E-MAGNETIC-0001-ENVIRONMENTAL-POTENTIAL-LIGHTNING-CAPTURE.md — environmental gradients / magnetic loop / controlled lightning analog; exploratory engineering experiment.

They are not duplicates and do not ask the same question.

For registry purposes they are two distinct blocks:
- E-MAGNETIC-0001A — Magnet/Coil Flux Cycle
- E-MAGNETIC-0001B — Environmental Potential / Lightning Analog

The original repository IDs are preserved as aliases. No historical file is renamed by this registry.

## 3. Canonical family counts

These are semantic research blocks, not claims that every block is scientifically validated.

| Family | Canonical blocks |
|---|---:|
| Ω-MEM | 11 |
| Ω-INF | 8 |
| Ω-B | 6 |
| Ω-LINK | 1 |
| Ω-BASIS | 3 |
| Ω-EMO | 2 |
| Ω-TIME | 9 |
| Ω-REL | 26 |
| Ω-ENERGY | 25 |
| PHYS-ELECTRON | 5 |
| CICADA | 6 |
| Ω-TEST | 10 |
| E-LIGHT | 6 |
| E-AC | 2 |
| E-MOTION | 2 |
| E-ENVIRONMENT | 0 executed |
| E-MAGNETIC | 2 |
| Ω-RH | 1 research/attack lineage |
| D/R/W/P + FOUNDATION | 1 research line |
| ORISIK registry objects | 20 |
| **Working semantic registry total** | **146** |

146 is the current semantic registry total for the listed families/objects. It is NOT 146 validated experiments.

It includes exploratory studies, controls, negative results, research/attack lineages and ORISIK registry objects with mixed epistemic status.

The number must not be compared directly to the 629 raw candidate files.

## 4. Evidence-status rules

PLANNED → CODED → EXECUTED → VALIDATED → REPRODUCED

Parallel terminal/negative states: REJECTED / INVALIDATED.

Source code is not execution evidence. A result document is not automatically validation. A historical mention is not execution evidence. A replication is not accepted merely because it has similar numbers; provenance and independent execution must be checked.

## 5. Important reconciliations

Ω-MEM: MEM-4 remains NOT VALIDATED because its implementation violated the preregistered protocol. MEM-4R is a corrected successor/replication and remains separate; its reported result is not treated as independently rerun merely because it is recorded.

Ω-BASIS-002-R2: numerical core reproduced, but full provenance/CI claims are incomplete. Not promoted to a universal foundation result.

Ω-EMO-001A-R1: validated only within the tested CIE-1931 representation/control. It does not establish a universal three-fundamental-colors claim.

Ω-RH: RH-01…64 is one research/attack/audit lineage, not 64 independent experiments. No RH claim is established.

D/R/W/P: D+R stronger than W+P remains UNKNOWN/UNPROVEN. The executable evaluator is not itself a proof.

Ω-TEST: TEST-7's first non-finite run is invalidated and the corrected blind rerun is the accepted execution lineage. It is not counted twice.

E-LIGHT: exploratory/toy-model work; not physical validation.

E-ENVIRONMENT: E-ENVIRONMENT-0001 is an environmental-gradient inventory/preparation object and is not counted as an executed experiment.

E-MAGNETIC: identifier collision is explicitly represented as A/B aliases in this registry. Underlying files remain untouched.

## 6. ORISIK rule

ORISIK's 20 registry objects are included as registry-level research objects, not automatically as validated experiments.

The B-Lab recursive inventory proves source-tree existence, not execution success.

Where the ORISIK registry is stale and primary execution/result artifacts exist, primary artifacts take precedence over the stale registry status.

Chain: PROTOCOL → EXECUTION → RAW RESULT → ACCEPTANCE → INTERPRETATION → EVIDENCE → HISTORY.

## 7. Final interpretation

The Ω archive contains substantially more research structure than the original 629-file count suggested, but the files are heavily multi-artifact.

629 raw candidate records → provenance/source/result/audit/history/code mixed together → semantic reconciliation → 146 current registry-level research blocks/objects → only a subset have execution evidence → an even smaller subset are validated/reproduced.

This is the scientifically safe count.

## 8. Remaining uncertainty

No blocker remains for maintaining the master registry.

The residual uncertainty is provenance quality inside several historical REL records and individual ORISIK objects whose original execution artifacts are not fully reconstructed in the current tree. That uncertainty is recorded rather than converted into false precision.

## 9. Next operational step

Use this registry as the canonical index.

Next pass should connect each semantic block to: FAMILY → EXPERIMENT → RUN → RESULT → AUDIT/CONTROL → REPLICATION → STATUS.

Do not create a new experiment merely to repair an inventory problem.