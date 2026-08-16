# Ω-Space — Communication Audience & Guardian Protocol v1.0

## Principle

A message's content does not determine its audience. Audience is an explicit security boundary.

Family communication, group communication, trusted contacts, specific recipients and public broadcast are different operations.

## Audience scopes

- `SELF` — internal/private message.
- `FAMILY` — explicitly registered family relationship.
- `GROUP` — membership in a defined group.
- `TRUSTED_CONTACTS` — explicitly trusted contacts.
- `SPECIFIC_RECIPIENTS` — explicit recipient list.
- `PUBLIC` — unrestricted/public publication; highest exposure.

## Mandatory path

```text
INTENT
  ↓
CONTENT CLASSIFICATION
  ↓
AUDIENCE SCOPE
  ↓
RECIPIENT RESOLUTION
  ↓
POLICY / CONSENT
  ↓
GUARDIAN
  ↓
TRANSPORT
  ↓
DELIVERY
  ↓
DELIVERY FEEDBACK
  ↓
MEMORY / AUDIT
```

No component may silently broaden the audience after authorization.

## Important distinction

```text
FAMILY ≠ TRUSTED_CONTACTS ≠ GROUP ≠ PUBLIC
```

A person being a family member does not automatically make them a public recipient, and a public recipient does not become a family member because they received a message.

## Guardian responsibility

Guardian checks both the communication operation and its scope. It must be able to block:

- accidental broadcast;
- unauthorized recipient expansion;
- disclosure of sensitive/private information;
- stale or revoked recipient identity;
- suspicious message volume or automation;
- cross-group leakage;
- attempts to bypass audience policy.

## Family and minors

Family SPACE may support age/role-aware policies and wellbeing reporting, but access must remain explicit and purpose-bound. Monitoring must not be treated as unlimited access to private information.

For minors, the system should distinguish:

- safety-critical signals;
- wellbeing indicators;
- ordinary activity;
- private content;
- emergency escalation.

The system must record why information was accessed or shared.

## Group messaging

A group is a set of members plus a policy, not merely a recipient list. Membership changes must be recorded in memory. Removing a member immediately affects future authorization; historical messages are not silently rewritten.

## Broadcast

Broadcast is an exceptional scope. It requires explicit authorization and, where applicable, consent. A SPACE must never infer `PUBLIC` from `FAMILY`, `GROUP`, or `TRUSTED_CONTACTS` membership.

## Final rule

> **The ability to communicate is not the ability to communicate with everyone.**

SPACE may interact broadly with the environment, but every boundary crossing must preserve identity, scope, purpose, trust, Guardian authorization and history.
