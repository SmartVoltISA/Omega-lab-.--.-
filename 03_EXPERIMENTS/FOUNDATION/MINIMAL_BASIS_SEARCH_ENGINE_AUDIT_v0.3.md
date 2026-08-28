# AUDIT — MINIMAL BASIS SEARCH ENGINE v0.3

Status: NOT EVIDENCE / TOOLING AUDIT

The v0.3 engine removes explicit target-capability constructor names, but it still assigns operational meanings to neutral constructors (`FILTER`→branch_like, `MAP`→successor_like, `PAIR`→retained_like, `ITER`→repeat_like). Therefore v0.3 is not yet an independent minimal-basis proof.

This is intentionally recorded immediately. No result from v0.3 may be promoted to VERIFIED or CANONICAL.

Required v0.4 change:
- constructor names must be semantically inert;
- traces must be defined as raw state transitions only;
- target properties must be predicates over traces defined independently of constructor names;
- demonstrate renaming/isomorphism invariance;
- include a negative-control language with the same syntax but randomized operational interpretation.

Current conclusion: D+R vs W+P remains UNKNOWN.
