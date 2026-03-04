# Multi-Seed Consistency — Multimodal Long Context

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


When the same multimodal query produces divergent outputs across seeds, context length, or session restarts, reasoning collapses and trust degrades.  
This page defines probes and guardrails to enforce consistency across seeds.

---

## What this page is
- Checklist for measuring stability across random seeds in multimodal runs.  
- Guardrails to prevent phantom variation across seeds.  
- Minimal reproducible probes you can drop into any LLM + RAG + multimodal stack.

---

## When to use
- Same video → text question gives different answers each run.  
- OCR transcript changes casing or spacing across seeds.  
- Frame annotations shift order or vanish between runs.  
- Retrieval top-k stable, but answers drift each time.  
- Support threads show inconsistent captions or timecode mismatches.

---

## Open these first
- [Cross-Modal Trace](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/cross-modal-trace.md)  
- [Alignment Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/alignment-drift.md)  
- [Phantom Visuals](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Multimodal_LongContext/phantom-visuals.md)  
- [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
- [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)  

---

## Common failure patterns
- **Seed drift**: ΔS fluctuates widely across seeds even with same input.  
- **Phantom anchor**: one seed introduces unseen frames or captions.  
- **λ flip**: λ_observe changes convergence state across paraphrases.  
- **Context order variance**: anchors appear in inconsistent order per seed.  
- **Audit mismatch**: trace tables differ across 3+ seeds.

---

## Fix in 60 seconds
1. **Seed audit**  
   - Run the same input across 3–5 seeds.  
   - Record ΔS, λ, and anchor references.

2. **Clamp variance**  
   - Apply BBAM to lock attention spread.  
   - Apply BBCR if trace tables diverge.

3. **Schema enforcement**  
   - Require deterministic `{frame_id, timestamp, region_id}`.  
   - Forbid free text anchors.

4. **Majority vs outlier filter**  
   - Accept only anchors seen in ≥ 70% of seeds.  
   - Flag outliers as phantom.

5. **Report reproducibility**  
   - Require ΔS ≤ 0.45 across seeds.  
   - Require λ convergent across at least 3 paraphrases.

---

## Copy-paste prompt

```txt
You have TXT OS and the WFGY Problem Map.

Task: Probe multi-seed consistency.

Protocol:
1. Run input across 3–5 seeds. Collect {ΔS, λ, anchors}.
2. Compare trace tables. If anchors diverge, apply BBCR bridge.
3. Clamp with BBAM if ΔS variance > 0.15 across seeds.
4. Report:
   - Seed-to-seed ΔS log
   - λ states
   - Majority anchor set
   - Flagged phantom anchors
````

---

## Acceptance targets

* ΔS(question, retrieved) ≤ 0.45 across all seeds.
* Variance ≤ 0.15 between seeds.
* λ remains convergent across 3 paraphrases.
* No phantom anchors.
* Trace Table reproducible across 3–5 seeds.

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

