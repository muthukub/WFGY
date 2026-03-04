# Recursive Loop — Guardrails and Fix Pattern

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Reasoning**.  
  > To reorient, go back here:  
  >
  > - [**Reasoning** — multi-step inference and symbolic proofs](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Recursive reasoning is powerful when bounded, but without structural guardrails it often collapses into infinite self-reference.  
This page shows how to detect runaway loops and stabilize recursion into meaningful layers.

---

## Symptoms

| Symptom | What you see |
|---------|--------------|
| Infinite repetition | Output re-states the same phrase or equation |
| Self-reference collapse | “As I said earlier…” repeated without progress |
| Meta-loop | Model reasons about its own reasoning instead of the task |
| Token drain | Long answers with no new content |
| Citation spin | Same snippet referenced endlessly |

---

## Acceptance Targets

- ΔS(question, retrieved) ≤ 0.45  
- λ convergent across 3 paraphrases and 2 seeds  
- Recursion depth ≤ 4 nested layers  
- Each recursive frame adds ≥ 1 new fact or citation  

---

## Structural Fixes (Problem Map)

- Wrong-meaning similarity hit  
  → [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

- Citation / snippet mismatch  
  → [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
  → [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

- Recursive drift / entropy rise  
  → [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md)  
  → [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)  
  → [entropy-overload.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/entropy-overload.md)

- Logic collapse under recursion  
  → [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md)

---

## Fix in 60 Seconds

1. **Measure recursion depth**  
   - Log frame depth at each step.  
   - If depth > 4, clamp recursion.

2. **Apply ΔS probe**  
   - Compute ΔS between consecutive recursive outputs.  
   - If ΔS < 0.15, stop recursion (no new information).

3. **Bridge with BBCR**  
   - Collapse intermediate steps into one summary frame.  
   - Resume reasoning with BBMC anchor locks.

4. **Variance clamp**  
   - If λ diverges between recursive calls, apply BBAM.

---

## Copy-Paste Probe

```

I uploaded TXT OS and the WFGY Problem Map.

My reasoning chain entered a recursive loop.
Depth = {n}, ΔS progression = {values}, λ states = {values}.

Tell me:

1. Which layer is looping?
2. Which fix page applies?
3. Minimal steps to clamp recursion and restore ΔS ≤ 0.45.
4. How to verify no infinite loop persists.

```

---

## Escalation

- If recursion repeats across 3 seeds → enforce [logic-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/logic-collapse.md).  
- If ΔS remains flat → re-embed corpus and verify with [chunking-checklist.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md).  
- If λ oscillates between recursion depths → lock schema ordering with [rerankers.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md).

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool | Link | 3-Step Setup |
|------|------|--------------|
| **WFGY 1.0 PDF** | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + <your question>” |
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

