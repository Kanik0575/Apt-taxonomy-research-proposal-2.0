"""
report_generator.py
───────────────────
Exports the final taxonomy report as:
  - outputs/reports/taxonomy_report.md  (full Markdown)
  - outputs/reports/summary.csv          (per-node stats)
"""

from __future__ import annotations
import os, csv
from datetime import date


OUTPUT_DIR = "outputs/reports"


class ReportGenerator:
    def __init__(self, corpus: list, taxonomy: dict, filtering_protocol):
        self.corpus   = corpus
        self.taxonomy = taxonomy
        self.fp       = filtering_protocol

    def export_markdown(self) -> None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        path = os.path.join(OUTPUT_DIR, "taxonomy_report.md")

        lines = [
            "# Automated Taxonomy of APT Attacks — Full Report",
            f"> Generated: {date.today().isoformat()} | Corpus: 100 papers | 2020–2026",
            "",
            "---",
            "",
            "## Search Protocol",
            "",
            "**Boolean Query:**",
            "",
            f"```\n{self.fp.get_boolean_query()}\n```",
            "",
            "**Databases:** IEEE Xplore | ACM Digital Library | SpringerLink | Scopus",
            "",
            "**Filtering Funnel:**",
            "| Stage | Input | Output | Action |",
            "|-------|-------|--------|--------|",
            "| 1 — Identification | — | ~1,208 | Keyword search across 4 DBs |",
            "| 2 — Deduplication | 1,208 | 900 | Remove cross-DB duplicates |",
            "| 3 — Screening | 900 | 260 | Inclusion/exclusion criteria |",
            "| 4 — Stratification | 260 | 100 | Temporal Stratification (14–16/yr) |",
            "",
            "---",
            "",
            "## Temporal Stratification Verification",
            "",
            "| Year | Allocated | Selected | Status |",
            "|------|-----------|----------|--------|",
        ]

        alloc = {2020:14,2021:14,2022:14,2023:14,2024:14,2025:14,2026:16}
        from collections import Counter
        year_counts = Counter(p["Year"] for p in self.corpus)
        for yr, exp in alloc.items():
            act = year_counts.get(yr, 0)
            lines.append(f"| {yr} | {exp} | {act} | {'✅ Verified' if act==exp else '❌ Error'} |")

        lines += [
            "",
            "---",
            "",
            "## Taxonomy Node Coverage",
            "",
            "| Node | Tactic Name | MITRE Tactic | Papers | Coverage |",
            "|------|-------------|--------------|--------|----------|",
        ]

        for nid, data in sorted(self.taxonomy["nodes"].items(),
                                  key=lambda x: -x[1]["paper_count"]):
            cov = data["paper_count"] / len(self.corpus) * 100
            lines.append(
                f"| {nid} | {data['name']} | {data['mitre_tactic']} "
                f"| {data['paper_count']}/100 | {cov:.0f}% |"
            )

        lines += ["", "---", "", "## Full Corpus (100 Papers)", "",
                  "| No. | Year | Title | Platform | Stage | Framework |",
                  "|-----|------|-------|----------|-------|-----------|"]

        for p in self.corpus:
            title = p["Paper_Title"].replace("|", "/")
            lines.append(
                f"| {p['No.']} | {p['Year']} | {title} "
                f"| {p['Platform']} | {p['APT_Stage_Focus']} "
                f"| {p['Classification_Framework']} |"
            )

        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        print(f"    Markdown report written to '{path}'")

    def export_csv_summary(self) -> None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        path = os.path.join(OUTPUT_DIR, "summary.csv")
        with open(path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["Node", "Tactic_Name", "MITRE_Tactic",
                              "Paper_Count", "Coverage_Pct", "Primary_CPs"])
            for nid, data in sorted(self.taxonomy["nodes"].items()):
                cov = data["paper_count"] / len(self.corpus) * 100
                writer.writerow([
                    nid, data["name"], data["mitre_tactic"],
                    data["paper_count"], f"{cov:.1f}",
                    " | ".join(data["primary_cps"])
                ])
        print(f"    CSV summary written to '{path}'")
