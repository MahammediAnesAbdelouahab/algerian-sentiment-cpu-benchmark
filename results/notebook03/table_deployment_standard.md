| dataset | model | format | macro-F1 (%) | Δ vs native (pts) | size (MiB) | serving peak RSS (MiB) | batch peak RSS (MiB) | cold start (s) | p50 (ms) | p95 (ms) | p50 range across passes (ms) | p50 spread (% of median) | passes | speed-up vs PyTorch fp32 | same predictions as notebook 02 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| twifil_clean | SVM-char | scikit-learn | 60.8 | 0.0 | 3.0 | 204.0 | 202.0 | 2.06 | 1.04 | 1.31 | 1.00–1.61 | 58.6 | 5 |  | True |
| twifil_clean | NB-char | scikit-learn | 60.4 | 0.0 | 4.6 | 195.0 | 195.0 | 1.89 | 1.55 | 1.91 | 1.52–1.57 | 3.0 | 5 |  | True |
| twifil_clean | LR-word+char | scikit-learn | 61.0 | 0.0 | 3.4 | 206.0 | 206.0 | 1.74 | 2.71 | 3.42 | 2.61–4.14 | 56.4 | 5 |  | True |
| twifil_clean | mE5-small | ONNX int8 | 69.8 | -0.01 | 129.1 | 473.0 | 519.0 | 2.46 | 14.43 | 32.72 | 13.91–14.96 | 7.2 | 5 | 2.58 | True |
| twifil_clean | mE5-small | ONNX int8 per-channel+RR | 69.9 | 0.1 | 129.3 | 473.0 | 519.0 | 2.55 | 15.39 | 34.6 | 13.98–15.58 | 10.4 | 5 | 2.42 | True |
| twifil_clean | mE5-small | ONNX fp32 | 69.8 | 0.0 | 465.3 | 876.0 | 875.0 | 4.6 | 24.11 | 52.33 | 22.26–24.89 | 10.9 | 5 | 1.54 | True |
| twifil_clean | DziriBERT | ONNX int8 | 70.5 | -0.3 | 120.6 | 250.0 | 316.0 | 1.37 | 36.62 | 85.81 | 36.33–39.82 | 9.5 | 5 | 3.02 | True |
| twifil_clean | mE5-small | PyTorch fp32 | 69.8 | 0.0 | 465.1 | 1011.0 | 1215.0 | 12.6 | 37.22 | 68.34 | 36.74–38.30 | 4.2 | 5 | 1.0 | True |
| twifil_clean | MARBERTv2 | ONNX int8 | 67.8 | -2.54 | 158.6 | 292.0 | 366.0 | 1.69 | 39.43 | 100.24 | 37.67–40.16 | 6.3 | 5 | 2.81 | True |
| twifil_clean | DziriBERT | ONNX int8 per-channel+RR | 70.7 | -0.1 | 121.0 | 247.0 | 342.0 | 1.24 | 39.68 | 86.92 | 37.01–40.09 | 7.8 | 5 | 2.79 | True |
| twifil_clean | MARBERTv2 | ONNX int8 per-channel+RR | 69.4 | -1.0 | 159.0 | 297.0 | 385.0 | 1.49 | 40.0 | 102.32 | 38.30–41.04 | 6.9 | 5 | 2.77 | True |
| twifil_clean | CAMeLBERT-DA | ONNX int8 | 58.8 | -6.96 | 105.5 | 231.0 | 376.0 | 1.0 | 44.06 | 127.9 | 43.27–46.31 | 6.9 | 5 | 2.64 | True |
| twifil_clean | CAMeLBERT-DA | ONNX int8 per-channel+RR | 59.9 | -5.87 | 105.9 | 245.0 | 397.0 | 1.0 | 45.43 | 129.87 | 43.49–46.76 | 7.2 | 5 | 2.56 | True |
| twifil_clean | DziriBERT | ONNX fp32 | 70.8 | 0.0 | 476.1 | 744.0 | 841.0 | 3.83 | 67.3 | 143.59 | 66.38–68.42 | 3.0 | 5 | 1.64 | True |
| twifil_clean | MARBERTv2 | ONNX fp32 | 70.4 | 0.0 | 624.0 | 975.0 | 991.0 | 5.03 | 68.18 | 157.35 | 65.49–71.66 | 9.1 | 5 | 1.62 | True |
| twifil_clean | CAMeLBERT-DA | ONNX fp32 | 65.8 | 0.0 | 417.1 | 697.0 | 862.0 | 2.99 | 78.45 | 190.42 | 77.15–79.15 | 2.6 | 5 | 1.48 | True |
| twifil_clean | DziriBERT | PyTorch fp32 | 70.8 | 0.0 | 475.9 | 909.0 | 1075.0 | 9.85 | 110.67 | 209.53 | 106.72–115.41 | 7.8 | 5 | 1.0 | True |
| twifil_clean | MARBERTv2 | PyTorch fp32 | 70.4 | 0.0 | 623.8 | 943.0 | 1193.0 | 10.32 | 110.73 | 221.27 | 109.28–114.21 | 4.5 | 5 | 1.0 | True |
| twifil_clean | CAMeLBERT-DA | PyTorch fp32 | 65.8 | 0.0 | 416.9 | 889.0 | 1155.0 | 9.53 | 116.2 | 260.89 | 111.90–120.61 | 7.5 | 5 | 1.0 | True |
| youtube | SVM-char | scikit-learn | 76.8 | 0.0 | 10.0 | 261.0 | 260.0 | 2.57 | 1.02 | 1.63 | 1.01–1.36 | 34.7 | 5 |  | True |
| youtube | NB-char | scikit-learn | 73.1 | 0.0 | 15.2 | 257.0 | 255.0 | 2.56 | 2.97 | 4.05 | 2.84–5.36 | 84.5 | 5 |  | True |
| youtube | LR-word+char | scikit-learn | 75.9 | 0.0 | 14.0 | 305.0 | 304.0 | 2.97 | 4.73 | 5.87 | 4.70–4.80 | 2.2 | 5 |  | True |
| youtube | mE5-small | ONNX int8 per-channel+RR | 75.8 | -0.34 | 129.3 | 474.0 | 621.0 | 1.82 | 14.42 | 46.93 | 13.61–16.03 | 16.8 | 5 | 2.52 | True |
| youtube | mE5-small | ONNX int8 | 75.6 | -0.53 | 129.1 | 474.0 | 622.0 | 1.8 | 14.68 | 50.81 | 13.28–15.19 | 13.0 | 5 | 2.48 | True |
| youtube | mE5-small | ONNX fp32 | 76.1 | 0.0 | 465.3 | 876.0 | 956.0 | 4.51 | 23.41 | 74.27 | 22.34–24.47 | 9.1 | 5 | 1.55 | True |
| youtube | DziriBERT | ONNX int8 | 79.7 | -0.44 | 120.6 | 271.0 | 512.0 | 1.38 | 33.96 | 121.21 | 33.30–35.63 | 6.8 | 5 | 3.13 | True |
| youtube | DziriBERT | ONNX int8 per-channel+RR | 79.8 | -0.41 | 121.0 | 253.0 | 472.0 | 1.39 | 33.99 | 121.68 | 33.68–35.03 | 4.0 | 5 | 3.12 | True |
| youtube | MARBERTv2 | ONNX int8 | 79.1 | 0.09 | 158.6 | 322.0 | 548.0 | 1.52 | 35.63 | 125.25 | 34.63–36.06 | 4.0 | 5 | 3.01 | True |
| youtube | mE5-small | PyTorch fp32 | 76.1 | 0.0 | 465.1 | 1016.0 | 1326.0 | 12.93 | 36.35 | 92.45 | 35.12–37.26 | 5.9 | 5 | 1.0 | True |
| youtube | MARBERTv2 | ONNX int8 per-channel+RR | 78.4 | -0.66 | 159.0 | 300.0 | 538.0 | 1.58 | 36.51 | 121.05 | 35.83–37.55 | 4.7 | 5 | 2.93 | True |
| youtube | CAMeLBERT-DA | ONNX int8 | 72.2 | -3.21 | 105.5 | 265.0 | 606.0 | 1.08 | 40.82 | 139.99 | 38.98–42.02 | 7.5 | 5 | 2.75 | True |
| youtube | CAMeLBERT-DA | ONNX int8 per-channel+RR | 74.2 | -1.2 | 105.9 | 243.0 | 621.0 | 1.24 | 41.56 | 140.41 | 39.60–43.91 | 10.4 | 5 | 2.7 | True |
| youtube | DziriBERT | ONNX fp32 | 80.2 | 0.0 | 476.1 | 752.0 | 956.0 | 4.63 | 64.82 | 181.92 | 63.93–67.30 | 5.2 | 5 | 1.64 | True |
| youtube | MARBERTv2 | ONNX fp32 | 79.0 | 0.0 | 624.0 | 975.0 | 1115.0 | 4.92 | 65.21 | 179.96 | 63.73–66.18 | 3.8 | 5 | 1.64 | True |
| youtube | CAMeLBERT-DA | ONNX fp32 | 75.4 | 0.0 | 417.1 | 693.0 | 911.0 | 2.99 | 72.06 | 205.12 | 68.61–76.97 | 11.6 | 5 | 1.56 | True |
| youtube | DziriBERT | PyTorch fp32 | 80.2 | 0.0 | 475.9 | 921.0 | 1212.0 | 9.79 | 106.19 | 257.05 | 95.78–107.23 | 10.8 | 5 | 1.0 | True |
| youtube | MARBERTv2 | PyTorch fp32 | 79.0 | 0.0 | 623.8 | 958.0 | 1394.0 | 9.66 | 107.08 | 252.42 | 105.56–110.95 | 5.0 | 5 | 1.0 | True |
| youtube | CAMeLBERT-DA | PyTorch fp32 | 75.4 | 0.0 | 416.9 | 899.0 | 1176.0 | 9.56 | 112.41 | 272.86 | 107.20–113.35 | 5.5 | 5 | 1.0 | True |
