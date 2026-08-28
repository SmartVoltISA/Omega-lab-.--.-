# MINIMAL BASIS MAPPING AUDIT v0.1

Date: 2026-08-28
Status: AUDIT / NOT CANONICAL

## Scope
Audit the D/R/W/P observational mapping against the neutral-machine implementation before claiming a minimal basis.

## Findings

1. The neutral machine has control state, tape, position and rule application as implementation mechanisms. These are not yet proven reducible to D/R/W/P.
2. Therefore mapping D/R/W/P directly to machine fields would risk importing implementation assumptions.
3. The current neutral-machine execution demonstrates behavioral richness, but does not establish primitive necessity.
4. The current repository evidence is therefore insufficient for a numerical D/R/W/P minimal-basis claim.

## Decision

No D/R/W/P superiority claim is VERIFIED.

## Required correction

The next evaluator must use a language whose machine substrate itself is part of the declared budget, or explicitly count substrate primitives as costs. Otherwise comparisons are confounded.

## Engineering consequence

We should compare complete computational descriptions by total primitive/constructor budget, not selectively declare some machine mechanisms free.

This audit supersedes any earlier interpretation that treated the neutral machine as evidence for D+R or W+P by itself.
