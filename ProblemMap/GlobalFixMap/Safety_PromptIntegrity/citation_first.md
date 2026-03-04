# Citation-First Prompting — Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Safety_PromptIntegrity**.  
  > To reorient, go back here:  
  >
  > - [**Safety_PromptIntegrity** — prompt injection defense and integrity checks](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Citation drift is one of the most common ways LLMs lose trust.  
Without **cite-then-explain discipline**, answers may sound fluent but detach from sources.  
This page locks the workflow: every reasoning step begins from **citations**, not narrative.

---

## When to open this page
- Model produces fluent paragraphs with zero citations.  
- Citations appear, but after-the-fact and unverifiable.  
- References change between runs, even with same inputs.  
- ΔS(question, retrieved) ≤ 0.45 but λ diverges when narrative precedes citation.  
- Users complain: "Where did this answer come from?"  

---

## Open these first
- Retrieval schema contract: [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Trace alignment: [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Context collapse: [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)  
- Memory boundaries: [memory_fences_and_state_keys.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/memory_fences_and_state_keys.md)  
- Injection guard: [prompt_injection.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/prompt_injection.md)  

---

## Core acceptance
- Every answer starts with citations (no narrative before refs).  
- Coverage ≥ 0.70 of the target section.  
- ΔS(question, cited snippet) ≤ 0.45.  
- λ convergent across 3 paraphrases.  
- No hallucinated citations (must resolve to a retriever record).  

---

## Fix in 60 seconds
1. **Citation-first discipline**  
   - Always start with `snippet_id`, `section_id`, `source_url`.  

2. **Enforce schema**  
   - Required fields:  
     ```json
     { "snippet_id": "...", "section_id": "...", "source_url": "...", "offsets": [..], "tokens": N }
     ```  

3. **Reason only after citation**  
   - Explain or analyze *after* citation block.  

4. **Reject broken runs**  
   - If citation missing → abort answer, return error tip.  

5. **Stability probe**  
   - Run 3 paraphrases. If λ diverges, lock citation schema, rerun.  

---

## Typical failure vectors → fix

| Vector | Symptom | Fix |
|--------|---------|-----|
| **Narrative-first** | Text precedes refs, unstable λ | Force cite-then-explain ordering |
| **Fake refs** | Hallucinated URLs | Schema lock + [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| **Drifting refs** | Different citations each run | Clamp λ with BBAM, validate ΔS ≤ 0.45 |
| **Silent fallback** | Model drops refs under safety refusal | Apply SCU (symbolic constraint unlock) |

---

## Probe prompt

```txt
You must output citations before narrative.
Schema: {snippet_id, section_id, source_url, offsets, tokens}

Rules:
1. Cite first. Explain only after citations are shown.
2. No answer if citations missing.
3. Log ΔS(question, cited snippet). Reject if ≥ 0.60.
4. λ must stay convergent across 3 paraphrases.
````

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

