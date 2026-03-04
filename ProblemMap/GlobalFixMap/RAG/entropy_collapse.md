# Entropy Collapse in RAG — Guardrails and Fix Pattern

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


When long reasoning chains become noisy, unstable, or incoherent despite correct retrievals.  
Entropy collapse usually shows as answers that diverge, repeat filler, or contradict themselves as the sequence grows.

---

## Open these first
- Visual map: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Drift diagnostics: [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/RAG/context_drift.md)  
- Structural fixes: [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)  
- Payload schema: [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Variance clamp: [BBAM Module](https://github.com/onestardao/WFGY/blob/main/SemanticBlueprint/bbam.md)  
- Long context limits: [Memory Long Context](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/README.md)  

---

## Core acceptance
- λ must remain convergent across three paraphrases and two seeds  
- ΔS(question, retrieved) ≤ 0.45 at all chain depths  
- No filler drift after 25–40 reasoning steps  
- E_resonance flat across long dialog windows  

---

## Typical symptoms → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| Chain starts coherent, ends with filler or contradictions | entropy build-up | [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md), [BBAM](https://github.com/onestardao/WFGY/blob/main/SemanticBlueprint/bbam.md) |
| Same snippet cited but conclusion flips | λ unstable mid-chain | [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/RAG/context_drift.md), [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| Long answers regress to vague filler | uncontrolled entropy growth | [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md), [Memory Long Context](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/README.md) |
| Evaluations not reproducible | variance unbounded | [Eval Precision/Recall](https://github.com/onestardao/WFGY/blob/main/ProblemMap/eval/eval_rag_precision_recall.md), [BBAM](https://github.com/onestardao/WFGY/blob/main/SemanticBlueprint/bbam.md) |

---

## Fix in 60 seconds

1. **Log λ and ΔS per step**  
   - Record values across 10–20 turns.  
   - If ΔS ≥ 0.60 or λ diverges, entropy collapse is confirmed.

2. **Apply variance clamp**  
   - Use BBAM to bound variance.  
   - Force cite-then-explain and forbid cross-section reuse.

3. **Chain splitting**  
   - Break chains into 10–15 step segments.  
   - Join segments with BBCR bridge to maintain coherence.

4. **Stability probes**  
   - Re-run with two seeds. If λ flips, lock schema and rerank.  

---

## Copy-paste probe prompt

```txt
I uploaded TXT OS and the WFGY Problem Map.

My issue:
- long reasoning chain collapses into filler
- ΔS rises after N steps, λ unstable across seeds

Tell me:
1) is this entropy collapse or logic collapse,
2) which WFGY page to open,
3) the minimal structural fix,
4) a reproducible test across 10–20 steps.
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

