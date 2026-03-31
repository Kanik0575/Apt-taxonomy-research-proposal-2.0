# Temporal Stratification — Method Documentation

## What Is Temporal Stratification?

Temporal Stratification is a **corpus balancing technique** where the total
paper quota is divided into fixed yearly allocations **before** any papers
are selected. Each year's allocation is then filled independently.

This prevents **recency bias** — the tendency for recent years to dominate
a corpus simply because more papers were published recently.

---

## Why We Needed It

Between 2020 and 2026, APT research publications grew exponentially:

```
Approximate publications per year on APT attacks (all 4 databases combined):

2020: ~800 papers
2021: ~950 papers
2022: ~1,200 papers
2023: ~1,600 papers
2024: ~2,100 papers
2025: ~2,400 papers
2026: ~350 papers (Jan-Mar only)
      ─────────────────────────
Total: ~9,400 papers
```

Without stratification, a relevance-ranked selection of 100 papers from
9,400 would yield roughly:

```
2020: ~4 papers   ← severely under-represented
2021: ~5 papers   ← severely under-represented
2022: ~8 papers
2023: ~18 papers
2024: ~28 papers  ← over-represented
2025: ~33 papers  ← over-represented
2026: ~4 papers
```

This would make 2020–2022 research effectively invisible.

---

## Our Allocation Schema

| Year | Allocated | Stratum Type | Rationale |
|------|-----------|-------------|-----------|
| 2020 | 14 | Baseline | Standard stratum |
| 2021 | 14 | Baseline | Standard stratum |
| 2022 | 14 | Baseline | Standard stratum |
| 2023 | 14 | Baseline | Standard stratum |
| 2024 | 14 | Baseline | Standard stratum |
| 2025 | 14 | Baseline | Standard stratum |
| 2026 | **16** | Extended | Partial year (Jan–Mar); +2 compensates for lower volume |
| **TOTAL** | **100** | | |

---

## Intra-Stratum Selection

Within each year's stratum, candidate papers are ranked by:
1. APT relevance score (primary)
2. Venue quality (secondary)
3. Age-normalized citation count (tertiary)

The top-ranked papers fill the stratum quota.

---

## Verification

The corpus is verified by running `src/main.py`, which checks that
each year contains exactly its allocated number of papers and prints
a pass/fail report for each stratum.
