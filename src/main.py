"""
==============================================================================
  AUTOMATED TAXONOMY OF APT ATTACKS
  Main Analysis Pipeline
  Post-Doctoral Cybersecurity Research | 2026
==============================================================================

This script:
  1. Loads the 100-paper corpus
  2. Simulates the full filtering protocol (keyword search → deduplication
     → inclusion/exclusion screening → temporal stratification)
  3. Generates the automated taxonomy classification report
  4. Produces all charts and exports a summary report

Run:
    python src/main.py
"""

import os
import sys

# Ensure project root is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.corpus_loader       import CorpusLoader
from src.filtering_protocol  import FilteringProtocol
from src.taxonomy_classifier import TaxonomyClassifier
from src.visualizer          import Visualizer
from src.report_generator    import ReportGenerator


def banner(title: str) -> None:
    width = 70
    print("\n" + "═" * width)
    print(f"  {title}")
    print("═" * width)


def main():
    banner("AUTOMATED APT TAXONOMY — FULL PIPELINE")

    # ── 1. Load corpus ──────────────────────────────────────────────
    banner("STEP 1 › Loading Corpus")
    loader = CorpusLoader("data/corpus.csv")
    corpus = loader.load()
    loader.print_summary()

    # ── 2. Run filtering protocol ───────────────────────────────────
    banner("STEP 2 › Simulating Filtering Protocol")
    fp = FilteringProtocol(corpus)
    fp.run()
    fp.print_report()

    # ── 3. Classify & build taxonomy ───────────────────────────────
    banner("STEP 3 › Running Automated Taxonomy Classifier")
    classifier = TaxonomyClassifier(corpus)
    taxonomy   = classifier.build_taxonomy()
    classifier.print_taxonomy_summary()

    # ── 4. Generate all visualizations ─────────────────────────────
    banner("STEP 4 › Generating Visualizations")
    viz = Visualizer(corpus, taxonomy)
    viz.plot_year_distribution()
    viz.plot_platform_distribution()
    viz.plot_stage_coverage()
    viz.plot_framework_wordcloud_proxy()
    viz.plot_classification_parameters()
    viz.plot_heatmap()
    print("  All charts saved to outputs/figures/")

    # ── 5. Export report ────────────────────────────────────────────
    banner("STEP 5 › Exporting Reports")
    rg = ReportGenerator(corpus, taxonomy, fp)
    rg.export_markdown()
    rg.export_csv_summary()
    print("  Reports saved to outputs/reports/")

    banner("PIPELINE COMPLETE")
    print("""
  Outputs:
    outputs/figures/   — all charts (PNG)
    outputs/reports/   — taxonomy_report.md + summary.csv
    data/corpus.csv    — 100-paper corpus
    data/corpus.json   — same data in JSON format
    """)


if __name__ == "__main__":
    main()
