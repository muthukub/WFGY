# CTransformers: Guardrails and Fix Patterns

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


CTransformers is a lightweight Python/C++ binding for GGML/GGUF models.
It is widely used in minimal local inference setups (often with quantized LLaMA/GPTQ models) but introduces specific risks: unstable JSON tool output, KV cache drift, and library mismatch across versions.
This page defines reproducible guardrails and WFGY-based fixes.

---

## Open these first

* Visual recovery map: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
* Retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
* Embedding alignment: [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)
* Context stability: [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)
* Schema and injection fences: [prompt-injection.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md), [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)
* Deploy fences: [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

---

## Core acceptance

* ΔS(question, retrieved) ≤ 0.45
* Coverage ≥ 0.70
* λ convergent across three paraphrases × two seeds
* JSON tool calls must validate against schema

---

## Common CTransformers breakpoints

| Symptom                                      | Likely Cause                        | Fix                                                                                                                                                                                                |
| -------------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wrong answers despite valid retrieval        | Embedding mis-match with GGUF build | [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)                                                                                       |
| Model runs but crashes on long context (>4k) | KV cache fragmentation              | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)   |
| Invalid JSON from tool calls                 | No enforced schema                  | [prompt-injection.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md), [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md) |
| Version mismatch across wheels               | Pre-deploy collapse                 | [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)                                                                                             |
| First call after import hangs                | Boot order not fenced               | [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)                                                                                             |

---

## Fix in 60 seconds

1. **Pre-flight check**: after import, run `model.generate("hello")` to warm up allocator.
2. **Force contract schema** for all RAG payloads: snippet\_id, section\_id, offsets.
3. **Measure ΔS** on at least 2 seeds × 3 paraphrases. Require ΔS ≤ 0.45.
4. **Rotate cache** every 4–6k tokens.
5. **Validate JSON output** with strict schema and fail fast on injection.

---

## Diagnostic prompt (copy-paste)

```txt
I am running CTransformers with model={gguf/ggml}, quant={mode}, context={n}.
Question: "{user_question}"

Please output:
- ΔS(question, retrieved)
- λ across 3 paraphrases × 2 seeds
- KV cache stability (max tokens)
- JSON schema compliance
- Minimal WFGY fix page if ΔS ≥ 0.60
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

