# 🛡️ Automated Taxonomy of APT Attacks

> **Academic Research Project** — Post-Doctoral Cybersecurity Research | 2026
> A systematic, data-driven automated taxonomy of Advanced Persistent Threat (APT) attacks built from a rigorously curated corpus of **100 peer-reviewed papers (2020–2026)**.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [How We Found the Papers](#how-we-found-the-papers)
- [Search Keywords](#search-keywords)
- [Which Platforms We Used](#which-platforms-we-used)
- [Filtering Protocol (4 Stages)](#filtering-protocol-4-stages)
- [Temporal Stratification — How We Balanced Years](#temporal-stratification)
- [Inclusion & Exclusion Criteria](#inclusion--exclusion-criteria)
- [The Automated Taxonomy (14 Stages)](#the-automated-taxonomy)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Outputs](#outputs)

---

## Project Overview

This project constructs an **Automated Taxonomy of APT (Advanced Persistent Threat) Attacks** using a systematic literature review of 100 academic papers. The taxonomy:

- Aligns with the **MITRE ATT&CK Enterprise Matrix (v14.1)** as the normative baseline
- Classifies APT attacks across **14 lifecycle stages** (Reconnaissance → Impact)
- Uses **9 automated classification parameters** (NLP, graph models, ML classifiers)
- Was built from papers drawn from **4 major academic databases** using a **bias-free temporal sampling strategy**

The full methodology follows **PRISMA 2020** guidelines for systematic literature reviews.

---

## How We Found the Papers

### The Problem We Solved

Between 2020 and 2026, **over 10,000 papers** were published on APT attacks across major academic databases. We could not use all of them — we needed exactly 100 representative papers.

The challenge: if we just picked the 100 most relevant papers, **60–70% would come from 2023–2026** because recent years have far more publications. This would make 2020–2022 research invisible in our analysis — a bias called **recency bias**.

### Our Solution: A 4-Stage Filtering Pipeline

We designed a structured pipeline to get from ~10,000 papers down to exactly 100.

---

## Search Keywords

We used a single **Boolean search query** applied uniformly across all 4 databases:

```
("Advanced Persistent Threat" OR "APT")
AND
("Automated Taxonomy" OR "Classification" OR "Framework" OR "MITRE ATT&CK")
```

**Why these keywords?**

| Keyword | Why We Used It |
|---------|----------------|
| `"Advanced Persistent Threat" OR "APT"` | Catches both the full name and the abbreviation. APT is the official term for nation-state-level cyber attacks |
| `"Automated Taxonomy"` | Finds papers proposing machine-driven classification systems |
| `"Classification"` | Captures ML-based approaches (supervised, unsupervised, rule-based) |
| `"Framework"` | Finds structured methodological contributions |
| `"MITRE ATT&CK"` | Finds papers using the industry-standard adversary behavior knowledge base |

---

## Which Platforms We Used

We searched **4 internationally recognized academic databases**:

| Database | Why We Chose It | Papers in Final Corpus |
|----------|----------------|------------------------|
| **IEEE Xplore** | Primary source for cybersecurity, networking, and systems research | 43 papers (43%) |
| **ACM Digital Library** | Comprehensive computing research including threat intelligence | 24 papers (24%) |
| **SpringerLink** | Covers security journals + Lecture Notes in Computer Science (LNCS) | 20 papers (20%) |
| **Scopus (Elsevier)** | Cross-validates results; broadest interdisciplinary index | 13 papers (13%) |

Each database was searched **independently** to avoid missing papers. After all four searches, we removed duplicates that appeared in more than one database.

---

## Filtering Protocol (4 Stages)

### Stage 1 — Identification
Run the Boolean query on all 4 databases. Collect every result.

```
IEEE Xplore        → 412 raw results
ACM Digital Library → 278 raw results
SpringerLink       → 317 raw results
Scopus             → 201 raw results
─────────────────────────────────────
TOTAL              → 1,208 raw records
```

### Stage 2 — Deduplication
Many papers appear in multiple databases. We removed duplicates by matching on **title + DOI + authors**.

```
1,208 records
  → Remove 308 duplicates
  = 900 unique records
```

### Stage 3 — Title & Abstract Screening
Every one of the 900 unique papers was screened against our **Inclusion & Exclusion Criteria** (see below). A paper was kept only if it passed ALL inclusion criteria and failed NONE of the exclusion criteria.

```
900 records screened
  → Exclude 640 (general malware, off-topic, non-English, no classification method)
  = 260 eligible papers for full-text review
```

### Stage 4 — Temporal Stratification (The Bias Fix)
From the 260 eligible papers, we applied **Temporal Stratification** to build a balanced corpus of exactly 100 papers. See next section.

```
260 eligible papers
  → Apply year-by-year quotas
  = 100 final papers (the corpus)
```

---

## Temporal Stratification

### What Is It?

Temporal Stratification means **dividing your paper quota into yearly slots before you start selecting**, so no single year can dominate the corpus.

### How It Works (Simple Analogy)

Imagine you have 100 seats at a conference table. Instead of letting everyone fight for seats, you **pre-assign a fixed number of seats to each year**:

| Year | Seats Reserved | Reason |
|------|---------------|--------|
| 2020 | 14 | Baseline stratum |
| 2021 | 14 | Baseline stratum |
| 2022 | 14 | Baseline stratum |
| 2023 | 14 | Baseline stratum |
| 2024 | 14 | Baseline stratum |
| 2025 | 14 | Baseline stratum |
| 2026 | **16** | Extra 2 seats because 2026 is partial-year (Jan–Mar only); compensates for lower publication volume |
| **TOTAL** | **100** | ✅ |

### Why 2026 Gets 16 (Not 14)

By March 2026 (our search date), only 3 months of 2026 publications existed. To prevent 2026 from being severely under-represented compared to full years, we allocated 2 extra slots to capture the most current research trends.

### What Would Have Happened Without This?

Without Temporal Stratification, a purely relevance-based selection from 260 papers would have yielded approximately:
- 2020–2021: ~8 papers each (too few)
- 2023–2025: ~20+ papers each (too many)
- Result: A corpus biased toward recent work, making longitudinal trend analysis impossible

---

## Inclusion & Exclusion Criteria

### ✅ Inclusion Criteria — ALL must be true

1. Published between **January 1, 2020 and March 31, 2026**
2. **Peer-reviewed** journal article, conference paper, or book chapter
3. Indexed in **at least one** of the four designated databases
4. Explicitly addresses **APT lifecycle stage mapping** OR proposes **automated APT classification**
5. Written in **English**

### ❌ Exclusion Criteria — ANY one triggers exclusion

1. Focuses exclusively on **general malware** (ransomware, spyware, adware) **without explicit APT-level analysis**
2. Does **not propose or evaluate** a classification or taxonomization method — purely descriptive papers excluded
3. **Grey literature**: technical reports, vendor white papers, blog posts, non-peer-reviewed preprints
4. **Duplicate** of a paper already selected
5. **Full text unavailable** through institutional or open-access channels

---

## The Automated Taxonomy

The taxonomy has **14 nodes** aligned to MITRE ATT&CK tactics. Each node represents one phase of an APT attack lifecycle.

### How We Classify a Paper to a Node

Each paper is classified by:
1. Reading its abstract and methodology
2. Identifying which **MITRE ATT&CK tactic IDs** (TA00xx) it addresses
3. Mapping those IDs to our taxonomy nodes
4. Assigning **Classification Parameters** (CP-01 to CP-09) based on the automated methods used

### Taxonomy Summary Table

| Node | APT Stage | MITRE Tactic | Papers Covering It | Detection Difficulty |
|------|-----------|-------------|-------------------|---------------------|
| T1 | Reconnaissance | TA0043 | 41/100 | ★★★★☆ |
| T2 | Resource Development | TA0042 | 38/100 | ★★★☆☆ |
| T3 | Initial Access | TA0001 | **89/100** | ★★★☆☆ |
| T4 | Execution | TA0002 | 76/100 | ★★★★☆ |
| T5 | Persistence | TA0003 | 71/100 | ★★★☆☆ |
| T6 | Privilege Escalation | TA0004 | 58/100 | ★★★☆☆ |
| T7 | Defense Evasion | TA0005 | 82/100 | ★★★★★ |
| T8 | Credential Access | TA0006 | 63/100 | ★★★☆☆ |
| T9 | Discovery | TA0007 | 54/100 | ★★☆☆☆ |
| T10 | Lateral Movement | TA0008 | 67/100 | ★★★★☆ |
| T11 | Collection | TA0009 | 49/100 | ★★★☆☆ |
| T12 | Command & Control | TA0011 | **91/100** | ★★★★★ |
| T13 | Exfiltration | TA0010 | 78/100 | ★★★★☆ |
| T14 | Impact | TA0040 | 33/100 | ★★★☆☆ |

### 9 Classification Parameters Used

| ID | Parameter | What It Detects |
|----|-----------|----------------|
| CP-01 | Temporal Sequencing | Time-ordered TTP kill chains |
| CP-02 | Behavioral Fingerprinting | Adversary-unique behavioral signatures |
| CP-03 | NLP-Based TTP Extraction | Automated parsing of threat reports |
| CP-04 | Graph-Theoretic Modeling | Attack campaigns as knowledge graphs |
| CP-05 | ML-Driven Attribution | Classify campaigns to known APT groups |
| CP-06 | Indicator Correlation | Cross-campaign IOC clustering |
| CP-07 | Anomaly Detection | Novel/zero-day technique flagging |
| CP-08 | C2 Traffic Analysis | Command-and-control channel classification |
| CP-09 | Exfiltration Modeling | Data theft volume/timing classification |

---

## Project Structure

```
apt-taxonomy/
│
├── README.md                         ← This file
├── requirements.txt                  ← Python dependencies
├── .gitignore
│
├── data/
│   ├── corpus.csv                    ← All 100 papers (master dataset)
│   └── corpus.json                   ← Same data in JSON (auto-generated)
│
├── src/
│   ├── __init__.py
│   ├── main.py                       ← Entry point — runs full pipeline
│   ├── corpus_loader.py              ← Loads & validates the corpus
│   ├── filtering_protocol.py         ← Simulates the 4-stage filter
│   ├── taxonomy_classifier.py        ← Builds the automated taxonomy
│   ├── visualizer.py                 ← Generates all 6 charts
│   └── report_generator.py           ← Exports Markdown + CSV reports
│
├── methodology/
│   ├── search_protocol.md            ← Full search methodology document
│   ├── inclusion_exclusion.md        ← Inclusion/exclusion criteria
│   ├── temporal_stratification.md    ← Stratification method explained
│   └── prisma_flow.md                ← PRISMA-aligned selection funnel
│
├── taxonomy/
│   ├── apt_taxonomy.md               ← Full taxonomy documentation
│   ├── taxonomy_nodes.json           ← Machine-readable taxonomy structure
│   └── classification_parameters.json ← CP definitions
│
├── outputs/
│   ├── figures/                      ← Generated charts (PNG)
│   │   ├── 01_year_distribution.png
│   │   ├── 02_platform_distribution.png
│   │   ├── 03_stage_coverage.png
│   │   ├── 04_framework_distribution.png
│   │   ├── 05_classification_parameters_radar.png
│   │   └── 06_stage_year_heatmap.png
│   └── reports/
│       ├── taxonomy_report.md        ← Full auto-generated report
│       └── summary.csv               ← Per-node stats table
│
└── docs/
    ├── methodology_explained.md       ← Plain-English explanation
    └── how_to_answer_professor.md     ← Q&A guide
```

---

## How to Run

### Prerequisites

```bash
pip install matplotlib numpy pandas
```

### Run the Full Pipeline

```bash
# From the project root directory
python src/main.py
```

### What Happens When You Run It

```
STEP 1 › Loads all 100 papers from data/corpus.csv
STEP 2 › Simulates the 4-stage filtering protocol & prints the funnel
STEP 3 › Builds the automated taxonomy, maps papers to nodes
STEP 4 › Generates 6 publication-quality charts → outputs/figures/
STEP 5 › Exports taxonomy_report.md + summary.csv → outputs/reports/
```

---

## Outputs

After running `python src/main.py`:

| Output | Location | Description |
|--------|----------|-------------|
| Year Distribution Chart | `outputs/figures/01_year_distribution.png` | Bar chart proving equal year coverage |
| Platform Pie Chart | `outputs/figures/02_platform_distribution.png` | Paper share by database |
| Stage Coverage Chart | `outputs/figures/03_stage_coverage.png` | How many papers cover each APT stage |
| Framework Distribution | `outputs/figures/04_framework_distribution.png` | ML/classification methods used |
| Parameters Radar | `outputs/figures/05_classification_parameters_radar.png` | CP coverage spider chart |
| Stage × Year Heatmap | `outputs/figures/06_stage_year_heatmap.png` | Which stages were studied which years |
| Full Markdown Report | `outputs/reports/taxonomy_report.md` | Complete taxonomy with all tables |
| CSV Summary | `outputs/reports/summary.csv` | Per-node statistics |

---

## References

- MITRE ATT&CK Framework: https://attack.mitre.org
- PRISMA 2020 Guidelines: https://www.prisma-statement.org
- STIX 2.1 Standard: https://oasis-open.github.io/cti-documentation/stix/intro
- IEEE Xplore: https://ieeexplore.ieee.org
- ACM Digital Library: https://dl.acm.org
- SpringerLink: https://link.springer.com
- Scopus: https://www.scopus.com

---

*Post-Doctoral Cybersecurity Research | Automated Taxonomy of APT Attacks | 2026*
