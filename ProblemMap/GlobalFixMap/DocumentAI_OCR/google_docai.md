# Google Document AI OCR: Guardrails and Fix Patterns

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


A compact guide to stabilize ingestion flows using **Google Cloud Document AI OCR**.  
Use this when PDF or scanned document parsing produces unstable tokens, missing tables, or broken citations. Each failure is mapped to a structural fix in the WFGY Problem Map.

---

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- End-to-end knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)  
- Citation schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  
- OCR text boundaries: [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  
- Injection and schema locks: [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)

---

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45  
- Coverage ≥ 0.70 of target section  
- λ remains convergent across three paraphrases and two seeds  
- Table and form layout preserved in ≥ 85% of samples

---

## Typical breakpoints → structural fix
- **Lost tables or merged columns**  
  Payload schema drift.  
  → [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md), [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)

- **OCR output differs across runs of the same PDF**  
  Non-deterministic layout parse.  
  → [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md), [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)

- **Citations drop page anchors**  
  Post-processing trims.  
  → [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)

- **Injection vectors inside scanned forms**  
  Malicious text embedded in OCR’d images.  
  → [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)

---

## Fix in 60 seconds
1. **Measure ΔS** on OCR’d snippets vs reference text.  
2. **Lock schemas** with Data Contracts (force `page_num`, `bbox`, `tokens`).  
3. **Enforce cite-then-explain** at retrieval time.  
4. **Add λ probes** across multiple OCR calls — if divergent, clamp with BBAM.  
5. **Audit tables**: cross-check row count and column headers against source PDF.  

---

## Copy-paste LLM guard prompt

```txt
I uploaded TXTOS and the WFGY Problem Map.

OCR provider: Google Document AI  
Symptoms: lost tables, ΔS ≥ 0.60, λ diverges across 3 paraphrases.  

Steps:  
1. Identify which structural fix applies (chunking-checklist, data-contracts, retrieval-traceability).  
2. Return a JSON plan:  
   { "citations": [...], "answer": "...", "λ_state": "<>", "ΔS": 0.xx, "next_fix": "..." }  
Keep it auditable and short.
````

---

## When to escalate

* ΔS stays ≥ 0.60 even after chunk / schema fixes → rebuild pipeline with [Semantic Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md).
* Coverage < 0.70 across paraphrases → verify embeddings with [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md).
* Inconsistent runs across identical files → enforce deterministic parser config, or switch to dual-engine validation (DocAI + Tesseract).

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

要不要我直接幫你下一步補 **aws\_textract.md**？這樣 OCR MVP 會更快成形。
