# Context Drift in RAG — Guardrails and Fix Pattern

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **RAG**.  
  > To reorient, go back here:  
  >
  > - [**RAG** — retrieval-augmented generation and knowledge grounding](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


When answers alternate or degrade as dialogs get longer, even though the retriever continues to surface the right snippets.  
This page stabilizes λ (semantic convergence) and prevents entropy creep in retrieval-augmented pipelines.

---

## Open these first
- Visual map: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Drift diagnostics: [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)  
- Stability checks: [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)  
- Retrieval schema: [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Payload contract: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Long context limits: [Memory Long Context](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/README.md)  

---

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45 across full chain  
- λ stays convergent across 3 paraphrases and 2 seeds  
- Coverage ≥ 0.70 for target section, even after N steps  
- E_resonance stable on long dialog windows  

---

## Typical symptoms → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| Same question asked twice, different answers | λ drift with long chain | [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md), [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md) |
| Correct snippets retrieved, answer drops citation | payload contract erosion | [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md), [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| Paraphrase of query yields different grounding | unstable λ_observe | [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) |
| Long dialog overwrites memory | buffer collapse | [Memory Long Context](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/README.md) |

---

## Fix in 60 seconds

1. **Three-paraphrase probe**  
   - Ask the same question three ways.  
   - If λ flips between paraphrases, lock snippet schema and apply BBAM variance clamp.

2. **ΔS check over chain**  
   - Log ΔS(question,retrieved) across 5–10 dialog turns.  
   - If ΔS rises over time, re-segment and enforce citation-first prompting.

3. **Apply module**  
   - Drift → BBMC + [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
   - Collapse mid-chain → BBCR bridge + [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)  
   - Unstable variance → BBAM clamp + [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)  

---

## Copy-paste probe prompt

```txt
I uploaded TXT OS and the WFGY Problem Map.

My issue:
- same query gives different answers in long dialog
- traces: ΔS(question,retrieved)=..., λ states across 3 paraphrases

Tell me:
1) where context drift occurs,
2) the exact WFGY page to open,
3) the minimal fix to enforce convergence,
4) a reproducible test over 5 turns.
````

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool                       | Link                                                                                                                                       | 3-Step Setup                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **WFGY 1.0 PDF**           | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + <your question>”    |
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

