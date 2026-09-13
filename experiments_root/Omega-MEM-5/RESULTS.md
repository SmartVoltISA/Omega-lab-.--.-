# Ω-MEM-5 Results

**Status:** EXECUTED (local reference implementation)  
**Date:** 2026-08-14  
**N:** 20,000 observations/generator/seed  
**Seeds:** 10  
**Nominal memory budget:** S=4

## Summary

| Generator | Memory | Accuracy | Conditional entropy | Predictive partition | Mean next choices |
|---|---|---:|---:|---:|---:|
| Periodic-4 | none | 0.5000 | 1.0000 | 2 | 2.00 |
| Periodic-4 | relevant | **1.0000** | **0.0000** | 4 | 1.00 |
| Periodic-4 | mismatched | 0.5011 | 0.9978 | 4 | 2.00 |
| Periodic-4 | random | 0.5011 | 0.9978 | 4 | 2.00 |
| Markov-2 | none | 0.6667 | 0.6667 | 2 | 1.50 |
| Markov-2 | relevant | **1.0000** | **0.0000** | 3 | 1.00 |
| Markov-2 | mismatched | 0.6709 | 0.6614 | 4 | 1.50 |
| Markov-2 | random | 0.6709 | 0.6614 | 4 | 1.50 |
| Thue-Morse | none | 0.6667 | 0.9183 | 2 | 2.00 |
| Thue-Morse | relevant | **1.0000** | **0.0000** | 4 | 1.00 |
| Thue-Morse | mismatched | 0.6667 | 0.9183 | 4 | 2.00 |
| Thue-Morse | random | 0.6667 | 0.9183 | 4 | 2.00 |
| HMM | none | 0.6698 | 0.9150 | 2 | 2.00 |
| HMM | relevant | **0.7442** | **0.8203** | 4 | 2.00 |
| HMM | mismatched | 0.6698 | 0.9150 | 4 | 2.00 |
| HMM | random | 0.6698 | 0.9150 | 4 | 2.00 |
| IID | none | 0.5045 | 0.9999 | 2 | 2.00 |
| IID | relevant | 0.5045 | 0.9999 | 4 | 2.00 |
| IID | mismatched | 0.5054 | 0.9998 | 4 | 2.00 |
| IID | random | 0.5054 | 0.9998 | 4 | 2.00 |

## Intervention check

A single memory-state substitution was performed at the midpoint while the external current observation was left unchanged. Across 10 seeds each, the relevant memory representation changed the next prediction in all tested deterministic generators (Periodic-4, Markov-2, Thue-Morse) and in the HMM control when the hidden-state memory was replaced by the alternative state.

## Immediate interpretation

The strongest controlled result is not simply that S=4 performs better. It is that, at the same nominal capacity, a structurally relevant memory representation can sharply reduce conditional next-transition entropy while an equal-capacity mismatched/random representation does not.

For the deterministic generators, relevant memory produces a predictive partition in which each retained context has a single next transition. The iid control does not benefit from additional structure.

The HMM result is weaker because the observable process remains stochastic even when hidden-state context is retained. This is expected and is not treated as failure of the hypothesis.

## Limits

This is a controlled computational result from the reference implementation, not a universal law. The HMM relevant memory uses the generator's hidden state as an oracle context. The implementation must still be independently audited before the result is treated as a strong laboratory conclusion.
