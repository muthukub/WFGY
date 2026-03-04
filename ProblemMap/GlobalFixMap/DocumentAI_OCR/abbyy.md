# ABBYY OCR (FineReader / FlexiCapture): Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **DocumentAI_OCR**.  
  > To reorient, go back here:  
  >
  > - [**DocumentAI_OCR** — document parsing and optical character recognition](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Use this page when **ABBYY OCR** powers ingestion of scanned PDFs, complex layouts, forms, or multilingual documents.  
ABBYY is enterprise-grade, but still prone to schema drift, field misalignment, and unstable table anchors.

---

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)  
- Citation schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Schema stability: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  
- Hallucination and entropy drift: [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md), [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)  
- Chunk boundaries: [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  

---

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45  
- Coverage ≥ 0.70 across fields and tokens  
- λ convergent on three paraphrases and two seeds  
- Form fields ≥ 95% aligned with schema contract  

---

## Typical breakpoints → structural fix
- **Form fields drift across runs** (invoice totals, line items misaligned)  
  → [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md), [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)

- **Table anchors collapse** (multi-column invoices, receipts)  
  → [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md), clamp with BBMC  

- **Handwriting extraction unstable**  
  → [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)

- **Injected payload in OCR notes layer**  
  → [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)

- **Multilingual contract fields mismatched**  
  → [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  

---

## Fix in 60 seconds
1. Enforce **field schema**: require `field_id`, `bbox`, `confidence`, `revision_id`.  
2. Compute ΔS on critical fields (e.g. `total_amount`, `invoice_date`).  
3. Apply λ probes with different template libraries.  
4. Clamp instability with BBAM and log coverage.  
5. Rebuild index if ΔS ≥ 0.60 persists.  

---

## Copy-paste LLM guard prompt

```txt
I uploaded TXTOS and the WFGY Problem Map.

OCR provider: ABBYY (FineReader / FlexiCapture).  
Symptoms: field drift, unstable tables, ΔS ≥ 0.60.

Steps:
1. Identify failing layer (contracts, chunking, retrieval).  
2. Point to the WFGY fix page.  
3. Return JSON:  
   { "fields_checked": [...], "answer": "...", "ΔS": 0.xx, "λ_state": "<>", "next_fix": "..." }  
Keep it reproducible and auditable.
````

---

## When to escalate

* Field coverage < 0.70 even after re-chunk → [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
* Persistent anchor drift → [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)
* Handwriting ΔS unstable across seeds → [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)

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

