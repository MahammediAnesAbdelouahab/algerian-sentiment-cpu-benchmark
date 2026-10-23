"""Print derived numbers quoted in the paper: grouped split, TWIFIL decomposition, int8 across seeds.

Run from the repository root: python scripts/paper_numbers.py
"""
import json, os, sys
import numpy as np, pandas as pd
R2 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results", "notebook03") + os.sep
G = pd.read_csv(R2 + "table_grouped_split.csv").set_index("model")
D = pd.read_csv(R2 + "table_twifil_decomposition.csv")
L = pd.read_csv(R2 + "table_int8_seeds_long.csv")
CL = ["NB-char", "SVM-char", "LR-word+char"]; TR = ["DziriBERT", "MARBERTv2", "CAMeLBERT-DA", "mE5-small"]
d = G["Δ grouped − random (pts)"]
print("grouped delta classical", d[CL].min(), d[CL].max(), "| transformers", d[TR].min(), d[TR].max())
dz = D[D["training data"] == "trained on DziriBERT split"].pivot(index="model", columns="test subset", values="accuracy (%)")
cz = D[D["training data"] == "trained on cleaned split"].pivot(index="model", columns="test subset", values="accuracy (%)")
A, W, K, U = "all test tweets", "with text (link-only removed)", "kept by the audit", "kept by the audit, text unseen in training"
steps = pd.DataFrame({"link-only": dz[A] - dz[W], "audit": dz[W] - dz[K], "unseen": dz[K] - dz[U], "total": dz[A] - dz[U],
                      "share link-only": (dz[A] - dz[W]) / (dz[A] - dz[U]), "clean-minus-official on unseen": cz[U] - dz[U]}).round(2)
print(steps)
print("audit+unseen", (dz[W] - dz[U]).min(), (dz[W] - dz[U]).max())
L["absd"] = L["Δ vs fp32 (pts)"].abs()
for m in TR:
    x = L[(L.model == m) & (L.format != "ONNX fp32")]
    print(m, "max |Δ| any config", x["absd"].max())
pc = L[L.format == "ONNX int8 per-channel (no RR)"]
col = pc[pc.model.isin(["MARBERTv2", "CAMeLBERT-DA"])]
print("collapsed PC noRR macro-F1 range", col["macro-F1 (%)"].min(), col["macro-F1 (%)"].max(), "Δ", col["Δ vs fp32 (pts)"].min(), col["Δ vs fp32 (pts)"].max(), "constant", col["constant predictions"].sum(), "of", len(col))
ok = pc[pc.model.isin(["DziriBERT", "mE5-small"])]
print("PC noRR Dz/mE5 max |Δ|", ok["absd"].max())
w = L.pivot_table(index=["dataset", "model", "seed"], columns="format", values="Δ vs fp32 (pts)")
diff = w["ONNX int8 per-channel+RR"] - w["ONNX int8"]
print("PC+RR minus default: min", diff.min(), "max", diff.max()); print(diff.sort_values().head(4)); print(diff.sort_values().tail(3))
cam = L[(L.model == "CAMeLBERT-DA") & (L.dataset == "twifil_clean") & (L.format == "ONNX int8")]
print("CAMeL TWIFIL default by seed", cam[["seed", "Δ vs fp32 (pts)"]].values.tolist())
