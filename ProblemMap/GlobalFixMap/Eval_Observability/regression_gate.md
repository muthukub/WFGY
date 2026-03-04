# Eval Observability — Regression Gate

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


A structural safeguard that enforces measurable thresholds before any pipeline is promoted to production.  
Use this page to define hard acceptance criteria (ΔS, coverage, λ, resonance) and stop silent regressions from shipping.

---

## Why regression gates matter

- **Catch semantic drift early**: A small rise in ΔS leads to compounding hallucinations downstream.  
- **Stable releases**: Prevents model upgrades or retraining from silently reducing accuracy.  
- **Auditable rules**: Clear thresholds mean every team member can verify before deploy.  
- **Cross-stack consistency**: Same rules apply across providers, retrievers, and orchestration layers.

---

## Core gate thresholds

| Metric | Requirement | Failure signal |
|--------|-------------|----------------|
| ΔS(question, retrieved) | ≤ 0.45 | drift ≥ 0.60 means block release |
| Coverage of target section | ≥ 0.70 | low coverage = missing context |
| λ_observe | Convergent across 3 paraphrases, 2 seeds | divergence = unstable reasoning |
| E_resonance | Flat on 50–100 step windows | spikes = entropy collapse risk |

---

## Deployment checklist

1. **Pre-release batch eval**  
   Run gold set of ~100–500 Q&A pairs. Collect ΔS, coverage, λ, resonance.

2. **Gate decision**  
   - If ΔS ≤ 0.45 AND coverage ≥ 0.70 → **pass**.  
   - If ΔS between 0.46–0.59 → **manual review**.  
   - If ΔS ≥ 0.60 OR coverage < 0.70 → **fail, block release**.

3. **Variance probe**  
   Check λ stability across 3 paraphrases × 2 seeds. Divergence disqualifies release.

4. **Regression log**  
   Store results with index hash + commit hash + retriever config.  
   Enables reproducibility and rollback.

---

## Example gating script (pseudo)

```yaml
# regression_gate.yml
metrics:
  deltaS: <=0.45
  coverage: >=0.70
  lambda: convergent
  resonance: flat
goldset: eval_set_500.json
policy:
  fail_on_drift: true
  manual_review_range: [0.46, 0.59]
  require_seeds: 2
  require_paraphrases: 3
````

---

## Common pitfalls

* **Changing retriever k** without updating gates. Always re-test thresholds.
* **Skipping paraphrase probes**. One stable query is not enough.
* **Not logging coverage**. ΔS alone cannot prove retrieval completeness.
* **Silent config drift**. Gate must bind to exact retriever + index hash.

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

