# Vectorstore Fragmentation — Guardrails and Fix Pattern

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


Use this page when **retrieval recall drops because the vector index is fragmented**.  
This happens when multiple shards, partitions, or replicas return partial results and the top-k merge is unstable.

---

## Open these first

- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Deployment issues: [deployment-deadlock.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md)  
- Retrieval playbook: [retrieval-playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)  
- Traceability schema: [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  

---

## Core acceptance

- Top-k results consistent across shards with variance ≤ 0.05.  
- Coverage ≥ 0.70 on the target section.  
- ΔS(question, retrieved) ≤ 0.45 across three paraphrases.  
- λ remains convergent under shard fanout.  

---

## Typical breakpoints and the right fix

- **Shards not balanced** → Some partitions miss updates, recall drops.  
  → Re-index with balanced sharding and verify ingestion logs.  

- **Merge strategy unstable** → Top-k from each shard merged without normalization.  
  → Apply global reranker after merging, not local-only.  

- **Version skew between replicas** → Old embeddings live in one shard.  
  → Enforce [deployment-deadlock.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md) checks and hash validation.  

- **Distributed query latency** → Timeout before all shards return.  
  → Add backpressure and enforce full quorum before top-k selection.  

---

## Fix in 60 seconds

1. **Run shard probe**  
   Fire the same query against each shard individually. Compare ΔS variance.

2. **Align replicas**  
   Verify `INDEX_HASH` matches across partitions. If not, rebuild.

3. **Global reranker**  
   Always normalize scores before merging. Rerank final list with semantic signal.

4. **Quorum guard**  
   Require ≥80% shard response before producing result. If missing, retry.

---

## Copy-paste probe script (pseudo)

```python
def shard_probe(query, shards):
    results = {}
    for shard in shards:
        hits = shard.search(query, k=10)
        ΔS_vals = [compute_deltaS(query, h) for h in hits]
        results[shard.id] = (np.mean(ΔS_vals), np.var(ΔS_vals))
    return results
````

Target: shard-to-shard ΔS variance ≤ 0.05.

---

## Common gotchas

* Shard IDs not logged → Cannot trace back retrieval → enforce [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md).
* Hybrid retriever mixing BM25 + dense done locally per shard → breaks weighting.
* Replicas updated asynchronously → ingestion race.

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

