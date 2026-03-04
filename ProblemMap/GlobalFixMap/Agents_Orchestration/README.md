<!--
Search Anchor:
agent orchestration bugs
multi-agent workflow failures
llm agent loop bugs
tool calling orchestration issues
agent role drift and coordination errors
-->


# Agents & Orchestration — Global Fix Map

<details>
  <summary><strong>🏥 Quick Return to Emergency Room</strong></summary>

<br>

  > You are in a specialist desk.  
  > For full triage and doctors on duty, return here:  
  > 
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md)  
  > 
  > Think of this page as a sub-room.  
  > If you want full consultation and prescriptions, go back to the Emergency Room lobby.
</details>

Agent and orchestration bugs are structural failures in multi-agent or tool-augmented systems, where coordination, role boundaries, execution order, or control flow break down even when the underlying model behaves correctly.

Most agent failures are not caused by model quality. They arise from role mixups, tool schema drift, uncontrolled loops, shared-state collisions, and cold-boot ordering errors. This page maps observable symptoms to structural fixes with measurable acceptance targets.

---

## Orientation: pick your orchestration layer

| Framework | What it is | Typical use | Link |
|---|---|---|---|
| Autogen | Multi-agent collaboration patterns | Debate, reviewer loops, tool arbitration | [autogen.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/autogen.md) |
| CrewAI | Role-based project crews | Task pipelines with clear roles | [crewai.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/crewai.md) |
| Haystack Agents | RAG-centric agents from deepset | Retrieval-heavy assistants | [haystack_agents.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/haystack_agents.md) |
| LangChain | Largest ecosystem of tools/memory | Rapid prototyping, complex chains | [langchain.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/langchain.md) |
| LangGraph | Graph execution over LC | Stateful paths, loops, guards | [langgraph.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/langgraph.md) |
| LlamaIndex | Knowledge-first orchestration | RAG pipelines, index control | [llamaindex.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/llamaindex.md) |
| OpenAI Assistants v2 | First-party assistants API | Files, tools, code-interpreter | [openai_assistants_v2.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/openai_assistants_v2.md) |
| Rewind Agents | Context replay paradigms | User-state reconstruction | [rewind_agents.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/rewind_agents.md) |
| Semantic Kernel | MS orchestration SDK | Plugins, plans, .NET/TS stacks | [semantic_kernel.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/semantic_kernel.md) |
| Smolagents | Minimalistic agent runtime | Constrained envs, fast spin-up | [smolagents.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/smolagents.md) |

---

## Core acceptance targets

- ΔS(question, retrieved) ≤ 0.45  
- Coverage ≥ 0.70 for the target section  
- λ stays convergent across 3 paraphrases and 2 seeds  
- E_resonance remains flat on long windows

These targets let you ship safely regardless of framework.

---

## Fix Hub — symptoms mapped to structural pages

| Symptom | Likely cause | Open this |
|---|---|---|
| JSON mode breaks, invalid tool objects | Tool protocol too loose | [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| Agents overwrite each other’s memory | Namespace collision, missing locks | Pattern: **memory-namespace split** in [patterns](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Agents_Orchestration/patterns) |
| Run loops never end | Unbounded cycles, missing guards | [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md) |
| High similarity yet wrong snippet | Metric/store mismatch or fragmentation | [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) |
| Alternating answers across runs | Prompt header reorder, λ flips | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| First live call fails after deploy | Cold boot and ordering issues | [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md) |
| Tool storms and rate limits | Missing backoff and budgets | Ops: **rate-limit backpressure**, **timeouts** in `ops/` |

---

## Minimal agent contract

1. **Separate memory namespaces**  
   One namespace per agent. Writes guarded by `mem_rev` and `mem_hash`.  
2. **Strict tool schemas**  
   Enforce JSON schemas. Reject free-text arguments and responses.  
3. **Path guards**  
   Max steps, variance clamp, and illegal cross-path suppression.  
4. **Traceability first**  
   Cite then explain. Require `{snippet_id, section_id, source_url, offsets, tokens}`.  
5. **Boot ordering**  
   Do not accept traffic until index hash, analyzer, and model versions match.  
6. **Observability**  
   Log ΔS and λ across retrieve → rerank → reason. Alert at ΔS ≥ 0.60.

---

## 60-second triage

1) **Measure ΔS** for question vs retrieved and vs anchor.  
2) **Probe λ** by varying top-k and prompt headers. If λ flips, clamp variance and lock the schema.  
3) **Apply**  
   Retrieval drift → BBMC + Data Contracts  
   Reasoning collapse → BBCR bridge + BBAM  
   Dead ends → BBPF alternate paths  
4) **Verify**  
   Coverage ≥ 0.70 on three paraphrases. λ convergent on two seeds.

---

## FAQ

**Why do agents step on each other’s memory?**  
Shared state without namespaces. Split memory by agent and lock writes.

**Why do I get infinite loops after adding a reviewer agent?**  
No path guards. Add step caps and illegal cross-path suppression.

**Why does tool calling randomly fail JSON?**  
Your tool protocol allows prose. Enforce strict JSON schemas both ways.

**Why is dev stable but prod flips answers?**  
Boot order and analyzer mismatch. Warm the index and verify hashes before traffic.

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

