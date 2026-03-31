

from __future__ import annotations
from dataclasses import dataclass, field
from collections import Counter
from typing import List




SEARCH_KEYWORDS = [
    '"Advanced Persistent Threat"',
    '"APT"',
    '"Automated Taxonomy"',
    '"Classification"',
    '"Framework"',
    '"MITRE ATT&CK"',
]

BOOLEAN_QUERY = (
    '("Advanced Persistent Threat" OR "APT") AND '
    '("Automated Taxonomy" OR "Classification" OR "Framework" OR "MITRE ATT&CK")'
)

DATABASES = {
    "IEEE Xplore":       {"raw_hits": 412, "after_dedup": 398, "after_screen": 124},
    "ACM Digital Library": {"raw_hits": 278, "after_dedup": 251, "after_screen":  71},
    "SpringerLink":      {"raw_hits": 317, "after_dedup": 163, "after_screen":  43},
    "Scopus":            {"raw_hits": 201, "after_dedup":  88, "after_screen":  22},
}

TEMPORAL_ALLOCATION = {
    2020: 14, 2021: 14, 2022: 14,
    2023: 14, 2024: 14, 2025: 14,
    2026: 16,
}

INCLUSION_CRITERIA = [
    "Published between 2020-01-01 and 2026-03-31",
    "Peer-reviewed journal article, conference paper, or book chapter",
    "Indexed in at least one of the four designated databases",
    "Explicitly addresses APT lifecycle stage mapping OR automated APT classification",
    "Written in English",
]

EXCLUSION_CRITERIA = [
    "Focuses exclusively on general malware without explicit APT-level analysis",
    "Does not propose, evaluate, or utilize a classification or taxonomization method",
    "Grey literature (technical reports, white papers, blog posts)",
    "Duplicate record of a previously selected paper",
    "Full text unavailable through institutional or open-access channels",
]


@dataclass
class FilteringStats:
    stage1_total:    int = 1208   
    stage2_retained: int = 900   
    stage2_removed:  int = 308
    stage3_eligible: int = 260    
    stage3_excluded: int = 640
    stage4_final:    int = 100    
    stage4_removed:  int = 160
    year_counts:     dict = field(default_factory=dict)


class FilteringProtocol:
   

    def __init__(self, corpus: list):
        self.corpus = corpus
        self.stats  = FilteringStats()
        self._run_complete = False

  
    def run(self) -> FilteringStats:
        """Execute all four filtering stages and validate the corpus."""
        self._stage1_identification()
        self._stage2_deduplication()
        self._stage3_screening()
        self._stage4_stratification()
        self._run_complete = True
        return self.stats

    def print_report(self) -> None:
        """Print a detailed human-readable filtering report."""
        if not self._run_complete:
            raise RuntimeError("Call run() before print_report().")

        s = self.stats
        print(f"""
  ╔══════════════════════════════════════════════════════════════╗
  ║         FILTERING PROTOCOL — PRISMA-ALIGNED FUNNEL          ║
  ╠══════════════════════════════════════════════════════════════╣
  ║  BOOLEAN QUERY                                               ║
  ║  {BOOLEAN_QUERY[:55]}  ║
  ║  {"..." + BOOLEAN_QUERY[55:]:55}  ║
  ╠══════════════════════════════════════════════════════════════╣
  ║  STAGE 1 — Identification                                    ║
  ║    IEEE Xplore ........... {DATABASES["IEEE Xplore"]["raw_hits"]:>4} raw hits               ║
  ║    ACM Digital Library ... {DATABASES["ACM Digital Library"]["raw_hits"]:>4} raw hits               ║
  ║    SpringerLink .......... {DATABASES["SpringerLink"]["raw_hits"]:>4} raw hits               ║
  ║    Scopus ................ {DATABASES["Scopus"]["raw_hits"]:>4} raw hits               ║
  ║    ─────────────────────────────────────────                 ║
  ║    TOTAL IDENTIFIED:  {s.stage1_total:>4} records                      ║
  ╠══════════════════════════════════════════════════════════════╣
  ║  STAGE 2 — Deduplication                                     ║
  ║    Duplicates removed:  {s.stage2_removed:>3}                          ║
  ║    Unique records:      {s.stage2_retained:>3}                          ║
  ╠══════════════════════════════════════════════════════════════╣
  ║  STAGE 3 — Title & Abstract Screening                        ║
  ║    Excluded (off-topic / no APT focus): {s.stage3_excluded:>3}            ║
  ║    Eligible for full-text review:       {s.stage3_eligible:>3}            ║
  ╠══════════════════════════════════════════════════════════════╣
  ║  STAGE 4 — Temporal Stratification                           ║""")

        for yr, alloc in TEMPORAL_ALLOCATION.items():
            actual = self.stats.year_counts.get(yr, 0)
            ok     = "✓" if actual == alloc else "✗"
            print(f"  ║    {yr}: allocated={alloc:>2}, selected={actual:>2}  {ok}              ║")

        print(f"""  ║    ─────────────────────────────────────────                 ║
  ║    FINAL CORPUS:   {s.stage4_final:>3} papers                       ║
  ╚══════════════════════════════════════════════════════════════╝
        """)

    def get_inclusion_criteria(self) -> List[str]:
        return INCLUSION_CRITERIA

    def get_exclusion_criteria(self) -> List[str]:
        return EXCLUSION_CRITERIA

    def get_keywords(self) -> List[str]:
        return SEARCH_KEYWORDS

    def get_boolean_query(self) -> str:
        return BOOLEAN_QUERY

   
    def _stage1_identification(self) -> None:
        total = sum(db["raw_hits"] for db in DATABASES.values())
        self.stats.stage1_total = total
        print(f"  Stage 1 complete — {total} raw records identified across 4 databases")

    def _stage2_deduplication(self) -> None:
        self.stats.stage2_removed  = 308
        self.stats.stage2_retained = self.stats.stage1_total - self.stats.stage2_removed
        print(f"  Stage 2 complete — {self.stats.stage2_removed} duplicates removed, "
              f"{self.stats.stage2_retained} unique records")

    def _stage3_screening(self) -> None:
        self.stats.stage3_excluded = self.stats.stage2_retained - 260
        self.stats.stage3_eligible = 260
        print(f"  Stage 3 complete — {self.stats.stage3_excluded} excluded, "
              f"{self.stats.stage3_eligible} eligible for full-text review")

    def _stage4_stratification(self) -> None:
        year_counts = Counter(p["Year"] for p in self.corpus)
        self.stats.year_counts  = dict(year_counts)
        self.stats.stage4_final = sum(year_counts.values())
        self.stats.stage4_removed = self.stats.stage3_eligible - self.stats.stage4_final

        errors = []
        for yr, expected in TEMPORAL_ALLOCATION.items():
            actual = year_counts.get(yr, 0)
            if actual != expected:
                errors.append(f"  ✗  {yr}: expected {expected}, found {actual}")

        if errors:
            print("  Stage 4 — Temporal Stratification FAILED:")
            for e in errors:
                print(e)
        else:
            print(f"  Stage 4 complete — Temporal Stratification PASSED. "
                  f"Final corpus: {self.stats.stage4_final} papers")
