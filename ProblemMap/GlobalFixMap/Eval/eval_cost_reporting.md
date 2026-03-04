# Eval: Cost Reporting and Efficiency

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Eval**.  
  > To reorient, go back here:  
  >
  > - [**Eval** — model evaluation and benchmarking](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>

> **Evaluation disclaimer (cost reporting)**  
> Any cost and efficiency numbers on this page come from specific runs with specific models and hardware.  
> They are for comparison inside that context only and are not economic guarantees or universal prices.

---

This page defines how to measure and report **cost per correct answer** in retrieval-augmented and reasoning pipelines. Latency and accuracy alone are insufficient. Without cost analysis, systems regress into wasteful configurations.

## Open these first

* Latency vs Accuracy trade-off: [eval\_latency\_vs\_accuracy.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval/eval_latency_vs_accuracy.md)
* Benchmark suite: [eval\_benchmarking.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval/eval_benchmarking.md)
* Observability probes: [alerting\_and\_probes.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval_Observability/alerting_and_probes.md)

---

## Acceptance targets

* **Cost per correct answer** ≤ 1.3× baseline
* **Cost stability variance** ≤ 15% across 3 seeds and 3 paraphrases
* **Token efficiency** ≥ 0.7 (fraction of tokens contributing to correct citation)
* **Budget alerting**: auto-flag when projected monthly spend > 110% of budget cap

---

## Reporting dimensions

Each evaluation run must record cost on three levels:

1. **Raw tokens**

   * input, output, total per query
   * broken down by retrieval, rerank, reasoning

2. **Cost per unit**

   * \$/1k tokens per provider and model
   * normalized into `usd_equiv`

3. **Cost per correct**

   * (total spend ÷ number of correct answers)
   * stratified by question bucket (short, medium, long)

---

## JSON schema

```json
{
  "suite": "v1_cost",
  "arm": "with_hybrid",
  "provider": "anthropic",
  "model": "claude-3.7-sonnet",
  "bucket": "long",
  "precision": 0.79,
  "recall": 0.68,
  "ΔS_avg": 0.41,
  "correct_answers": 40,
  "total_questions": 50,
  "tokens": { "in": 2850, "out": 920, "total": 3770 },
  "cost_per_1k_tokens_usd": 0.006,
  "spend_usd": 0.0226,
  "cost_per_correct": 0.00056,
  "variance_across_runs": 0.11,
  "notes": "within budget and stable"
}
```

---

## Diagnostic questions

* Are rerankers worth the extra spend? → check ΔS reduction vs token increase.
* Is hybrid retrieval doubling retrieval tokens with little gain?
* Does the large model add accuracy, or is a small model + WFGY equal at lower cost?
* Is citation length inflated (long snippets)? → enforce snippet contract.

---

## Escalation and fixes

* **High cost per correct** → switch to caching, smaller model with WFGY overlay.
* **Variance >15%** → clamp paraphrases, normalize prompt headers.
* **Budget overrun** → auto-throttle evals, alert with [alerting\_and\_probes.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval_Observability/alerting_and_probes.md).

---

## Minimal run

1. Select 20 mixed-length questions.
2. Run baseline and candidate arms.
3. Compute cost per correct.
4. Ship only if candidate ≤ 1.3× baseline and stable across seeds.

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

