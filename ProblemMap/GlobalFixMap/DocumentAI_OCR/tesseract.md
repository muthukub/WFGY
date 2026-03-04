# Tesseract OCR: Guardrails and Fix Patterns

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


A compact field guide to stabilize Tesseract or Tesseract.js when used in AI pipelines, document ingestion, or hybrid RAG flows. Use these checks to pin down the failure, then jump directly to the WFGY structural fixes.

## Open these first

- Architecture baseline: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Chunking rules: [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  
- Misaligned snippets: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Schema enforcement: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Semantic mismatch: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  
- Boot order issues: [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [Deployment Deadlock](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md), [Pre-Deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

---

## Core acceptance

- ΔS(ground truth, OCR text) ≤ 0.35  
- Coverage ≥ 0.85 tokens per line  
- λ stays convergent across three OCR runs  
- Table cell alignment error ≤ 1 cell  
- Unicode normalization accuracy ≥ 0.95  

---

## Typical Tesseract breakpoints → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| Garbled characters (utf-8 vs utf-16) | codepage drift or bad normalization | [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md), [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| Wrong line breaks, merged words | bounding box drift or missing language model | [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| High similarity but meaningless embeddings | dirty OCR tokens, confusable glyphs | [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) |
| First call returns empty result | engine not ready, fonts not loaded | [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md) |
| Index ingestion with half-baked OCR text | deployment race or auth loop | [Deployment Deadlock](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md), [Pre-Deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md) |

---

## Fix in 60 seconds

1. **Run three OCR passes** on the same page.  
   Compare λ states. If they diverge, normalize with Unicode NFC and re-chunk.  

2. **Enforce contracts**.  
   Require `{line_id, bbox, text, lang}` per line. Reject entries missing `lang`.  

3. **ΔS probe**.  
   Compute ΔS against ground-truth anchors (gold set). If ΔS ≥ 0.45, enforce schema locks and rerun chunk alignment.  

4. **Publish only after stable run**.  
   Coverage ≥ 0.85 and ΔS ≤ 0.35 across 3 seeds.  

---

## Copy-paste prompt for OCR → LLM stage

```txt
You have TXTOS and the WFGY Problem Map loaded.

My OCR pipeline used Tesseract and produced N lines with fields {line_id, bbox, text, lang}.
Question: "{user_question}"

Do:

1. Validate ΔS against the anchor set.
2. If ΔS ≥ 0.45, point me to the minimal fix page (chunking-checklist, embedding-vs-semantic, retrieval-traceability).
3. Return JSON:
   { "citations": [...], "answer": "...", "ΔS": 0.xx, "λ_state": "...", "next_fix": "..." }
````

---

## Common gotchas

* Mixed fonts break recognition. Always load the correct traineddata file.
* Parallel OCR threads overwrite the same KV entry. Use idempotency keys.
* Tesseract.js on web workers drops unicode range ≥ U+3000. Force full model load.
* Line segmentation differs across seeds. Lock page segmentation mode (PSM).

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

