# 📚 Glossary — Terms, Symbols, and Short Definitions

> **Quick Nav**  
> [RAG Map 2.0](./rag-architecture-and-recovery.md) ·
> [Retrieval Playbook](./retrieval-playbook.md) ·
> [Patterns](./patterns/README.md) ·
> [Eval](./eval/README.md)

---

## Core instruments

- **ΔS (delta-S)** — *Semantic stress.* `ΔS = 1 − cos(I, G)` where `I` is item embedding, `G` is ground/anchor.  
  Thresholds: `<0.40` stable · `0.40–0.60` transitional · `≥0.60` high risk.

- **λ_observe** — *Layered observability state.*  
  Symbols: `→` convergent · `←` divergent · `<>` recursive · `×` chaotic.

- **E_resonance** — *Coherence indicator.* Rolling mean of |residual| under BBMC; rising E with high ΔS ⇒ apply BBCR/BBAM.

---

## Repair operators (WFGY modules)

- **BBMC** — *Boundary-Bounded Memory Chunks.* Reduce semantic residue vs anchors; align chunks/sections with tasks.  
- **BBPF** — *Branch-Bounded Prompt Frames.* Explore multiple semantic paths safely; stabilize context windows.  
- **BBCR** — *Break-Before-Crash Reset.* Detect collapse, insert bridge node, restart cleanly.  
- **BBAM** — *Attention Modulation.* Reduce variance in attention to avoid entropy melt on long contexts.

---

## Retrieval, ranking & prompting

- **RRF (Reciprocal Rank Fusion)** — Fuse ranks from multiple retrievers via `1/(k + rank)`.  
- **MMR (Maximal Marginal Relevance)** — Diversify candidates balancing relevance and novelty.  
- **BM25** — Sparse lexical scoring for exact term match; strong for code/IDs.  
- **HyDE** — Hypothetical document expansion; creates a synthetic query/doc to improve recall.  
- **Cross-encoder reranker** — Jointly encodes `[query ⊕ doc]` for precision@k gains.

---

## Patterns (named failure modes)

- **SCU (Symbolic Constraint Unlock)** — Model merges sources or violates “cite-then-explain” schema. Fix: per-source fences + locked schema.  
- **Query Parsing Split** — Dense and sparse retrievers use different analyzers/tokenizers; hybrid breaks.  
- **Vectorstore Fragmentation** — Index contains “ghost” gaps; facts exist but never retrieved; fix shard/id audits.  
- **Memory Desync** — State flips between sessions/tabs; require `mem_rev`+`mem_hash`.  
- **Role Drift** — Multi-agent persona swap; tag agent IDs and lock via BBCR.

---

## Multi-agent

- **Agent boundary** — Contract that limits what an agent can read/write; prevents overwrite.  
- **ΔS peer check** — Measures divergence between agents’ plans to catch conflicts early.

---

## Data & ops

- **Gold set** — Small set (10–50) of realistic Q/A with citations; used for CI (recall@50, nDCG@10, ΔS).  
- **Traceability** — Provenance from answer → prompt → citations → chunks → source file.

---

## Notation quickies

- `I` — item (retrieved chunk) embedding; `G` — ground/anchor embedding.  
- `‖B‖ ≥ B_c` — collapse threshold on residual magnitude (BBCR).  
- *Convergent λ* — layer is stable across paraphrases; *divergent λ* — layer is drifting.

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

