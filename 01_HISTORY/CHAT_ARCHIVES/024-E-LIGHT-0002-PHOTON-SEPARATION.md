# E-LIGHT-0002 — Photon-driven separation test

Date: 2026-08-23

## Question
Can an optical excitation, represented only as added excitation energy plus a thresholded interaction, produce separation of a previously coupled state without explicitly imposing the direction of separation?

## Control/model
Two coupled degrees of freedom. Separation coordinate q=(x1-x2)/sqrt(2). Baseline coupling tends to restore q toward 0. A photon pulse supplies excitation energy E. The toy model allows separation only when E exceeds an interaction threshold; the direction is selected stochastically rather than hard-coded.

N = 50,000 trajectories per energy level; fixed RNG seed 7.

## Results
E=0.25: separation events 0%; mean |q| 0.01375.
E=0.50: separation events 0%; mean |q| 0.01374.
E=1.00: separation events 33.43%; mean |q| 0.29671; median 0.01977; 90th percentile 0.92836.
E=2.00: separation events 100%; mean |q| 0.86061.
E=4.00: separation events 100%; mean |q| 0.86060.

## Interpretation
A thresholded light-energy input can produce a transition from a coupled state to a separated state in the toy system. The transition is strongly nonlinear: below threshold, the system remains near the coupled state; above threshold, separated trajectories appear and then dominate.

## Critical limitation
This is NOT a physical simulation of photons, electrons, molecular orbitals, or Maxwell/quantum dynamics. The threshold and mapping from photon energy to separation were explicitly chosen in the toy model. Therefore the result establishes only that the proposed relational mechanism is internally realizable, not that light universally separates connections in nature.

## External physical check
Real photochemical systems do exhibit light-induced charge separation. DOE describes photosynthetic reaction centers in which photon excitation leads to electron transfer and spatial electron-hole separation; semiconductor photoelectrodes likewise generate mobile positive and negative carriers after light absorption. These observations make the toy mechanism physically relevant as a hypothesis, but do not validate the model itself.

## Next test
Replace the hand-defined separation operator with a minimal physical interaction model (e.g. two-state Hamiltonian / coupled potential with optical driving), then test whether separation emerges from the dynamics rather than being encoded in the transition rule.

Status: exploratory result; hypothesis remains open.
