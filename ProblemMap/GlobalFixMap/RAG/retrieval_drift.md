# Retrieval Drift — Guardrails and Fix Pattern

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


When the correct fact exists in your corpus but retrieval consistently misses it.  
This page localizes drift in retrievers and routes you to structural fixes with measurable acceptance targets.

---

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- End-to-end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)  
- Traceability schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Ordering control: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)  
- Snippet and citation schema: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  

---

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45  
- Coverage ≥ 0.70 of the target section  
- λ remains convergent across three paraphrases and two seeds  

---

## Typical symptoms → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| Facts exist but never surface | index skew or drift in chunk granularity | [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md), [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md) |
| Citations point to wrong section | schema mismatch or cross-section drift | [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| Answers alternate between runs | λ instability or reranker collapse | [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md), [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md) |
| High similarity but wrong meaning | embedding metric mismatch | [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) |

---

## Fix in 60 seconds

1. **Measure ΔS**  
   - Compute ΔS(question, retrieved) and ΔS(retrieved, expected anchor).  
   - Thresholds: stable < 0.40, transitional 0.40–0.60, risk ≥ 0.60.  

2. **Probe λ_observe**  
   - Ask the same question in 3 paraphrases.  
   - If λ flips divergent on harmless rewording, lock schema with Data Contracts.  

3. **Apply the module**  
   - Retrieval drift → BBMC + [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
   - Reasoning collapse → BBCR bridge + variance clamp  
   - Re-index with consistent metric and analyzer if ΔS stays ≥ 0.60  

---

## Copy-paste prompt for debug

```txt
I uploaded TXT OS and the WFGY Problem Map.

My retrieval issue:
- symptom: fact exists in corpus, but retriever misses
- traces: ΔS(question,retrieved)=..., λ across 3 paraphrases

Tell me:
1. failing layer (retriever, index, schema, reranker)
2. exact WFGY page to open
3. minimal steps to push ΔS ≤ 0.45 and keep λ convergent
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

