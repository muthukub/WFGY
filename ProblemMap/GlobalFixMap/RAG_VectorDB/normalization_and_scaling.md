# Normalization and Scaling — Guardrails and Fix Pattern

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


Use this page when **vector similarity is unstable because embeddings are not normalized or scaling factors differ** between training and retrieval.  
This failure often appears when cosine distance is requested but vectors are stored raw, or when IP/dot metrics exaggerate magnitude.

---

## Open these first

- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Embedding vs meaning: [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  
- Metric mismatch: [metric_mismatch.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/RAG_VectorDB/metric_mismatch.md)  
- Chunking checklist: [chunking-checklist.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  

---

## Core acceptance

- Vectors are L2-normalized when using cosine similarity.  
- ΔS(question, retrieved) ≤ 0.45, stable across three paraphrases.  
- Coverage ≥ 0.70 on the target section.  
- λ remains convergent across seeds.  

---

## Typical breakpoints and the right fix

- **Cosine similarity reported but vectors not normalized**  
  → [metric_mismatch.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/RAG_VectorDB/metric_mismatch.md)  

- **Dot product used without rescaling** (large norm vectors dominate retrieval)  
  → Normalize or rescale embeddings before indexing.  

- **Cross-model mixing** (embeddings from different checkpoints with different norms)  
  → Re-normalize the corpus and queries to unit length.  

- **Hybrid dense + sparse weighting unstable** (scale mismatch between BM25 scores and vector norms)  
  → Apply explicit min-max or z-score scaling before weighted sum.  

---

## Fix in 60 seconds

1. **Check norms**  
   Sample 100 embeddings. Compute mean L2 norm. If not ~1.0 under cosine, normalization missing.

2. **Normalize queries**  
   Ensure `query_vector = vector / ||vector||` before retrieval when using cosine.

3. **Corpus re-index**  
   Drop and rebuild index with normalized vectors if store does not enforce it.

4. **Hybrid scaling**  
   Normalize dense similarity scores into the same 0–1 range as BM25 before combining.

---

## Copy-paste probe

```python
import numpy as np

def check_norms(vectors):
    norms = np.linalg.norm(vectors, axis=1)
    return norms.mean(), norms.std()

mean_norm, std_norm = check_norms(sample_vectors)
print("Mean norm:", mean_norm, "Std:", std_norm)
````

Target: mean ≈ 1.0, std ≤ 0.05 for cosine retrieval.

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

