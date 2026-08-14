# Ω-MEM-6 Pilot — Results

**Status:** PILOT / preliminary
**N:** 20,000 symbols per generator
**Random seed:** 7

Values are conditional entropy in bits: `H(X_next | context)`.

| Generator | Current only | Relevant memory | Random/irrelevant memory |
|---|---:|---:|---:|
| Periodic-4 | 0.5000 | 0.0000 | 0.4998 |
| Markov-2 | 0.6667 | 0.0000 | 0.6666 |
| Thue-Morse | 0.9183 | 0.6667 | 0.9182 |
| IID | 0.9999 | — | 0.9997 |

## Immediate observation

For the deterministic generators, relevant memory lowers next-transition uncertainty while a capacity-matched random memory does not. For IID data, memory provides no meaningful predictive reduction.

This is consistent with the working chain:

`memory → distinguishable future transitions → reduced next-transition uncertainty`.

## Caveat

This is a single-seed pilot, not a final statistical result. It does not establish causality or agency. A full Ω-MEM-6 run must add multiple seeds, matched architectures, explicit predictive-partition counts, intervention, confidence intervals, and independent audit.
