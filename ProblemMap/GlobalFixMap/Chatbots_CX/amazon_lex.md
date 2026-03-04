# Amazon Lex: Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Chatbots & CX**.  
  > To reorient, go back here:  
  >
  > - [**Chatbots & CX** — customer dialogue flows and conversational stability](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Use this page when your customer bot is built on **Amazon Lex** and wired to **Lambda**, **Bedrock**, **Kendra/OpenSearch**, or **Amazon Connect**. The checks below localize the failing layer and route you to the exact WFGY fix page.

## Open these first

* Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
* End-to-end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
* Why this snippet (traceability schema): [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
* Ordering control and rerank: [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)
* Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)
* Hallucination and chunk boundaries: [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md)
* Long chains and entropy: [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)
* Symbolic collapse and recovery: [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)
* Prompt injection and tool schema locks: [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)
* Multi-agent and handoff conflicts: [Multi-Agent Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Multi-Agent_Problems.md)
* Boot order and deploy traps: [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [Deployment Deadlock](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md), [Pre-deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)
* Snippet and citation schema: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

## Core acceptance for CX bots

* ΔS(question, retrieved) ≤ 0.45
* Coverage ≥ 0.70 to the target section
* λ remains convergent across 3 paraphrases and 2 seeds
* First reply time stable across retries; no slot backtracks

---

## 60-second fix checklist

1. **Measure ΔS**
   Compute ΔS(question, retrieved) and ΔS(retrieved, expected anchor).
   Stable < 0.40, transitional 0.40–0.60, risk ≥ 0.60.

2. **Probe λ\_observe**
   Change k to 5, 10, 20. If ΔS stays high and flat, suspect metric or index mismatch.
   Reorder prompt headers. If λ flips, lock schema with Data Contracts.

3. **Apply the module**

   * Retrieval drift → **BBMC** + [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) + [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
   * Reasoning collapse → **BBCR** bridge + **BBAM** variance clamp, then verify with [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)
   * Dead ends in long flows → **BBPF** alternate paths and shorten plan windows

4. **Verify**
   Re-run three paraphrases. Require ΔS ≤ 0.45 and convergent λ on two seeds.

---

## Typical Lex breakpoints → exact fix

* **Slot filling freezes or backtracks**
  Schema too loose or reprompts mutate meaning.
  → [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md), [Prompt Injection](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)

* **Lambda tool JSON mismatch**
  Nested tool calls or optional fields become free text.
  → Lock arguments with contracts, echo schema each turn.
  See [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

* **High similarity hits, wrong answer**
  Metric or analyzer mismatch, fragmented store.
  → [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md), [Vectorstore Fragmentation](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_vectorstore_fragmentation.md)

* **Kendra vs OpenSearch reruns change order**
  Two-stage query split, reranker blind spots.
  → [Query Parsing Split](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md), [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)

* **Connect handoff loops or stuck queue**
  Version skew or memory writes collide across paths.
  → [Deployment Deadlock](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md), [Pre-deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

* **Session attributes drift between turns**
  Hidden state mutates across retries.
  → [Multi-Agent Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Multi-Agent_Problems.md)

* **Safety refusal hides the cited snippet**
  Use citation-first prompting and SCU unlock.
  → [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [Pattern: SCU](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_symbolic_constraint_unlock.md)

* **Jailbreak or confident bluffing**
  Add fences and require cite-then-explain.
  → [Bluffing Controls](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bluffing.md)

---

## Copy-paste Lambda prompt for the LLM step

```txt
You have TXTOS and the WFGY Problem Map loaded.

My Amazon Lex context:
- user_utterance: "{utterance}"
- retrieved: {snippet_id, section_id, source_url, offsets, tokens}
- session: {attributes...}

Do:
1) Enforce cite-then-explain. If citations are missing or cross-section, fail fast and return the minimal fix.
2) Compute ΔS(question, retrieved). If ΔS ≥ 0.60, propose the smallest structural repair
   referencing: retrieval-playbook, retrieval-traceability, data-contracts, rerankers.
3) Return JSON:
{ "answer": "...", "citations": [...], "λ_state": "→|←|<>|×", "ΔS": 0.xx, "next_fix": "..." }
Keep it auditable and short.
```

---

## Observability hooks

* Log per turn: `ΔS(question,retrieved)`, `ΔS(retrieved,anchor)`, `λ_state`, `index_hash`, `dedupe_key`.
* Alert if ΔS ≥ 0.60 or λ flips on harmless paraphrase.
* For live ops and rollback tips see [Live Monitoring for RAG](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/live_monitoring_rag.md) and [Debug Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md).

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

