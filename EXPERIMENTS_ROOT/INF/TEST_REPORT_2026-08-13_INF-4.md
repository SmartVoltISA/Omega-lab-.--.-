# Ω-INF-4 — Test Report

**Date:** 2026-08-13

## Automated checks

The implementation was checked for:

1. exact sequence-length preservation;
2. exact character-multiset preservation;
3. exact bigram-multiset preservation;
4. exact trigram-multiset preservation;
5. invariance of first-order conditional entropy;
6. invariance of second-order conditional entropy;
7. invariance of unique-bigram and unique-trigram counts;
8. change in compressed representation;
9. deterministic execution for the fixed seed range.

## Expected control behavior

The reconstruction must use every original trigram exactly once. Therefore any failure of items 2–7 is a methodological failure, not a negative scientific result.

## Numerical result

Independent execution of the fixed protocol produced 100 valid reconstructions.

- original zlib size: **654 bytes**;
- reconstructed mean: **680.29 bytes**;
- range: **665–692 bytes**;
- standard deviation: **5.41 bytes**.

## Methodological significance

Ω-INF-4 removes the first- and second-order n-gram statistics as explanations for the observed compression difference. The result therefore indicates that the tested compression measure is sensitive to organization beyond the exact trigram inventory.

It does **not** establish semantic information, meaning, or a universal hierarchy of information.

## Status

**PASS — protocol invariants satisfied; H-INF-4 remains partially supported and requires independent-corpus replication.**
