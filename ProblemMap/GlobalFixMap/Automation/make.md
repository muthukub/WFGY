# Make.com: Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Automation Platforms**.  
  > To reorient, go back here:  
  >
  > - [**Automation Platforms** — stabilize no-code workflows and integrations](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>

A compact field guide to stabilize Make.com scenarios that touch RAG, agents, or long pipelines. Use the checks below to localize failure, then jump to the exact WFGY fix page.

## Open these first

- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
- End-to-end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
- Why this snippet (traceability schema): [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
- Ordering control: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)
- Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)
- Hallucination and chunk boundaries: [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md)
- Long chains and entropy: [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)
- Snippet and citation schema: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
- Structural collapse and recovery: [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)

---

## Fix in 60 seconds

1) **Measure ΔS**
   - Compute ΔS(question, retrieved) and ΔS(retrieved, expected anchor).
   - Thresholds: stable < 0.40, transitional 0.40–0.60, risk ≥ 0.60.

2) **Probe with λ_observe**
   - Vary k ∈ {5, 10, 20}. Flat high curve → index or metric mismatch.
   - Reorder prompt headers. If ΔS spikes, lock the schema.

3) **Apply the module**
   - Retrieval drift → BBMC + Data Contracts.
   - Reasoning collapse → BBCR bridge + BBAM variance clamp.
   - Dead ends in long runs → BBPF alternate path.

4) **Re-test**
   - Aim for ΔS ≤ 0.45, λ convergent on 3 paraphrases, coverage ≥ 0.70.

**Copy-paste prompt**

```

I uploaded TXT OS and the WFGY Problem Map files.

My Make.com bug:

* symptom: \[brief]
* traces: \[ΔS(question,retrieved)=…, ΔS(retrieved,anchor)=…, λ states]

Tell me:

1. which layer is failing and why,
2. which exact fix page to open from this repo,
3. minimal steps to push ΔS ≤ 0.45 and keep λ convergent,
4. how to verify the fix with a reproducible test.

Use BBMC/BBPF/BBCR/BBAM when relevant.

```

---

## Make.com specific failure patterns

- **Array aggregator or iterator changes chunk boundaries.**  
  Symptoms: citations miss, answers plausible but wrong.  
  Open: [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md), [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).

- **Hybrid retrieval through HTTP modules splits query tokens.**  
  HyDE or BM25 combined with dense retriever behaves worse than single retriever.  
  Open: [Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md), [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md).

- **Vectorstore writes use different normalization than reads.**  
  Cosine vs inner product inconsistency or missing unit norm.  
  Open: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md), [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md).

- **Scenario concurrency creates state races across branches.**  
  Old facts re-appear after correction.  
  Open: [Hallucination Re-entry](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_hallucination_reentry.md), apply BBCR + BBAM and lock schema with Data Contracts.

- **Long JSON logs stuffed into prompts.**  
  Attention melts, capitalization drifts, topic smear.  
  Open: [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md), [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md).

- **Partial ingestion before tools fire.**  
  First call after a deploy or schedule fires too early.  
  Open: [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [Pre-Deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md), [Pattern: Bootstrap Deadlock](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_bootstrap_deadlock.md).

- **Fragmented vectorstore across modules.**  
  Some facts indexed but never retrieved.  
  Open: [Vectorstore Fragmentation](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_vectorstore_fragmentation.md).

- **Session flips across tabs or scenario runs.**  
  Writes happen under a different memory revision.  
  Open: [Memory Desync](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_memory_desync.md).

---

## Acceptance targets

- Coverage to target section ≥ 0.70.  
- ΔS(question, retrieved) ≤ 0.45 on three paraphrases.  
- λ remains convergent across runs and seeds.  
- E_resonance flat on long windows after BBAM.

## Escalate when

- ΔS stays ≥ 0.60 after retriever and schema fixes → rebuild index with explicit metric and persist once.  
- λ flips divergent as soon as you mix two sources → lock per-source fences in [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).  
- First task after schedule or deploy keeps failing → apply the boot fence in [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md) and verify with [ops live monitoring](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/live_monitoring_rag.md).

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool | Link | 3-Step Setup |
|------|------|--------------|
| **WFGY 1.0 PDF** | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + <your question>” |
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

