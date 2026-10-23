| dataset | scenario | best configuration | macro-F1 (%) | size (MiB) | p95 (ms) | candidates that fit |
|---|---|---|---|---|---|---|
| twifil_clean | Tight budget (≤ 25 MiB, p95 ≤ 20 ms) | LR-word+char (scikit-learn) | 61.0 | 3.4 | 3.42 | 3 |
| twifil_clean | Moderate budget (≤ 150 MiB, p95 ≤ 100 ms) | DziriBERT (ONNX int8 per-channel+RR) | 70.7 | 121.0 | 86.92 | 7 |
| twifil_clean | No constraint | DziriBERT (ONNX fp32) | 70.8 | 476.1 | 143.59 | 19 |
| youtube | Tight budget (≤ 25 MiB, p95 ≤ 20 ms) | SVM-char (scikit-learn) | 76.8 | 10.0 | 1.63 | 3 |
| youtube | Moderate budget (≤ 150 MiB, p95 ≤ 100 ms) | SVM-char (scikit-learn) | 76.8 | 10.0 | 1.63 | 5 |
| youtube | No constraint | DziriBERT (ONNX fp32) | 80.2 | 476.1 | 181.92 | 19 |
