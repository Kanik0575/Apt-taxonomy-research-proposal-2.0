# Methodology Explained — Plain English Guide

This document explains the entire project methodology in simple, clear language.
Use this to understand the project before your presentation.

---

## The Big Picture — What Did We Do?

We wanted to build a **map of how APT (Advanced Persistent Threat) attacks work**,
based on what the academic world has discovered between 2020 and 2026.

An APT is not a regular virus or ransomware attack. APT attacks are run by
**nation-states or highly sophisticated criminal groups** who:
- Spend weeks or months inside a network without being detected
- Have specific goals (steal defence secrets, disrupt infrastructure, etc.)
- Use advanced, custom techniques that normal antivirus cannot catch

Our taxonomy is essentially a **structured, automated map** of all the techniques
APT attackers use at each stage of their attack.

---

## Step 1 — Why We Needed Papers

To build this map, we needed **evidence from peer-reviewed research**. We could not
just rely on one or two reports — we needed a broad, balanced view of what the
academic community has found.

So we decided to use **100 papers** as our evidence base. This is called a **corpus**.

---

## Step 2 — Where We Found the Papers (Platforms)

We searched four major academic databases:

**IEEE Xplore**
- Think of this as the world's largest library of engineering and computer science research
- Where most cybersecurity conference papers are published

**ACM Digital Library**
- The Association for Computing Machinery's library
- Covers computing, AI, networking, and security

**SpringerLink**
- Covers journals and book chapters in computer science and security
- Includes the Lecture Notes in Computer Science (LNCS) series

**Scopus**
- The broadest academic index — covers all of the above plus more
- We used it to cross-check that we had not missed anything

---

## Step 3 — What Keywords We Searched

We did not just type "APT attack" into Google. We used a specific **Boolean search query**:

```
("Advanced Persistent Threat" OR "APT")
AND
("Automated Taxonomy" OR "Classification" OR "Framework" OR "MITRE ATT&CK")
```

**Breaking it down:**

The first part — `("Advanced Persistent Threat" OR "APT")`:
- We need BOTH the full phrase and the abbreviation
- Because some papers say "Advanced Persistent Threat" and others just say "APT"
- Using OR means we get both

The second part — `("Automated Taxonomy" OR "Classification" OR "Framework" OR "MITRE ATT&CK")`:
- We only want papers that actually DO something with APT data — classify it,
  organize it, or build a framework around it
- "Automated Taxonomy" = papers that automatically organize APT attacks
- "Classification" = papers that sort APT attacks into categories using ML
- "Framework" = papers that propose a structured way to analyze APTs
- "MITRE ATT&CK" = papers using the industry-standard APT knowledge base

The AND between the two parts means a paper must match BOTH conditions to appear.

---

## Step 4 — The Problem We Discovered (Too Many Papers)

Our keyword search returned **1,208 papers** across the 4 databases.

But here is the problem — we only needed 100. And we could not just pick the
"top 100" because of a statistical problem called **recency bias**:

```
Publications on APT attacks grew like this:
  2020: ~800 papers published that year
  2021: ~950 papers
  2022: ~1,200 papers
  2023: ~1,600 papers
  2024: ~2,100 papers
  2025: ~2,400 papers
```

If we simply picked the 100 most relevant papers, we would end up with
maybe 80 papers from 2023–2025 and only 5–8 papers from 2020–2021.

**Why is this bad?**
- We could not study how APT techniques CHANGED over time
- Early research (2020–2021) would be invisible
- Our taxonomy would only reflect recent thinking, not the full picture

---

## Step 5 — Our Solution: The 4-Stage Filtering Protocol

We designed a 4-stage pipeline to filter from 1,208 papers down to exactly 100.

### Stage 1 — Identification
Run the keyword search. Collect all results. Total: 1,208 papers.

### Stage 2 — Deduplication
Many papers appeared in multiple databases. We removed duplicates by
matching on title + DOI + author names.
- Removed: 308 duplicates
- Kept: 900 unique papers

### Stage 3 — Screening
Two researchers read the title and abstract of all 900 papers.
A paper was kept only if it passed ALL inclusion criteria and failed NONE
of the exclusion criteria.
- Excluded: 640 papers (mostly general malware papers with no APT focus)
- Kept: 260 eligible papers

### Stage 4 — Temporal Stratification (The Anti-Bias Fix)
From 260 eligible papers, we applied our year-by-year quota system.
See the next section for full explanation.
- Final corpus: exactly 100 papers

---

## Step 6 — Temporal Stratification Explained Simply

**The analogy:**
Imagine you are organizing a conference and you have 100 seats. You want
representatives from every year between 2020 and 2026. If you just sell seats
on a first-come basis, 2024 and 2025 researchers will fill 80 seats because there
are more of them. So instead, you **pre-reserve** seats for each year:

| Year | Reserved Seats | Why |
|------|---------------|-----|
| 2020 | 14 | Baseline allocation |
| 2021 | 14 | Baseline allocation |
| 2022 | 14 | Baseline allocation |
| 2023 | 14 | Baseline allocation |
| 2024 | 14 | Baseline allocation |
| 2025 | 14 | Baseline allocation |
| 2026 | 16 | Extra 2 seats — only Jan–Mar 2026 existed when we searched |
| **TOTAL** | **100** | |

This is exactly what we did with papers. Each year has its own reserved slots,
filled independently by the best-ranked papers from that year.

**2026 gets 16 (not 14) because:**
We searched in March 2026. Only 3 months of 2026 data existed. A full year would
normally produce more papers. So we gave 2026 two extra slots to compensate
for the partial year.

---

## Step 7 — How We Chose Papers Within Each Year

When a year had more eligible papers than its quota (e.g., 2023 had 48 eligible
papers but only 14 slots), we ranked the papers by:

1. **APT Relevance Score** (most important)
   - Does the abstract explicitly address APT lifecycle stages or automated classification?
   - Scored 0–3 by two independent reviewers

2. **Venue Quality** (second most important)
   - Is this a top journal (Q1/Q2 Scimago) or top conference (CORE A*/A rated)?

3. **Citation Impact** (tie-breaker)
   - How many times has it been cited, adjusted for how old it is?

The top-ranked papers fill the slots.

---

## Step 8 — How We Built the Taxonomy

Once we had our 100 papers, we read each one and tagged it with:
- Which **APT lifecycle stages** it covers (MITRE ATT&CK tactic codes like TA0001)
- Which **automated classification methods** (CP-01 to CP-09) it uses

Then our Python code:
1. Maps all tactic codes to our 14 taxonomy nodes (T1–T14)
2. Counts how many papers cover each node
3. Identifies which classification methods dominate each stage
4. Generates all visualizations and the final report

---

## Key Numbers to Remember for Your Presentation

| Metric | Value |
|--------|-------|
| Databases searched | 4 (IEEE, ACM, Springer, Scopus) |
| Raw papers found | 1,208 |
| After deduplication | 900 |
| After screening | 260 |
| Final corpus | 100 |
| Papers per year (2020–2025) | 14 each |
| Papers for 2026 | 16 |
| Taxonomy nodes | 14 |
| Classification parameters | 9 |
| Most-covered stage | T12 Command & Control (91/100 papers) |
| Hardest to detect stages | T7 Defense Evasion + T12 C2 (both ★★★★★) |
