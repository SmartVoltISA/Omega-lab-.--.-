# Ω-MEM-4R Results

## P1 — Periodic-4

| Architecture | S=2 | S=4 | S=8 | S=16 | S=32 | S=64 |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | .500 | .500 | .500 | .500 | .500 | .500 |
| Counter | .500 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Random | .652 | .756 | .844 | .898 | .939 | .950 |
| Matched | 1.000* | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

*P1 Matched S=2 is internally forced to S=4; not a valid equal-S comparison.

**Observation:** expressiveness threshold at S=4 for the phase counter. Counter S=4 intervention showed a reported +0.500 immediate accuracy drop when reset to a different phase, with recovery within one period.

## P2 — True Markov-2

| Architecture | S=2 | S=4 | S=8 |
|---|---:|---:|---:|
| Baseline | .499 | .499 | .499 |
| Context-1 | .823 | .823 | .823 |
| Context-2 | .823 | .823 | .823 |
| Context-3 | .823 | .823 | .823 |
| Random | .577 | .634 | .682 |
| Matched | .823 | .823 | .823 |

The tested transition table produced a sufficient predictive partition using the last symbol; Context-2 adds only about 0.002 bits of conditional-entropy reduction over Context-1. This is evidence for a minimal-sufficient-statistic principle in this generator, not a universal theorem about all second-order Markov processes.

## P3 — Thue-Morse

| Architecture | S=2 | S=4 | S=8 | S=16 | S=32 | S=64 |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | .500 | .500 | .500 | .500 | .500 | .500 |
| Context-2 | .666 | .666 | .666 | .666 | .666 | .666 |
| Context-3 | .666 | .666 | .666 | .666 | .666 | .666 |
| Counter | .500 | .500 | .499 | .502 | .501 | .500 |
| Random | .558 | .596 | .632 | .663 | .701 | .730 |
| Matched | .500 | .500 | .499 | .502 | .501 | .500 |

**Critical counterexample:** the chosen matched position-counter does not encode sufficient predictive information for Thue-Morse at any tested S. Random S=64 reaches about .730 and Context-2/3 about .666.

Permutation contrast confirms predictive mapping for Context-3 (reported original ≈.666 vs permuted ≈.502). The reported Random S=64 ensemble permutation values were ≈.730 original and ≈.731 permuted; this means the ensemble-level permutation diagnostic is not interpretable as evidence of a unique fixed state→prediction map and should not be overclaimed.

## P4 — HMM

| Architecture | S=2 | S=4 | S=8 | S=16 | S=32 | S=64 |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | .494 | .494 | .494 | .494 | .494 | .494 |
| Context-1 | .704 | .704 | .704 | .704 | .704 | .704 |
| Context-2 | .700 | .700 | .700 | .700 | .700 | .700 |
| Random | .545 | .584 | .613 | .633 | .636 | .635 |
| Matched | .704 | .702 | .702 | .699 | .698 | .696 |

Conditional entropy of Matched decreased with S, approximately .873 → .822 bits, while accuracy did not improve. This is consistent with implementation/discretization loss and sparse state occupancy.

## P5 — Random-iid

All tested architectures remain approximately .50. The negative control behaves as expected.

## Equal-S comparison

- Periodic-4 S=8: Matched 1.000 vs Random .844.
- Markov-2 S=4: Matched .823 vs Random .634.
- Thue-Morse S=8: Matched .500 vs Random .632.
- HMM S=8: Matched .702 vs Random .613.

Reported paired t-tests: Periodic t=29.4; Markov-2 t=25.1; Thue-Morse t=-15.2; HMM t=8.7; all reported p<0.001.

## Status interpretation

H-MEM-2.2: REFINED, not universally confirmed. 3/4 structured processes support Matched > Random at representative equal S; Thue-Morse contradicts the universal version.

H-MEM-2.3: PARTIALLY CONFIRMED. Supported components: expressive threshold, process-specific minimal sufficient statistic, implementation loss, and successful iid negative control. Counterevidence: Thue-Morse and random-feature advantage over the hand-designed matched counter.

These results establish empirical observations for the tested generators and implementations. They do not establish a universal law connecting memory state count S to information volume, area, energy, Kolmogorov complexity, or physical reality.
