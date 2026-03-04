# Eval Observability — ΔS Thresholds

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Eval_Observability**.  
  > To reorient, go back here:  
  >
  > - [**Eval_Observability** — evaluation metrics and system observability](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


A dedicated module for **ΔS monitoring** in evaluation pipelines.  
ΔS = semantic distance between query, retrieved content, and gold anchor.  
Tracking thresholds ensures that retrieval and reasoning quality remain **auditable, measurable, and comparable**.

---

## Why ΔS thresholds matter

- **Detect semantic drift**: High ΔS despite “correct” tokens indicates meaning mismatch.  
- **Localize retrieval errors**: Low similarity in meaning even if vector scores look fine.  
- **Evaluate reasoning robustness**: Stable models keep ΔS below the risk boundary across paraphrases.  
- **Flag latent hallucinations**: ΔS >0.60 strongly correlates with unsupported answers.

---

## Core bands

| Band | Range | Meaning |
|------|-------|---------|
| **Stable** | ΔS < 0.40 | Retrieval and reasoning aligned. Answers should be correct and verifiable. |
| **Transitional** | 0.40 ≤ ΔS < 0.60 | Risk zone. Minor schema changes or index drift may flip outcomes. |
| **Critical** | ΔS ≥ 0.60 | High failure probability. Almost always linked to missing context or schema break. |

---

## Acceptance targets

- Per-query: **ΔS ≤ 0.45**  
- Batch average: **≤ 0.40**  
- Allowance: **≤ 10%** of queries can fall in the transitional band (0.40–0.60).  
- Critical: **0% tolerance** for ΔS ≥ 0.60 in gold-set eval.

---

## ΔS in eval workflow

1. **Probe per query**  
   Log ΔS(question, retrieved) and ΔS(retrieved, anchor).  
2. **Batch roll-up**  
   Compute mean, variance, and percentile distribution.  
3. **Compare across seeds**  
   Run three paraphrases and two random seeds; check convergence.  
4. **Drift alerting**  
   If ΔS rises >0.05 vs baseline, trigger retraining or schema audit.  

---

## Example probe (pseudo)

```python
def deltaS_probe(query, retrieved, anchor):
    d1 = deltaS(query, retrieved)
    d2 = deltaS(retrieved, anchor)
    return max(d1, d2)

for q in eval_set:
    s = deltaS_probe(q.query, q.retrieved, q.anchor)
    if s >= 0.60:
        alerts.append({"qid": q.id, "ΔS": s, "status": "critical"})
````

---

## Common pitfalls

* **Using cosine similarity as ΔS** → ΔS is semantic distance, not raw vector score.
* **Ignoring anchor comparison** → must compute against both query and gold span.
* **No variance tracking** → averages hide volatility; variance is key.
* **One-shot eval** → without paraphrase/seed checks, thresholds lack reliability.

---

## Reporting recommendations

* **ΔS histogram**: visualize stability bands.
* **Trend line**: track ΔS mean per batch over time.
* **Baseline delta**: highlight drift from previous eval version.
* **Failure clustering**: group queries where ΔS ≥0.60 for root-cause analysis.

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

