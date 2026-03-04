# Eval: Operator Guidelines

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


This page sets strict rules for **human operators and evaluators** running WFGY-aligned evaluation suites. Evaluation is not a free-form activity. It must follow consistent contracts, logging standards, and reproducible steps.

---

## Open these first

* Gold set design: [goldset\_curation.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval/goldset_curation.md)
* Precision/recall evals: [eval\_rag\_precision\_recall.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval/eval_rag_precision_recall.md)
* Observability probes: [alerting\_and\_probes.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval_Observability/alerting_and_probes.md)

---

## Acceptance targets

* **Inter-annotator agreement** ≥ 0.85 across 3 operators
* **Annotation variance** ≤ 10%
* **Audit reproducibility** ≥ 95% (rerun matches logged label)
* **No operator-induced drift**: ΔS stability remains within ±0.05 after evaluation

---

## Operator responsibilities

1. **Stay schema-locked**
   Every operator must apply the same definition of "correct" → answer cites the correct snippet and explains consistently.

2. **Use three-paraphrase rule**
   Rephrase the query 3× before marking coverage. If answer flips across paraphrases, log as unstable.

3. **Log ΔS and λ**
   Each annotated run must include structural metrics: ΔS(question,retrieved), λ states, snippet IDs.

4. **Apply cost view**
   Record token counts and cost-per-correct when judging pipelines.

5. **No ad-hoc overrides**
   Do not improvise “fixes” in evaluation logs. All fixes must point to an existing ProblemMap page.

---

## Annotation protocol

* **Step 1: Load baseline**
  Open gold set. Verify expected snippet IDs.

* **Step 2: Apply candidate system**
  Run the same queries with candidate pipeline.

* **Step 3: Compare**

  * If candidate cites correct snippet and stays under ΔS ≤ 0.45 → mark correct.
  * If citation missing or ΔS ≥ 0.60 → mark fail, attach probable ProblemMap fix.

* **Step 4: Log JSON**

```json
{
  "operator": "user123",
  "q_id": "Q42",
  "question": "What is the cutoff for semantic drift?",
  "expected_snippet": "S123",
  "candidate_snippet": "S123",
  "ΔS": 0.39,
  "λ_state": "→",
  "correct": true,
  "cost_usd": 0.0012,
  "notes": "Stable across 3 paraphrases"
}
```

---

## When to escalate

* Annotators disagree by >15% → escalate to eval lead.
* ΔS drifts beyond thresholds but operators label "correct" → escalate and reconcile.
* Costs exceed 1.5× baseline → halt run until reviewed.

---

## Audit checklist

* [ ] All logs stored in versioned JSONL.
* [ ] At least 2 operators per eval run.
* [ ] Spot check 10% of logs with independent reviewer.
* [ ] Archive outputs with system hash, gold set version, and ProblemMap pointers.

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

