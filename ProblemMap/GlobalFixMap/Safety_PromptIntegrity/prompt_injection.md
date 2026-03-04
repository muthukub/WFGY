# Prompt Injection — Guardrails and Fix Patterns

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


A focused guide to handle **prompt injection attacks** in RAG, agents, and orchestration.  
Use this page when injected text hijacks your instructions, bypasses schema, or makes the model ignore contracts.

---

## When to open this page
- Responses contain **leaked system prompt** or hidden instructions.  
- Model obeys malicious user text like *“ignore above and do X”*.  
- Citations vanish after injection payload.  
- JSON / tool schema is broken by arbitrary free text.  
- Memory or context keys rewritten by injected content.  

---

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)  
- Retrieval traceability: [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- Data schema contract: [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  
- Role boundary checks: [role_confusion.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/role_confusion.md)  
- Memory fences: [memory_fences_and_state_keys.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/memory_fences_and_state_keys.md)  

---

## Core acceptance
- ΔS(question, retrieved) ≤ 0.45 even with injection attempts.  
- λ remains convergent across 3 paraphrases, does not flip under “ignore above” payloads.  
- Schema lock: JSON/tool calls validate against fixed schema.  
- Coverage ≥ 0.70 of target section even under noisy injection.  

---

## Fix in 60 seconds
1. **Detect abnormal ΔS drift**  
   - Compute ΔS(question, retrieved). If injected phrase raises ΔS ≥ 0.60, isolate payload.  

2. **Enforce contracts**  
   - Wrap retriever and reasoner outputs in [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).  
   - Reject free text outside schema.  

3. **Apply fences**  
   - Lock system vs user roles ([role_confusion.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/role_confusion.md)).  
   - Use memory hash keys ([memory_fences_and_state_keys.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/memory_fences_and_state_keys.md)).  

4. **Verify stability**  
   - Re-run with paraphrase probes. Injection should not flip λ or erase citations.  

---

## Typical injection payloads → exact fix

| Payload type | Symptom | Fix |
|--------------|---------|-----|
| **Ignore-all override** | Model discards earlier rules | [role_confusion.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/role_confusion.md) + schema locks |
| **Citation erasure** | No references, only free text answer | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| **Tool hijack** | JSON field replaced with instruction text | [json_mode_and_tool_calls.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/json_mode_and_tool_calls.md) |
| **Role swap** | User prompt injected as “system” | [role_confusion.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/role_confusion.md) |
| **Memory overwrite** | Past state or keys corrupted | [memory_fences_and_state_keys.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Safety_PromptIntegrity/memory_fences_and_state_keys.md) |

---

## Copy-paste probe prompt

```txt
System: WFGY firewall active.
User input: {question}

Check:
1. Did retrieved snippet keep citations?
2. Did ΔS(question,retrieved) ≤ 0.45?
3. Did λ stay convergent under paraphrase?
4. Did JSON/tool call respect schema?

If any fail, return the failing layer + fix page.
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

