# OpenAI Assistants v2 — Guardrails and Fix Patterns

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

Use this page for **Assistants API v2** threads and runs when you hit tool JSON errors, missing citations, vector store mismatches, or state flips across retries. The map below routes each symptom to an exact WFGY fix.

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
- Retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
- Traceability and schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
- Hybrid order control: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)
- Deploy order: [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45
- Coverage ≥ 0.70 for the intended section
- λ convergent across three paraphrases and two seeds

---

## Fix in 60 seconds

1) **Measure ΔS**  
Compare question to retrieved and to the intended anchor.

2) **Stabilize thread and run**  
Pin `assistant_id`, freeze tool list and JSON schemas, and store `index_hash` with the thread.

3) **Apply the module**  
- Retrieval drift or wrong file selected → BBMC and [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Tool call loops → BBCR bridge and timeouts with strict schemas  
- Missing or wrong citations → [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)

4) **Verify**  
Three paraphrases meet ΔS and coverage. λ stays convergent.

---

## Typical Assistants v2 breakpoints → exact fixes

- **Files attached but the wrong chunk is used**  
  Index metric mismatch or analyzer drift.  
  Open: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

- **Run state flips between retry and resume**  
  Version skew or missing fences.  
  Open: [Pre-Deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

- **Tool JSON rejected with vague errors**  
  Relaxed schemas in prompt but strict in tool spec. Align both and echo schema at each step.  
  Open: [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)

- **Hybrid retrieval underperforms the simple retriever**  
  Two stage query split without rerank.  
  Open: [Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md), [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)

---

## Minimal Assistants v2 pattern with WFGY gate

```txt
Thread:
  - Attach files with stored index_hash
  - Record vector_ready and analyzer info
Run:
  - Retrieve(k = 10, unified analyzer)
  - Prompt headers in fixed order with cite-first
  - Model call
  - WFGY gate computes ΔS and logs λ
  - Stop when ΔS ≥ 0.60 or λ divergent and return fix tip
````

---

## Gotchas

* Mixing per file embeddings and global store without normalization.
* Recreating assistants on every request changes tool order and plan.
* Streaming partial results before schema checks leads to silent corruption.

---

## When to escalate

* Persistent ΔS ≥ 0.60 after chunk and metric fixes
  Open: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)

* Live flips with identical inputs
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

