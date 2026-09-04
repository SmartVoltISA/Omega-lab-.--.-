# E-ENERGY-HYSTERESIS-BALANCE-001

## Question
Does a history-dependent internal state create an apparent energy residual when that state is omitted from the system boundary, while a full state/accounting description closes the balance?

## Model
Dimensionless magnetic-relaxation toy model:

- `F(H,M) = 0.5*a*M^2 - b*H*M`
- `Mdot = -gamma * dF/dM`
- `a = 2`, `b = 1`, `gamma = 8`
- external field: triangular closed cycle `H: -1 -> +1 -> -1`
- 20 cycles used to remove the initial transient

Energy accounting uses:

`W_ext = Delta F + D`

where `D = integral(Mdot^2/gamma dt) >= 0`.

## Result
Final cycle:

| Quantity | Value |
|---|---:|
| External work `W_ext` | 0.374983213917 |
| State-energy change `Delta F` | 0.000000000000 |
| Dissipation `D` | 0.375283440670 |
| Full-account residual | -3.00227e-4 |
| Visible-only residual | 0.374983213917 |
| Final `M` | -0.375258353943 |

The full residual is small relative to the cycle work (~0.08%) and is attributable to the explicit Euler/time-discretization error. The visible-only account leaves essentially the entire cycle work unaccounted because `H` returns to its starting value while the internal state `M` and its dissipative dynamics are omitted.

## Interpretation

This supports the **accounting architecture**, not a new physical law.

1. A closed visible coordinate does not imply zero energy transfer when an internal state participates in the dynamics.
2. Omitting the internal state can produce an apparent residual.
3. Restoring the internal state and its dissipation channel closes the balance within numerical error.
4. The model is physically motivated by magnetic relaxation/hysteresis, but it is still a normalized computational model and is not a measurement of a real material.

## Status
**COMPUTATIONAL CONTROL — INFORMATIVE**

No claim of anomalous energy, free energy, or energy creation is supported.

## Next test
Replace the normalized relaxation model with a standard rate-independent hysteresis model (e.g. a Preisach-style or play-operator model), then test the same boundary-accounting question and compare the loop integral against the explicitly modeled loss channel.
