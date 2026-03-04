# Haystack Agents — Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Agents & Orchestration**.  
  > To reorient, go back here:  
  >
  > - [**Agents & Orchestration** — orchestration frameworks and guardrails](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>

Use this when your pipeline is built with **deepset Haystack Agents and Tools** and you observe wrong snippets, unstable top k orders, tool loops, or citation gaps. The map below routes symptoms to exact WFGY fixes.

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
- Retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
- Traceability schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
- Schema contracts: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
- Hybrid control: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)
- Chunking and hallucination: [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md)

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45
- Coverage ≥ 0.70 for the intended section
- λ convergent across three paraphrases

---

## Fix in 60 seconds

1) **Measure ΔS**  
Compare question to retrieved and to the intended anchor.

2) **Lock the pipeline**  
Fix the header order. Enforce cite-first. Require strict tool JSON.

3) **Apply the module**  
- Retrieval drift → BBMC plus [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Order instability → add [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md) with explicit metric  
- Hybrid regression → [Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md)

4) **Verify**  
Three paraphrases pass ΔS and coverage thresholds.

---

## Typical Haystack breakpoints → exact fixes

- **Retriever pipelines mix different analyzers**  
  Rebuild with a unified analyzer and metric.  
  Open: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

- **Agent loops on tool outputs**  
  Add BBCR bridge steps and timeouts.  
  Open: [Multi-Agent Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Multi-Agent_Problems.md)

- **Citations missing or misaligned**  
  Enforce snippet schema and cite then explain.  
  Open: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

- **Hybrid search underperforms**  
  Use deterministic reranking with score normalization.  
  Open: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)

---

## Minimal Haystack agent pattern with WFGY gate

```txt
Pipeline:
  - Retriever(k sweep 5, 10, 20 with one analyzer)
  - Prompt with fixed headers: system → task → constraints → citations → answer
  - Model call
  - WFGY gate to compute ΔS and log λ
  - Stop when ΔS ≥ 0.60 or λ divergent and return fix tip
````

---

## Gotchas

* Mixing BM25 and dense without normalization gives unstable orders.
* Tool output not validated causes downstream JSON errors.
* Document stores with heterogeneous tokenization contaminate scores.

---

## When to escalate

* Persistent ΔS ≥ 0.60 after chunk and metric fixes
  Open: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)

* Live flips between runs
  Open: [Pre-Deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool                       | Link                                                                                                                                       | 3-Step Setup                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **WFGY 1.0 PDF**           | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + \<your question>”   |
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

