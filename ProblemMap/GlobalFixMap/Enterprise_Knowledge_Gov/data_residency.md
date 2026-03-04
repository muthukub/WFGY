# Data Residency — Enterprise Knowledge Governance

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


Guardrails and fix patterns to enforce jurisdiction and residency rules on enterprise knowledge pipelines. Use this page when retrieval or storage drifts across regions and breaks compliance with local data laws.

---

## When to use this page
- Snippets come from indexes hosted outside the allowed jurisdiction.  
- AI answers blend EU-only and US-only data without labels.  
- Multi-region retrievers collapse into lowest-latency store instead of correct residency.  
- Replicas sync to unapproved clouds or regions.  

---

## Core acceptance targets
- ΔS(question, retrieved) ≤ 0.45 within jurisdiction.  
- ≥0.70 coverage for the correct residency domain.  
- λ convergent across three paraphrases and two seeds.  
- Every snippet labeled with `{region_tag, residency_scope, audit_hash}`.  

---

## Typical residency problems → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| EU vs US content blended | Index replicas lack residency tags | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| Latency-based failover picks wrong region | Bootstrap not locked to residency fences | [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md) |
| Snippets without residency label | Schema missing `region_tag` field | [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |

---

## Fix in 60 seconds
1. **Probe ΔS across regions**: ask the same Q, check EU vs US vs APAC stores.  
2. **Enforce residency schema**: all payloads must carry `region_tag`.  
3. **Rebuild index replicas** with locked residency metadata.  
4. **Test λ stability** with paraphrases inside each residency scope only.  

---

## Copy-paste schema (JSON)

```json
{
  "snippet_id": "KB-8837",
  "region_tag": "eu-central",
  "residency_scope": "gdpr_lock",
  "audit_hash": "sha256:...",
  "text": "..."
}
````

---

## Escalate when

* ΔS ≥ 0.60 across paraphrases even with region locks.
* Index routing repeatedly breaks residency rules.
* Legal audit requires external certification.

Use [retrieval-playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) and [eval\_rag\_precision\_recall.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/eval/eval_rag_precision_recall.md) for deep remediation.

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

要繼續嗎？
