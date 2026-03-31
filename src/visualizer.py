
from __future__ import annotations
import os
from collections import Counter, defaultdict

import matplotlib
matplotlib.use("Agg")   
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUTPUT_DIR = "outputs/figures"

BLUE_PALETTE = [
    "#1F3864", "#2E5FA3", "#4A90D9", "#6BAED6",
    "#9ECAE1", "#C6DBEF", "#DEEBF7",
]
ACCENT = "#E84545"


def _save(fig: plt.Figure, name: str) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"    Saved: {path}")


class Visualizer:
    def __init__(self, corpus: list, taxonomy: dict):
        self.corpus   = corpus
        self.taxonomy = taxonomy

    
    def plot_year_distribution(self) -> None:
        year_counts = Counter(p["Year"] for p in self.corpus)
        years  = sorted(year_counts)
        counts = [year_counts[y] for y in years]
        target = [14, 14, 14, 14, 14, 14, 16]

        fig, ax = plt.subplots(figsize=(10, 5))
        bars = ax.bar(years, counts, color=BLUE_PALETTE[1], edgecolor="white",
                      linewidth=0.8, zorder=3)
        ax.step([years[0] - 0.5] + years + [years[-1] + 0.5],
                [target[0]] + target + [target[-1]],
                where="mid", color=ACCENT, linewidth=2.0,
                linestyle="--", label="Temporal Stratification Target", zorder=4)

        for bar, cnt in zip(bars, counts):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.3, str(cnt),
                    ha="center", va="bottom", fontsize=11,
                    fontweight="bold", color=BLUE_PALETTE[0])

        ax.set_xlabel("Publication Year", fontsize=12)
        ax.set_ylabel("Number of Papers Selected", fontsize=12)
        ax.set_title("Corpus Year Distribution — Temporal Stratification Protocol",
                     fontsize=13, fontweight="bold", color=BLUE_PALETTE[0])
        ax.set_xticks(years)
        ax.set_ylim(0, 20)
        ax.yaxis.grid(True, linestyle="--", alpha=0.5, zorder=0)
        ax.set_axisbelow(True)
        ax.legend(fontsize=10)
        fig.tight_layout()
        _save(fig, "01_year_distribution.png")

   
    def plot_platform_distribution(self) -> None:
        plat_counts = Counter(p["Platform"] for p in self.corpus)
        labels  = list(plat_counts.keys())
        sizes   = list(plat_counts.values())
        colors  = BLUE_PALETTE[:len(labels)]
        explode = [0.04] * len(labels)

        fig, ax = plt.subplots(figsize=(7, 7))
        wedges, texts, autotexts = ax.pie(
            sizes, labels=labels, colors=colors, explode=explode,
            autopct="%1.0f%%", startangle=140,
            textprops={"fontsize": 11},
            wedgeprops={"edgecolor": "white", "linewidth": 1.5}
        )
        for at in autotexts:
            at.set_fontweight("bold")
            at.set_fontsize(12)

        ax.set_title("Corpus Distribution by Academic Database",
                     fontsize=13, fontweight="bold",
                     color=BLUE_PALETTE[0], pad=20)
        fig.tight_layout()
        _save(fig, "02_platform_distribution.png")

  
    def plot_stage_coverage(self) -> None:
        nodes = self.taxonomy.get("nodes", {})
        names  = []
        counts = []
        total  = len(self.corpus)

        order = ["T12", "T3", "T7", "T13", "T4", "T5", "T10",
                 "T8", "T6", "T9", "T11", "T1", "T2", "T14"]

        for nid in order:
            if nid in nodes:
                names.append(f"{nid} — {nodes[nid]['name']}")
                counts.append(nodes[nid]["paper_count"])

        pcts  = [c / total * 100 for c in counts]
        colors = [BLUE_PALETTE[1] if p >= 70 else
                  BLUE_PALETTE[2] if p >= 50 else
                  BLUE_PALETTE[3] for p in pcts]

        fig, ax = plt.subplots(figsize=(10, 8))
        bars = ax.barh(names, pcts, color=colors, edgecolor="white", linewidth=0.5)

        for bar, pct, cnt in zip(bars, pcts, counts):
            ax.text(pct + 0.5, bar.get_y() + bar.get_height() / 2,
                    f"{cnt}/100 ({pct:.0f}%)",
                    va="center", ha="left", fontsize=9, color="#333333")

        ax.axvline(50, color=ACCENT, linestyle="--", linewidth=1.2,
                   label="50% Threshold", alpha=0.8)
        ax.set_xlabel("% of Corpus Papers Addressing Stage", fontsize=11)
        ax.set_title("APT Taxonomy Node Coverage Across 100-Paper Corpus",
                     fontsize=13, fontweight="bold", color=BLUE_PALETTE[0])
        ax.set_xlim(0, 110)
        ax.xaxis.grid(True, linestyle="--", alpha=0.4)
        ax.set_axisbelow(True)
        ax.legend(fontsize=9)
        ax.invert_yaxis()
        fig.tight_layout()
        _save(fig, "03_stage_coverage.png")

    
    def plot_framework_wordcloud_proxy(self) -> None:
        """Bar chart of the top classification frameworks used."""
        fw_counts = Counter(p["Classification_Framework"] for p in self.corpus)

        
        grouped: Counter = Counter()
        for fw, cnt in fw_counts.items():
            fw_lower = fw.lower()
            if "att&ck" in fw_lower or "attack" in fw_lower:
                grouped["MITRE ATT&CK-based"] += cnt
            elif "gnn" in fw_lower or "graph neural" in fw_lower or "gcn" in fw_lower:
                grouped["Graph Neural Network"] += cnt
            elif "bert" in fw_lower or "llm" in fw_lower or "gpt" in fw_lower:
                grouped["Transformer / LLM"] += cnt
            elif "knowledge graph" in fw_lower or "kg" in fw_lower:
                grouped["Knowledge Graph"] += cnt
            elif "random forest" in fw_lower or "rf" in fw_lower or "xgboost" in fw_lower:
                grouped["Random Forest / XGBoost"] += cnt
            elif "hmm" in fw_lower or "markov" in fw_lower:
                grouped["Markov / HMM"] += cnt
            elif "ontology" in fw_lower or "owl" in fw_lower:
                grouped["OWL Ontology"] += cnt
            elif "bayesian" in fw_lower:
                grouped["Bayesian Network"] += cnt
            elif "stix" in fw_lower or "taxii" in fw_lower:
                grouped["STIX / TAXII"] += cnt
            else:
                grouped["Other ML / Statistical"] += cnt

        labels, counts = zip(*grouped.most_common())
        fig, ax = plt.subplots(figsize=(10, 5))
        bars = ax.bar(labels, counts, color=BLUE_PALETTE[:len(labels)],
                      edgecolor="white", linewidth=0.8)
        for bar, cnt in zip(bars, counts):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.3, str(cnt),
                    ha="center", va="bottom", fontsize=10, fontweight="bold")

        ax.set_ylabel("Number of Papers", fontsize=11)
        ax.set_title("Classification Framework Groupings Across the Corpus",
                     fontsize=13, fontweight="bold", color=BLUE_PALETTE[0])
        ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9)
        ax.yaxis.grid(True, linestyle="--", alpha=0.5)
        ax.set_axisbelow(True)
        fig.tight_layout()
        _save(fig, "04_framework_distribution.png")

   
    def plot_classification_parameters(self) -> None:
        cp_data = self.taxonomy.get("classification_parameters", {})
        labels  = [f"{k}\n{v['name'][:18]}" for k, v in cp_data.items()]
        values  = [v["paper_count"] for v in cp_data.values()]
        N       = len(labels)

        angles  = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
        values_c = values + [values[0]]
        angles_c = angles + [angles[0]]

        fig, ax = plt.subplots(figsize=(8, 8),
                               subplot_kw={"projection": "polar"})
        ax.plot(angles_c, values_c, "o-", linewidth=2, color=BLUE_PALETTE[1])
        ax.fill(angles_c, values_c, alpha=0.25, color=BLUE_PALETTE[2])
        ax.set_xticks(angles)
        ax.set_xticklabels(labels, size=8)
        ax.set_title("Classification Parameter Coverage Across Corpus",
                     fontsize=13, fontweight="bold",
                     color=BLUE_PALETTE[0], pad=20)
        fig.tight_layout()
        _save(fig, "05_classification_parameters_radar.png")

    
    def plot_heatmap(self) -> None:
        YEARS  = list(range(2020, 2027))
        STAGES = ["T1","T2","T3","T4","T5","T6","T7",
                  "T8","T9","T10","T11","T12","T13","T14"]
        TACTIC_TO_NODE = {
            "TA0043":"T1","TA0042":"T2","TA0001":"T3","TA0002":"T4",
            "TA0003":"T5","TA0004":"T6","TA0005":"T7","TA0006":"T8",
            "TA0007":"T9","TA0008":"T10","TA0009":"T11",
            "TA0011":"T12","TA0010":"T13","TA0040":"T14",
        }
        grid = defaultdict(Counter)
        for paper in self.corpus:
            yr = paper["Year"]
            for tc in paper.get("Stage_List", []):
                node = TACTIC_TO_NODE.get(tc.strip())
                if node:
                    grid[yr][node] += 1

        matrix = np.array([[grid[yr].get(stage, 0)
                             for yr in YEARS]
                            for stage in STAGES], dtype=float)

        fig, ax = plt.subplots(figsize=(12, 7))
        im = ax.imshow(matrix, cmap="Blues", aspect="auto")
        ax.set_xticks(range(len(YEARS)));  ax.set_xticklabels(YEARS, fontsize=10)
        ax.set_yticks(range(len(STAGES))); ax.set_yticklabels(STAGES, fontsize=9)
        ax.set_xlabel("Publication Year", fontsize=11)
        ax.set_ylabel("Taxonomy Node", fontsize=11)
        ax.set_title("APT Stage Focus × Year Heatmap (Paper Count per Cell)",
                     fontsize=13, fontweight="bold", color=BLUE_PALETTE[0])

        for i in range(len(STAGES)):
            for j in range(len(YEARS)):
                val = int(matrix[i, j])
                if val > 0:
                    txt_col = "white" if val >= matrix.max() * 0.6 else BLUE_PALETTE[0]
                    ax.text(j, i, str(val), ha="center", va="center",
                            fontsize=8, color=txt_col)

        plt.colorbar(im, ax=ax, fraction=0.03, pad=0.02, label="Paper Count")
        fig.tight_layout()
        _save(fig, "06_stage_year_heatmap.png")
