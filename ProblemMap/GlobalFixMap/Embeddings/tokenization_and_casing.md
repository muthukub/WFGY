# Tokenization and Casing — Guardrails for Embedding Stability

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Embeddings**.  
  > To reorient, go back here:  
  >
  > - [**Embeddings** — vector representations and semantic search](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


A focused guide to remove silent drift caused by mismatched tokenization, casing, and text cleanup. Use this to align query-time and index-time preprocessing, then verify with measurable targets.

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
- End to end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
- Why this snippet (traceability schema): [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
- Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)
- Payload schema for audits: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
- Query split and hybrid failures: [Pattern: Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md)
- Reranking and ordering control: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)
- Related: normalization and length scaling: [Normalization & Scaling](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Embeddings/normalization_and_scaling.md)

## When to use this page
- High similarity yet wrong meaning after a casing change.
- Same document retrieved for lowercase but not for Title Case.
- Index built with a different tokenizer than the client.
- Unicode variants or punctuation collapse changes results.
- Hybrid retrieval recalls but top-k order flips between runs.

## Acceptance targets
- ΔS(question, retrieved) ≤ 0.45 on three paraphrases.
- Coverage of the correct section ≥ 0.70.
- λ remains convergent across two seeds.
- Tokenization invariance check: replacing case or applying Unicode NFC does not move the top anchor beyond rank 3 and keeps ΔS shift ≤ 0.10.

---

## Map symptoms → exact fix

- Wrong-meaning hits only when case changes  
  → Lock a single case policy and tokenizer in both paths. Verify with [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) and enforce with [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).

- HyDE or BM25 path finds it, embedding path misses it  
  → Audit query preprocessing vs index preprocessing. If different, unify and retest. See [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) and [Pattern: Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md).

- Unicode look-alikes or punctuation variants break recall  
  → Normalize to NFC and collapse zero-width characters at both index and query. Re-embed affected shards. Cross check with [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md).

- Order flips across runs after a client upgrade  
  → Version the tokenizer and preprocessing in the snippet payload. If versions mismatch, rebuild or add a translation shim. Enforce with [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).

---

## 60-second fix checklist

1) **Freeze the tokenizer and case policy**
   - Choose one tokenizer build and one case policy: `lower`, `preserve`, or `smart`.  
   - Record both in the contract:  
     `{"tokenizer":"spm-1.2.3","tokenizer_hash":"...","case_policy":"lower"}`.

2) **Normalize before tokenization**
   - Apply Unicode NFC, collapse repeated whitespace, remove zero-width, standardize quotes and dashes.  
   - Apply the same rules to both index and query.

3) **Keep segmentation symmetric**
   - If you split code identifiers (camelCase, snake_case), do it in both paths.  
   - If you strip stopwords or punctuation, do it in both paths. Prefer not to strip unless you must.

4) **Log and test invariance**
   - Run a three-paraphrase probe per query: original, lowercased, and NFC-normalized.  
   - Accept only if the anchor section remains within top 3 and ΔS shift ≤ 0.10.

5) **Add a rerank safety net**
   - If invariance is hard to reach, add a lexical or cross-encoder rerank after vector recall. See [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md).

---

## Contract fields to add

Add these to every snippet and to the query audit log. Use them during triage.

```json
{
  "preproc_version": "v3",
  "unicode_norm": "NFC",
  "case_policy": "lower",
  "punctuation_policy": "keep",
  "identifier_split": "camel+snake",
  "tokenizer": "spm-1.2.3",
  "tokenizer_hash": "sha256:...",
  "ngram": "none"
}
````

---

## Repro suite

* **Case flip test**
  Query A vs lowercase(A). Accept if ΔS shift ≤ 0.10 and anchor rank ≤ 3.

* **Unicode fold test**
  Replace curly quotes with straight quotes, normalize to NFC. Accept if ranks stable.

* **Tokenizer skew test**
  Run the same query through client and index tokenizers and compare token ids. Any mismatch is a fail that requires rebuild or a client shim.

---

## Copy-paste prompt for LLM triage

```
I uploaded TXT OS and the WFGY Problem Map.

My embedding issue:
- symptom: wrong top-k only when casing or unicode changes
- traces: ΔS(question,retrieved)=..., anchor=..., tokenizer=..., case_policy=...

Tell me:
1) which layer is failing and why,
2) which WFGY page to open,
3) the minimal steps to align tokenization and casing,
4) how to verify with a three-paraphrase probe.
Use Data Contracts and Rerankers if needed.
```

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

