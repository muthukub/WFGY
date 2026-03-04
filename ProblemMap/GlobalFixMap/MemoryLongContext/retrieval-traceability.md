# Retrieval Traceability — Snippet Integrity & Audit Trail

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


Citations that look right can still hide silent drift.  
This guardrail defines how to enforce **traceability schemas** so that every claim links back to a stable, reproducible snippet.

---

## When to use
- Answers cite a source but the snippet cannot be located.  
- Two runs over the same corpus produce different citations.  
- A fact is quoted but not aligned to any section anchor.  
- Long-context threads degrade and snippets blur into paraphrase.  
- Multi-agent systems pass partial context and lose attribution.  

---

## Root causes
- **Orphan citations**: snippet ID missing or fabricated.  
- **Boundary drift**: citation spans cross section joins.  
- **Silent truncation**: tokens dropped at cut points.  
- **Cache overwrite**: citation schema lost after session reload.  
- **Free-text cites**: URLs or titles given without offsets.  

---

## Core acceptance targets
- Each claim must include `snippet_id`, `section_id`, `start_line`, `end_line`, `source_url`.  
- ΔS(question, retrieved) ≤ 0.45 overall.  
- Joins between snippets ≤ 0.50 ΔS.  
- λ convergent across 3 paraphrases.  
- Audit trail reproducible from log alone.  

---

## Structural fixes

- **Snippet table schema**  
  Require `{snippet_id | section_id | start_line | end_line | citation}`.  

- **Fence joins**  
  Split at section boundaries. Reject cross-section reuse.  

- **Trace log**  
  Store `{ΔS, λ_state, mem_rev, mem_hash}` per step.  

- **Contract lock**  
  Apply [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) for payload validation.  

---

## Fix in 60 seconds
1. **Enforce snippet table** with unique IDs and line ranges.  
2. **Verify ΔS** across each join ≤ 0.50.  
3. **Echo λ states** at retrieval, assembly, reasoning.  
4. **Reject orphan claims** (no snippet_id).  
5. **Log trail** so same inputs → same citations.  

---

## Copy-paste prompt

```

You have TXT OS and the WFGY Problem Map.

Goal: Ensure every claim links to a reproducible snippet.

Protocol:

1. Build a Snippet Table {snippet\_id, section\_id, start\_line, end\_line, citation}.
2. Require cite-then-answer.
3. Forbid cross-section reuse.
4. If a claim has no snippet\_id, stop and request citation.
5. Report ΔS(question,retrieved), joins ΔS, and λ states.
6. Store {mem\_rev, mem\_hash, task\_id} for audit trail.
7. Answer only with snippets present in the table.

```

---

## Common failure signals
- Citations alternate across runs → missing trace schema.  
- URL without offsets → orphan citation.  
- Facts cited but no snippet_id → schema lock failed.  
- Session reload erases citations → ghost cache in memory.  

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

要直接開始 **data-contracts.md** 嗎？
