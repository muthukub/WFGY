# Azure OCR (Computer Vision): Guardrails and Fix Patterns

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


Use this page when **Azure OCR** (part of Azure Cognitive Services / Computer Vision) drives ingestion for PDFs, scanned images, or mixed-language docs.  
Typical failures involve layout instability, multilingual tokenization errors, or coverage gaps in table/handwriting recognition.

---

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)  
- Citation schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  
- Hallucination and drift: [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md)  
- Chunk stability: [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  

---

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45  
- Coverage ≥ 0.70 to target section  
- λ convergent across 3 paraphrases and 2 seeds  
- Multilingual tokens ≥ 90% fidelity (baseline against source)  

---

## Typical breakpoints → structural fix
- **Language mixing errors** (Chinese + English, Arabic + Latin text)  
  → [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md), [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)

- **Table recognition drops column anchors**  
  → [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md), [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)

- **Handwriting recognition unstable across runs**  
  → [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)

- **ΔS > 0.60 when OCR normalizes accents/diacritics**  
  → [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), clamp with BBAM  

- **Injected content hidden in image metadata**  
  → [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)  

---

## Fix in 60 seconds
1. **Measure ΔS** between OCR tokens and reference text.  
2. **Enforce schema**: page, block, line, word. Require `bbox` and language tag.  
3. **Cross-check coverage**: at least 70% of expected lines present.  
4. **Apply λ probes** — vary recognition mode (printed, handwriting, mixed).  
5. **Clamp variance** with BBAM if multilingual drift repeats.  

---

## Copy-paste LLM guard prompt

```txt
I uploaded TXTOS and the WFGY Problem Map.

OCR provider: Azure OCR (Computer Vision).  
Symptoms: unstable multilingual recognition, ΔS ≥ 0.60, coverage < 0.70.

Steps:
1. Identify failing layer (chunking, contracts, retrieval).
2. Point to the WFGY fix (embedding-vs-semantic, chunking-checklist, retrieval-traceability).
3. Return JSON:
   { "citations": [...], "answer": "...", "ΔS": 0.xx, "λ_state": "<>", "next_fix": "..." }
Keep it auditable.
````

---

## When to escalate

* Multilingual drift remains after re-chunking → verify with [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md).
* Tables drop anchors repeatedly → rebuild layout with [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).
* Handwriting ΔS unstable across seeds → clamp with BBAM, audit using [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md).

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

要不要我接著直接幫你寫 **abbyy.md**？這樣 OCR 四大主流 (Tesseract、Google、AWS、Azure + ABBYY) 就全到齊。
