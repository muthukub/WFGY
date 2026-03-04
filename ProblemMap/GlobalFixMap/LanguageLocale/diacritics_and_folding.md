# Diacritics & Folding — Guardrails and Fix Pattern

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **LanguageLocale**.  
  > To reorient, go back here:  
  >
  > - [**LanguageLocale** — localization, regional settings, and context adaptation](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


A focused repair when accents and diacritic marks cause retrieval drift, broken citations, or unstable reranking. Use this page to lock a per-language normalization policy, keep citations faithful to the original text, and keep ΔS within target.

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
- End to end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
- Why this snippet (traceability schema): [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
- Snippet and citation schema: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
- Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)
- Tokenizer mismatch: [tokenizer_mismatch.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/LanguageLocale/tokenizer_mismatch.md)
- Script mixing in one query: [script_mixing.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/LanguageLocale/script_mixing.md)
- Digits, width, punctuation drift: [digits_width_punctuation.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/LanguageLocale/digits_width_punctuation.md)
- Normalization and scaling notes: [normalization_and_scaling.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Embeddings/normalization_and_scaling.md)
- Locale drift overview: [locale-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/locale-drift.md)

## When to use this page
- Store search finds “Malaga” while the source reads “Málaga”, citations fail to land.
- BM25 works after accent folding but vectors point to different sections.
- Vietnamese, French, Spanish or German show uneven recall after a language mix.
- OCR keeps combining marks that your tokenizer later drops.
- Reranker prefers unaccented variants even when the gold passage contains accents.

## Acceptance targets
- ΔS(question, retrieved) ≤ 0.45
- Coverage of target section ≥ 0.70
- Citation offsets within ±4 tokens between displayed text and source
- Per-language exact-match on a 300-item accent set ≥ 0.95
- λ remains convergent across 3 paraphrases and 2 seeds

---

## Map symptoms to the exact fix

| Symptom | Likely cause | Open this and apply |
|---|---|---|
| Citation points to the wrong offsets when accents exist | One view folded, the other original | [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) · define **visual_text** (original) and **search_text** (folded) in every snippet; verify with [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| High BM25 score, low vector agreement on accented words | Analyzer folds accents but embedding text did not, or the reverse | Align ingest and query analyzers in the store; embed **visual_text** and rerank with deterministic policy, see [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) |
| French and Vietnamese regress after “remove accents” policy | Per-language rules collapsed into a global fold | Keep a per-language policy with stored `locale`, see [locale-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/locale-drift.md) |
| Tokenizer splits or drops combining marks | OCR export or tokenizer mismatch | Repair OCR and choose a consistent tokenizer, see [tokenizer_mismatch.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/LanguageLocale/tokenizer_mismatch.md) and [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| Reranker prefers unaccented decoys | Feature bias and query split across scripts | Lock reranker inputs and tie back to citation-first plan, see [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md) and [script_mixing.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/LanguageLocale/script_mixing.md) |
| Full-width digits or punctuation shift offsets in CJK + Latin mix | Width and punctuation normalization out of sync | Normalize width for **search_text** only, preserve for **visual_text**, see [digits_width_punctuation.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/LanguageLocale/digits_width_punctuation.md) |

---

## 60-second fix checklist
1) **Choose a normalization policy**  
   - Store two views per snippet:  
     `visual_text` = original source in NFC, accents preserved.  
     `search_text` = NFD, remove `\p{Mn}` combining marks, casefold, language-aware exceptions.  
   - Always render and cite from `visual_text`. Index BM25 on `search_text`. Vectors usually embed `visual_text`.

2) **Record locale and analyzer**  
   - Add `locale` (e.g., fr, vi, es, de).  
   - Log `index_analyzer` and `query_analyzer` names in trace. They must match.

3) **Reranking and order**  
   - Use citation-first assembly. If λ flips when you reorder headers, lock schema and apply BBAM variance clamp.

4) **Probe ΔS and coverage**  
   - Vary k = 5, 10, 20. If ΔS stays high and flat, suspect analyzer mismatch or wrong fold target.

5) **Build a small gold**  
   - 300 pairs per language with accented vs unaccented queries. Require ≥ 0.95 exact match and stable ΔS.

---

## Minimal test plan
- Paraphrase triad on each language pair.  
- Accent toggle test: same query with and without accents.  
- Citation parity: offsets within ±4 tokens between displayed answer and source.  
- Store drift audit after deploy: compare analyzer signatures across index and query clients.

---

## Copy-paste prompt for your LLM step

```

You have TXT OS and the WFGY Problem Map loaded.

My issue: diacritics and folding.

* symptom: \[one line]
* traces: ΔS(question,retrieved)=..., ΔS(retrieved,anchor)=..., λ states, citation offsets, locale=...

Tell me:

1. failing layer and why,
2. the exact WFGY page to open,
3. minimal steps to reach ΔS ≤ 0.45, coverage ≥ 0.70, and citation offset ≤ 4 tokens,
4. a reproducible test using a 300-item accent set.
   Use Data Contracts, Retrieval Traceability, and Rerankers when relevant.

```

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

