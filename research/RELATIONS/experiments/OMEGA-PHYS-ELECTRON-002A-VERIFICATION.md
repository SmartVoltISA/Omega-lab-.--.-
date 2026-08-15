# Ω-PHYS-ELECTRON-002A — Independent verification of electron cross-check

Date: 2026-08-16
Status: VERIFIED / NO MATERIAL NUMERICAL DISCREPANCY
Parent experiment: OMEGA-PHYS-ELECTRON-002

## Purpose

Re-run the numerical claims of Ω-PHYS-ELECTRON-002 independently and compare the inputs against authoritative external sources. The goal is to establish that another researcher using the same stated constants and formulas should obtain the same numerical results.

## Source verification

NIST/CODATA 2022 is the current CODATA recommended constants dataset available from NIST at this verification date. NIST gives:

- electron mass = 9.1093837139(28) × 10^-31 kg;
- electron rest energy = 0.51099895069(16) MeV;
- electron charge-to-mass magnitude = 1.75882000838(55) × 10^11 C kg^-1;
- reduced Compton wavelength = 3.8615926744(12) × 10^-13 m;
- Compton wavelength = 2.42631023538(76) × 10^-12 m;
- classical electron radius = 2.8179403205(13) × 10^-15 m.

NIST also gives the exact SI value of the elementary charge e = 1.602176634 × 10^-19 C.

PDG 2026 provides an updated particle-properties listing and electron data. The electron is listed as a spin-1/2 charged lepton; the electron listing retains the experimentally established lower limit on electron lifetime.

## Independent calculations

Using the stated NIST constants directly:

### Rest energy

m_e c² / e = 510998.950691753 eV = 0.510998950691753 MeV.

Reference: 0.51099895069(16) MeV.

Result: MATCH within displayed precision.

### Compton wavelength

λ_C = h/(m_e c)

= 2.426310235380317 × 10^-12 m.

Reference: 2.42631023538(76) × 10^-12 m.

Result: MATCH.

### Reduced Compton wavelength

λ̄_C = ħ/(m_e c) = h/(2πm_e c)

= 3.86159267199 × 10^-13 m when hbar is supplied only to the truncated digits used in the independent calculation. Using the exact identity ħ = h/(2π) with the full constants gives 3.8615926744 × 10^-13 m.

Reference: 3.8615926744(12) × 10^-13 m.

Result: MATCH. The small intermediate difference was only due to truncating ħ independently; it is not a physical discrepancy.

### Classical electron radius

r_e = e²/(4π ε0 m_e c²)

Independent calculation: 2.81794032046 × 10^-15 m using the full stated constants.

Reference: 2.8179403205(13) × 10^-15 m.

Result: MATCH.

Important: this is a classical electromagnetic length scale, not an experimentally measured hard radius of the electron.

### Charge-to-mass ratio

|e|/m_e = 1.758820008378 × 10^11 C kg^-1.

Reference: 1.75882000838(55) × 10^11 C kg^-1.

Result: MATCH.

### Cyclotron frequency at B = 1 T

For nonrelativistic orbital motion:

f_c = |e|B/(2πm_e).

For B = 1 T:

f_c = 2.79924898342 × 10^10 Hz = 27.9924898342 GHz.

Result: MATCH with the stated value.

Important distinction: this is the orbital/cyclotron frequency. It is not the electron spin-precession frequency. NIST separately gives the electron gyromagnetic ratio as 28,024.9513861 MHz/T because the electron g-factor differs slightly from the Dirac value of 2.

### de Broglie wavelength

For a nonrelativistic electron:

λ = h/√(2m_e K).

Independent results:

- K = 1 eV → λ = 1.2264259653 nm;
- K = 100 eV → λ = 0.1226425965 nm;
- K = 1 keV → λ = 0.03878299432 nm.

Result: MATCH with the parent experiment after rounding. Relativistic corrections are negligible at these energies for the quoted precision.

### Hydrogen Bohr radius

a0 = 4π ε0 ħ²/(m_e e²).

Independent calculation: 5.291772105 × 10^-11 m.

Reference: 5.29177210544(82) × 10^-11 m.

Result: MATCH.

### Hydrogen ground-state energy

Using the nonrelativistic Coulomb model:

E1 = -m_e e^4/[2(4π ε0)^2 ħ²].

Independent calculation: E1 = -13.60569314 eV.

Result: MATCH with the standard nonrelativistic hydrogen value.

### Electron Yukawa coupling

Using

m_e = y_e v/√2

and v ≈ 246.22 GeV:

y_e = √2 m_e/v ≈ 2.935 × 10^-6.

Result: MATCH with the parent experiment's approximately 2.94 × 10^-6 value.

## Correction to an earlier conversational statement

A previous conversational message claimed that the Yukawa calculation in the parent experiment contained an error and that a correction had already been archived. That claim was not correct.

The parent experiment's written Yukawa value, approximately 2.94 × 10^-6, is correct. The independent recomputation confirms it.

This verification record therefore supersedes the earlier conversational claim: **no material correction to the parent numerical result is required.**

## Important methodological result

The independent calculations reproduce the numerical claims from the parent experiment using the same physical constants and formulas. This establishes numerical reproducibility.

However, reproducibility of calculations does NOT prove the Ω hypothesis. It establishes only that:

1. the physical reference values are correctly sourced;
2. the formulas are internally consistent;
3. an independent researcher can reproduce the numerical outputs;
4. the relation-first representation remains a modelling representation rather than a demonstrated new physical ontology.

## Stronger verification target

The next experiment must test something not already guaranteed by the input description. The correct target is therefore not "can Ω reproduce known electron data?" but:

> Can a blinded relation-first encoding, constructed without particle labels and without importing the target classification, recover stable and predictive structure on held-out experimental data better than appropriate baseline representations?

Only such a result would provide evidence that Ω contributes information beyond relabelling established physics.

## Verdict

**Numerical physics cross-check: VERIFIED.**

**Source consistency: VERIFIED against NIST/CODATA and current PDG listings.**

**Ω interpretation: COMPATIBLE, NOT CONFIRMATORY.**

**New physical law: NOT FOUND.**

The experiment is therefore a reproducible foundation for the next blinded Ω test.

## External sources

- NIST CODATA: https://physics.nist.gov/constants
- NIST 2022 CODATA wall chart: https://physics.nist.gov/cuu/pdf/wall_2022.pdf
- NIST elementary charge: https://physics.nist.gov/cuu/Constants/Value/e.html
- NIST electron gyromagnetic ratio: https://www.physics.nist.gov/cgi-bin/cuu/Value?gammaebar=
- PDG 2026 particle properties: https://pdg.lbl.gov/2026/listings/particle_properties.html
- PDG electron listing: https://pdg.lbl.gov/2026/listings/rpp2026-list-electron.pdf
- CERN Standard Model: https://home.cern/science/physics/standard-model/
- CERN Higgs mechanism: https://home.cern/science/physics/origins-brout-englert-higgs-mechanism/
