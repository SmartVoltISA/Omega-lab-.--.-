# Ω-INF-8 — Results

Date: 2026-08-13

## Execution audit

The protocol was independently executed after commit. 80 reconstructions were evaluated for each corpus and each policy. Exact trigram preservation was asserted for every reconstruction.

## Mean Δ zlib bytes (reconstruction minus original)

| Corpus | shuffle | random_pop | reverse | sorted |
|---|---:|---:|---:|---:|
| technical_ru | -3.1625 | -3.2625 | 0 | -11 |
| literary_ru | -1.8250 | -1.8500 | 0 | -10 |
| structured_en | +8.0000 | +8.2125 | 0 | 0 |
| randomish_en | -0.0375 | +0.1000 | 0 | 0 |

## Independent observables

For all trigram-preserving reconstructions, character entropy, bigram entropy, and unique-bigram count were invariant to numerical precision in the executed run. Therefore this particular falsification attempt did NOT find a change in those observables. Compression was the only observable among these four that varied.

## Sampling-policy result

The two stochastic policies (`shuffle` and `random_pop`) agreed in sign for the three non-null corpus classes: technical negative, literary negative, structured positive. The randomish corpus remained near zero and changed sign between policies.

The deterministic `reverse` and `sorted` controls are not stochastic samples and are therefore not treated as equivalent evidence about a distribution. They are included as adversarial controls.

## Interpretation

Ω-INF-8 did not break the narrow observation that trigram-preserving reconstructions can have different zlib sizes. It DID narrow the claim: among the tested observables, the effect was specific to compression; and its direction remained corpus-dependent.

This does not establish a universal property of information, semantics, or relations. It only makes the simple explanation "the result is caused solely by one random traversal implementation" less plausible for the tested corpora.

## Important methodological note

This experiment was executed from the committed protocol, not by trusting a generated result file. The result file is an archive of the independently calculated output.