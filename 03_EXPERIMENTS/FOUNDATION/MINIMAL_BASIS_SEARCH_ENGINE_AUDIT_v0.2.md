# MINIMAL BASIS SEARCH ENGINE — AUDIT v0.2

Status: AUDIT / NOT EVIDENCE

The v0.2 engine is intentionally preserved as a prototype, but it is NOT accepted as experimental evidence.

Reason: the grammar contains operators APPLY, TEST, STEP, STORE and LOOP whose semantics already encode application, branching, succession, memory and repetition. Therefore the engine can smuggle target capabilities through operator definitions even when the primitive inventory is small.

Required correction for v0.3:

1. Separate primitive symbols from evaluator semantics.
2. Treat every operational operator as a separately budgeted primitive unless its behavior is derived from lower-level rewrite rules.
3. Define a tiny neutral transition machine whose only built-in behavior is symbol rewriting / term reduction.
4. Express candidate capabilities as trace predicates over resulting machine traces, not as named operators.
5. Run leakage controls by renaming all primitive symbols and checking semantic equivalence.
6. Record minimal budgets only after a witness survives reverse replay from the declared grammar.

Current conclusion remains UNKNOWN regarding the minimal basis of D+R versus W+P.
