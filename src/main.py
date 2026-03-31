

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

 
    banner("STEP 1 › Loading Corpus")
    loader = CorpusLoader("data/corpus.csv")
    corpus = loader.load()
    loader.print_summary()

   
    banner("STEP 2 › Simulating Filtering Protocol")
    fp = FilteringProtocol(corpus)
    fp.run()
    fp.print_report()

   
    banner("STEP 3 › Running Automated Taxonomy Classifier")
    classifier = TaxonomyClassifier(corpus)
    taxonomy   = classifier.build_taxonomy()
    classifier.print_taxonomy_summary()

   
    banner("STEP 4 › Generating Visualizations")
    viz = Visualizer(corpus, taxonomy)
    viz.plot_year_distribution()
    viz.plot_platform_distribution()
    viz.plot_stage_coverage()
    viz.plot_framework_wordcloud_proxy()
    viz.plot_classification_parameters()
    viz.plot_heatmap()
    print("  All charts saved to outputs/figures/")

    
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
