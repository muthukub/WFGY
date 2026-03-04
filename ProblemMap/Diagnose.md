# 🩺 Semantic Failure Diagnostic Sheet

Select the symptom(s) you observe.  
Each entry links to the corresponding solution page in the WFGY Problem Map.  
🧩 Prefer runnable examples? **MVP Demos** → [ProblemMap/mvp_demo/README.md](./mvp_demo/README.md)

---

## Quick Nav
[Problem Map 1.0](./README.md) ·
[RAG Problem Map 2.0](./rag-architecture-and-recovery.md) ·
[Semantic Clinic Index](./SemanticClinicIndex.md) ·
[Retrieval Playbook](./retrieval-playbook.md) ·
[Rerankers](./rerankers.md) ·
[Data Contracts](./data-contracts.md) ·
[Multilingual Guide](./multilingual-guide.md) ·
[Privacy & Governance](./privacy-and-governance.md)

---

## Core 16 failures

| # | Symptom | Problem ID | Solution |
|---|---------|------------|----------|
| 1 | **Retriever returns wrong/irrelevant chunks; citations miss expected section** | #1 Hallucination & Chunk Drift | [hallucination.md](./hallucination.md) |
| 2 | **Correct chunks are present, but reasoning is wrong** | #2 Interpretation Collapse | [retrieval-collapse.md](./retrieval-collapse.md) |
| 3 | Multi-step tasks drift off-topic after a few hops | #3 Long Reasoning Chains | [context-drift.md](./context-drift.md) |
| 4 | Model answers confidently with made-up facts | #4 Bluffing / Overconfidence | [bluffing.md](./bluffing.md) |
| 5 | High cosine similarity but meaning is wrong | #5 Semantic ≠ Embedding | [embedding-vs-semantic.md](./embedding-vs-semantic.md) |
| 6 | Logic dead-ends; retries loop or reset nonsense | #6 Logic Collapse & Recovery | [logic-collapse.md](./logic-collapse.md) |
| 7 | Long conversation: model forgets previous context | #7 Memory Breaks Across Sessions | [memory-coherence.md](./memory-coherence.md) |
| 8 | Pipeline is opaque; unable to trace “why this snippet” | #8 Debugging is a Black Box | [retrieval-traceability.md](./retrieval-traceability.md) |
| 9 | Attention melts; output incoherent or repetitive | #9 Entropy Collapse | [entropy-collapse.md](./entropy-collapse.md) |
| 10 | Responses become flat, literal, lose creativity | #10 Creative Freeze | [creative-freeze.md](./creative-freeze.md) |
| 11 | Formal/symbolic prompts break the model | #11 Symbolic Collapse | [symbolic-collapse.md](./symbolic-collapse.md) |
| 12 | Self-reference / paradox crashes reasoning | #12 Philosophical Recursion | [philosophical-recursion.md](./philosophical-recursion.md) |
| 13 | Multiple agents overwrite or misalign logic (overview) | #13 Multi-Agent Chaos | [Multi-Agent_Problems.md](./Multi-Agent_Problems.md) |
| 14 | System runs but outputs nothing; boot order off | #14 Bootstrap Ordering | [bootstrap-ordering.md](./bootstrap-ordering.md) |
| 15 | System never reaches expected state; actions stall | #15 Deployment Deadlock | [deployment-deadlock.md](./deployment-deadlock.md) |
| 16 | First prod call after deploy crashes / “empty logic” | #16 Pre-Deploy Collapse | [predeploy-collapse.md](./predeploy-collapse.md) |

---

## Extended patterns (targeted fixes)

| Pattern | When to use | Fix page |
|---|---|---|
| **Rerankers (ordering control)** | Recall seems fine but top-k ordering is messy | [rerankers.md](./rerankers.md) |
| **Retrieval Playbook (end-to-end knobs)** | You want a guided checklist across retriever params | [retrieval-playbook.md](./retrieval-playbook.md) |
| **Query Parsing Split** | HyDE/BM25 hybrid worse than single retriever | [patterns/pattern_query_parsing_split.md](./patterns/pattern_query_parsing_split.md) |
| **Symbolic Constraint Unlock (SCU)** | “Who said what” merges across sources; cross-bleed | [patterns/pattern_symbolic_constraint_unlock.md](./patterns/pattern_symbolic_constraint_unlock.md) |
| **Hallucination Re-entry** | You correct the model, but the wrong claim returns | [patterns/pattern_hallucination_reentry.md](./patterns/pattern_hallucination_reentry.md) |
| **Vectorstore Fragmentation** | Some facts can’t be retrieved though indexed | [patterns/pattern_vectorstore_fragmentation.md](./patterns/pattern_vectorstore_fragmentation.md) |
| **Memory Desync** | Tabs/sessions flip between old/new facts | [patterns/pattern_memory_desync.md](./patterns/pattern_memory_desync.md) |
| **Bootstrap Deadlock (RAG boot fence)** | Tools fire before data/index is ready | [patterns/pattern_bootstrap_deadlock.md](./patterns/pattern_bootstrap_deadlock.md) |
| **Data Contracts** | Need a standard schema for snippets/citations | [data-contracts.md](./data-contracts.md) |
| **Multilingual Guide** | Non-English corpora drift / tokenizer mismatch | [multilingual-guide.md](./multilingual-guide.md) |
| **Privacy & Governance** | PII/compliance concerns for traces/logs | [privacy-and-governance.md](./privacy-and-governance.md) |

---

## Minimal triage rules

- **Measure first**:  
  - ΔS(question, retrieved\_context) = 1 − cosθ  
  - **High risk** if **ΔS ≥ 0.60**; **investigate** if **0.40–0.60** *and* λ ∈ {←, <>}.  
- **Accept when**: **ΔS ≤ 0.45** · λ stays **convergent (→)** on ≥3 paraphrases · **E\_resonance** flat.  
- **Coverage sanity**: retrieved tokens vs target section ≥ **0.70** for direct QA.

👉 Not sure where it fits? Run ΔS / λ_observe first, or use the MVP demos for quick diagnosis:
python ProblemMap/mvp_demo/main.py (run from repo root)

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

