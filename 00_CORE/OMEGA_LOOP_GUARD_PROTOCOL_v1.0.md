# Ω-LOOP-GUARD v1.0

## Status
FOUNDATION / ACTIVE DESIGN

## Origin
Identified during live laboratory interaction on 2026-08-16. The system repeatedly emitted semantically equivalent progress messages (e.g. “копаю дальше”) instead of producing a new computation/result. This exposed a missing architectural control: feedback existed, but there was no explicit STOP condition for unproductive repetition.

## Problem
A feedback system can become a positive loop:

input → attempt → feedback → same attempt → same feedback → …

Without a termination condition, the system may confuse activity with progress.

## Principle
**No new information + repeated state + repeated action = STOP and re-plan.**

The guard must distinguish:
- productive iteration: state changes, evidence increases, hypothesis is tested, or strategy changes;
- unproductive repetition: substantially identical state/action/output with no new evidence.

## Core cycle
OBSERVE → COMPARE → SCORE PROGRESS →
IF NEW INFORMATION: CONTINUE
IF REPEATED WITHOUT PROGRESS: STOP
→ DIAGNOSE LOOP → CHANGE STRATEGY → RESET LOOP COUNTER → CONTINUE

## Required signals
1. State fingerprint — compact representation of current task/state.
2. Action fingerprint — what the system is actually doing.
3. Output fingerprint — semantic similarity of recent outputs.
4. Evidence delta — new measurements, files, calculations, citations, tests, or verified facts.
5. Strategy delta — whether the method actually changed.
6. Loop counter — consecutive repeated cycles.
7. Stop threshold — configurable maximum repetition without progress.

## Minimal rule
If N consecutive cycles satisfy:

state_similarity ≥ S
AND action_similarity ≥ A
AND evidence_delta = 0
AND strategy_delta = 0

then:

LOOP_GUARD = TRIGGERED
ACTION = STOP

The system must not merely announce that it is “continuing”. It must either produce a new result or explicitly state that the current strategy has failed and select another strategy.

## Escalation
Level 0 — normal iteration.
Level 1 — repetition detected; inspect state/action.
Level 2 — STOP current strategy.
Level 3 — generate alternative strategy.
Level 4 — run the alternative and compare against the failed strategy.
Level 5 — if all available strategies fail, archive the failure and report the unresolved question.

## Anti-self-deception rule
A change in wording is NOT a strategy change.
A longer explanation is NOT progress.
A citation is NOT new evidence unless it changes the tested claim.
A promise to continue is NOT an iteration.
Only measurable state/evidence/strategy change counts as progress.

## Laboratory test
Observed failure:
- user requested continued search;
- system repeatedly produced progress statements instead of advancing the computation;
- user identified the cycle;
- analysis showed that feedback existed but lacked an explicit automatic stop/replan guard.

Result: FAILURE CONFIRMED.

## Relation to Ω architecture
The protocol extends the existing feedback-ring concept with a negative-feedback termination mechanism. The goal is not to eliminate iteration, but to prevent iteration from becoming a closed semantic loop.

Core relation:

ENTITY → RELATION → STATE → FEEDBACK → CHANGE

If CHANGE = 0 across repeated cycles, the relation has ceased producing useful information and the loop must be broken.

## Acceptance criteria
The protocol is considered operational only when a test can demonstrate that:
1. a deliberately repeated task triggers the guard;
2. the system stops repeating the same action;
3. an alternative strategy is selected;
4. productive progress resumes, or the failure is archived;
5. the guard itself does not become a new repetitive loop.

## Important limitation
This document defines the protocol and laboratory requirement. It does not claim that the guard is already integrated into every Ω-Lab runtime component. Integration requires implementation and testing.
