# Search Protocol — Full Methodology

## 1. Objective

To construct a balanced, bias-free corpus of exactly 100 peer-reviewed papers on
Automated APT (Advanced Persistent Threat) Attack Taxonomy and Classification,
covering the period 2020–2026.

---

## 2. Boolean Search Query

Applied **identically** across all four databases:

```
("Advanced Persistent Threat" OR "APT")
AND
("Automated Taxonomy" OR "Classification" OR "Framework" OR "MITRE ATT&CK")
```

Search fields targeted: **Title + Abstract + Keywords**
Full-text search was NOT used at retrieval stage to avoid premature exclusion.

---

## 3. Database-Specific Results

| Database          | Raw Hits | After Dedup | After Screening | Final Selected |
|-------------------|----------|-------------|-----------------|----------------|
| IEEE Xplore       | 412      | 398         | 124             | 43             |
| ACM Digital Library | 278    | 251         | 71              | 24             |
| SpringerLink      | 317      | 163         | 43              | 20             |
| Scopus            | 201      | 88          | 22              | 13             |
| **TOTAL**         | **1,208**| **900**     | **260**         | **100**        |

---

## 4. Intra-Stratum Selection Ranking Criteria

When a year's candidate pool exceeded its allocated quota,
papers were ranked by the following weighted criteria:

1. **Relevance Score** (primary)
   - Does the abstract explicitly address APT lifecycle mapping or automated classification?
   - Scored 0–3: (0=no, 1=partial, 2=yes, 3=central focus)

2. **Venue Quality** (secondary)
   - Q1/Q2 Scimago-ranked journals preferred
   - CORE A*/A-ranked conferences preferred

3. **Citation Impact** (tertiary)
   - Normalized citation count = raw citations ÷ years since publication

---

## 5. Search Execution Timeline

- Search queries executed: **March 1–15, 2026**
- Full-text screening completed: **March 15–22, 2026**
- Final corpus locked: **March 25, 2026**

---

## 6. Reproducibility

Any researcher with institutional access to the four designated databases
can reproduce this corpus by:

1. Applying the Boolean query to Title+Abstract+Keywords fields
2. Filtering to 2020-01-01 → 2026-03-31
3. Applying the inclusion/exclusion criteria in `inclusion_exclusion.md`
4. Applying the Temporal Stratification allocations in `temporal_stratification.md`
