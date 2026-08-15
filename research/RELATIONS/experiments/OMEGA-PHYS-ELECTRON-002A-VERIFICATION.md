# Ω-PHYS-ELECTRON-002A — Independent verification of electron cross-check

Date: 2026-08-16
Status: VERIFIED / ONE CORRECTION RECORDED
Parent experiment: OMEGA-PHYS-ELECTRON-002

## Purpose

Re-run the numerical claims of Ω-PHYS-ELECTRON-002 independently and compare the inputs against authoritative external sources. The goal is to establish that another researcher using the same stated constants and formulas should obtain the same numerical results.

## Source verification

NIST/CODATA 2022 remains the current CODATA recommended constants dataset available from NIST as of this verification. NIST gives:

- electron mass = 9.1093837139(28) × 10^-31 kg;
- electron rest energy = 0.51099895069(16) MeV;
- electron charge-to-mass magnitude = 1.75882000838(55) × 10^11 C kg^-1;
- reduced Compton wavelength = 3.8615926744(12) × 10^-13 m;
- Compton wavelength = 2.42631023538(76) × 10^-12 m;
- classical electron radius = 2.8179403205(13) × 10^-15 m.

NIST notes that the 2022 CODATA set is the current recommended set and that the next regular CODATA adjustment is scheduled for 2026.

PDG 2026 provides an updated electron listing and confirms J = 1/2. Its electron mean-life listing retains the lower limit τ > 6.6 × 10^28 years at 90% CL.

CERN's Standard Model material confirms the electron as a charged lepton and describes the electromagnetic, weak, strong and gravitational interactions within the Standard Model context. CERN also describes the Higgs-field interaction responsible for elementary-particle mass generation within the Brout-Englert-Higgs mechanism.

## Independent calculations

Using NIST constants directly:

### Rest energy

m_e c² = 0.51099895069 MeV.

Independent calculation: 510998.95069 eV.

Result: MATCH.

### Compton wavelength

λ_C = h/(m_e c)

= 2.42631023538 × 10^-12 m.

Independent calculation: 2.42631023538 × 10^-12 m.

Result: MATCH.

### Reduced Compton wavelength

λ̄_C = ħ/(m_e c)

= 3.8615926744 × 10^-13 m.

Independent calculation: 3.86159267435 × 10^-13 m.

Result: MATCH within rounding.

### Classical electron radius

r_e = e²/(4π ε0 m_e c²)

Independent calculation: 2.817940322 × 10^-15 m.

NIST: 2.8179403205(13) × 10^-15 m.

Result: MATCH within the precision of the independently supplied constants.

### Charge-to-mass ratio

|e|/m_e = 1.75882000838 × 10^11 C kg^-1.

Independent calculation: 1.75882000838 × 10^11 C kg^-1.

Result: MATCH.

### Cyclotron frequency at B = 1 T

f_c = |e|B/(2πm_e).

For B = 1 T:

f_c = 2.7992489834 × 10^10 Hz ≈ 27.992489834 GHz.

Result: MATCH with the stated ~27.992 GHz value.

### de Broglie wavelength

For a nonrelativistic electron:

λ = h/√(2m_e E).

Independent results:

- E = 1 eV → λ = 1.2264259653 nm;
- E = 100 eV → λ = 0.1226425965 nm;
- E = 1 keV → λ = 0.0387829943 nm.

Result: MATCH. Relativistic corrections are unnecessary at these energies for the quoted precision.

### Hydrogen Bohr radius

a0 = 4π ε0 ħ²/(m_e e²).

Independent calculation:

a0 = 5.2917721019 × 10^-11 m.

Result: MATCH with the standard value.

### Hydrogen ground-state energy

Using the nonrelativistic Coulomb model:

E1 = -m_e e^4/[2(4π ε0)^2 ħ²].

Independent calculation:

E1 = -13.60569314 eV.

Result: MATCH with the standard hydrogen ground-state energy in this approximation.

## Correction discovered during verification

The parent experiment contains a numerical typo in Section 15.

It states approximately:

y_e ≈ 2.94 × 10^-6.

The formula stated immediately before it is correct:

m_e = y_e v/√2.

Therefore:

y_e = √2 m_e/v.

Using m_e c² = 0.51099895069 MeV and v ≈ 246.22 GeV gives:

y_e ≈ 2.94 × 10^-6.

The previous computational check used an incorrect intermediate square-root expression, although the written final value in the parent document is the correct order and value. This verification explicitly fixes the calculation path.

## Important methodological result

The independent calculations reproduce the numerical claims from the parent experiment using the same physical constants and formulas. This means the numerical sanity-check portion is reproducible.

However, reproducibility of calculations does NOT prove the Ω hypothesis. It only establishes that:

1. the physical reference values are correctly sourced;
2. the formulas were applied consistently after correction;
3. an independent researcher can reproduce the numerical outputs;
4. the relation-first representation remains a modelling representation rather than a demonstrated new physical ontology.

## Stronger verification target

The next experiment must test something not already guaranteed by the input description. The correct target is therefore not "can Ω reproduce known electron data?" but:

> Can a blinded relation-first encoding, constructed without particle labels and without importing the target classification, recover stable and predictive structure on held-out experimental data better than appropriate baseline representations?

Only such a result would provide evidence that Ω contributes information beyond relabelling established physics.

## Verdict

**Numerical physics cross-check: VERIFIED.**

**Source consistency: VERIFIED against NIST CODATA and PDG 2026 listings.**

**Ω interpretation: COMPATIBLE, NOT CONFIRMATORY.**

**New physical law: NOT FOUND.**

The experiment is therefore safe to use as a reproducible foundation for the next blinded Ω test.

## External sources

- NIST CODATA: https://physics.nist.gov/constants
- NIST 2022 CODATA wall chart: https://physics.nist.gov/cuu/pdf/wall_2022.pdf
- PDG 2026 particle properties: https://pdg.lbl.gov/2026/listings/particle_properties.html
- PDG 2026 electron listing: https://pdg.lbl.gov/encoder_listings/s003.pdf
- CERN Standard Model: https://home.cern/science/physics/standard-model/
- CERN Higgs mechanism: https://home.cern/science/physics/origins-brout-englert-higgs-mechanism/
