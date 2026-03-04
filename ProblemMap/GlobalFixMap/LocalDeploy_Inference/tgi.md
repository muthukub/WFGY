# Hugging Face TGI: Guardrails and Fix Patterns

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


Stabilization guide for **Text Generation Inference (TGI)**, the Hugging Face high-throughput serving stack.
Use these checks when local inference works in notebooks but collapses when deployed via TGI servers.

---

## Open these first

* Visual recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
* Retrieval tuning knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
* Snippet traceability: [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)
* Ordering & race fixes: [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [deployment-deadlock.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md), [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)
* Embedding issues: [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

---

## Core acceptance

* ΔS(question, retrieved) ≤ 0.45
* Coverage ≥ 0.70 for target section
* λ remains convergent across 3 paraphrases and 2 seeds
* Responses remain stable across concurrent clients (no flip-flops)

---

## Typical TGI breakpoints and fix

| Symptom                                           | Likely cause                            | Fix                                                                                                                                                                                                            |
| ------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Logs show healthy, outputs differ across replicas | Worker desync / weight loading skew     | [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md) |
| Citations disappear under concurrent load         | Async merge loses trace offsets         | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| ΔS rises >0.60 when concurrency >10               | Context fragmentation across shards     | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)               |
| Errors vanish in dry run, appear in production    | Race condition in warm-up path          | [deployment-deadlock.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md)                                                                                                       |
| JSON outputs invalid at scale                     | Schema loosening during parallel decode | [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md), [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)                 |

---

## Fix in 60 seconds

1. **Batch probe**: Run same query at concurrency=1 and concurrency=16.
   If ΔS only rises at higher concurrency, lock async merging.
2. **λ probe**: Test 3 paraphrases, 2 seeds. If λ flips, apply BBAM variance clamp.
3. **Contracts**: Require `snippet_id`, `offsets`, `tokens` in every response.
4. **Warm-up fencing**: Run dummy batch before live serve to sync workers.
5. **Verify**: Replay test dataset at concurrency=32. Expect stable ΔS ≤ 0.45.

---

## Copy-paste test prompt

```txt
I am running Hugging Face TGI for local inference.  
Concurrent clients sometimes cause unstable answers.  
Question: "{user_question}"  

Please return:
1. ΔS at concurrency=1 vs concurrency=16  
2. λ across paraphrases  
3. Whether citations are preserved  
4. Minimal fix module if ΔS ≥ 0.60  
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

