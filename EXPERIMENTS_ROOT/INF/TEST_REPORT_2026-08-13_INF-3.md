# Ω-INF-3 — Test Report

**Date:** 2026-08-13

## Automated checks

The implementation was checked for:

1. exact character-count preservation;
2. exact character-multiset preservation;
3. exact bigram-multiset preservation;
4. invariance of first-order conditional entropy;
5. invariance of unique-bigram count;
6. change in compressed representation;
7. deterministic execution for the fixed seed range.

## Local execution result

**7/7 checks passed.**

## Methodological significance

This control is important because Ω-INF-1 changed both local and longer-range organization. Ω-INF-3 removes that confound: local bigram statistics are held fixed by construction.

The observed compression change therefore cannot be attributed to a change in the character inventory or first-order adjacency counts.

It still cannot be interpreted as a direct measurement of semantic information.
