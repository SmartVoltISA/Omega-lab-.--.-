# Ω-Space — Inter-Organism Protocol v1.0

## Principle

A SPACE may know another SPACE's lineage without trusting it. Trust may authorize a request without granting unrestricted access. Guardian remains the final execution authority.

## Relationship stack

```text
IDENTITY
  ↓
PROVENANCE / LINEAGE
  ↓
HISTORY / MEMORY
  ↓
EVIDENCE
  ↓
TRUST
  ↓
CAPABILITY SCOPE
  ↓
GUARDIAN DECISION
  ↓
TRANSPORT / ACTION
  ↓
FEEDBACK
```

## Four independent questions

1. **Who are you?** — identity.
2. **Where did you come from?** — lineage/provenance.
3. **What has happened to you?** — history/evidence.
4. **What may you do now?** — trust + capability + Guardian decision.

These questions must not be collapsed into one field.

## Interaction

SPACE-to-SPACE requests carry sender, receiver, capability, purpose, correlation, freshness and payload. The receiving side independently evaluates the request. A parent/child or sibling relation never bypasses this evaluation.

## Trust

Trust is dynamic and evidence-backed. Trust changes are themselves historical events. A trust increase does not erase previous lower trust; a trust decrease does not erase previous higher trust.

## Privacy

Lineage metadata may be visible according to policy. Private memory, secrets, internal state and unrestricted tools remain local unless an explicit capability and Guardian decision authorize disclosure.

## Feedback

A successful interaction produces evidence and feedback. The receiver may update its own memory and trust assessment. The sender may also record the interaction. Neither side silently rewrites the other's history.

## Failure

A denied request is a valid outcome, not a protocol failure. Repeated denials, anomalies, stale identity or integrity concerns may lower trust or trigger quarantine/recovery.

## Core rule

> **Relationship explains context. Evidence builds trust. Capability defines scope. Guardian decides. Memory preserves the whole story.**
