# Pipedream — Guardrails and Fix Patterns

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

Use this when your integration is built on **Pipedream** (HTTP triggers, Node/Python steps, marketplace components) and answers look plausible but wrong, citations don’t line up, or flows pass step-by-step while users still see inconsistencies.

**Acceptance targets**
- ΔS(question, retrieved) ≤ 0.45
- Coverage ≥ 0.70 to the intended section/record
- λ stays convergent across 3 paraphrases

---

## Typical breakpoints → exact fixes

- Output sounds right but cites the wrong snippet or section  
  Fix No.1: **Hallucination & Chunk Drift** →  
  [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md) ·  
  [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)

- High vector similarity, wrong meaning in answers  
  Fix No.5: **Embedding ≠ Semantic** →  
  [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

- Indexed facts exist (S3/GSheet/Notion/DB) but never appear in top-k  
  Pattern: **Vectorstore Fragmentation** →  
  [Vectorstore Fragmentation](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_vectorstore_fragmentation.md)

- Can’t show “why this snippet?” from within step logs  
  Fix No.8: **Retrieval Traceability** + snippet/citation schema →  
  [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) ·  
  [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

- Long multi-step flows drift in tone or logic (especially with retries)  
  Fix No.3/No.9: **Context Drift** and **Entropy Collapse** →  
  [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md) ·  
  [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)

- Works in test events, fails in scheduled/production runs (secrets/env mismatch)  
  Infra: **Pre-Deploy / Bootstrap / Deadlock** →  
  [Pre-Deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md) ·  
  [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md) ·  
  [Deployment Deadlock](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md)

- Model answers confidently with wrong claims  
  Fix No.4: **Bluffing / Overconfidence** →  
  [Bluffing](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bluffing.md)

---

## Minimal Pipedream pattern with WFGY checks

A compact flow outline that enforces **cite-first schema**, **observable retrieval**, and **ΔS/λ** validation.

```txt
Trigger: HTTP / Webhook (POST)

Step 1 — Parse input
- Extract "question" and optional "k" (default 10)

Step 2 — Retrieve context (custom component or HTTP)
- POST to your retriever: { question, k }
- Return: snippets[], each with { snippet_id, text, source, section_id }

Step 3 — Assemble prompt (Node step)
SYSTEM:
  Cite lines before any explanation. Keep per-source fences.
TASK:
  Answer only from the provided context. Return citations as [snippet_id].
CONTEXT:
  <joined snippets with snippet_id + source + text>
QUESTION:
  <user question>

Step 4 — Call LLM (component or HTTP)
- Input: prompt from Step 3
- Output: answer + raw citations if available

Step 5 — WFGY post-check (HTTP to your wfgyCheck function)
- Body: { question, context, answer }
- Return: { deltaS, lambda, coverage, notes }

Step 6 — Gate
IF deltaS ≥ 0.60 OR lambda != "→"
   → Fail fast with 422 and include trace table (snippet_id↔citation)
ELSE
   → 200 OK with { answer, deltaS, lambda, coverage, citations[] }
````

Reference specs:
[RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) ·
[Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) ·
[Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) ·
[Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

---

## Pipedream-specific gotchas

* **Event truncation**: large contexts exceed step memory or event size. Use external store for snippets, inject only ids + short preview into the prompt, and re-fetch on demand.
  See [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

* **Package/runtime drift**: Node/Python versions or package pins differ between components. Pin versions and rebuild embeddings/index with the same runtime.
  See [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

* **Concurrent runs reorder records** and break implicit ranking. Add a **rerank** step after per-source ΔS ≤ 0.50.
  See [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)

* **Secret/connection mismatch across sources**: different tokens for ingestion vs query cause empty/partial retrieval. Verify in a boot check before first LLM call.
  See [Pre-Deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

* **Marketplace components hide prompts**: wrap LLM calls in your own component so the **cite-first schema** and fences are explicit in code.
  See [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)

---

## When to escalate

* ΔS stays ≥ 0.60 after chunking/retrieval fixes → rebuild index with explicit metric flags and unit normalization.
  [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)

* Answers flip between preview and deployed sources → verify version skew, secret scope, and environment variables.
  [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md) ·
  [Deployment Deadlock](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md)


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

