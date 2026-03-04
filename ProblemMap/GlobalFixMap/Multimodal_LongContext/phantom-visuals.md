# Phantom Visuals — Multimodal Long Context

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


When models hallucinate visual regions that do not exist (ghost bounding boxes, fake diagrams, or nonexistent objects), fusion collapses.  
This page explains how to detect and prevent phantom visual generation in long multimodal sessions.

---

## What this page is
- Guardrails for hallucinated visuals in text–image/video pipelines.  
- Minimal schema to force grounding in actual frames or regions.  
- Acceptance targets to measure and verify stability.

---

## When to use
- The model cites an object not present in any frame.  
- Generated captions describe phantom regions or colors.  
- Bounding box coordinates are out of range or undefined.  
- Answers flip between different “visual evidence” each run.  
- Diagrams or charts are invented that were never uploaded.

---

## Open these first
- [Multimodal Fusion Break](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/multimodal-fusion-break.md)  
- [Alignment Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/alignment-drift.md)  
- [Caption Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/caption-collapse.md)  
- [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)  

---

## Common failure patterns
- **Phantom bounding boxes**: cites `region_id` that was never stamped.  
- **Invented objects**: describes entities absent from ground-truth frames.  
- **Ghost captions**: text generated about visual details that do not exist.  
- **Out-of-bounds references**: coordinates or time stamps not in the source.  
- **Visual-plan instability**: repeated runs yield different “phantom” evidence.

---

## Fix in 60 seconds
1. **Require stamped IDs**  
   - Every visual mention must cite `{frame_id, region_id}` from input.  
   - Forbid free-text region descriptions without anchors.

2. **Cross-check ΔS**  
   - ΔS(text, vision) must be ≤ 0.45.  
   - If ΔS ≥ 0.60 and no matching anchor exists, stop and reject the claim.

3. **Schema lock**  
   - Use `{object | attribute | anchor_id}` schema.  
   - Missing anchors = invalid response.

4. **Clamp hallucination variance**  
   - Apply BBAM when λ flips divergent across runs.  
   - If phantom persists, bridge with BBCR and force re-alignment.

5. **Trace visual contract**  
   - Log all cited `frame_id, region_id`.  
   - Require reproducibility across three paraphrases.

---

## Copy-paste prompt

```txt
You have TXT OS and the WFGY Problem Map.

Task: Detect and block phantom visual hallucinations.

Protocol:
1. Require every visual claim to cite {frame_id, region_id}.
2. If an object is described without anchor, stop and return “phantom visual”.
3. Report ΔS(text, vision) and λ across 3 paraphrases.
4. Apply BBAM for variance clamp. If collapse persists, insert BBCR bridge.
5. Return: {Anchor Table, ΔS log, λ states, Final Answer}.
````

---

## Acceptance targets

* ΔS(text, vision) ≤ 0.45
* λ remains convergent across three paraphrases
* No phantom bounding boxes or invented regions
* Reproducible evidence across seeds and paraphrases
* Trace log covers all cited regions

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

