

from __future__ import annotations
from collections import Counter, defaultdict
from typing import Dict, List




TACTIC_MAP = {
    "TA0043": {"code": "T1",  "name": "Reconnaissance",        "mitre": "TA0043"},
    "TA0042": {"code": "T2",  "name": "Resource Development",   "mitre": "TA0042"},
    "TA0001": {"code": "T3",  "name": "Initial Access",         "mitre": "TA0001"},
    "TA0002": {"code": "T4",  "name": "Execution",              "mitre": "TA0002"},
    "TA0003": {"code": "T5",  "name": "Persistence",            "mitre": "TA0003"},
    "TA0004": {"code": "T6",  "name": "Privilege Escalation",   "mitre": "TA0004"},
    "TA0005": {"code": "T7",  "name": "Defense Evasion",        "mitre": "TA0005"},
    "TA0006": {"code": "T8",  "name": "Credential Access",      "mitre": "TA0006"},
    "TA0007": {"code": "T9",  "name": "Discovery",              "mitre": "TA0007"},
    "TA0008": {"code": "T10", "name": "Lateral Movement",       "mitre": "TA0008"},
    "TA0009": {"code": "T11", "name": "Collection",             "mitre": "TA0009"},
    "TA0011": {"code": "T12", "name": "Command & Control (C2)", "mitre": "TA0011"},
    "TA0010": {"code": "T13", "name": "Exfiltration",           "mitre": "TA0010"},
    "TA0040": {"code": "T14", "name": "Impact",                 "mitre": "TA0040"},
}


    "CP-02": "Behavioral Fingerprinting",
    "CP-03": "NLP-Based TTP Extraction",
    "CP-04": "Graph-Theoretic Modeling",
    "CP-05": "ML-Driven Attribution",
    "CP-06": "Indicator Correlation",
    "CP-07": "Anomaly Detection",
    "CP-08": "C2 Traffic Analysis",
    "CP-09": "Exfiltration Modeling",
}



STAGE_TO_CP = {
    "TA0043": ["CP-06", "CP-07"],          
    "TA0042": ["CP-02", "CP-04"],         
    "TA0001": ["CP-03", "CP-07"],         
    "TA0002": ["CP-02", "CP-03"],         
    "TA0003": ["CP-02", "CP-04"],         
    "TA0004": ["CP-07"],                   
    "TA0005": ["CP-03", "CP-07"],          
    "TA0006": ["CP-02", "CP-07"],          
    "TA0007": ["CP-04", "CP-07"],          
    "TA0008": ["CP-01", "CP-04"],          
    "TA0009": ["CP-09"],                   
    "TA0011": ["CP-08"],                   
    "TA0010": ["CP-01", "CP-09"],          
    "TA0040": ["CP-07"],                  
}


class TaxonomyClassifier:
    """
    Builds the automated taxonomy from the corpus.
    """

    def __init__(self, corpus: list):
        self.corpus   = corpus
        self.taxonomy = {}
        self._built   = False

    

    def build_taxonomy(self) -> Dict:
        """
        Iterate over all papers, map each to taxonomy nodes,
        and compute per-node statistics.
        """
        node_paper_counts = Counter()
        node_papers       = defaultdict(list)
        cp_counts         = Counter()
        framework_counts  = Counter()

        for paper in self.corpus:
            fw = paper.get("Classification_Framework", "Unknown")
            framework_counts[fw] += 1

            for tactic_code in paper.get("Stage_List", []):
                tc = tactic_code.strip()
                if tc in TACTIC_MAP:
                    node = TACTIC_MAP[tc]["code"]
                    node_paper_counts[node] += 1
                    node_papers[node].append(paper["No."])
                    for cp in STAGE_TO_CP.get(tc, []):
                        cp_counts[cp] += 1

        
        self.taxonomy = {
            "nodes": {},
            "classification_parameters": {},
            "framework_distribution": dict(framework_counts.most_common(15)),
        }

        for tactic_code, meta in TACTIC_MAP.items():
            node = meta["code"]
            self.taxonomy["nodes"][node] = {
                "name":         meta["name"],
                "mitre_tactic": meta["mitre"],
                "paper_count":  node_paper_counts.get(node, 0),
                "paper_ids":    sorted(node_papers.get(node, [])),
                "primary_cps":  STAGE_TO_CP.get(tactic_code, []),
            }

        for cp, name in CLASSIFICATION_PARAMS.items():
            self.taxonomy["classification_parameters"][cp] = {
                "name":       name,
                "paper_count": cp_counts.get(cp, 0),
            }

        self._built = True
        return self.taxonomy

    def print_taxonomy_summary(self) -> None:
        """Print a per-node coverage table."""
        if not self._built:
            raise RuntimeError("Call build_taxonomy() first.")

        print(f"\n  {'Node':<6} {'Tactic Name':<28} {'MITRE':<10} "
              f"{'Papers':>6}  {'Coverage':>8}  {'Primary CPs'}")
        print("  " + "─" * 80)

        total = len(self.corpus)
        for node_id, data in sorted(
            self.taxonomy["nodes"].items(),
            key=lambda x: -x[1]["paper_count"]
        ):
            cov  = data["paper_count"] / total * 100
            stars = "★" * min(5, int(cov / 20)) + "☆" * (5 - min(5, int(cov / 20)))
            cps   = ", ".join(data["primary_cps"][:2])
            print(f"  {node_id:<6} {data['name']:<28} {data['mitre_tactic']:<10} "
                  f"{data['paper_count']:>6}  {cov:>6.1f}%   {cps}")

        print()
        print("  Classification Parameter Usage:")
        print("  " + "─" * 50)
        for cp, data in sorted(
            self.taxonomy["classification_parameters"].items()
        ):
            bar = "█" * (data["paper_count"] // 5)
            print(f"  {cp}: {data['name']:<30} {bar} ({data['paper_count']})")
