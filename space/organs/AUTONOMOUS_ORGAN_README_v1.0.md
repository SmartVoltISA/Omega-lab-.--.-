# Ω-Space Autonomous Organ Layer

This layer defines the minimum contract for organs that must remain independently usable.

## Contract

`AutonomousOrgan` owns:

- identity;
- lifecycle;
- local state;
- local memory;
- explicit operation allow-list.

`OrganMessage` carries source, target and requested operation. It is a communication envelope, not an authority grant.

`OrganRuntime` routes explicit messages to registered targets and does not merge organ memory.

## Boundary

Guardian remains responsible for authorization at the execution boundary. This layer intentionally does not add network discovery, self-deployment, automatic graph fusion or shared memory.
