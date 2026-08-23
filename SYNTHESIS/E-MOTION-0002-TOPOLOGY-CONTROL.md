# E-MOTION-0002 — Same Energy, Different Topology

Date: 2026-08-23
Status: exploratory numerical control

## Question
If the initial energy is normalized to the same value, does changing only graph topology change how that energy manifests through time?

## Model
Small mass-spring-like relational network. Each node has a scalar state x and velocity v. Coupling is represented by graph Laplacian L. Dynamics:

x'' = -(I + L)x - gamma x'

with gamma = 0.01. Initial displacement is normalized so the initial total modeled energy is approximately 1 for every topology.

Topologies:
- open chain: 12 nodes, 11 edges
- ring: 12 nodes, 12 edges
- binary tree: 15 nodes, 14 edges
- 3x4 grid: 12 nodes, 17 edges
- small-world mesh: 12 nodes, 24 edges

This is not a physical electrical model. It is a topology-control model.

## Results
All cases start with approximately the same normalized energy (~1.0), but the spatial/relational manifestation differs.

Peak state asymmetry (std of node states):
- open chain: ~0.276
- ring: ~0.226
- tree: ~0.204
- grid: ~0.226
- mesh: ~0.159

Mean node-state magnitude over the run:
- open chain: ~0.175
- ring: ~0.143
- tree: ~0.125
- grid: ~0.143
- mesh: ~0.100

The finite damping used here did not reduce the total energy below 0.5 during the chosen window, so no half-life ranking is claimed.

## Result
With equal normalized initial energy, topology changes the distribution and visible dynamics of the state. More connected topologies in this toy model suppress local asymmetry and spread the state more broadly; open topology permits larger local asymmetry.

## Interpretation
Supported at model level:
- energy budget and manifestation can be separated;
- topology changes the pathways through which a disturbance propagates;
- the same initial potential can produce different temporal/spatial patterns solely because relation structure differs.

Not established:
- that graph topology alone determines physical energy;
- that this toy Laplacian is a universal model of electricity, light, lightning, or markets.

## Connection to synthesis
This is a useful control for the working statement:
> Potential is stored in the current configuration/constraints; motion is the time evolution of that configuration; topology determines available paths for restructuring.

## Next
Use a physically grounded electrical network (RLC or transmission-line model) with equal initial stored energy and vary topology. Measure current, voltage, field energy, dissipation, recurrence, and memory separately.
