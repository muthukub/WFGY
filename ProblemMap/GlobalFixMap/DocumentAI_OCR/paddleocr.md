# PaddleOCR: Guardrails and Fix Patterns

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


Use this page when your stack integrates **PaddleOCR** (from Baidu PaddlePaddle).  
It’s widely used for open-source OCR pipelines, especially in Chinese / multilingual contexts.  
Common risks: unstable detection boxes, segmentation drift, and mixed-language confusion.

---

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- End-to-end knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)  
- Traceability schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Schema contracts: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  
- Chunking rules: [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  
- Injection risks: [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)  

---

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45  
- Coverage ≥ 0.70 across multilingual tokens  
- λ convergent across 3 paraphrases  
- BBox coverage ≥ 95% on gold set images  

---

## Typical breakpoints → structural fix
- **Chinese / English mix mis-segmented**  
  → [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md), [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

- **Bounding boxes drift** (word cropped or merged incorrectly)  
  → [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), enforce field anchors

- **Long text lines wrapped unpredictably**  
  → [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)

- **Injected noise from non-text graphics**  
  → [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)

- **Low recall on handwriting or distorted fonts**  
  → [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)  

---

## Fix in 60 seconds
1. Normalize text direction (LTR vs RTL) before feeding embeddings.  
2. Apply schema: `bbox`, `text`, `lang`, `confidence`, `rev_id`.  
3. Measure ΔS(question, retrieved). Threshold ≥ 0.60 → suspect segmentation or index.  
4. Clamp λ with BBAM if paraphrases diverge.  
5. Re-chunk with stride windows for multilingual pages.  

---

## Copy-paste guard prompt

```txt
I uploaded TXTOS and the WFGY Problem Map.

OCR provider: PaddleOCR.  
Symptoms: multilingual mis-segmentation, ΔS ≥ 0.60, bbox drift.

Steps:
1. Identify failing layer (chunk, retrieval, schema).  
2. Point to correct WFGY page.  
3. Return JSON:  
   { "bbox_checked": [...], "answer": "...", "ΔS": 0.xx, "λ_state": "<>", "next_fix": "..." }  
Keep it short, reproducible, auditable.
````

---

## When to escalate

* Persistent bbox drift → [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
* Schema mismatch across languages → [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
* ΔS unstable across seeds → [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

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

