"""Figures of the paper (300 dpi PNG at the printed size, 6.5 in wide, so font sizes are true sizes).

Run from the repository root: python scripts/make_figures.py
Figure 1: pipeline (two rows of numbered steps, abbreviations spelled out).
Figure 2: Pareto frontiers from table_deployment_standard.csv (standardised benchmark)."""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch
from matplotlib.ticker import FuncFormatter, LogLocator
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R2 = os.path.join(ROOT, "results", "notebook03")
FIG_DIR = os.path.join(ROOT, "results", "figures")
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8, "axes.linewidth": 0.7})
INK, INK_2, GRID, FILL = "#0b0b0b", "#3d3c39", "#e4e3df", "#f4f3f0"
W = 6.5

# ------------------------------------------------------------------ Figure 1: pipeline
boxes = [
    ("1. Public datasets", ["TWIFIL: 9,437 tweets", "YouTube: 45,000 comments", "NArabizi: 966 sentences", "(Latin script)"]),
    ("2. Audit and splits", ["(1) texts without content", "(2) conflicting labels", "(3) duplicates within a split",
                             "(4) duplicates across splits", "+ YouTube split by video"]),
    ("3. Training", ["3 TF-IDF classifiers", "4 transformers × 3 seeds", "on one NVIDIA T4 GPU",
                     "model selection on the", "development set"]),
    ("4. Export", ["PyTorch fp32", "ONNX fp32", "ONNX int8, default", "ONNX int8, per-channel", "+ reduce-range"]),
    ("5. CPU benchmark", ["fresh process, one thread", "size, peak memory (RSS)", "cold start", "latency p50 / p95",
                          "test-set macro-F1"]),
    ("6. Analysis", ["accuracy–cost trade-offs", "(Pareto frontiers)", "int8 accuracy over seeds", "link-only shortcut",
                     "video-grouped split"]),
]
fig = plt.figure(figsize=(W, 3.9))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis("off")
bw, bh, gx = 30.0, 25.0, 4.0
xs = [1.0 + k * (bw + gx) for k in range(3)]
ys = [33.0, 2.0]
pos = [(xs[k % 3], ys[k // 3]) for k in range(6)]
for (title, lines), (x, y) in zip(boxes, pos):
    ax.add_patch(FancyBboxPatch((x, y), bw, bh, boxstyle="round,pad=0.25,rounding_size=1.2",
                                linewidth=0.8, edgecolor=INK_2, facecolor=FILL))
    ax.text(x + bw / 2, y + bh - 3.2, title, ha="center", va="center", fontsize=9, fontweight="bold", color=INK)
    for k, line in enumerate(lines):
        ax.text(x + bw / 2, y + bh - 8.3 - k * 3.75, line, ha="center", va="center", fontsize=8, color=INK_2)
arrow = dict(arrowstyle="-|>", color=INK_2, lw=0.9, shrinkA=0, shrinkB=0, mutation_scale=8)
for k in (0, 1, 3, 4):
    x, y = pos[k]
    ax.annotate("", xy=(x + bw + gx - 0.4, y + bh / 2), xytext=(x + bw + 0.4, y + bh / 2), arrowprops=arrow)
# elbow from step 3 (top right) to step 4 (bottom left)
x3, y3 = pos[2]
x4, y4 = pos[3]
ymid = (y4 + bh + y3) / 2
ax.plot([x3 + bw / 2, x3 + bw / 2, x4 + bw / 2], [y3 - 0.4, ymid, ymid], color=INK_2, lw=0.9)
ax.annotate("", xy=(x4 + bw / 2, y4 + bh + 0.4), xytext=(x4 + bw / 2, ymid), arrowprops=arrow)
fig.savefig(os.path.join(FIG_DIR, "fig1_pipeline.png"), dpi=300, facecolor="white")
plt.close(fig)

# ------------------------------------------------------------------ Figure 2: Pareto frontiers
D = pd.read_csv(os.path.join(R2, "table_deployment_standard.csv"))
FAMILY = {"NB-char": "Classical (TF-IDF)", "SVM-char": "Classical (TF-IDF)", "LR-word+char": "Classical (TF-IDF)",
          "mE5-small": "Multilingual small transformer", "DziriBERT": "Arabic/dialect BERT",
          "MARBERTv2": "Arabic/dialect BERT", "CAMeLBERT-DA": "Arabic/dialect BERT"}
COLOUR = {"Classical (TF-IDF)": "#2a78d6", "Multilingual small transformer": "#eb6834", "Arabic/dialect BERT": "#1baf7a"}
MARKER = {"scikit-learn": "o", "PyTorch fp32": "o", "ONNX fp32": "s", "ONNX int8": "^", "ONNX int8 per-channel+RR": "D"}
TITLES = {("twifil_clean", 0): "(a) TWIFIL, cleaned split: latency", ("twifil_clean", 1): "(b) TWIFIL, cleaned split: size",
          ("youtube", 0): "(c) YouTube, random split: latency", ("youtube", 1): "(d) YouTube, random split: size"}
LAT, SIZE = "p50 (ms)", "size (MiB)"
# optional hand-placed label offsets (dataset, axis column, model, format) -> (dx, dy, ha) in points
LABELS = {
    ("twifil_clean", "p50 (ms)", "LR-word+char", "scikit-learn"): (6, 14, "left"),
    ("twifil_clean", "p50 (ms)", "mE5-small", "ONNX int8"): (-8, 9, "right"),
    ("twifil_clean", "size (MiB)", "SVM-char", "scikit-learn"): (4, -9, "left"),
    ("twifil_clean", "size (MiB)", "LR-word+char", "scikit-learn"): (6, 12, "left"),
}
DEFAULT = (5, 5, "left")


def pareto(cost, qual):
    cost, qual = np.asarray(cost), np.asarray(qual)
    keep = np.ones(len(cost), bool)
    for i in range(len(cost)):
        dom = (cost <= cost[i]) & (qual >= qual[i]) & ((cost < cost[i]) | (qual > qual[i]))
        keep[i] = not dom.any()
    return keep


fig_h = 7.2
fig, axes = plt.subplots(2, 2, figsize=(W, fig_h))
for i, ds in enumerate(["twifil_clean", "youtube"]):
    b = D[D.dataset == ds].reset_index(drop=True)
    for j, (col, lab) in enumerate([(LAT, "Median latency p50, one comment, one thread (ms, log scale)"),
                                    (SIZE, "Size on disk (MiB, log scale)")]):
        ax = axes[i][j]
        m = pareto(b[col], b["macro-F1 (%)"])
        f = b[m].sort_values(col)
        ax.step(f[col], f["macro-F1 (%)"], where="post", color=INK_2, lw=1.0, zorder=1)
        for mdl, fmt_, xv, yv in zip(b["model"], b["format"], b[col], b["macro-F1 (%)"]):
            ax.scatter(xv, yv, s=38, marker=MARKER[fmt_], color=COLOUR[FAMILY[mdl]], edgecolor="white", linewidth=0.9, zorder=3)
        seen = set()
        for mdl, fmt_, xv, yv in zip(f["model"], f["format"], f[col], f["macro-F1 (%)"]):
            dx, dy, ha = LABELS.get((ds, col, mdl, fmt_), DEFAULT)
            if (ds, col, mdl, fmt_) not in LABELS and mdl in seen:
                continue                      # one automatic label per model and panel
            seen.add(mdl)
            ax.annotate(mdl, (xv, yv), xytext=(dx, dy), textcoords="offset points", fontsize=7.5, color=INK,
                        ha=ha, va="bottom" if dy > 0 else "top",
                        arrowprops=dict(arrowstyle="-", color="#a8a7a2", lw=0.5, shrinkA=0, shrinkB=3))
        ax.set_xscale("log")
        ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
        ax.xaxis.set_minor_locator(LogLocator(base=10, subs=(2, 5)))
        ax.xaxis.set_minor_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
        ax.set_xlabel(lab, fontsize=8, color=INK_2)
        ax.set_ylabel("Macro-F1 (%)", fontsize=8, color=INK_2)
        ax.set_title(TITLES[(ds, j)], fontsize=9, color=INK, loc="left")
        ax.grid(True, which="major", color=GRID, lw=0.6)
        ax.set_axisbelow(True)
        ax.tick_params(which="both", labelsize=7.5, colors=INK_2, length=2.5)
        for s_ in ("top", "right"):
            ax.spines[s_].set_visible(False)
        for s_ in ("left", "bottom"):
            ax.spines[s_].set_color("#b5b4af")
        ys_ = b["macro-F1 (%)"]
        ax.set_ylim(ys_.min() - 1.5, ys_.max() + 2.0)
        print(ds, col, "frontier:", list(zip(f["model"], f["format"])))
fam = [Line2D([], [], ls="", marker="o", ms=6, color=c, markeredgecolor="white", label=k) for k, c in COLOUR.items()]
fmt = [Line2D([], [], ls="", marker=mk, ms=6, color=INK_2, markeredgecolor="white", label=k)
       for k, mk in (("native: scikit-learn or PyTorch fp32", "o"), ("ONNX fp32", "s"), ("ONNX int8, default", "^"),
                     ("ONNX int8, per-channel + reduce-range", "D"))]
fr = [Line2D([], [], color=INK_2, lw=1.0, label="Pareto frontier")]
fig.tight_layout(rect=(0, 0.95 / fig_h, 1, 1), h_pad=1.8, w_pad=1.8)
fig.legend(handles=fam + fmt + fr, loc="lower center", ncol=2, fontsize=8, frameon=False, bbox_to_anchor=(0.5, 0.0),
           columnspacing=1.6, handletextpad=0.4)
fig.savefig(os.path.join(FIG_DIR, "fig2_pareto.png"), dpi=300, facecolor="white")
print("figures written")
