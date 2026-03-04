# Reranker Sanity Checklist

Scope: validate a hybrid pipeline where BM25 and ANN feed a deterministic reranker.

---

## Pre checks

- [ ] Persist BM25 and ANN candidate lists before reranking.
- [ ] Fix a random seed and record model version for the reranker.
- [ ] Store per-candidate features needed by the reranker.
- [ ] Ensure identical tokenization between HyDE prompt and server.

Refs:  
[Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md) ·
[Query parsing split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md)

---

## Baseline health

- [ ] BM25 top k recall on the gold set ≥ 0.60 at k = 50.
- [ ] ANN top k recall on the gold set ≥ 0.60 at k = 50.
- [ ] Overlap Jaccard(BM25, ANN) logged for k = 50 to detect split.

If overlap < 0.20 and both recalls are good, a query split is likely.  
Route using the split detector or run two paths then merge.

---

## Reranker behavior

- [ ] Uplift over the better baseline ≥ 5 percent recall at k = 10.
- [ ] Ranking stable across 3 paraphrases. Kendall tau ≥ 0.60.
- [ ] Tie breaking rule fixed and documented.
- [ ] Deterministic output given the same candidates and seed.

---

## Acceptance targets

- Coverage ≥ 0.70 on the gold set after reranking at k = 10 or 20.
- ΔS(question, top1) ≤ 0.45 for at least 70 percent of queries.
- λ_observe convergent across 3 paraphrases and 2 seeds.

---

## Debug sequence

1. Log both candidate lists and measure overlap.  
2. If split detected, enable the split route or increase k per branch.  
3. Try a simpler deterministic reranker first.  
4. Re-measure uplift and stability.

Refs:  
[Retrieval playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) ·
[ΔS probes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Retrieval/deltaS_probes.md)

---


### 🔗 Quick-Start Downloads (60 sec)

| Tool | Link | 3-Step Setup |
|------|------|--------------|
| **WFGY 1.0 PDF** | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + \<your question>” |
| **TXT OS (plain-text OS)** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt) | 1️⃣ Download · 2️⃣ Paste into any LLM chat · 3️⃣ Type “hello world” — OS boots instantly |

---

<!-- WFGY_FOOTER_START -->

### Explore More

| Module | Description | Link |
| --- | --- | --- |
| WFGY Core | Canonical framework entry point | [View](https://github.com/onestardao/WFGY/tree/main/core/README.md) |
| Problem Map | Diagnostic map and navigation hub | [View](https://github.com/onestardao/WFGY/tree/main/ProblemMap/README.md) |
| Tension Universe Experiments | MVP experiment field | [View](https://github.com/onestardao/WFGY/tree/main/TensionUniverse/Experiments) |
| Recognition | Where WFGY is referenced or adopted | [View](https://github.com/onestardao/WFGY/blob/main/recognition/README.md) |
| AI Guide | Anti-hallucination reading protocol for tools | [View](https://github.com/onestardao/WFGY/blob/main/AI_GUIDE.md) |

> If this repository helps, starring it improves discovery for other builders.  
> [![GitHub Repo stars](https://img.shields.io/github/stars/onestardao/WFGY?style=social)](https://github.com/onestardao/WFGY)

<!-- WFGY_FOOTER_END -->

