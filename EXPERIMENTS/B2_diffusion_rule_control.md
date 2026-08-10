# Ω-B2 — Diffusion-rule control

## Question

Are persistent multiple domains an emergent property of the internal dynamics, or are they produced by the specific diffusion rule?

## Reported comparison

The reported run compared the project's non-standard diffusion rule with standard neighbor diffusion under otherwise matched conditions.

## Reported results

| Metric | Project diffusion | Standard diffusion | Ratio |
|---|---:|---:|---:|
| Number of domains | 23 | 1 | 23× |
| Mean domain size | 8.7 | 200 | 0.04× |

The standard diffusion run converged to one domain, while the project diffusion maintained approximately 23 domains.

## Interpretation

This is a **negative result for the original interpretation**.

The persistence of many domains is strongly dependent on the architecture of the diffusion rule. It therefore cannot be presented as evidence that the system spontaneously generates many stable structures independently of its update rule.

## Why this matters

This experiment is kept in the repository because it prevents a common failure mode in exploratory research: mistaking a behavior deliberately encoded in the update rule for an emergent property.

## Next step

If persistent multi-domain behavior remains scientifically interesting, construct a new model where stabilization is introduced through a mechanism that is independently motivated, such as delay, nonlocal coupling, or another explicitly defined interaction, and then repeat the controls.

## Classification

**A/B — architectural effect; not evidence for the original hypothesis.**
