# Chunking to Embedding Contract — Guardrails and Fix Pattern

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **RAG_VectorDB**.  
  > To reorient, go back here:  
  >
  > - [**RAG_VectorDB** — vector databases for retrieval and grounding](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Use this page when **retrieval fails because the chunk schema is not aligned with the embedding ingestion contract**.  
If the retriever expects fields that were never embedded, or chunks omit IDs/offsets/anchors, then citations drift and ΔS rises.

---

## Open these first

- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Snippet and citation schema: [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Retrieval traceability: [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Chunking checklist: [chunking-checklist.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  

---

## Core acceptance

- Every chunk has `chunk_id`, `section_id`, `source_url`, `offsets`, `tokens`.  
- Embedding index was built from the same schema as retrieval contract.  
- ΔS(question, retrieved) ≤ 0.45 across 3 paraphrases.  
- Coverage ≥ 0.70 to the target section.  

---

## Typical breakpoints and the right fix

- **Missing fields** in ingestion (e.g., no `section_id`)  
  → Enforce [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).  

- **Different schema for ingest vs retrieve**  
  → Corpus ingested raw text, retriever expects chunk JSON → rebuild with schema.  

- **Offsets not tracked**  
  → Cannot map back to original document → enforce `offsets` at ingest.  

- **Tokenizer drift**  
  → Chunk IDs differ between preprocessing runs → use [chunking-checklist.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md).  

---

## Fix in 60 seconds

1. **Check ingestion schema**  
   Compare the fields stored in the index with the fields expected in retrieval.

2. **Align contracts**  
   Define `chunk = {chunk_id, section_id, source_url, offsets, tokens, text}`.  
   Enforce that this exact object is used both in ingestion and retrieval.

3. **Rebuild index if misaligned**  
   If fields differ, re-ingest corpus with enforced schema.

---

## Copy-paste schema

```json
{
  "chunk_id": "uuid-v4",
  "section_id": "doc-23-sec-7",
  "source_url": "https://example.com/doc23",
  "offsets": [120, 320],
  "tokens": 512,
  "text": "...."
}
````

Target: retriever always returns this schema, LLM consumes directly.

---

## Common gotchas

* Only `text` embedded, no IDs → cannot trace back → citations drift.
* Chunk boundaries not logged → hallucinations reappear.
* JSON schema updated mid-deploy → index mismatch.

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

