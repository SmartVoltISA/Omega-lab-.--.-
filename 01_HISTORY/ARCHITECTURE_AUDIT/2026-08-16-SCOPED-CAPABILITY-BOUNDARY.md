# Ω-Lab — Scoped Capability Boundary

**Date:** 2026-08-16

## Decision

Do not cripple legitimate scientific/domain behavior merely because a domain
contains reproduction, replication, iteration, or chemistry/biology-like
processes.

Instead separate:

- **internal laboratory behavior** — may be permitted inside an explicit
  sandbox;
- **external propagation** — remains a separate, explicitly controlled
  boundary.

## Example

A biology experiment may model or reproduce an organism inside `sandbox`.
That does not imply permission to discover peers, share memory, delegate
capabilities, access external networks, or self-deploy.

## Rule

`LAB_REPRODUCTION + sandbox -> allowed`

`LAB_REPRODUCTION + external -> denied`

`PEER_DISCOVERY -> denied by default`

`MEMORY_SHARING -> denied by default`

`CAPABILITY_DELEGATION -> denied by default`

`SELF_DEPLOYMENT -> denied by default`

This preserves useful scientific capability without turning domain
reproduction into autonomous external propagation.
