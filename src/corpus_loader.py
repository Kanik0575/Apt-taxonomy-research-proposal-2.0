
import csv
import json
import os
from collections import Counter


class CorpusLoader:
   

    REQUIRED_COLUMNS = {
        "No.", "Year", "Paper_Title", "Platform",
        "APT_Stage_Focus", "Classification_Framework",
        "Stage_Codes", "Inclusion_Reason"
    }

    def __init__(self, csv_path: str):
        self.csv_path  = csv_path
        self.papers    = []
        self._loaded   = False

    
    def load(self) -> list:
        """Parse the corpus CSV and return a list of paper dicts."""
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"Corpus file not found: {self.csv_path}")

        with open(self.csv_path, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            self._validate_columns(set(reader.fieldnames or []))
            for row in reader:
                row["Year"] = int(row["Year"])
                row["No."]  = int(row["No."])
                row["Stage_List"] = [
                    s.strip() for s in row["Stage_Codes"].split(",") if s.strip()
                ]
                self.papers.append(row)

        self._loaded = True
        self._export_json()
        print(f"  Loaded {len(self.papers)} papers from '{self.csv_path}'")
        return self.papers

    def print_summary(self) -> None:
        """Print a formatted corpus summary to stdout."""
        self._check_loaded()
        year_counts = Counter(p["Year"] for p in self.papers)
        plat_counts = Counter(p["Platform"] for p in self.papers)

        print("\n  ┌─ Year Distribution ─────────────────────────────┐")
        for yr in sorted(year_counts):
            bar = "█" * year_counts[yr]
            status = "✓" if year_counts[yr] in (14, 16) else "✗"
            print(f"  │  {yr}: {bar:<20} {year_counts[yr]:>2} papers  {status}  │")
        print(f"  │  {'TOTAL':>4}  {'':20} {len(self.papers):>2} papers     │")
        print("  └─────────────────────────────────────────────────┘")

        print("\n  ┌─ Platform Distribution ──────────────────────────┐")
        for plat, cnt in plat_counts.most_common():
            bar = "█" * cnt
            pct = cnt / len(self.papers) * 100
            print(f"  │  {plat:<10} {bar:<20} {cnt:>2} ({pct:.0f}%)      │")
        print("  └─────────────────────────────────────────────────┘")

   

    def _validate_columns(self, found: set) -> None:
        missing = self.REQUIRED_COLUMNS - found
        if missing:
            raise ValueError(f"Corpus CSV is missing columns: {missing}")

    def _export_json(self) -> None:
        os.makedirs("data", exist_ok=True)
        out_path = "data/corpus.json"
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(self.papers, fh, indent=2, ensure_ascii=False)
        print(f"  JSON export written to '{out_path}'")

    def _check_loaded(self) -> None:
        if not self._loaded:
            raise RuntimeError("Call load() before accessing corpus data.")
