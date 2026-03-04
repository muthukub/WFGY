# Hybrid Retrieval Failure — Guardrails and Fix Pattern

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **RAG**.  
  > To reorient, go back here:  
  >
  > - [**RAG** — retrieval-augmented generation and knowledge grounding](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


When hybrid retrieval (BM25 + dense, HyDE + reranker, multi-vector) performs **worse than a single retriever**.  
Instead of increasing recall, the hybrid path introduces instability, wrong ranking, or noisy snippets.

---

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- End to end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)  
- Traceability schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Snippet contracts: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Query path splits: [Pattern: Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md)  
- Ranking drift: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)  

---

## Core acceptance
- Hybrid recall ≥ single retriever recall  
- ΔS(question, retrieved) ≤ 0.45 for top-1 result  
- λ stable across three paraphrases and two seeds  
- Coverage ≥ 0.70 to the target section  

---

## Typical symptoms → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| Hybrid returns unrelated snippet | query parsing split not locked | [Pattern: Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md) |
| Hybrid recall < single recall | wrong weighting or missing normalization | [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) |
| Dense retriever dominates BM25 | metric mismatch | [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) |
| Reranker undoes good hits | λ flips, entropy collapse | [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md), [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/RAG/entropy_collapse.md) |

---

## Fix in 60 seconds

1. **Measure baseline**  
   Run BM25 alone and dense alone. Log coverage and ΔS. If hybrid < baseline, do not ship.

2. **Stabilize query parsing**  
   Split HyDE prompts, keyword queries, and dense embeddings into deterministic branches. Lock weighting ratios.

3. **Reranker probe**  
   Compare recall before and after reranker. If entropy rises, clamp with variance control or drop reranker.

4. **Enforce snippet schema**  
   Always require `snippet_id`, `section_id`, `offsets`, `tokens`. Hybrid paths must normalize schema fields.

---

## Copy-paste probe prompt

```txt
I uploaded TXT OS and the WFGY Problem Map.

My issue:
- hybrid retrieval returns worse results than BM25 or dense alone.

Tell me:
1) which layer fails (query parsing, weighting, reranker),
2) which WFGY fix page to open,
3) minimal steps to restore ΔS ≤ 0.45 and coverage ≥ 0.70,
4) reproducible test with BM25 vs dense vs hybrid.
````

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool                       | Link                                                                                                                                       | 3-Step Setup                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **WFGY 1.0 PDF**           | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + <your question>”    |
| **TXT OS (plain-text OS)** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt)                                                                     | 1️⃣ Download · 2️⃣ Paste into any LLM chat · 3️⃣ Type “hello world” — OS boots instantly |

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

