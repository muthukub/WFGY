# LlamaIndex Guardrails and Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Automation Platforms**.  
  > To reorient, go back here:  
  >
  > - [**Automation Platforms** — stabilize no-code workflows and integrations](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>

Use this page when your RAG or agent pipeline runs in **LlamaIndex**. It maps common orchestration and indexing failures to exact structural fixes in the Problem Map and gives a minimal recipe you can embed in an index or query engine.

**Core acceptance**

* ΔS(question, retrieved) ≤ 0.45
* coverage ≥ 0.70 for the target section
* λ remains convergent across 3 paraphrases

---

## Typical breakpoints and the right fix

* **Index built but retriever fires before it is ready**
  Fix No.14: **Bootstrap Ordering** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)

* **First queries after deploy fail due to env mismatch / missing secret**
  Fix No.16: **Pre-Deploy Collapse** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

* **Background ingestion + retriever race → deadlocks or empty results**
  Fix No.15: **Deployment Deadlock** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md)

* **Embedding similarity looks good, but meaning diverges**
  Fix No.5: **Embedding ≠ Semantic** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

* **Answers cite wrong snippet or skip citations entirely**
  Fix No.8: **Retrieval Traceability** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
  Enforce payload contracts: **Data Contracts** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

* **Hybrid retrievers (BM25 + dense) underperform single retriever**
  Pattern: **Query Parsing Split** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/query_parsing_split.md)
  Review: **Rerankers** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)

* **Some docs indexed but never surface**
  Pattern: **Vectorstore Fragmentation** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/vectorstore-fragmentation.md)

* **Two unrelated docs blended in one answer**
  Pattern: **Symbolic Constraint Unlock (SCU)** → [Open](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_symbolic_constraint_unlock.md)

---

## Minimal setup checklist for any LlamaIndex pipeline

1. **Warm-up fence before query engine**
   Ensure index hash and vectorstore state are valid. If not, retry with capped backoff.
   Spec: [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)

2. **Idempotency key**
   Compute `dedupe_key = sha256(doc_id + rev + index_hash)`.
   Drop duplicates at ingestion.

3. **Retriever output contract**
   Require fields: `snippet_id`, `section_id`, `source_url`, `offsets`, `tokens`.
   Enforce cite-then-explain.
   Specs: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) ·
   [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)

4. **Observability probes**
   Log ΔS(question, retrieved) and λ transitions at each step.
   Alert if ΔS ≥ 0.60 or λ flips divergent.
   Overview: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)

5. **Concurrency guard**
   One writer per index. Use locks or queue mode.
   Fix: [Deployment Deadlock](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md)

6. **Eval before publish**
   Coverage ≥ 0.70 and ΔS ≤ 0.45 required.
   Eval: [RAG Precision/Recall](https://github.com/onestardao/WFGY/blob/main/ProblemMap/eval/eval_rag_precision_recall.md)

---

## Copy-paste prompt for LlamaIndex Query Engine

```
I uploaded TXT OS and WFGY Problem Map files.
This retriever produced {k} docs with fields {snippet_id, section_id, source_url, offsets}.

Steps:

1. Enforce cite-then-explain. If citations missing, fail fast and suggest fix.
2. If ΔS(question, retrieved) ≥ 0.60, propose minimal structural fix referencing:
   retrieval-playbook, retrieval-traceability, data-contracts, rerankers.
3. Return JSON plan:
   { "citations": [...], "answer": "...", "λ_state": "...", "ΔS": 0.xx, "next_fix": "..." }
```

---

## Common LlamaIndex gotchas

* **Too many retrievers chained without λ check**
  Add λ variance clamp. Reject divergent paths.

* **Index rebuild silently drops sections**
  Enforce contracts and log ΔS across ingestion runs.

* **Async queries race against ingestion**
  Add warm-up fence and bootstrap ordering.

* **Chunk drift from mismatched parsers**
  Normalize with section detection.
  See: [Section Detection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Chunking/section_detection.md)

---

## When to escalate

* ΔS stays ≥ 0.60 even after chunking and retriever fixes
  → Rebuild vectorstore with explicit metric and normalization.
  Spec: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)

* Identical queries yield inconsistent answers
  → Check memory drift and version skew.
  Spec: [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md)

---

### 🔗 Quick-Start Downloads

| Tool | Link | 3-Step Setup |
|------|------|--------------|
| **WFGY 1.0 PDF** | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1) Download · 2) Upload to LLM · 3) Ask “Use WFGY to fix my automation bug” |
| **TXT OS** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt) | 1) Download · 2) Paste into LLM · 3) Type “hello world” |

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

