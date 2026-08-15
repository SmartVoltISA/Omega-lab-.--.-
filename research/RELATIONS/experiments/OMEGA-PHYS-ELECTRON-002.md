# Ω-PHYS-ELECTRON-002 — Electron: physical definition, governing laws, and Ω-Lab relation cross-check

Date: 2026-08-16
Status: COMPLETED ANALYTICAL CROSS-CHECK / HYPOTHESIS OPEN

## 1. Research question

What is an electron in modern physics, how is its behaviour described, which experimentally established laws govern it, and what happens when its experimentally established relation structure is analysed through the Ω-Lab relation-first framework?

## 2. Scope and epistemic rule

This experiment separates four layers:

1. established experimental/physical facts;
2. mathematical laws used to model those facts;
3. analytical observations produced by the Ω-Lab representation;
4. Ω hypotheses, which remain hypotheses unless independently tested.

The experiment does NOT attempt to redefine the electron, replace the Standard Model, or infer that the electron is literally made from Ω relation units.

## 3. Established physical definition

The electron is an elementary charged lepton and a fermion. It has electric charge -e, rest mass about 0.51099895 MeV/c², and intrinsic spin 1/2. The electron is treated in the Standard Model as an elementary particle, i.e. not as a known composite object. Current experiments have not established a finite internal structure or substructure.

The most useful modern description is field-theoretic: the electron is a quantum excitation of the electron field. The field exists throughout spacetime; an electron detected in an experiment is a quantized state/excitation of that field. This is more accurate than the classical picture of a tiny hard ball moving along a definite trajectory.

The positron is the electron's antiparticle. It has the same mass and spin magnitude and the opposite electric charge.

## 4. Numerical reference values

Using NIST 2022 CODATA and the 2025 PDG update:

- elementary charge: e = 1.602176634 × 10^-19 C, exact in the SI;
- electron charge: q_e = -e;
- electron mass: m_e = 9.1093837139 × 10^-31 kg (2022 CODATA);
- electron rest energy: m_e c² ≈ 0.51099895069 MeV;
- spin: J = 1/2;
- Compton wavelength: λ_C = h/(m_e c) ≈ 2.426310235 × 10^-12 m;
- reduced Compton wavelength: ħ/(m_e c) ≈ 3.861592674 × 10^-13 m;
- classical electron radius: r_e ≈ 2.8179403205 × 10^-15 m.

Important: r_e is a classical electromagnetic scale, not a measured physical radius of the electron.

PDG 2025 gives a mean-life lower limit for the electron of τ > 6.6 × 10^28 years (90% CL), so the electron is experimentally stable on all ordinary and currently accessible timescales.

## 5. What "electron works" means

An electron does not have a mechanical operating principle like a machine. Its behaviour is determined by the state of the electron field, its quantum state, its interactions with other fields, and the boundary/initial conditions of the experiment.

At the deepest currently tested level relevant here:

- the electron field is a quantum fermion field;
- its free relativistic dynamics are described by the Dirac equation;
- its electromagnetic interaction is described by quantum electrodynamics (QED);
- weak interactions are described by the electroweak Standard Model;
- its mass is connected to its Yukawa coupling to the Higgs field;
- gravity acts on its energy-momentum, although gravity is negligible compared with electromagnetism for ordinary electron-scale laboratory phenomena;
- when many electrons are present, Fermi-Dirac statistics and the Pauli exclusion principle become essential.

## 6. Dirac equation

For a free electron, the relativistic wave equation is

(i ħ γ^μ ∂_μ - m c) ψ = 0.

Here ψ is a four-component spinor field/state, γ^μ are Dirac matrices, and m is the electron mass.

The equation simultaneously incorporates:

- special relativity;
- quantum mechanics;
- intrinsic spin 1/2;
- the existence of negative-energy/antiparticle solutions, interpreted in quantum field theory through the positron.

For electromagnetic coupling, the derivative is replaced by the gauge-covariant derivative. In compact form the interaction is introduced through

D_μ = ∂_μ + i q A_μ/ħ

(up to sign/convention choices), where A_μ is the electromagnetic four-potential and q is the electron charge.

This is the mathematical point where the electron's electric charge becomes a coupling to the electromagnetic field.

## 7. Quantum electrodynamics

QED is the quantum field theory of charged leptons and the electromagnetic field.

The schematic QED Lagrangian is

L_QED = ψ̄(i γ^μ D_μ - m)ψ - 1/4 F_{μν}F^{μν}.

The electromagnetic field is represented by A_μ and its field tensor F_{μν}. The electron couples to the photon field through its electric charge.

The popular statement that "two electrons exchange photons" is a useful perturbative description of electromagnetic interaction. It should not be interpreted as saying that a literal little photon is continuously flying back and forth between classical particles. In QED the interaction is described by quantum amplitudes; Feynman diagrams are a calculation language for those amplitudes.

## 8. Classical limit

When quantum and relativistic effects can be neglected, the electron can be approximated by a classical charged particle.

The Lorentz force is

F = q(E + v × B).

For an electron q = -e, so the force is opposite to the electric-field direction for a purely electric field.

The corresponding acceleration in a weak-field, nonrelativistic limit is approximately

a = qE/m.

For E = 1 V/m, the magnitude is approximately

|a| = eE/m_e ≈ 1.7588 × 10^11 m/s².

This is not a new result; it is a numerical sanity check showing how the same charge and mass parameters reproduce the classical response.

## 9. Magnetic motion

In a uniform magnetic field with v perpendicular to B, the nonrelativistic cyclotron angular frequency is

ω_c = |q|B/m.

For one tesla and an electron, the corresponding frequency is approximately

f_c = |q|B/(2πm_e) ≈ 27.992 GHz.

Relativistically, the effective frequency depends on the electron energy through the Lorentz factor.

The electron also has intrinsic spin and a magnetic moment. The electron g-factor is very close to -2, with the measured anomaly giving (g-2)/2 ≈ 0.00115965218062 in the PDG 2025 summary. The small deviation from the Dirac value is one of the classic precision tests of QED.

## 10. Wave behaviour

An electron is not adequately described as only a particle with a classical trajectory.

Its de Broglie wavelength is

λ = h/p.

For a nonrelativistic electron of kinetic energy E,

p ≈ √(2mE).

Numerical checks:

- 1 eV electron: λ ≈ 1.226 nm;
- 100 eV electron: λ ≈ 0.1226 nm;
- 1 keV electron: λ ≈ 0.0388 nm.

These scales are directly relevant to electron diffraction and microscopy. Davisson-Germer-type electron diffraction experiments demonstrated that electrons exhibit wave behaviour.

The correct statement is not that the electron sometimes "turns into a wave". Quantum theory assigns a state/amplitude whose evolution produces particle-like detection events and wave-like interference/diffraction patterns.

## 11. Uncertainty principle

For position and momentum,

Δx Δp ≥ ħ/2.

This is not merely a limitation of a bad measuring instrument. It is a structural property of quantum states because position and momentum are represented by non-commuting operators.

Therefore a bound electron in an atom cannot be understood as a tiny planet following a sharply defined classical orbit around the nucleus.

## 12. Electron in an atom

For hydrogen-like atoms, the dominant interaction is electromagnetic attraction between the negative electron charge and the positive nucleus.

In the simplest nonrelativistic approximation, the electron is described by the Schrödinger equation with Coulomb potential

V(r) = -e²/(4π ε₀ r).

The ground-state energy of hydrogen is approximately

E_1 = -13.6057 eV,

and the Bohr radius is

a₀ = 4π ε₀ ħ²/(m_e e²) ≈ 5.29177 × 10^-11 m.

These are not evidence that the electron literally travels in a circular Bohr orbit. The modern description uses stationary quantum states/orbitals and probability amplitudes.

For high precision, relativistic Dirac theory, QED corrections, nuclear motion, recoil, spin interactions and other corrections become important.

## 13. Statistics and Pauli exclusion

The electron is a fermion. Identical electrons obey Fermi-Dirac statistics.

The Pauli exclusion principle states that two identical electrons cannot occupy the same complete quantum state.

This principle is essential for:

- atomic shell structure;
- the periodic table;
- stability and structure of matter;
- electron degeneracy in dense matter;
- the electronic properties of solids.

The Pauli principle is not an additional classical force acting between electrons. It follows from the quantum-statistical structure of identical fermions.

## 14. Interaction hierarchy

### Electromagnetic interaction

This is the dominant ordinary interaction of an electron. It governs electrical forces, atomic binding, conduction, scattering, radiation and most laboratory electron dynamics.

### Weak interaction

The electron participates in the electroweak interaction through W and Z bosons. Weak processes include beta decay and neutrino-related processes. The weak interaction is much less important than electromagnetism for ordinary electron motion, but it is fundamental to the Standard Model.

### Strong interaction

The electron has no colour charge and does not participate directly in the strong interaction as quarks and gluons do.

### Gravity

The electron has energy and momentum and therefore gravitates. For ordinary microscopic laboratory situations, gravity is overwhelmingly weaker than electromagnetic interaction and can normally be neglected.

## 15. Higgs field and electron mass

The Standard Model connects the electron mass to its Yukawa coupling with the Higgs field.

Schematically,

m_e = y_e v/√2,

where v is the Higgs vacuum expectation value and y_e is the electron Yukawa coupling.

Using v ≈ 246.22 GeV gives a very small dimensionless Yukawa coupling of roughly

y_e ≈ 2.94 × 10^-6.

This explains the framework in which the electron mass parameter arises, but it does not explain why nature chooses exactly that Yukawa value. The numerical value remains an input of the Standard Model.

## 16. Conservation laws relevant to the electron

Electron processes are constrained by conservation laws and symmetries, including:

- conservation of electric charge;
- conservation of energy and momentum;
- conservation of angular momentum;
- conservation of electric charge in electromagnetic interactions;
- Lorentz symmetry/relativistic invariance;
- gauge symmetry underlying the electromagnetic interaction;
- fermionic quantum statistics and the Pauli principle.

Lepton-number accounting is useful in Standard Model processes, although one must distinguish exact gauge-charge conservation from approximate/global bookkeeping rules and from the fact that neutrino flavour mixing complicates flavour-specific lepton numbers.

## 17. Why the electron is stable

The electron is the lightest known charged lepton. A hypothetical decay into only neutral lighter particles would have to preserve electric charge, which immediately blocks an ordinary decay into neutral final states. More exotic charge-conserving possibilities are also experimentally constrained.

PDG 2025 quotes an electron mean-life lower limit of τ > 6.6 × 10^28 years at 90% confidence.

Thus "the electron is stable" is shorthand for a very strong experimental and Standard Model statement, not a metaphysical claim that no deeper theory could ever change it.

## 18. Experimental anchors

The electron is not accepted as fundamental because of a philosophical assumption. Its properties are supported by many independent classes of measurements, including:

- cathode-ray and charge-to-mass measurements;
- electron scattering;
- atomic spectroscopy;
- electron diffraction;
- Penning-trap mass and magnetic-moment measurements;
- cyclotron and synchrotron motion;
- QED precision tests;
- collider experiments;
- tests of electron/positron charge and mass equality;
- searches for electron decay and substructure.

A particularly important methodological point is that the same small set of parameters repeatedly predicts results across very different experimental systems.

## 19. Ω-Lab relation-first representation

The electron was represented without changing its established physics.

Primary relation nodes:

E = electron
γ = electromagnetic/photon field
W/Z = weak interaction carriers
H = Higgs field
G = gravitational field/spacetime coupling
N = external matter/nucleus
M = measurement/detector

Principal relations:

E --EM coupling--> γ
E --weak coupling--> W/Z
E --mass/Yukawa relation--> H
E --energy-momentum--> G
E --electromagnetic binding/scattering--> N
E --quantum-state/measurement relation--> M
E --fermionic statistics--> other identical electrons
E --spin/magnetic-moment relation--> electromagnetic field

Dynamic states include:

free → accelerated → scattered → bound → excited → ionized

and, when an antiparticle is present,

e⁻ + e⁺ → annihilation channels.

These are relation structures, not claims that the listed fields are physical subcomponents of an electron.

## 20. Ω-Lab control against false ontology

A critical control was applied:

DO NOT map

charge -e → Ω relation -1

or

spin 1/2 → Ω relation class

as if the numerical similarity were a physical identity.

Ω relation classes are a modelling language. The electron's charge is a measured physical property with a precise unit definition; Ω's -1/0/+1 classes are model states. Conflating them would be a category error.

The same control applies to the earlier Ω-PHYS-CROSSCHECK-001 result concerning e/3 charge bookkeeping.

## 21. Ω structural observations

Observation O1: The electron is not adequately characterised by one scalar property. Its experimentally relevant identity is a coupled signature of charge, mass, spin, magnetic moment, statistics, field coupling and allowed transitions.

Observation O2: The most informative description is relational. The electron's behaviour is determined not by an isolated list of numbers but by how its quantum state couples to electromagnetic, weak, Higgs, gravitational and environmental degrees of freedom.

Observation O3: Stable macroscopic phenomena involving electrons emerge from repeated relations: electron-nucleus binding, electron-electron statistics, electromagnetic fields, lattice interactions and measurement/environmental coupling.

Observation O4: The relation-first representation is compatible with the established physics, but compatibility is not evidence that relations are ontologically more fundamental than fields or particles.

Observation O5: The electron provides a strong test case for Ω because its behaviour is known with unusually high precision and across multiple scales.

## 22. What the laboratory did NOT find

The experiment did NOT derive:

- the electron from Ω relations;
- the electron charge;
- the electron mass;
- spin 1/2;
- QED;
- the Standard Model;
- the Higgs mechanism;
- a new particle;
- a new physical law.

No claim of new physics is justified by this analysis.

## 23. Preliminary Ω hypothesis generated by the cross-check

H-E1:

A sufficiently rich relation graph may encode a particle's experimentally relevant behavioural signature without treating the particle as an isolated primitive object.

This is testable as a representation/compression hypothesis.

H-E2:

Some stable physical states may be recognisable as attractor-like or persistent configurations in a relation/state graph.

This is a hypothesis about modelling and emergence, not a claim that physical particles literally are graph attractors.

H-E3:

If Ω is useful beyond relabelling known physics, a relation-first representation should reproduce or predict nontrivial observables on held-out systems better than an appropriate baseline, without importing the target answer into the relation encoding.

## 24. Required next experiment

Construct a blind relation encoding for a small set of elementary particles and interactions using only experimentally specified observables, then test whether stable relation signatures cluster by particle type without supplying particle labels during feature construction.

Controls must include:

- shuffled relations;
- randomised relation weights;
- removal of one interaction class at a time;
- alternative graph encodings;
- a standard baseline classifier/graph method;
- held-out particle/process data.

The target result must be specified before analysis.

## 25. Laboratory verdict

Status: COMPATIBLE / NOT CONFIRMATORY.

The electron fits naturally into a relation-first description because its observable behaviour is defined through interactions, symmetries, conservation laws and transitions. However, this is expected: modern physics itself is fundamentally relational in the operational sense that measurable behaviour is defined by interactions between fields, particles and measuring apparatus.

The present experiment therefore strengthens the case for testing Ω as an analytical representation, but it does not support the stronger ontological claim that the electron is literally an emergent object made from Ω relations.

The next useful step is a blinded comparative experiment, not a philosophical extrapolation.

## 26. Reproducibility record

External reference set used:

- NIST CODATA 2022 recommended constants;
- Particle Data Group 2025 update;
- CERN Standard Model and Higgs/interaction explanatory material;
- established electron diffraction evidence.

Computational sanity checks independently reproduced:

- electron rest energy;
- Compton wavelength;
- classical electron radius;
- 1 T cyclotron frequency;
- de Broglie wavelengths at selected electron energies;
- hydrogen Bohr radius and ground-state energy;
- approximate electron Yukawa coupling from m_e = y_e v/√2.

No empirical laboratory apparatus was claimed. This record is an analytical and computational cross-check of established physics.

## 27. Final Ω-Lab statement

> The electron is not best understood as a tiny charged ball. It is an excitation of a quantum fermion field with a precisely measured charge, mass, spin and magnetic moment, whose behaviour is governed by quantum mechanics, special relativity, QED and the electroweak Standard Model, with gravity as a universal but ordinarily negligible interaction at this scale. Its observable identity is inseparable from its relations to other fields, particles, states and measurements.
>
> Ω-Lab can represent those relations and test whether useful structure emerges from them. It cannot declare that this representation is the underlying ontology without a separate predictive experimental success.

## Sources

1. NIST, CODATA 2022: https://physics.nist.gov/constants
2. NIST, 2022 CODATA full tables: https://physics.nist.gov/cuu/pdf/wall_2022.pdf
3. Particle Data Group, 2025 update: https://pdg.lbl.gov/2025/
4. PDG 2025 lepton summary: https://pdg.lbl.gov/2025/tables/rpp2025-sum-leptons.pdf
5. PDG 2025 electron listing: https://pdg.lbl.gov/2025/listings/rpp2025-list-electron.pdf
6. CERN, Standard Model: https://home.cern/science/physics/standard-model/
7. CERN, Higgs mechanism: https://home.cern/science/physics/origins-brout-englert-higgs-mechanism/
8. CERN, force carriers and electron-photon interaction: https://home.cern/science/physics/higgs-boson/what/
9. APS, electron diffraction / Davisson-Germer: https://physics.aps.org/story/v17/st17
10. Existing Ω-Lab physics cross-check: research/RELATIONS/experiments/OMEGA-PHYS-CROSSCHECK-001.md
