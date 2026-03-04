# ExLlamaV2: Guardrails and Fix Patterns

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


ExLlamaV2 is a specialized inference backend for LLaMA-family models with optimized 4-bit quantization.  
It provides faster throughput and lower VRAM usage compared to generic backends, but introduces new risks in accuracy, schema drift, and numerical stability.  
This page maps those issues to WFGY structural fixes with measurable acceptance targets.

---

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- End-to-end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)  
- Embedding vs meaning: [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  
- Chunk schema: [Chunking Checklist](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  
- Collapse and entropy: [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md), [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)  
- Ordering and boot issues: [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [Pre-deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)  

---

## Core acceptance
- ΔS drift vs FP16 baseline ≤ 0.10  
- Coverage ≥ 0.70 for target section  
- λ convergent across 3 paraphrases and 2 seeds  
- Latency improvement ≥ 25% with accuracy loss ≤ 5%  

---

## Typical ExLlamaV2 breakpoints → exact fix

| Symptom | Likely cause | Open this |
|---|---|---|
| Text fluency high, citations missing | Schema loosened in quantized path | [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md), [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| Wrong snippet despite high similarity | Index mismatch after quantization | [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md), [Vectorstore Fragmentation](https://github.com/onestardao/WFGY/blob/main/ProblemMap/vectorstore-fragmentation.md) |
| JSON breaks frequently | Quantization noise amplifies schema drift | [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md), [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| Long chain divergence after 20–40 steps | Numerical error accumulation | [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md), [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md) |
| Deployment mismatch | Torch vs ExLlama kernels version skew | [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [Pre-deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md) |

---

## Fix in 60 seconds

1) **Measure ΔS**  
   Run 20 QA pairs on FP16 baseline vs ExLlamaV2.  
   Acceptable drift ≤ 0.10.  

2) **Probe λ_observe**  
   Increase retrieval k. If λ flips divergent, apply BBAM schema lock.  

3) **Apply the module**  
   - Retrieval drift → BBMC + Retrieval Traceability  
   - Reasoning collapse → BBCR + BBAM clamp  
   - Long-chain instability → BBPF alternate paths  

4) **Verify**  
   Coverage ≥ 0.70, λ convergent, ΔS ≤ 0.10.  

---

## Minimal setup

```python
from transformers import AutoTokenizer
from exllamav2 import ExLlamaV2, ExLlamaV2Cache, ExLlamaV2Tokenizer

model_path = "your-llama-model"

tokenizer = AutoTokenizer.from_pretrained(model_path)

# Initialize ExLlamaV2
model = ExLlamaV2(model_path, quant="4bit", gpu_split="auto")
cache = ExLlamaV2Cache(model)

prompt = "Hello, world!"
tokens = tokenizer.encode(prompt, return_tensors="pt").cuda()

output = model.generate(tokens, max_new_tokens=128, cache=cache)
print(tokenizer.decode(output[0]))
````

---

## Ops checklist

* Always compare ΔS/λ vs FP16 baseline before shipping
* Pin ExLlama kernels to version matching torch/cuBLAS build
* Log coverage and citation schema at runtime
* Guard JSON outputs with schema validators

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

