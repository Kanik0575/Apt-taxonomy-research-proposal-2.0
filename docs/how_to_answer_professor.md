# How to Explain This Project to Your Professor

## Q: "How did you find these papers?"

We ran a Boolean keyword search on 4 databases (IEEE Xplore, ACM Digital Library,
SpringerLink, Scopus) using this exact query:

  ("Advanced Persistent Threat" OR "APT") AND
  ("Automated Taxonomy" OR "Classification" OR "Framework" OR "MITRE ATT&CK")

This returned 1,208 raw results across all databases.

---

## Q: "How do you know a paper is actually about APT attacks?"

We applied strict Inclusion Criteria. A paper was only kept if it:
1. Explicitly mapped APT lifecycle stages (Initial Access, Lateral Movement, etc.)
   OR proposed an automated method to classify APT threats.

General malware papers (ransomware, spyware) with no APT-specific analysis
were excluded under Exclusion Criterion E1.

---

## Q: "How did you prevent bias toward recent years?"

This is Temporal Stratification. Before selecting any papers, we pre-assigned
yearly quotas:
- 2020 to 2025: 14 papers each
- 2026: 16 papers (only Jan-Mar data, so slightly higher to compensate)

Each year's quota was filled independently from its own candidate pool.
No year could "steal" quota from another. This means 2020 research gets
exactly equal representation as 2024 research — even though 5x more papers
were published in 2024.

---

## Q: "Why not just pick the 100 most relevant papers?"

Because 80+ of them would be from 2023-2025, and you'd effectively be studying
only recent APT attacks. Temporal Stratification ensures you can study how
APT techniques evolved OVER TIME from 2020 to 2026.

---

## Q: "What are the classification parameters?"

The 9 CPs are the automated methods each paper uses. For example:
- CP-03 (NLP-Based TTP Extraction): The paper uses BERT or LLMs to read
  threat reports and automatically extract what attack techniques were used.
- CP-04 (Graph-Theoretic Modeling): The paper represents an APT campaign
  as a knowledge graph and classifies it by graph structure.
- CP-08 (C2 Traffic Analysis): The paper classifies network traffic to
  identify command-and-control channels.

When we classified each paper, we tagged which CPs it uses,
then used those tags to build the taxonomy.

---

## Q: "How does a paper get assigned to a taxonomy node?"

Each paper has Stage_Codes in the corpus (e.g., TA0001, TA0011).
These are MITRE ATT&CK tactic IDs. Our code maps:
  TA0001 → T3 (Initial Access)
  TA0011 → T12 (Command & Control)
  etc.

So if a paper focuses on C2 channel detection, it gets assigned to node T12.
If it covers the full kill chain, it's assigned to all relevant nodes.

---

## Q: "Why 100 papers specifically?"

100 is large enough for statistically meaningful coverage across 14 taxonomy
nodes AND across 7 years, while remaining manageable for full-text review.
With 14-16 papers per year and 14 taxonomy nodes, each node gets meaningful
coverage without any single node dominating.
