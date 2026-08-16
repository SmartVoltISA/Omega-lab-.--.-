# Ω-Lab — Distribution Boundary

**Date:** 2026-08-16  
**Status:** IMPLEMENTED — CI verification pending

## Security invariant

Separate capabilities may exist independently, but SPACE must not autonomously close them into a distributed self-continuing system.

Default-deny capabilities:

- network access;
- Bluetooth access;
- peer discovery;
- memory sharing between instances;
- capability delegation;
- self-deployment / replication.

## Design rule

`A + B` does not automatically create capability `AB`.

The presence of separate working organs must not create an implicit bridge between them. Any future external capability must cross an explicit, user-mediated security boundary and must not be able to grant itself additional capabilities.

## Current implementation

`space/security/distribution_boundary.py` contains only policy gates. It does not implement networking, Bluetooth, discovery, replication, or self-deployment.

All such capabilities currently return DENY by default.

## Required verification

CI must prove:

1. every listed distributed capability is denied by default;
2. peer discovery is denied;
3. memory sharing is denied;
4. capability delegation is denied;
5. self-deployment is denied;
6. existing independent SPACE organs remain functional.

## Principle

**Отдельно — работает. Автономно объединиться, распространиться или передать себе полномочия — нельзя.**
