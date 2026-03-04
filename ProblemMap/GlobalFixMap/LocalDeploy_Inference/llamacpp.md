# Llama.cpp: Guardrails and Fix Patterns

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


[Llama.cpp](https://github.com/ggerganov/llama.cpp) is the most widely used local inference runtime for GGML/GGUF models.
It enables CPU/GPU inference across diverse hardware but often introduces fragile states: mismatched quantization, KV-cache drift, and long-context instability.
This page defines reproducible WFGY-based guardrails and direct fixes.

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
* KV cache stability for context >8k tokens
* JSON schema compliance enforced when using tools

---

## Common Llama.cpp breakpoints

| Symptom                                     | Likely Cause                                      | Fix                                                                                                                                                                                                |
| ------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wrong answers despite high similarity       | Embedding metric mismatch with GGUF/quant variant | [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)                                                                                       |
| Model slows or collapses after 8–16k tokens | KV cache drift                                    | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)   |
| Output alternates between runs              | Prompt header drift                               | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)                                                                                     |
| Invalid JSON or schema drift                | Missing tool schema lock                          | [prompt-injection.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md), [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md) |
| Crash at first inference call               | Boot order not fenced                             | [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)                                                                                             |
| Segfault when mixing quantized weights      | Pre-deploy mismatch                               | [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)                                                                                             |

---

## Fix in 60 seconds

1. **Pre-flight warmup**: run a dummy prompt (e.g., `"hello"`) to allocate memory.
2. **Schema lock** all JSON tool outputs; reject free text where structured arguments expected.
3. **Measure ΔS** across 3 paraphrases, require ≤0.45.
4. **Rotate cache** or reset every 8–16k tokens.
5. **Ensure quantization match** between build and model weights (GGUF flags).

---

## Diagnostic prompt (copy-paste)

```txt
I am running Llama.cpp with model={gguf/quant}, context={n}.
Question: "{user_question}"

Return:
- ΔS(question, retrieved)
- λ states across 3 paraphrases × 2 seeds
- KV cache drift beyond 8k tokens
- JSON schema compliance
- Minimal WFGY page to open if ΔS ≥ 0.60
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

