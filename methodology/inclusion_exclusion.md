# Inclusion & Exclusion Criteria

## Inclusion Criteria

A paper must satisfy **ALL** of the following to be included:

| # | Criterion | How Checked |
|---|-----------|-------------|
| I1 | Published between 2020-01-01 and 2026-03-31 | Publication date in database metadata |
| I2 | Peer-reviewed (journal article, conference paper, or book chapter) | Publication type filter in database |
| I3 | Indexed in at least one of the four designated databases | Confirmed by retrieval source |
| I4 | Explicitly addresses APT lifecycle stage mapping OR proposes automated APT classification | Abstract screening by two reviewers |
| I5 | Written in English | Language filter in database |

## Exclusion Criteria

A paper is excluded if it meets **ANY** of the following:

| # | Criterion | Rationale |
|---|-----------|-----------|
| E1 | Focuses exclusively on general malware (ransomware, spyware) without explicit APT-level analysis | Not within scope — APT requires nation-state/advanced actor context |
| E2 | Does not propose, evaluate, or utilize a classification or taxonomization method | Purely descriptive papers do not contribute to automated taxonomy construction |
| E3 | Grey literature: technical reports, vendor white papers, blog posts | Lack peer-review rigor required for academic corpus |
| E4 | Duplicate record of a previously selected paper | Regardless of which database retrieved it |
| E5 | Full text unavailable through institutional or open-access channels | Cannot perform full-text verification of methodology |

## Borderline Cases — Decision Rules

- **"APT" mentioned but focus is on malware analysis:** → EXCLUDE under E1
  unless the paper explicitly maps APT lifecycle stages.

- **Survey/review paper with no new classification method:** → INCLUDE if it
  provides a synthesis of automated classification approaches (contributes
  to taxonomy scope mapping).

- **Paper on MITRE ATT&CK but applied to generic threats:** → EXCLUDE under E1
  unless the paper's evaluation dataset consists specifically of APT campaigns.

- **Preprint (arXiv) later published in a conference:** → INCLUDE the
  published version; EXCLUDE the preprint version.
