# EVIDENCE CLOSURE AUDIT v0.2

Date: 2026-09-27
Scope: full current Ω-Lab / ORISIK registry pass after MASTER_EXPERIMENT_REGISTRY_v0.4 and EVIDENCE_GRAPH_v0.1.

## 1. Audit result

The repository-wide pass is complete at the semantic/evidence-architecture level.

The current registry contains 146 semantic research blocks/objects, but a final numerical count of VALIDATED/REPRODUCED blocks is intentionally NOT frozen because several historical and ORISIK records still lack complete protocol→run→result provenance in the current tree.

This is not a missing experiment. It is a missing evidence link.

## 2. Strong-evidence anchors currently confirmed

### VALIDATED

1. Ω-EMO-001A-R1 — explicitly VALIDATED for the tested CIE 1931 control only; execution provenance recorded; same code/input twice with identical output SHA; independent NumPy recomputation agrees; claim scope is representation-specific.

### REPRODUCED

2. Ω-BASIS-002-R2 — explicitly REPRODUCED for the numerical core; independent rerun; N=5000, 100 seeds; audit identifies incomplete bootstrap/provenance closure; therefore numerical-core reproduction, not universal-foundation validation.

## 3. Completed evidence with restricted claim scope

Ω-INF-3/4/5/6/7/8; Ω-MEM-4R; Ω-TEST-1/2/3/4/5/7/9/10/11/12; PHYS-ELECTRON-002/002A/003/004/005; CICADA C1-002/015/016/017/018/019; D/R/W/P neutral-machine execution; finite deterministic dynamics enumeration; hidden-state/memory enumeration; topology 8-node 3-regular sweep; selected Ω-TIME blocks; selected ENERGY blocks; corrected REL records with primary execution artifacts.

These are evidence objects with different strengths. They must not be collapsed into one status.

## 4. Explicitly rejected / invalidated / superseded

- Ω-BASIS-002 original execution: REJECTED.
- Ω-MEM-4: NOT VALIDATED because implementation violated the preregistered protocol.
- Ω-TEST-7 first run: invalidated because of non-finite scores.
- Ω-REL-018 first reversal-direction result: invalidated; corrected run retained.
- E-ENERGY-0032R: negative exact numerical reproduction.
- PHYS-ELECTRON-003: superseded for affected interpretation by corrected 004.
- RH attack routes with missing proof obligations: not proof.

Failed results remain part of the evidence graph.

## 5. Research lines that must not be upgraded

Ω-RH: RH-01…64 is one research/attack/audit lineage. Current evidence does not establish the Riemann Hypothesis.

D/R/W/P: neutral-machine execution demonstrates properties of the implemented transition system. It does not establish that D/R/W/P are fundamental primitives. D+R stronger than W+P remains UNKNOWN/UNPROVEN.

Ω-ENERGY: completed toy-model results, controls, replications and speculative mechanisms exist; branch-level hypothesis remains OPEN / NOT CONFIRMED.

Ω-MEM: MEM-4 and MEM-4R are different evidence states. Corrected replication does not retroactively validate the defective original.

ORISIK: registry entries are not equivalent to execution evidence. Source SHA, mapped summary, exact copy, execution and result remain separate states.

## 6. Current evidence hierarchy

A — strong: validated result with provenance and independent checks; or independently reproduced result with known limitations.
B — execution-backed: execution record and result exist, but generality or independent reproduction is limited.
C — preliminary: reported/executed result with incomplete provenance, limited control, or exploratory status.
D — protocol/source only: planned, coded, architectural, source-only, mapped-only, or otherwise not execution-verified.
E — rejected/invalidated: execution failed or later evidence invalidated the original claim.

## 7. Important correction to the interpretation of 146

146 means: 146 current semantic registry objects/blocks requiring evidence classification.
It does NOT mean 146 experiments have been proven.

The evidence graph deliberately prevents that category error.

## 8. Per-object ledger status

The requested final ledger cannot honestly assign VALIDATED/REPRODUCED status to every one of the 146 objects from the current repository evidence.

Where an object has no complete protocol/run/result chain, its status is: UNRESOLVED — PROVENANCE CLOSURE REQUIRED.

This is an evidence status, not a negative scientific result.

The ledger invariant is:

known evidence → explicit status
missing evidence → UNKNOWN
never → inferred execution

## 9. Final audit decision

The scientific bookkeeping layer is now closed enough for synthesis.
The evidence layer is NOT allowed to invent remaining links.
The next meaningful work is targeted provenance closure of unresolved objects, followed by claim extraction.

Final synthesis must use:

CLAIM_ALLOWED = f(STATUS, CONTROL, REPLICATION, PROVENANCE)

not file count, result count, or narrative strength.

## 10. Canonical next operation

For every unresolved object: locate protocol; locate exact executable/run; locate execution record; locate raw result; locate audit/control; locate replication; assign status; write the smallest claim actually supported.

Only after this closure should the final VALIDATED/REPRODUCED totals be frozen.