# Memory Coherence — Multi-Session and State Alignment

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


Keep multi-turn and multi-session dialogs stable by fencing memory state.  
This page shows how to prevent forks, desync, and ghost buffers when conversations span long contexts or multiple agents.

---

## When to use this page
- Long support chats (~days) forget earlier task context.  
- Model switches or tab refreshes flip prior facts.  
- Two agents on the same ticket give inconsistent answers.  
- OCR transcripts look fine but later steps rewrite history.  
- Persona or role change contaminates state with old context.  

---

## Core acceptance targets
- Each turn stamped with `mem_rev` and `mem_hash`.  
- No forks across sessions for the same `task_id`.  
- ΔS(question, retrieved) ≤ 0.45 with joins ≤ 0.50.  
- λ remains convergent across three paraphrases.  
- All claims cite snippet_id, no orphans.  

---

## Structural fixes

- **Stamp and fence**  
  Require `mem_rev`, `mem_hash`, and `task_id` at every turn.  
  Forbid writes if stamps mismatch.

- **Shard state**  
  Partition prompts as `{system | task | constraints | snippets | answer}`.  
  Forbid snippet reuse across sections.

- **Normalize consistently**  
  Enforce Unicode NFC, strip zero width marks, unify full/half width.  
  Block OCR lines below confidence threshold.

- **Recover forks**  
  If two agents diverge, reconcile by ΔS triangulation and pick the lower-entropy path.

- **Bridge collapse**  
  Apply BBCR if attention melt or desync detected mid-chain.

---

## Fix in 60 seconds
1. At turn start, echo {mem_rev, mem_hash, task_id}.  
2. If stamps mismatch, reject write and request sync.  
3. Split snippets by section, forbid cross-reuse.  
4. Normalize all inputs.  
5. Apply BBAM/BBCR if λ drifts or collapse appears.  
6. Verify ΔS(question, retrieved) ≤ 0.45 and joins ≤ 0.50.  

---

## Copy-paste prompt

```

You have TXT OS and the WFGY Problem Map.

Goal: Keep memory coherent across multi-session dialogs.

Protocol:

1. Print {mem\_rev, mem\_hash, task\_id}.
2. Assemble prompt as {system | task | constraints | snippets | answer}.
3. Enforce guardrails:

   * cite then answer
   * forbid cross-section reuse
   * reject orphan claims without snippet\_id
4. If λ flips, apply BBAM. If collapse, insert BBCR bridge.
5. Report ΔS(question, retrieved), ΔS across joins, λ states, and final answer.

```

---

## Common failure patterns
- **State fork**: two parallel tabs rewrite history differently.  
- **Ghost buffer**: old role text leaks into new session.  
- **Desync**: memory IDs mismatch after refresh.  
- **OCR drift**: spacing or casing breaks snippet alignment.  

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

