# E-MAGNETIC-0001 — Magnet + Coil: Flux, Motion and Energy

Date: 2026-08-23
Status: EXPERIMENT / CONTROL MODEL

## Question
Can a magnetic field be used as the controlled relational link in a closed transformation cycle, and what determines the energy available per cycle?

## Established physics used as control
Faraday's law:

ε = -N dΦ/dt

Magnetic flux:

Φ = ∫ B·dA

For an approximately uniform field:

Φ ≈ B A cos(θ)

Magnetic energy stored in an inductor:

U_L = 1/2 L I²

Magnetic-field energy density in vacuum:

u_B = B²/(2 μ₀)

These are established relations and are not Ω hypotheses.

## Minimal relational graph

MAGNETIC FIELD
    ↓
FLUX THROUGH COIL
    ↓
CHANGE OF FLUX
    ↓
INDUCED EMF
    ↓
CURRENT / LOAD
    ↓
ELECTROMAGNETIC RESPONSE
    ↓
FORCE / BACK-REACTION
    ↺

The loop is only closed dynamically if the generated response affects the mechanical or magnetic configuration. It is not a claim of self-sustaining energy.

## Critical control
A stationary magnet relative to a stationary coil produces no continuing induction from a static field. Relative motion or another change of flux is required.

Increasing speed increases the rate of flux change and therefore can increase induced EMF. Increasing turns N also increases induced EMF for the same flux-change rate.

## Energy accounting
For every cycle measure or calculate:

E_mech,in
E_elec,out
E_stored
E_loss

and test:

E_mech,in ≈ E_elec,out + ΔE_stored + E_loss

A transformer/generator can change voltage and current relationships, but cannot create net energy. Real losses make useful output less than input.

## Proposed controlled geometry
Start with a fixed permanent magnet and a coil. Use a repeatable relative displacement rather than free-running feedback.

Control variables:
- magnet type and dimensions;
- coil turns N;
- coil area A;
- distance and displacement;
- speed v or angular frequency ω;
- load resistance R;
- core material, if used.

Measure:
- B where possible;
- coil resistance;
- induced voltage V(t);
- current I(t) under load;
- displacement/time;
- input mechanical work where feasible.

## First numerical experiment
Use a parameter sweep rather than selecting a single attractive configuration. Compare the same magnet and coil under several speeds and loads.

Primary prediction from established physics:
- ε increases with |dΦ/dt|;
- open-circuit voltage can be high while delivered power remains low;
- loading the coil produces current and opposing magnetic reaction (Lenz law), requiring mechanical work to sustain motion.

## Ω test hypothesis
Topology and coupling determine how a fixed energy input is distributed among voltage, current, stored field energy, motion and losses.

This is a modeling hypothesis to test, not a new physical law.

## Closed-loop extension
After the open-loop experiment is validated, connect the coil to an electromagnetic actuator that influences the magnet/rotor.

Then compare:
1. no feedback;
2. passive feedback;
3. controlled feedback with a small external energy input.

Measure whether feedback changes stability, frequency, losses or useful output. It must not be interpreted as free energy.

## Environmental extension
Later compare the required external energy per cycle with candidate ambient gradients:
- Earth's magnetic field;
- vibration;
- wind;
- temperature gradient;
- electromagnetic background.

The ambient source must be measured as an energy flux, not inferred from field strength alone.

## Current result
The magnetic route is physically valid as an energy transformation mechanism: changing magnetic flux produces EMF, and magnetic fields can store energy. The open-loop relation is established physics.

The Ω-specific question remains open: whether topology, feedback and memory provide a useful general optimization framework for distributing a fixed energy budget across transformations.

## Safety
Do not attempt experiments with lightning, mains voltage, high-energy capacitors or uncontrolled high-current magnetic systems. Begin with low-energy bench-scale sources and measurement equipment.
