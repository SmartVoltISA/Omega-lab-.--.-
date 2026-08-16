# Ω-Lab CI Execution Gating Rule v1.0

**Status:** CORE / ACTIVE

## Rule

A code or architecture change is **not considered completed** merely because files were written or a commit exists.

Completion requires a real CI execution for the resulting commit and a recorded outcome.

```text
CHANGE
  ↓
COMMIT
  ↓
CI RUN
  ↓
RESULT
  ├── SUCCESS → may be considered verified/completed
  └── FAILURE → not completed; diagnose and repair
```

If no workflow run exists, the work remains **PENDING VERIFICATION**.

If a workflow is queued or running, the work remains **PENDING VERIFICATION**.

Only an observed successful CI result may move the change to **VERIFIED / COMPLETED**.

## Memory rule

The completion state must preserve:

- commit SHA;
- workflow/run identifier when available;
- execution status;
- relevant failed/passed jobs;
- final verification result;
- timestamp/provenance.

A missing CI result must never be silently interpreted as success.

## Operational rule

For every subsequent implementation cycle, check the latest relevant commit's CI status before declaring the previous cycle complete.
