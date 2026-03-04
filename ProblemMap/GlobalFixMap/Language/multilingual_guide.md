# Multilingual Guide — Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Language**.  
  > To reorient, go back here:  
  >
  > - [**Language** — multilingual processing and semantic alignment](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


A compact field guide to stabilize multilingual RAG across CJK, RTL, mixed scripts, and locale drift.
Use this page to check symptoms, apply structural fixes, and verify with measurable targets.

---

## Open these first

* Visual recovery map: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
* Tokenization vs semantics: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)
* OCR parsing in multilingual docs: [OCR Parsing Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ocr-parsing-checklist.md)
* Chunk joins across scripts: [Semantic Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)
* Why this snippet: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
* Snippet schema enforcement: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

---

## Core acceptance

* ΔS(question, retrieved) ≤ 0.45 across at least 2 languages
* Coverage ≥ 0.70 for the target section in each language
* λ remains convergent across three paraphrases in mixed scripts
* E\_resonance stays flat for long bilingual/RTL runs

---

## Common multilingual failure modes

| Symptom                                                       | Likely cause                                    | Open this                                                                                                                     |
| ------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Retrieval drops snippets when query is in Chinese or Japanese | Tokenizer mismatch (no whitespace segmentation) | [tokenizer\_mismatch.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Language/tokenizer_mismatch.md) |
| Citations collapse when Arabic/Hebrew text mixes with English | Script directionality conflict                  | [script\_mixing.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Language/script_mixing.md)           |
| High similarity but meaning flips across locale               | Locale analyzer mismatch (stemming / stopwords) | [locale\_drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Language/locale_drift.md)             |
| HyDE/BM25 retrieval different per language                    | Query expansion language bias                   | [hyde\_multilingual.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Language/hyde_multilingual.md)   |

---

## Fix in 60 seconds

1. **Probe with ΔS**
   Run the same question in English and one target language. If ΔS differs by >0.15, suspect tokenization or analyzer mismatch.

2. **Apply λ\_observe**
   Paraphrase the query three ways in the non-English language. If λ diverges, enforce schema lock and re-index with language-specific analyzers.

3. **Structural repair**

   * Tokenizer mismatch → [tokenizer\_mismatch.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Language/tokenizer_mismatch.md)
   * Script mixing issues → [script\_mixing.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Language/script_mixing.md)
   * Locale drift → [locale\_drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Language/locale_drift.md)
   * HyDE instability → [hyde\_multilingual.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Language/hyde_multilingual.md)

---

## Diagnostic checklist

* **Tokenizer**: verify segmentation strategy (whitespace vs character-level)
* **Analyzer**: confirm stemming and stopword lists match query language
* **Scripts**: normalize Unicode, check RTL/LTR flags
* **Locale drift**: run same snippet under two locales, compare ΔS
* **Hybrid retriever**: ensure rerankers operate on normalized embeddings

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

