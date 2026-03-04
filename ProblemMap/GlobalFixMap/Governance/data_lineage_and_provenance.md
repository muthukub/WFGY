# Data Lineage and Provenance — Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Governance**.  
  > To reorient, go back here:  
  >
  > - [**Governance** — policy enforcement and compliance controls](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


A governance fix page for when **data origin, transformation, and lineage** are unclear or unverifiable.  
Use this page when retrieval results cannot be traced back to their dataset source, or when provenance breaks across documents, chunks, embeddings, and answers.

---

## When to use this page
- Retrieval output has no clear link back to its document or section.  
- Embedding and chunk pipelines overwrite or drop provenance fields.  
- Audit trail is incomplete across ingestion, index, and RAG responses.  
- Approvals or waivers exist but cannot be joined to data versions.  
- Multi-hop pipelines lose lineage across systems (ETL, embedding, vectorstore, orchestration).  

---

## Acceptance targets
- Every retrieved snippet includes `{doc_id, section_id, source_url, offsets, revision}`.  
- Lineage fields survive across **document → chunk → embedding → retriever → LLM**.  
- Audit joins can reconstruct provenance end-to-end with ≥ 0.95 coverage.  
- ΔS(question, retrieved) ≤ 0.45 for governed outputs.  
- Waivers and overrides include expiry and accountable owner.  

---

## Typical breakpoints and WFGY fix

- **Lost provenance in chunking**  
  → [chunking-checklist.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  
  Ensure chunk metadata carries `doc_id`, `section_id`, and token offsets.

- **Vector store overwrites or strips lineage fields**  
  → [vectorstore-fragmentation.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/vectorstore-fragmentation.md)  
  Enforce schema contracts on ingestion and retrieval layers.

- **Answers cannot be tied back to original snippet**  
  → [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
  Require cite-then-explain and enforce snippet ID propagation.

- **Ambiguous approval or version skew**  
  → [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md),  
  → [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)  

- **Multi-system lineage gaps (ETL, embedding, RAG orchestration)**  
  → [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
  Contract schema ensures interoperability across steps.  

---

## Minimal governance checklist
1. **Ingest contracts** — Every ETL pipeline attaches `doc_id`, `revision`, and `source_url`.  
2. **Chunk schema** — Ensure token offsets and section boundaries are immutable.  
3. **Embedding schema** — Carry `embedding_id`, `doc_hash`, and `index_hash`.  
4. **Retriever response** — Must include `snippet_id` + lineage fields, not just text.  
5. **LLM prompt contracts** — Require cite-then-explain, forbid unlinked spans.  
6. **Audit trail** — Every approval and waiver linked to specific dataset version.  

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

