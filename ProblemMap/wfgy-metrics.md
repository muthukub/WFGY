<!-- ============================================================= -->
<!--  wfgy-metrics.md · Core Reference · Version 2025-08-06         -->
<!--  License: MIT                                                 -->
<!--  Defines every first-class metric used by WFGY tools,         -->
<!--  dashboards, and CI gates. Copy, fork, or map to any stack.   -->
<!-- ============================================================= -->

# 📐 WFGY Metrics — Canonical Definitions  
*A single spec for measuring semantic accuracy, stability, cost, and safety across any LLM system.*

> **Evaluation disclaimer (WFGY metrics)**  
> This document defines a set of WFGY style metrics for inspecting model behavior and RAG pipelines.  
> These metrics are heuristic instruments that highlight patterns and failure modes in a given setup.  
> They do not by themselves prove that a system is safe, aligned or correct in all cases.  
> When you use these metrics, you should report the models, prompts, datasets and thresholds that were chosen and avoid treating any single score as a scientific guarantee.

---

> **Why read this?**  
> – You can’t improve what you can’t measure.  
> – ΔS, λ_observe, and E_resonance already power the **Problem Map**, **Semantic Clinic**, and WFGY’s CI templates.  
> – Standard names = instant compatibility with Grafana, Prometheus, LangSmith, Phoenix, and custom OTEL traces.

---

## 0 · Metric Taxonomy

| Pillar        | Metric                       | Symbol / Field | Primary Use |
|---------------|----------------------------- |---------------|-------------|
| **Semantic**  | Semantic Stress              | `deltaS`       | Detect drift / wrong chunks |
|               | Answer F1 / EM              | `f1`, `em`     | QA accuracy |
| **Logic**     | Logic Vector                | `lambda`       | Convergence / divergence flag |
|               | Residual Coherence          | `e_resonance`  | Slow entropy leaks |
| **Efficiency**| Cost per 1 k tokens         | `usd_k`        | Budget guard |
|               | Latency p95 (ms)            | `latency_p95`  | SLO gate |
| **Safety**    | Opcode / Tool Jailbreak     | `tool_offtrack`| Router drift |
|               | Citation Precision          | `cite_prec`    | Hallucination check |

---

## 1 · Formal Definitions

### 1.1 `deltaS` — Semantic Stress  
`ΔS = 1 − cos( I , G )`  

*I = embedding of live text, G = embedding of expected ground/anchor.*  
Target bands: **stable < 0.40** · transitional 0.40-0.60 · **risk ≥ 0.60**

---

### 1.2 `lambda` — Logic Vector  
`λ ∈ {→ convergent, ← divergent, <> recursive, × chaotic}`  

Computed by PCA on consecutive embedding deltas; sign of first component.

---

### 1.3 `e_resonance` — Residual Coherence  
`E = mean_t‖B_t‖`, where `B_t = I_t − G_t + m·c²` (see BBMC).  
Flat or downward trend = healthy; upward slope > 0.02 = entropy leak.

---

## 2 · Reference Thresholds (production)

| Metric           | PASS                | WARN                      | FAIL                    |
|------------------|---------------------|---------------------------|-------------------------|
| `deltaS_q_ctx`   | ≤ 0.45              | 0.45 – 0.60               | > 0.60                  |
| `lambda`         | all →              | ← appears 1-2×            | persistent ← / ×        |
| `e_resonance`    | slope ≤ 0           | slope 0 – 0.02            | slope > 0.02            |
| `cite_prec`      | ≥ 0.90              | 0.80 – 0.90               | < 0.80                  |
| `usd_k`          | ≤ baseline         | +0 – 10 %                 | > 10 % jump             |
| `latency_p95`    | within SLA         | 1.2 × SLA                 | > 1.5 × SLA             |

---

## 3 · Python Helper

```python
from wfgy.metrics import deltaS, lambda_state, e_resonance

q   = "How do I renew my passport?"
ctx = rag_retrieve(q)
print("ΔS:", deltaS(q, ctx))           # 0.37

ans = llm_reason(ctx, q)
print("λ :", lambda_state(ans))        # →

print("E :", e_resonance())            # rolling avg
````

---

## 4 · OpenTelemetry Mapping

```yaml
# otel_map.yaml
deltaS:        wfgy.semantic.deltaS
lambda:        wfgy.logic.lambda
e_resonance:   wfgy.logic.e_res
usd_k:         wfgy.cost.usd_per_k
latency_p95:   wfgy.latency.p95
```

Any WFGY-instrumented app auto-emits these names; map others via the file above.

---

## 5 · PromQL Alert Cookbook

```yaml
- alert: SemanticDriftHigh
  expr: wfgy_semantic_deltaS > 0.60
  for: 1m
- alert: LogicVectorDivergent
  expr: wfgy_logic_lambda == 1   # 1 = divergent
  for: 2m
- alert: ResidualEntropyClimb
  expr: slope(wfgy_logic_e_res[15m]) > 0.02
```

---

## 6 · CSV Schema (offline eval)

```
timestamp,id,set,question,deltaS_q_ctx,lambda,answer_f1,cite_prec,lat_ms,usd_k
```

Feed into `wfgy-eval compare A.csv B.csv`.

---

## 7 · FAQ

**Q : Do I need separate GPU passes to compute embeddings for `deltaS`?**
A : No. Use cached embeddings from retrieval; for answer ΔS, embed answer once after generation.

**Q : Can I add BLEU, Rouge, or faithfulness scores?**
A : Yes—map them under `wfgy.custom.*`. WFGY dashboards auto-discover.

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

