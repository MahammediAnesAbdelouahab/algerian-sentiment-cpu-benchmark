| dataset | model | seeds | fp32 macro-F1 (%) | Δ default (pts) | Δ default range | default: seeds / constant | Δ PC, no RR (pts) | Δ PC, no RR range | PC, no RR: seeds / constant | Δ PC+RR (pts) | Δ PC+RR range | PC+RR: seeds / constant |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| twifil_clean | DziriBERT | 3 | 70.8 ± 0.1 | -0.4 ± 0.7 | -1.1 to +0.2 | 3 / 0 | -1.0 ± 0.9 | -1.5 to +0.1 | 3 / 0 | -0.3 ± 0.7 | -1.0 to +0.3 | 3 / 0 |
| twifil_clean | MARBERTv2 | 3 | 70.3 ± 0.4 | -2.3 ± 0.7 | -2.9 to -1.5 | 3 / 0 | -51.9 ± 3.6 | -54.1 to -47.7 | 3 / 2 | -1.1 ± 0.5 | -1.6 to -0.6 | 3 / 0 |
| twifil_clean | CAMeLBERT-DA | 3 | 63.4 ± 2.5 | -16.9 ± 9.1 | -24.9 to -7.0 | 3 / 0 | -44.1 ± 1.1 | -45.0 to -43.0 | 3 / 2 | -15.8 ± 8.8 | -22.8 to -5.9 | 3 / 0 |
| twifil_clean | mE5-small | 3 | 70.1 ± 0.6 | -0.8 ± 0.8 | -1.6 to -0.0 | 3 / 0 | -0.3 ± 0.7 | -0.8 to +0.5 | 3 / 0 | -0.5 ± 0.5 | -0.8 to +0.1 | 3 / 0 |
| youtube | DziriBERT | 3 | 79.6 ± 0.8 | -0.1 ± 0.3 | -0.4 to +0.0 | 3 / 0 | -0.3 ± 0.8 | -1.2 to +0.5 | 3 / 0 | -0.2 ± 0.2 | -0.4 to -0.1 | 3 / 0 |
| youtube | MARBERTv2 | 3 | 79.1 ± 0.3 | -0.8 ± 0.8 | -1.3 to +0.1 | 3 / 0 | -61.5 ± 1.8 | -63.2 to -59.7 | 3 / 1 | -0.5 ± 0.4 | -0.7 to -0.1 | 3 / 0 |
| youtube | CAMeLBERT-DA | 3 | 75.9 ± 0.4 | -4.6 ± 1.5 | -6.2 to -3.2 | 3 / 0 | -59.3 ± 4.1 | -63.7 to -55.6 | 3 / 1 | -2.0 ± 1.7 | -3.9 to -0.9 | 3 / 0 |
| youtube | mE5-small | 3 | 76.1 ± 0.5 | -0.4 ± 0.4 | -0.7 to +0.0 | 3 / 0 | -0.8 ± 0.3 | -1.1 to -0.5 | 3 / 0 | -0.1 ± 0.3 | -0.3 to +0.3 | 3 / 0 |
