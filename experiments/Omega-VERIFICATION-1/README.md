# Ω-VERIFICATION-1 — EXPECTED → ACTUAL

Verification is deliberately separate from execution.

```text
EXPECTED RESULT
      ↓
ACTUAL RESULT
      ↓
COMPARE
      ↓
CONFIRMED / PARTIAL / FAILED / UNKNOWN
```

The first implementation uses exact equality for deterministic values. It does not invent a success when the actual result is missing or different.

A richer comparator can later be added for numeric tolerances, structured outputs and domain-specific verification rules without changing the boundary.
