# Ω-Lab — Experiment Registry

All experiments must preserve:

- Experiment ID
- date
- time and UTC offset when known
- hypothesis / research question
- model and parameters
- method
- raw or derived outputs
- controls
- failures and rejected results
- corrected results
- conclusion and epistemic status
- provenance / associated files

Canonical rule:

```text
RESULT ≠ TRUTH
RESULT → VERIFY → CLASSIFY → RECORD
```

Failed tests and methodological failures are retained. Corrected results supersede invalid measurements but do not erase their provenance.
