# E-AC-0001 — AC phase/neutral and balance

## Question
Can the three-state interpretation be mapped onto a sinusoidal AC system without confusing model labels with physical quantities?

## Minimal physical control
For an ideal sinusoidal source:
- V(t) = Vpk sin(ωt)
- neutral is the reference node in the ideal single-phase model
- resistive load: I(t)=V(t)/R
- instantaneous power: P(t)=V(t)I(t)=V(t)^2/R

## Computed control
For Vpk=1, R=1 over one full cycle:
- mean voltage = 0
- mean current = 0
- mean instantaneous power = 0.5
- instantaneous power is never negative for the resistor

With a simple sign-state encoding:
- red = V < 0
- green = V ≈ 0
- blue = V > 0

At exact zero threshold the ideal continuous sinusoid spends essentially zero time in green; with deadband ±0.1 Vpk the approximate fractions are:
- red 46.8%
- green 6.4%
- blue 46.8%

## Result
The AC waveform naturally gives two opposed half-cycles around a neutral crossing. Neutral is a reference/crossing condition, not a source of energy. Most importantly, zero mean voltage does NOT imply zero energy transfer: a resistive load has positive mean power.

## Interpretation boundary
This supports the structural analogy:

opposed states ↔ alternating phase sign
neutral ↔ reference/crossing
load ↔ relation between states
power ↔ consequence of the interaction

It does NOT establish that red/green/blue are fundamental physical categories, nor that electrons universally 'seek neutral'. Those remain hypotheses.

## Next experiment
Use an RLC load and compare the state/phase relation of voltage and current. Test whether the proposed 'energy as consequence of relation change' survives reactive storage and return of energy.
