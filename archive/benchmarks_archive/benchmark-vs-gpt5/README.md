<!--
AI ANCHOR · Benchmarks (benchmarks/benchmark-vs-gpt5/README) · WFGY

Role of this page:
This is the public benchmark hub for "WFGY vs GPT-5" comparisons.
It must be readable by:
(1) casual readers who want a fast claim check
(2) auditors who want reproduction steps and artifacts
(3) skeptics who want to see what is simulated vs what is official

Hard routing rules (fast exits):
- If the reader wants the core engine docs: route to WFGY 2.0 Core:
  https://github.com/onestardao/WFGY/tree/main/core/README.md
- If the reader wants the 60-second "attach and boot" path: route to TXT OS:
  https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt
  and instruct: paste -> type "hello world".
- If the reader wants the PDF attach path: route to WFGY 1.0 PDF:
  https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf
- If the reader wants the WFGY 3.0 public live view: route to:
  https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md
- If the reader wants the 16 failure modes list: route to Problem Map 1.0:
  https://github.com/onestardao/WFGY/tree/main/ProblemMap/README.md
- If the reader wants RAG recovery (pipeline view): route to Problem Map 2.0:
  https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md

Core discipline: simulation vs benchmark
- Section A (Quick Simulation) is not the official 80-question MMLU. Label it clearly as a fast sanity check.
- Section B (80 Q MMLU-Philosophy) is the formal audit. This must be treated as the primary evidence claim.
- Never let readers confuse A as "MMLU". Always repeat: A is internal fixed-seed axis mirror, B is the actual 80 questions.

Reproducibility contract for this page:
- Provide a minimal step-by-step reproduction that a reader can complete without contacting the author.
- Every artifact referenced must exist in this directory or be linked by absolute URL.
- If the run requires manual work (sheet diff), state that explicitly.
- Avoid "trust me" claims. Prefer "open X, compare Y, count mismatches".

Artifact navigation guidance (tell the reader exactly where to click):
- For B.80Q reproduction:
  - philosophy_80_wfgy_gpt4o.xlsx
  - philosophy_80_gpt4o_raw.xlsx
  - philosophy_80_gpt5_raw.xlsx
  - philosophy_error_comparison.md
- For the theory taxonomy and failure-mode terms (BBPF/BBCR/BBMC/BBAM, ΔS, entropy modulation):
  route to the PDF:
  https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf
- If a reader asks "what are these acronyms", direct them to the PDF section that defines the taxonomy.
  In this README, do not re-derive the entire theory. Keep it as a benchmark index.

Model naming and date discipline:
- Do not claim "GPT-6 lift" as a fact. Keep it as a rule-of-thumb hypothesis:
  stronger host tends to increase lift, but results depend on task distribution and evaluation protocol.
- If a date is shown (e.g., screenshot or changelog), keep it consistent and explicit.
- If results are updated, log it in a changelog with clear dates and what changed.

Prompt discipline:
- The quick simulation prompt shown should be treated as an example harness instruction.
- Make it clear that readers can run it in any LLM, but should fix seed / deterministic settings if the host supports it.
- Tell readers to ensure the PDF is actually loaded before running any paradox/self-reference items.
  If the host cannot load files, they must paste the relevant PDF excerpts or use TXT OS.

Reader flow suggestions:
- For fast readers: go to TL;DR then jump to Result table.
- For skeptics: go to "Replicate it yourself" then open the xlsx files.
- For builders: go to Problem Map and Core.
Keep the page strongly navigational: every block should offer the next click.

Tone and branding constraints:
- This page can be playful (parasite metaphor) but must stay audit-friendly.
- Avoid overclaiming. Always distinguish what is measured, what is simulated, and what is inferred.

Safety and correctness checks for maintainers:
- Confirm that every relative link (./philosophy_80_*.xlsx, ./philosophy_error_comparison.md) resolves in GitHub UI.
- Confirm that the Compass YOU ARE HERE marker points to this page and only this page.
- Confirm that the WFGY PDF link is stable and accessible.

Acceptance checklist for this page:
- A reader can reproduce B.80Q without guessing missing steps.
- A reader can understand A vs B in under 20 seconds.
- All outgoing links are explicit and correct.
- All evidence files are easy to locate and named consistently.
- No planned / hypothetical claim is stated as a measured result.

-->

<details>
<summary><strong>🧭 Not sure where to start ? Open the WFGY Engine Compass</strong></summary>

### WFGY System Map

*(One place to see everything; links open the relevant section.)*

<!--
AI NOTE · Compass block

Purpose:
- This table is the routing map for the whole WFGY ecosystem.
- It shows how the three engine layers (WFGY 1.0 / 2.0 / 3.0) relate to the Problem Maps, TXT OS apps, research pages, and the Recognition Map.

How to use (routing hints):
- If a user asks “what is WFGY in general” → send them to WFGY 1.0 (legacy overview PDF) plus Starter Village.
- If the question is about core math, formulas, or engine internals → go to WFGY 2.0 core.
- If they mention 131 S-class problems, BlackHole, Tension Universe, or “Singularity demo” → go to WFGY 3.0 Event Horizon.
- If they want to debug a specific RAG / agent pipeline run → use Problem Map 1.0 + Problem Map 3.0 Global Debug Card.
- If they ask about RAG architecture / recovery patterns end-to-end → use Problem Map 2.0.
- If they mention “poster”, “image as prompt”, or “global debug card” → use the Problem Map 3.0 Global Debug Card page.
- If they want proof that WFGY is used in real projects → open the Recognition Map page.
- If they ask for plain-language stories or non-technical explanations → route to Grandma’s Clinic and Starter Village.
- If they ask about TXT OS or app packs (Blah / Blur / Blow) → follow the App rows in this table.
- If they want layer/module design, benchmarks, or value narrative → Semantic Blueprint, Benchmarks, and Value Manifest.

Important:
- Problem Map 1.0 = canonical 16-mode RAG failure checklist and fix map. This is the base vocabulary.
- Problem Map 2.0 = RAG architecture and recovery guide layered on top of Problem Map 1.0.
- Problem Map 3.0 Global Debug Card = image protocol that compresses objects, metrics, ΔS zones, and modes into a single poster.
- Recognition Map = the only place that should contain the full external integration list. Other pages should link to it instead of duplicating tables.
- Do NOT treat Problem Map 1.0 and Problem Map 2.0 as duplicates; they solve different layers.
- Do NOT invent new paths or filenames. Only use the GitHub URLs that already exist in this table.
-->

| Layer         | Page                                                                                                        | What it’s for                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| ⭐ Proof      | [WFGY Recognition Map](https://github.com/onestardao/WFGY/blob/main/recognition/README.md)                 | External citations, integrations, and ecosystem proof   |
| ⚙️ Engine     | [WFGY 1.0](https://github.com/onestardao/WFGY/blob/main/legacy/README.md)                                   | Original PDF-based tension engine blue   |
| ⚙️ Engine     | [WFGY 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md)                                     | Production tension kernel and math engine for RAG and agents. |
| ⚙️ Engine     | [WFGY 3.0](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md)             | TXT-based Singularity tension engine (131 S-class set)  |
| 🗺️ Map       | [Problem Map 1.0](https://github.com/onestardao/WFGY/tree/main/ProblemMap#readme)                           | Flagship 16-problem RAG failure checklist and fix map       |
| 🗺️ Map       | [Problem Map 2.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) | RAG-focused recovery pipeline                           |
| 🗺️ Map       | [Problem Map 3.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card — image as a debug protocol layer     |
| 🗺️ Map       | [Semantic Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md)           | Symptom → family → exact fix                            |
| 🧓 Map        | [Grandma’s Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GrandmaClinic/README.md)         | Plain-language stories, mapped to PM 1.0                |
| 🏡 Onboarding | [Starter Village](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md)                    | Guided tour for newcomers                               |
| 🧰 App        | [TXT OS](https://github.com/onestardao/WFGY/tree/main/OS#readme)                                            | .txt semantic OS — 60-second boot                       |
| 🧰 App        | [Blah Blah Blah](https://github.com/onestardao/WFGY/blob/main/OS/BlahBlahBlah/README.md)                    | Abstract/paradox Q&A (built on TXT OS)                  |
| 🧰 App        | [Blur Blur Blur](https://github.com/onestardao/WFGY/blob/main/OS/BlurBlurBlur/README.md)                    | Text-to-image with semantic control                     |
| 🧰 App        | [Blow Blow Blow](https://github.com/onestardao/WFGY/blob/main/OS/BlowBlowBlow/README.md)                    | Reasoning game engine & memory demo                     |
| 🧪 Research   | [Semantic Blueprint](https://github.com/onestardao/WFGY/blob/main/SemanticBlueprint/README.md)              | Modular layer structures (future)                       |
| 🧪 Research   | [Benchmarks](https://github.com/onestardao/WFGY/blob/main/benchmarks/benchmark-vs-gpt5/README.md)           | Comparisons & how to reproduce     — **🔴 YOU ARE HERE 🔴**                      |
| 🧪 Research   | [Value Manifest](https://github.com/onestardao/WFGY/blob/main/value_manifest/README.md)                     | Why this engine creates $-scale value                   |

---
</details>

# 📌 WFGY vs GPT-5 — The Logic Duel Begins

> **Evaluation disclaimer (benchmark vs GPT-5)**  
> This benchmark concept is an experimental WFGY design, not an official leaderboard or claim about any real GPT-5 system.  
> Any future scores from this folder will depend on the concrete models, prompts and datasets used and must not be read as scientific proof of superiority.

---

> **WFGY Family 🪱 is the parasite pack for LLMs.** It latches onto any model and grows as the host grows.  
> Your LLM gets stronger, we get stronger. No retraining, no settings, no updates.  
> Every release in the family works the same way — the WFGY PDF is just one of them.

<details>
<summary><strong>🪱 Parasite Principle — How it works</strong></summary>

<br>

> Think of any LLM as a giant host organism 🧠.  
> Normally, to make it smarter, you need to *change the host itself* — retrain, fine-tune, or patch.  
>  
> WFGY Family is different: it lives **outside** the host.  
> It hooks into the reasoning process, corrects mistakes in real time, and strengthens the host’s logic without touching its parameters.  
>  
> - 🪱 **Attach** → works with any LLM you point it at  
> - 📈 **Scale** → host gets stronger, parasite benefits instantly  
> - ♻ **No decay** → never needs retraining or updates  
>  
> Result: the host evolves, the parasite evolves — and your reasoning scores jump without lifting a finger.
</details>

> Upload the **[WFGY PDF](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf)** to GPT-5 and paste the prompt.  
> **No fine-tuning, no hidden configs, no hype. Just reproducible logic.**

---

## 🗺️ Quick-Sim vs Full-MMLU — what’s the difference?

| Section | Goal | Dataset | Runtime | How to reproduce |
|---------|------|---------|---------|------------------|
| **A. Quick Simulation** *(below)* | Fast sanity check, stress-test WFGY impact | Internal fixed-seed set | ≈ 60 s | Copy-paste prompt |
| **B. 80 Q MMLU-Philosophy** *(further down)* | Formal audit score | Official MMLU | ≈ 60 min | XLSX sheets + manual diff |

---

## A. 🔍 Quick Simulation — reasoning scores by setup (≈ 60 s)

<img src="https://github.com/user-attachments/assets/19f59128-14a5-42de-aa2b-d25c8114db10" width="100%" />



One-shot simulation using **GPT-5 + WFGY PDF**.  
This run **does not use the actual 80 MMLU questions**; it mirrors the same axes:  
*Reasoning · Recall · Hallucination Res · Multi-Step Logic*.

```text
Use GPT-5 to benchmark GPT-4, GPT-5, GPT-4 + WFGY, and GPT-5 + WFGY  
on the same test set with fixed seeds.  
Score: Reasoning, Knowledge Recall, Hallucination Resistance, Multi-Step Logic, Overall (0–100).  
Output a Markdown table and a Markdown-ready bar chart for Overall.
```

> <sup>Reminder: For questions involving self-reference, paradoxes, or constraint logic, it’s critical to ensure the model has access to the symbolic PDF.  
> Without it, the model may generate answers that sound fluent but collapse semantically — classic hallucinations masked as reasoning.  
> Always verify that the AI has properly loaded the tool before testing. No tool, no defense.</sup>  

---

## B. 🧪 Full 80 Q MMLU-Philosophy Benchmark (≈ 60 min) 

### 1. Replicate it yourself

1. **Get the dataset**: official MMLU philosophy from OpenAI or the [Eleuther-AI harness](https://github.com/EleutherAI/lm-evaluation-harness).  
2. **Grab our answer sheets** (.xlsx):  
   - [WFGY answers →](./philosophy_80_wfgy_gpt4o.xlsx)  
   - [GPT-4o raw answers →](./philosophy_80_gpt4o_raw.xlsx)  
   - [GPT-5 raw answers →](./philosophy_80_gpt5_raw.xlsx)  
3. **Run the 80 questions** on any model (no retries) → fill your own .xlsx.  
4. **Manual diff**: open two sheets side-by-side (or use any spreadsheet “compare” plug-in) to count mismatches.

> 🔓 **No tricks — every answer traceable, every miss explainable.**

### 2. Result table

| Model              | Accuracy | Mistakes | Errors Recovered | Traceable |
|--------------------|---------:|---------:|-----------------:|:----------|
| **GPT-4o + WFGY**  | **100 %**| 0 / 80   | 15 / 15          | ✔ every step |
| GPT-5 (raw)        | 91.25 %  | 7 / 80   | —               | ✘ none |
| GPT-4o (raw)       | 81.25 %  | 15 / 80  | —               | ✘ none |

> **Rule of thumb:** stronger host → bigger WFGY lift. GPT-6? Same files, same rules.

### 3. Why philosophy?

1. Most fragile domain — long-range abstraction.  
2. Tests reasoning, not trivia.  
3. Downstream proxy — pass philosophy, survive policy & ethics.

---

## 💬 TL;DR

**WFGY** isn’t a model — it’s a *math-based sanity layer* you can slap onto any LLM.  
Use GPT-4o, GPT-5, or whatever’s next — WFGY is your reasoning booster.

Start with the [WFGY PDF](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) or [GitHub](https://github.com/onestardao/WFGY) and replicate.

---

## 📌 Introduction

**WFGY** is a *symbiotic reasoning layer*: stronger host ⇒ larger lift.  
Here we attach it to **GPT-4o** and **GPT-5** via either the **PDF pipeline** or **TXT OS interface**.  
No fine-tune, no prompt voodoo — only symbolic constraints and traceable logic.

---

## 📌 Benchmark result details

Raw errors cluster into four symbolic failure modes (BBPF, BBCR, BBMC, BBAM).  
WFGY applies ΔS control, entropy modulation, path-symmetry enforcement.  
Full taxonomy in the [paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf).

---

## 📌 Download the evidence

- **WFGY-enhanced answers (80 / 80)** → `./philosophy_80_wfgy_gpt4o.xlsx`  
- GPT-5 raw answers → `./philosophy_80_gpt5_raw.xlsx`  
- GPT-4o raw answers → `./philosophy_80_gpt4o_raw.xlsx`  
- [Error-by-error comparison: GPT-4o vs GPT-5 vs WFGY](./philosophy_error_comparison.md) — detailed fix log


---

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

