# E-MAGNETIC-0001 — Environmental Potential, Magnetic Loop and Lightning Analog

Date: 2026-08-23
Status: exploratory engineering experiment

## Question
Can a closed relational/magnetic system be driven by weak environmental gradients, and what energy scale is available? Can lightning be represented safely by a controlled capacitor/discharge analog rather than captured directly?

## Environmental candidates
1. Atmospheric electric field.
2. Earth/ground potential and telluric/geoelectric fields.
3. Earth magnetic field and time-varying geomagnetic field.
4. Temperature gradients.
5. Solar radiation.
6. Wind / vibration / mechanical motion.
7. Humidity and evaporation gradients.
8. Triboelectric/contact-separation charge.
9. RF/electromagnetic background.
10. Pressure/acoustic/mechanical fluctuations.

## Atmospheric electric field baseline
NOAA/NSSL reports a fair-weather electric field near the surface of roughly 100 V/m (values around 130 V/m are also reported in NOAA atmospheric-electricity references). The global atmospheric circuit has a very small fair-weather conduction current density on the order of pA/m^2.

Important: the existence of field does not mean a large harvestable power source. The available steady power is limited by conductivity, geometry, leakage and the external circuit.

## Simple capacitor estimate
For parallel plates:
C = epsilon A/d
U = 1/2 C V^2
V approximately E*d for a uniform field.

Example only, not a practical power claim:
A = 1 m^2, d = 1 m, E = 100 V/m
C ≈ 8.85 pF
V ≈ 100 V
U ≈ 44 nJ.

At d = 10 m, using the same uniform-field approximation:
C ≈ 0.885 pF
V ≈ 1000 V
U ≈ 0.44 microJ.

The replenishment current in fair weather is extremely small, so this is a high-voltage/very-low-power regime.

## Magnetic candidate
A permanent magnet is not an energy source by itself. A closed magnetic system can store field energy and exert forces, but repeated cyclic motion requires an energy input to overcome losses unless an external gradient supplies the energy.

Useful loop:
magnetic configuration -> mechanical displacement -> changing magnetic flux -> induced voltage/current -> changed magnetic field -> force/torque -> displacement.

Test variables:
B, flux Phi, coil turns N, inductance L, resistance R, displacement x, velocity v, frequency f, mechanical loss, electrical loss.

Measure per cycle:
input energy, recovered energy, dissipated energy, state change, phase relation and memory/repeatability.

## Lightning analog
Do NOT attempt to capture a natural lightning strike in a homemade container or capacitor. Lightning involves extreme voltage/current and rapidly changing fields and can be fatal.

Instead build a controlled low-energy analog:
charge a known capacitor with a safe electrostatic source; measure V; trigger a controlled spark gap/discharge into a designed load; measure V(t), I(t), deposited energy and optical/EM response.

Stored energy is U = 1/2 C V^2. This provides a scalable analog of:
charge separation -> field buildup -> threshold/breakdown -> conductive channel -> discharge -> new state.

The NOAA/NWS educational demonstrations show small static discharges and explain lightning as discharge after charge separation; these are analogs, not natural-lightning capture methods.

## Relational interpretation
The working graph is:
ENVIRONMENT
 -> gradient / difference
 -> potential
 -> constrained storage
 -> threshold
 -> asymmetry
 -> restructuring
 -> discharge / motion
 -> changed topology/state
 -> memory
 -> next cycle

## Hypotheses
H-M1: weak environmental gradients can sustain measurable state changes when the device is designed for high impedance and low leakage.
H-M2: topology changes the conversion efficiency and recurrence pattern for equal initial stored energy.
H-M3: magnetic loops can exhibit repeated state restructuring only when an external energy gradient supplies losses.
H-M4: controlled electrostatic discharge can reproduce the structural sequence of lightning at safe laboratory scale.
H-M5: the most useful environmental source may be the one with the largest product of gradient, coupling, duty cycle and low loss—not necessarily the largest raw field.

## Current conclusion
The environment contains multiple gradients and reservoirs, but they differ by energy density, power density, coupling and accessibility. Atmospheric electric field is real but weakly coupled in fair weather. Triboelectric, thermal, solar, mechanical and RF sources may provide more practical harvested power depending on application.

The correct engineering question is not "where is free energy?" but "which environmental gradient can continuously supply the energy required by a defined relational cycle, at what efficiency?"

## Next controlled calculations
1. Build an energy-density/power-density table for the candidate environmental sources.
2. Design a magnetic ring model and solve its minimum drive energy per cycle.
3. Compare open, ring, cell and mesh topology at equal stored energy.
4. Build a safe capacitor-discharge lightning analog and compare its state trajectory with the graph model.
5. Quantify memory as cycle-to-cycle dependence of the next state on prior state.
