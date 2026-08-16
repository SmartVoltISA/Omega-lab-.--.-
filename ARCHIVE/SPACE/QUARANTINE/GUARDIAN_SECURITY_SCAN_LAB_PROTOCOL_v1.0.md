# Guardian Security Scan Lab Protocol v1.0

## Purpose
Provide Guardian with a controlled defensive laboratory boundary for virus/malware screening without granting arbitrary execution authority.

## Allowed
- receive an artifact into quarantine;
- calculate cryptographic hashes and metadata;
- inspect the artifact read-only;
- invoke an explicitly configured antivirus engine as a scanner;
- record CLEAN / DETECTED / UNSCANNED outcomes;
- preserve evidence for later review.

## Forbidden by default
- executing the inspected artifact;
- loading it into trusted memory;
- promoting it to trusted state automatically;
- arbitrary outbound network access;
- modifying the original source artifact.

## Flow
`external artifact -> quarantine -> Guardian -> scanner -> evidence -> decision -> optional controlled promotion`

An antivirus engine is an external capability, not a source of authority. A clean scan is evidence, not permission to execute.

## Safety invariant
**Visibility may be granted without granting authority.**

The current runtime implements the quarantine, hashing and optional read-only scanner adapter. Real antivirus-engine integration is host-dependent and must be tested on the target device/server before being marked hardware-verified.
