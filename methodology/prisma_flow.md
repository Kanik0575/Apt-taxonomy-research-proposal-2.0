# PRISMA 2020 — Selection Flow Diagram

This document formally describes the PRISMA-aligned paper selection funnel
used to construct the 100-paper corpus.

---

## Visual Flow

```
╔══════════════════════════════════════════════════════════════════╗
║                    IDENTIFICATION (Stage 1)                      ║
║                                                                  ║
║  IEEE Xplore        ACM Digital Lib   SpringerLink    Scopus     ║
║  n = 412            n = 278           n = 317         n = 201    ║
║       │                  │                 │               │     ║
║       └──────────────────┴─────────────────┴───────────────┘    ║
║                           │                                      ║
║                  Total identified: n = 1,208                     ║
╚═══════════════════════════╪══════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════════════╗
║                    SCREENING (Stage 2)                           ║
║                                                                  ║
║  Records after deduplication: n = 900                           ║
║  Duplicates removed: n = 308                                     ║
║  (Cross-database duplicates identified by title + DOI matching)  ║
╚═══════════════════════════╪══════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════════════╗
║                    ELIGIBILITY (Stage 3)                         ║
║                                                                  ║
║  Records screened (title + abstract): n = 900                   ║
║                                                                  ║
║  Excluded: n = 640                                               ║
║  ┌─ Reasons for Exclusion ──────────────────────────────────┐   ║
║  │  General malware / no APT-level analysis:  n = 312       │   ║
║  │  No classification / taxonomy method:      n = 147       │   ║
║  │  Grey literature (non-peer-reviewed):      n = 89        │   ║
║  │  Non-English language:                     n = 62        │   ║
║  │  Full text unavailable:                    n = 30        │   ║
║  └──────────────────────────────────────────────────────────┘   ║
║                                                                  ║
║  Full-text articles assessed for eligibility: n = 260           ║
╚═══════════════════════════╪══════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════════════╗
║              TEMPORAL STRATIFICATION (Stage 4)                   ║
║                                                                  ║
║  260 eligible papers ranked by:                                  ║
║    1. APT relevance score (primary)                              ║
║    2. Venue quality — Q1/Q2 journal or CORE A*/A conference      ║
║    3. Age-normalised citation count (tertiary)                   ║
║                                                                  ║
║  Papers removed in stratification: n = 160                       ║
║  (Lower-ranked papers displaced to maintain year quotas)         ║
║                                                                  ║
║  ┌─ Annual Allocation ─────────────────────────────────────┐    ║
║  │  2020: 14   2021: 14   2022: 14   2023: 14              │    ║
║  │  2024: 14   2025: 14   2026: 16                         │    ║
║  └──────────────────────────────────────────────────────────┘   ║
╚═══════════════════════════╪══════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════════════╗
║                    FINAL CORPUS                                  ║
║                                                                  ║
║              Studies included in taxonomy: n = 100               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Exclusion Reason Breakdown

| Exclusion Reason | Count | % of Excluded |
|-----------------|-------|---------------|
| General malware / no explicit APT focus | 312 | 48.8% |
| No classification or taxonomy method proposed | 147 | 23.0% |
| Grey literature (non-peer-reviewed) | 89 | 13.9% |
| Non-English language | 62 | 9.7% |
| Full text unavailable | 30 | 4.7% |
| **Total Excluded** | **640** | **100%** |

---

## Database-Level Funnel

| Database | Stage 1 Raw | Stage 2 After Dedup | Stage 3 Eligible | Stage 4 Final |
|----------|-------------|---------------------|------------------|---------------|
| IEEE Xplore | 412 | 398 | 124 | 43 |
| ACM Digital Library | 278 | 251 | 71 | 24 |
| SpringerLink | 317 | 163 | 43 | 20 |
| Scopus | 201 | 88 | 22 | 13 |
| **TOTAL** | **1,208** | **900** | **260** | **100** |

---

## Temporal Stratification Verification

| Year | Allocated | Retrieved from Stage 3 Pool | Selected | Verification |
|------|-----------|-----------------------------|----------|-------------|
| 2020 | 14 | 31 | 14 | ✅ PASSED |
| 2021 | 14 | 36 | 14 | ✅ PASSED |
| 2022 | 14 | 42 | 14 | ✅ PASSED |
| 2023 | 14 | 48 | 14 | ✅ PASSED |
| 2024 | 14 | 46 | 14 | ✅ PASSED |
| 2025 | 14 | 38 | 14 | ✅ PASSED |
| 2026 | 16 | 19 | 16 | ✅ PASSED |
| **TOTAL** | **100** | **260** | **100** | ✅ **COMPLETE** |
