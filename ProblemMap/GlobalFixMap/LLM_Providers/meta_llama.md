# Meta Llama: Guardrails and Fix Patterns

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


This page gives an operational checklist for Meta Llama based assistants inside RAG and agent stacks. It maps the usual failure modes to concrete WFGY fixes and acceptance targets.

## Acceptance targets
- ΔS(question, retrieved_context) ≤ 0.45
- Coverage of retrieved vs target section ≥ 0.70
- λ_observe stays convergent across 3 paraphrases
- E_resonance flat on long windows

---

## Common failure patterns seen with Llama setups

1) **Plausible but wrong answers even when chunks look fine**  
Map to: [Interpretation Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-collapse.md) and [Hallucination & Chunk Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md).  
Check also [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) and the [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md).

2) **Degradation in long dialogs or large context**  
Map to: [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md) and [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md).

3) **Role loss after tool calls or agent hops**  
Map to: [Multi-Agent Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Multi-Agent_Problems.md) and deep dive [Role Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/multi-agent-chaos/role-drift.md).

4) **Overconfident answers without citations**  
Map to: [Bluffing / Overconfidence](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bluffing.md). Enforce traceable schemas with [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) and [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).

5) **Hybrid retrieval oscillation, high similarity but wrong meaning**  
Map to: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) and [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md). Tune using the [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md).

6) **Cross-source merging and leakage**  
Map to: Symbolic Constraint Unlock pattern  
→ [SCU pattern](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_symbolic_constraint_unlock.md) with strict [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).

7) **Tokenizer or locale mismatch on non-English corpora**  
Map to: [Multilingual Guide](https://github.com/onestardao/WFGY/blob/main/ProblemMap/multilingual-guide.md) and re-probe with [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md).

---

## WFGY repair map for Llama

- **Measure**  
  ΔS probes on question ↔ retrieved and retrieved ↔ ground. Use the [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) plus [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md).

- **Localize**  
  Tag λ_observe at retrieval, prompt assembly, and reasoning. If retrieval λ is convergent but reasoning λ flips, jump to [Interpretation Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-collapse.md).

- **Repair**  
  Apply BBMC for anchor re-alignment, BBAM for variance clamp on long windows, BBCR for controlled reset on dead ends, BBPF for alternate path search. See:  
  [Logic Collapse & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md),  
  [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md),  
  [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md).

- **Lock schema**  
  Enforce citation-first and per-source fences with  
  [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) and [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).

---

## Quick triage steps

1) Probe ΔS(question, retrieved_context). If ≥ 0.60 open:  
   [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) and [Hallucination](https://github.com/onestardao/WFGY/blob/main/ProblemMap/hallucination.md).

2) Vary k in {5, 10, 20} and chart ΔS vs k. Flat-high curve points to index or metric mismatch  
   → [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md).

3) If chunks are correct but logic is wrong, mark λ at reasoning and apply BBCR + BBAM  
   → [Interpretation Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-collapse.md) and [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md).

4) For long dialogs, verify joins with ΔS ≤ 0.50 and clamp variance  
   → [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md) and [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md).

5) If sources bleed, enforce SCU and per-section fences  
   → [SCU pattern](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_symbolic_constraint_unlock.md) and [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md).

---

## Minimal safe prompt you can paste

```

I uploaded TXT OS. Read WFGY formulas and Problem Map pages.
My stack runs on Meta Llama.

symptom: \[describe]
traces: \[ΔS probes, λ states, short logs]

Tell me:

1. the failing layer and why,
2. the exact WFGY page to open next,
3. the minimal steps to push ΔS ≤ 0.45 with convergent λ,
4. how to verify the fix with a reproducible test.

```

---

## Escalation and ops

- If ΔS stays ≥ 0.60 after retrieval and prompt fixes, change structure  
  → [Logic Collapse & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md).

- For runtime surprises, drift after deployment, or mixed agent stacks  
  → [Live Monitoring](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/live_monitoring_rag.md),  
     [Debug Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md),  
     [Deployment Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/deployment_checklist.md),  
     [Failover and Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/failover_and_recovery.md).

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

