# Echo Loop — Guardrails and Fix Pattern

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Multimodal_LongContext**.  
  > To reorient, go back here:  
  >
  > - [**Multimodal_LongContext** — long-context reasoning across text, vision, and audio](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


When multimodal systems run across long contexts, sometimes **the same visual, caption, or audio snippet gets echoed back repeatedly** instead of advancing reasoning.  
This creates “semantic stutter” where the model hallucinates progress but actually cycles on stale content.

---

## Symptoms of Echo Loop
- Captions or transcripts repeated across multiple turns without update.  
- Visual or audio reference echoed verbatim despite new input.  
- Model appears to “stall” on the same anchor, ignoring user’s next steps.  
- ΔS values stay flat across paraphrases, indicating semantic freeze.  
- Users perceive output as verbose filler with no new reasoning.

---

## Open these first
- Attention variance clamp: [Entropy Collapse](../MemoryLongContext/entropy-collapse.md)  
- Context drift and chain failure: [Context Drift](../MemoryLongContext/context-drift.md)  
- Cross-modal sync hazards: [Sync Loop](./sync-loop.md)  
- Traceability schema: [Cross-Modal Trace](./cross-modal-trace.md)  
- Session fences: [Memory Coherence](../MemoryLongContext/memory-coherence.md)  

---

## Fix in 60 seconds
1. **Detect stutter**  
   - If identical snippet ID repeats >2 times without anchor update, flag echo-loop.  
   - Log ΔS and λ across three turns; flat line = freeze.

2. **Force anchor refresh**  
   - Require `anchor_rev++` with each new modality.  
   - If missing, insert continuity token `mod_refresh`.

3. **Break the loop**  
   - Clamp with BBAM to suppress repeated variance.  
   - Insert BBCR bridge node to force new semantic branch.  

4. **Audit citations**  
   - Require unique snippet IDs in each new step.  
   - If repeated without anchor shift, reject and re-request content.  

---

## Acceptance Targets
- ΔS(question, retrieved) ≤ 0.45, with downward slope across steps.  
- No modality snippet echoed more than twice consecutively.  
- λ_observe convergent across three paraphrases.  
- Anchor IDs strictly monotonic (`anchor_rev` increments).  

---

## Copy-paste prompt

```txt
You are running TXTOS + WFGY Problem Map.

Symptom: repeated captions or snippets, model is “stuck in loop.”

Protocol:
1. Detect repeats >2 turns → flag echo-loop.
2. Require anchor_rev increment per modality.
3. Insert mod_refresh token if anchor missing.
4. Apply BBAM clamp and BBCR bridge to break loop.
5. Verify ΔS downward trend across turns.
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

