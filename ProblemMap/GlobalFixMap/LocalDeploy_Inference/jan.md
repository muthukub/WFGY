# Jan: Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **LocalDeploy_Inference**.  
  > To reorient, go back here:  
  >
  > - [**LocalDeploy_Inference** — on-prem deployment and model inference](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


[Jan](https://jan.ai) is a desktop-native inference environment that allows you to run local LLMs with a polished UI, cross-platform support, and tight integration with quantized model formats.
While easier to use than CLI runtimes, Jan inherits common problems: unstable context handling, schema drift, citation loss, and device-specific crashes.
This page gives WFGY-based fixes to stabilize Jan deployments.

---

## Open these first

* Architecture recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
* Retrieval knobs: [retrieval-playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
* Embedding sanity: [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)
* Context stability: [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)
* Safety and schema: [prompt-injection.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md), [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)
* Boot/deploy: [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

---

## Core acceptance

* ΔS(question, retrieved) ≤ 0.45
* Coverage ≥ 0.70 for the target section
* λ convergent across 3 paraphrases × 2 seeds
* JSON schema locked for tool calls
* Observability of ΔS and λ logged per run

---

## Common Jan breakpoints

| Symptom                               | Likely Cause                            | Fix                                                                                                                                                                                                            |
| ------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First run fails on GPU device         | CUDA/Metal init order                   | [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)                                                                                                         |
| Correct snippets but drifting answers | Schema mismatch in local context buffer | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| Answers alternate between runs        | λ flip, unstable headers                | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md)                                                                                                                   |
| JSON parse breaks                     | Inconsistent serialization in UI layer  | [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)                                                                                                                 |
| Safety refusal hides citations        | Missing citation-first prompting        | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)                                                                                                 |

---

## Fix in 60 seconds

1. **Run warm-up**: issue a small dummy query to stabilize device kernels.
2. **Schema enforce**: lock JSON outputs for tools and citations.
3. **Trace citations**: enforce cite-then-explain.
4. **Measure ΔS and λ**: if ΔS ≥ 0.60, rebuild index with proper embedding metric.
5. **Watch entropy**: reset conversation memory after 4k–8k tokens or entropy rise.

---

## Diagnostic prompt (copy-paste)

```txt
I am using Jan to run a local GGUF/GGML model.
Question: "{user_question}"

Return:
- ΔS(question, retrieved)
- λ across paraphrases and seeds
- JSON schema compliance
- Which WFGY fix page to open if ΔS ≥ 0.60
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

