# E-ENERGY-PREISACH-001 — History-dependent hysteresis loop

## Status
COMPUTATIONAL RESULT — toy/model-level evidence only.

## Question
Can a model with explicit internal memory produce a nonzero closed-cycle work integral, while a memoryless constitutive relation at the same visible input does not?

## Model
A Preisach-style ensemble of 149 binary relays is driven by a dimensionless external field `H` from -1 to +1, back to -1, and again to +1. Each relay has an upper switching threshold `alpha` and lower threshold `beta`; its state is therefore history dependent.

The observable output is the ensemble mean `M`.

## Independent computational result
- Number of relays: **149**
- `M_min`: **-1.000000**
- `M_max`: **+1.000000**
- Oriented loop integral `∫ M dH`: **-2.9505805**
- Loop-area magnitude: **2.9505805**

The sign is determined by traversal orientation; the magnitude is the relevant cyclic-work proxy in this normalized model.

At the same visible field, multiple internal states occur:

| H | observed M range across the cycle |
|---|---:|
| -0.5 | -1.0000 … -0.3289 |
| 0.0 | -1.0000 … +0.6107 |
| +0.5 | -0.0067 … +1.0000 |

Thus `H` alone does not specify the full state.

## Interpretation
The model produces a genuine hysteresis loop because the internal relay states retain history. The nonzero closed-cycle integral is therefore not an unexplained energy source: it represents work associated with traversing a dissipative hysteretic state trajectory in the chosen normalized model.

The key boundary test is:

`visible state H only -> apparent residual`

versus

`H + internal relay state -> history-dependent trajectory -> nonzero cycle work`

This supports the narrower architectural claim that omitting internal state can make energy accounting appear incomplete. It does **not** establish a new physical law or free-energy mechanism.

## Controls / limitations
1. The model is dimensionless and computational.
2. The relay ensemble is an explicit phenomenological construction, not a measurement of a particular material.
3. The loop integral is a normalized work/dissipation proxy; conversion to joules requires a physical constitutive model and units.
4. The next stronger test is to attach a physical magnetic constitutive scale and verify energy balance against independently defined stored and dissipated terms.

## Conclusion
**Positive model result:** explicit internal history creates path dependence and a nonzero closed-cycle work integral. The result remains fully compatible with ordinary energy conservation; the cycle work is not energy created from nothing.
