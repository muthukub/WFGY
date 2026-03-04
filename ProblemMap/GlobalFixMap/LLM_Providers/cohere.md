# Cohere: Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **LLM_Providers**.  
  > To reorient, go back here:  
  >
  > - [**LLM_Providers** — model vendors and deployment options](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Use this page when issues look provider-specific on Cohere (Command family, chat tools, embeddings). The checks below route you to the exact WFGY fix page and give a minimal recipe you can paste into your pipeline.

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
- End-to-end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
- Why this snippet (traceability schema): [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
- Ordering control: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)
- Embedding ≠ semantic meaning: [Embedding vs Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)
- Hallucination and chunk boundaries: [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md)
- Long chains and entropy: [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)
- Snippet and citation schema: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
- Structural collapse and recovery: [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)
- Ops and live checks: [Debug Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md), [Live Monitoring](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/live_monitoring_rag.md)
- Patterns to confirm: [Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md), [Vectorstore Fragmentation](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_vectorstore_fragmentation.md)
- Governance and locale: [Safety Boundary Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Safety_Boundary_Problems.md), [Multilingual Guide](https://github.com/onestardao/WFGY/blob/main/ProblemMap/multilingual-guide.md)

## Fix in 60 seconds

1) **Measure ΔS**
   - Compute ΔS(question, retrieved) and ΔS(retrieved, expected anchor).
   - Thresholds: stable < 0.40, transitional 0.40–0.60, risk ≥ 0.60.

2) **Probe with λ_observe**
   - Vary k = {5, 10, 20}. Flat high curve ⇒ index or metric mismatch.
   - Reorder prompt headers. If ΔS spikes, lock the schema.

3) **Apply WFGY modules**
   - Retrieval drift ⇒ **BBMC** + **Data Contracts**.
   - Reasoning collapse ⇒ **BBCR** bridge + **BBAM** variance clamp.
   - Dead ends in long runs ⇒ **BBPF** alternate path.

4) **Provider checks that often matter on Cohere**
   - **Function-call / tool JSON**: enforce the contract with a header block; validate outputs against your [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).
   - **Context truncation**: if answers “forget” late citations, run [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md) + [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md) probes and shorten or re-chunk.
   - **Embedding mismatch**: if using Cohere embeddings with a third-party store, confirm metric and dimension, then run [Embedding vs Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) and [Vectorstore Fragmentation](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_vectorstore_fragmentation.md).
   - **Safety over-blocks**: if citations are removed or text is blanked, check [Safety Boundary Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Safety_Boundary_Problems.md) and tighten source scoping in the prompt.
   - **Multi-tool chaos**: if tool calls flip between runs, review [Multi-Agent Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Multi-Agent_Problems.md) and split memory namespaces.

## Typical breakpoints and the right fix

| Symptom | Likely cause | Open this | Minimal repair |
|---|---|---|---|
| Citations point to the wrong passage | retrieval drift or reranker noise | [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md), [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md) | BBMC + reranker window tune; verify with ΔS ≤ 0.45 |
| Tool output misses required keys | schema unlocked | [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) | Add schema header + reject-and-retry loop |
| Good chunks, wrong reasoning | logic collapse | [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md) | BBCR bridge + BBAM clamp |
| High similarity, wrong meaning | embedding metric mismatch | [Embedding vs Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) | Re-embed or change index metric; re-verify ΔS |
| Answers flip across seeds | memory namespace collisions | [Multi-Agent Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Multi-Agent_Problems.md) | Split mem namespaces; lock rev/hash |
| Streaming cuts mid-sentence | truncation or stop join fail | [Debug Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md) | Increase limits, add join checks, re-measure ΔS |

## Acceptance targets

- Coverage to target section ≥ 0.70.  
- ΔS(question, retrieved) ≤ 0.45 across three paraphrases.  
- λ stays convergent across seeds.  
- E_resonance flat on long windows.

## Copy-paste prompt (safe)

```

I uploaded TXT OS and the WFGY Problem Map files.

My Cohere issue:

* symptom: \[brief]
* traces: \[ΔS(question,retrieved)=..., ΔS(retrieved,anchor)=..., λ states]

Tell me:

1. which layer is failing and why,
2. which exact fix page to open from this repo,
3. minimal steps to push ΔS ≤ 0.45 and keep λ convergent,
4. how to verify with a reproducible test.

Use BBMC/BBPF/BBCR/BBAM when relevant.

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

If you want me to continue with another provider now, I’ll go in this order unless you say otherwise: `azure_openai.md` → `bedrock.md` → `groq.md` → `together.md` → `openrouter.md` → `perplexity.md` → `nvidia_nim.md`.
