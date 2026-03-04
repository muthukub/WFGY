# Context Drift — Long Reasoning Chain Instability

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **MemoryLongContext**.  
  > To reorient, go back here:  
  >
  > - [**MemoryLongContext** — extended context windows and memory retention](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


When reasoning spans 20–40 hops or more, attention shifts accumulate and context drifts.  
This page explains how to diagnose λ divergence, stabilize reasoning chains, and repair collapsed context.

---

## When to use this page
- Long reasoning plans (~20+ steps) start with logic but later flip or contradict.  
- Multi-agent workflows repeat or miss earlier facts.  
- Citations remain valid, but final answers drift from original question.  
- λ flips divergent after harmless paraphrases.  
- Answers alternate between runs with identical inputs.

---

## Core acceptance targets
- ΔS(question, retrieved) ≤ 0.45  
- Retrieval coverage ≥ 0.70 for target section  
- λ remains convergent across three paraphrases  
- Chain length stable up to 40 hops without collapse  
- Entropy variance remains bounded in mid-to-late steps  

---

## Structural fixes

- **Three-paraphrase probe**  
  Re-ask the same question three ways. Log ΔS and λ at each hop.  
  If λ flips, schema is unstable.

- **Clamp with BBAM**  
  Apply variance clamp when λ flips across harmless paraphrases.

- **Bridge with BBCR**  
  Insert bridge nodes when long chains stall. Anchor back to earlier stable nodes.

- **Enforce snippet fences**  
  Require each reasoning step cite snippet_id. Forbid cross-section reuse.

- **Re-anchor with anchors**  
  Compare ΔS(question, anchor) vs ΔS(question, decoy).  
  If ΔS is close, re-chunk corpus.

---

## Fix in 60 seconds
1. **Log ΔS and λ** across 3 paraphrases.  
2. **Clamp** with BBAM if λ flips.  
3. **Bridge** with BBCR if reasoning halts.  
4. **Re-anchor** using anchor triangulation.  
5. **Verify** coverage ≥ 0.70 and ΔS ≤ 0.45.  

---

## Copy-paste prompt

```

You have TXT OS and the WFGY Problem Map.

Goal: Detect and repair context drift in long reasoning chains.

Protocol:

1. Ask the same question three ways.
2. Log ΔS(question, retrieved) for each.
3. Log λ states across all hops.
4. If λ flips:

   * Apply BBAM clamp.
   * If reasoning stalls, apply BBCR and anchor bridge.
5. Require snippet\_id at each step.
6. Report:

   * ΔS(question, retrieved)
   * λ states across paraphrases
   * bridge nodes inserted
   * final answer with citations

```

---

## Common failure patterns
- **Chain stall**: reasoning halts after ~25–30 hops.  
- **Paraphrase drift**: harmless rewordings flip λ.  
- **Repeating answers**: earlier snippets loop back with filler.  
- **Contradictions**: late chain contradicts early reasoning.  

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

