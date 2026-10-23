| training data | model | test subset | n | accuracy (%) | macro-F1 (%) | seeds |
|---|---|---|---|---|---|---|
| trained on DziriBERT split | NB-char | all test tweets | 2360 | 73.0 | 72.9 | 1 |
| trained on DziriBERT split | NB-char | with text (link-only removed) | 2042 | 69.0 | 63.8 | 1 |
| trained on DziriBERT split | NB-char | kept by the audit | 1942 | 68.6 | 63.3 | 1 |
| trained on DziriBERT split | NB-char | kept by the audit, text unseen in training | 1844 | 67.3 | 62.1 | 1 |
| trained on DziriBERT split | SVM-char | all test tweets | 2360 | 73.6 | 73.3 | 1 |
| trained on DziriBERT split | SVM-char | with text (link-only removed) | 2042 | 69.7 | 64.0 | 1 |
| trained on DziriBERT split | SVM-char | kept by the audit | 1942 | 69.2 | 63.4 | 1 |
| trained on DziriBERT split | SVM-char | kept by the audit, text unseen in training | 1844 | 67.9 | 62.4 | 1 |
| trained on DziriBERT split | LR-word+char | all test tweets | 2360 | 72.6 | 72.1 | 1 |
| trained on DziriBERT split | LR-word+char | with text (link-only removed) | 2042 | 68.6 | 63.1 | 1 |
| trained on DziriBERT split | LR-word+char | kept by the audit | 1942 | 68.1 | 62.7 | 1 |
| trained on DziriBERT split | LR-word+char | kept by the audit, text unseen in training | 1844 | 66.4 | 61.2 | 1 |
| trained on DziriBERT split | DziriBERT | all test tweets | 2360 | 80.2 | 79.6 | 3 |
| trained on DziriBERT split | DziriBERT | with text (link-only removed) | 2042 | 77.3 | 72.5 | 3 |
| trained on DziriBERT split | DziriBERT | kept by the audit | 1942 | 76.9 | 72.2 | 3 |
| trained on DziriBERT split | DziriBERT | kept by the audit, text unseen in training | 1844 | 75.8 | 71.2 | 3 |
| trained on DziriBERT split | MARBERTv2 | all test tweets | 2360 | 80.0 | 79.4 | 3 |
| trained on DziriBERT split | MARBERTv2 | with text (link-only removed) | 2042 | 77.1 | 72.2 | 3 |
| trained on DziriBERT split | MARBERTv2 | kept by the audit | 1942 | 76.7 | 71.8 | 3 |
| trained on DziriBERT split | MARBERTv2 | kept by the audit, text unseen in training | 1844 | 75.8 | 71.2 | 3 |
| trained on DziriBERT split | CAMeLBERT-DA | all test tweets | 2360 | 75.5 | 74.8 | 3 |
| trained on DziriBERT split | CAMeLBERT-DA | with text (link-only removed) | 2042 | 72.1 | 66.3 | 3 |
| trained on DziriBERT split | CAMeLBERT-DA | kept by the audit | 1942 | 71.6 | 65.9 | 3 |
| trained on DziriBERT split | CAMeLBERT-DA | kept by the audit, text unseen in training | 1844 | 70.6 | 65.2 | 3 |
| trained on DziriBERT split | mE5-small | all test tweets | 2360 | 79.5 | 79.2 | 3 |
| trained on DziriBERT split | mE5-small | with text (link-only removed) | 2042 | 76.4 | 71.5 | 3 |
| trained on DziriBERT split | mE5-small | kept by the audit | 1942 | 75.9 | 71.0 | 3 |
| trained on DziriBERT split | mE5-small | kept by the audit, text unseen in training | 1844 | 74.8 | 70.0 | 3 |
| trained on cleaned split | NB-char | kept by the audit | 1942 | 67.1 | 60.4 | 1 |
| trained on cleaned split | NB-char | kept by the audit, text unseen in training | 1844 | 66.5 | 60.4 | 1 |
| trained on cleaned split | SVM-char | kept by the audit | 1942 | 67.9 | 60.8 | 1 |
| trained on cleaned split | SVM-char | kept by the audit, text unseen in training | 1844 | 66.9 | 60.3 | 1 |
| trained on cleaned split | LR-word+char | kept by the audit | 1942 | 66.2 | 61.0 | 1 |
| trained on cleaned split | LR-word+char | kept by the audit, text unseen in training | 1844 | 65.2 | 60.4 | 1 |
| trained on cleaned split | DziriBERT | kept by the audit | 1942 | 75.8 | 70.8 | 3 |
| trained on cleaned split | DziriBERT | kept by the audit, text unseen in training | 1844 | 75.1 | 70.4 | 3 |
| trained on cleaned split | MARBERTv2 | kept by the audit | 1942 | 76.0 | 70.3 | 3 |
| trained on cleaned split | MARBERTv2 | kept by the audit, text unseen in training | 1844 | 75.9 | 70.4 | 3 |
| trained on cleaned split | CAMeLBERT-DA | kept by the audit | 1942 | 70.1 | 63.5 | 3 |
| trained on cleaned split | CAMeLBERT-DA | kept by the audit, text unseen in training | 1844 | 69.3 | 63.2 | 3 |
| trained on cleaned split | mE5-small | kept by the audit | 1942 | 74.8 | 70.1 | 3 |
| trained on cleaned split | mE5-small | kept by the audit, text unseen in training | 1844 | 74.3 | 69.9 | 3 |
