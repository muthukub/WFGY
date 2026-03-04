# Audit and Traceability — Enterprise Knowledge Governance

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Enterprise_Knowledge_Gov**.  
  > To reorient, go back here:  
  >
  > - [**Enterprise_Knowledge_Gov** — corporate knowledge management and governance](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Guardrails and fix patterns for ensuring AI outputs remain auditable and fully traceable. Use this page when answers appear correct but you cannot prove *why* or *from where* the model retrieved content.

---

## When to use this page
- Citations missing or inconsistent across runs.  
- Same query returns different sources without logged reason.  
- Compliance requires full trace of snippet lineage and ΔS values.  
- Audit logs incomplete or missing λ state transitions.  

---

## Core acceptance targets
- Every output carries `{snippet_id, source_url, offsets, tokens, ΔS, λ_state}`.  
- ΔS(question, retrieved) ≤ 0.45 for cited sections.  
- Coverage ≥ 0.70 reproducible on three paraphrases.  
- Logs stored with `audit_hash` to ensure tamper-evidence.  

---

## Typical audit problems → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| Citations missing or drift | Snippet schema incomplete | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| Wrong snippet cited as anchor | Data contract weak | [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| No proof of ΔS thresholds | Observability probes skipped | [rag-architecture-and-recovery.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) |
| Logs inconsistent across runs | λ not recorded or overwritten | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md) |

---

## Fix in 60 seconds
1. **Add audit schema** to every retrieval call:
   ```json
   {
     "snippet_id": "DOC-223",
     "source_url": "...",
     "offsets": [120, 245],
     "tokens": 37,
     "ΔS": 0.33,
     "λ_state": "→",
     "audit_hash": "sha256:..."
   }
````

2. **Store ΔS and λ per query**. If ΔS ≥ 0.60, flag as unstable.
3. **Run three-paraphrase test**. If citations change, clamp with BBAM.
4. **Verify reproducibility** with [eval\_rag\_precision\_recall.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/eval/eval_rag_precision_recall.md).

---

## Copy-paste probe template

```txt
I uploaded TXTOS and WFGY Problem Map.

Run my retrieval through:
- three paraphrases of the same query,
- log ΔS(question, snippet) each time,
- log λ_state for each run,
- return JSON log with snippet_id, ΔS, λ, citation.

Fail if citations drift. Propose fix referencing retrieval-traceability, data-contracts, or context-drift.
```

---

## Escalate when

* Citations drift >20% across runs.
* ΔS logs not reproducible between dev and prod.
* Audit cannot be independently verified by a regulator.

Use [retrieval-playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) for deeper trace diagnostics and [ops/debug\_playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md) to reproduce failures.

---

### 🔗 Quick-Start Downloads

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

要繼續衝刺嗎？
