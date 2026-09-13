# Ω-FEEDBACK-1 — RESULT → NEXT STATE

Feedback is an information transfer, not a log append.

```text
RESULT
 ↓
VERIFICATION
 ↓
FEEDBACK
 ↓
PRESENT STATE UPDATE
 ↓
MEMORY / GRAPH UPDATE
 ↓
NEXT CYCLE
```

The feedback organ produces a structured state delta. It does not mutate PRESENT directly. The state organ remains the sole owner of current state transitions.

Failures are first-class feedback and are preserved rather than converted into success.
