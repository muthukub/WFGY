# LM Studio: Guardrails and Fix Patterns

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


[LM Studio](https://lmstudio.ai) is a desktop-native app for running LLMs locally. It integrates a polished UI, GGUF/GGML model loading, and provides both chat and API endpoints for developers.
While convenient, LM Studio inherits typical inference-layer bugs: schema drift, memory desync, device initialization errors, and retrieval instability.
This page aligns LM Studio workflows with WFGY guardrails.

---

## Open these first

* Visual map and recovery: [rag-architecture-and-recovery.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
* Retrieval knobs: [retrieval-playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
* Snippet traceability: [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
* Data schema lock: [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)
* Context and entropy issues: [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)
* Boot and deploy ordering: [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

---

## Core acceptance

* ΔS(question, retrieved) ≤ 0.45
* Coverage ≥ 0.70 for the target section
* λ remains convergent across paraphrases and seeds
* API mode enforces JSON schema and idempotency
* Logs include ΔS and λ for reproducibility

---

## Common LM Studio breakpoints

| Symptom                           | Likely Cause                  | Fix                                                                                                                                                                                            |
| --------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| App boots but first query fails   | Device/driver not initialized | [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)                                                                                         |
| Answers alternate across sessions | λ instability                 | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md)                                                                                                   |
| JSON responses malformed          | Schema drift in API mode      | [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md), [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| Citations missing or inconsistent | No snippet schema enforcement | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)                                                                                 |
| Long multi-turn sessions degrade  | Entropy accumulation          | [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)                                                                                             |

---

## Fix in 60 seconds

1. **Warm-up query**: issue a simple echo prompt to stabilize device context.
2. **Enforce schema**: define JSON outputs explicitly in LM Studio API mode.
3. **Measure ΔS**: log ΔS(question, retrieved) per run. If ≥ 0.60, rebuild embeddings.
4. **Clamp λ**: if λ flips across paraphrases, lock headers and shorten memory.
5. **Trace citations**: ensure “cite-then-explain” contract is enforced.

---

## Diagnostic prompt (copy-paste)

```txt
You are running LM Studio as a local inference API.

Given Question: "{user_question}"

Return:
- ΔS(question, retrieved)
- λ state across 3 paraphrases
- JSON compliance (true/false)
- Which WFGY fix page applies if ΔS ≥ 0.60
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

