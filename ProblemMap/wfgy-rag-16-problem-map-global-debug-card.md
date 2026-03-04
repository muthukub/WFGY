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

| Layer         | Page                                                                                                        | What it’s for                                                  |
| ------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| ⭐ Proof      | [WFGY Recognition Map](https://github.com/onestardao/WFGY/blob/main/recognition/README.md)                 | External citations, integrations, and ecosystem proof          |
| ⚙️ Engine     | [WFGY 1.0](https://github.com/onestardao/WFGY/blob/main/legacy/README.md)                                   | Original PDF-based tension engine blue                         |
| ⚙️ Engine     | [WFGY 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md)                                     | Production tension kernel and math engine for RAG and agents.  |
| ⚙️ Engine     | [WFGY 3.0](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md)            | TXT-based Singularity tension engine (131 S-class set)         |
| 🗺️ Map       | [Problem Map 1.0](https://github.com/onestardao/WFGY/tree/main/ProblemMap#readme)                          | Flagship 16-problem RAG failure checklist and fix map          |
| 🗺️ Map       | [Problem Map 2.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) | RAG-focused recovery pipeline                                |
| 🗺️ Map       | [Problem Map 3.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card - image as a debug protocol layer - **🔴 YOU ARE HERE 🔴** |
| 🗺️ Map       | [Semantic Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md)          | Symptom → family → exact fix                                   |
| 🧓 Map        | [Grandma’s Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GrandmaClinic/README.md)        | Plain-language stories, mapped to PM 1.0                       |
| 🏡 Onboarding | [Starter Village](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md)                   | Guided tour for newcomers                                      |
| 🧰 App        | [TXT OS](https://github.com/onestardao/WFGY/tree/main/OS#readme)                                            | .txt semantic OS - 60-second boot                              |
| 🧰 App        | [Blah Blah Blah](https://github.com/onestardao/WFGY/blob/main/OS/BlahBlahBlah/README.md)                   | Abstract/paradox Q&A (built on TXT OS)                         |
| 🧰 App        | [Blur Blur Blur](https://github.com/onestardao/WFGY/blob/main/OS/BlurBlurBlur/README.md)                   | Text-to-image with semantic control                            |
| 🧰 App        | [Blow Blow Blow](https://github.com/onestardao/WFGY/blob/main/OS/BlowBlowBlow/README.md)                   | Reasoning game engine & memory demo                            |

---
</details>

# 🚀 WFGY 3.0 · RAG 16 Problem Map · Global Debug Card
### Image as a Structured Debug Prompt for RAG / Agent Pipelines

<details>
<summary>🌐 Recognition & ecosystem integration</summary>
<br>

> As of 2026-03, the **WFGY RAG 16 Problem Map** line has been adopted or referenced by
> **20+ frameworks, academic labs, and curated lists** in the RAG and agent ecosystem.
> Most external references use the WFGY ProblemMap as a diagnostic layer for RAG / agent pipelines,
> not the full WFGY product stack.
> A smaller but growing set also uses **WFGY 3.0 · Singularity Demo** as a long-horizon TXT stress test.

Some representative integrations:

| Project | Stars | Segment | How it uses WFGY ProblemMap | Proof (PR / doc) |
| --- | --- | --- | --- | --- |
| [RAGFlow](https://github.com/infiniflow/ragflow) | [![GitHub Repo stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social)](https://github.com/infiniflow/ragflow) | Mainstream RAG engine | Adds a RAG failure modes checklist guide in its official docs, adapted from the WFGY 16-problem failure map for step-by-step RAG pipeline diagnostics. | [PR #13204](https://github.com/infiniflow/ragflow/pull/13204) |
| [LlamaIndex](https://github.com/run-llama/llama_index) | [![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social)](https://github.com/run-llama/llama_index) | Mainstream RAG infra | Integrates the WFGY 16-problem RAG failure checklist into its official RAG troubleshooting docs as a structured failure-mode reference. | [PR #20760](https://github.com/run-llama/llama_index/pull/20760) |
| [ToolUniverse (Harvard MIMS Lab)](https://github.com/mims-harvard/ToolUniverse) | [![GitHub Repo stars](https://img.shields.io/github/stars/mims-harvard/ToolUniverse?style=social)](https://github.com/mims-harvard/ToolUniverse) | Academic lab / tools | Provides a `WFGY_triage_llm_rag_failure` tool that wraps the 16-mode map for incident triage. | [PR #75](https://github.com/mims-harvard/ToolUniverse/pull/75) |
| [Rankify (Univ. of Innsbruck)](https://github.com/DataScienceUIBK/Rankify) | [![GitHub Repo stars](https://img.shields.io/github/stars/DataScienceUIBK/Rankify?style=social)](https://github.com/DataScienceUIBK/Rankify) | Academic lab / system | Uses the 16 failure patterns in RAG and re-ranking troubleshooting docs. | [PR #76](https://github.com/DataScienceUIBK/Rankify/pull/76) |
| [Multimodal RAG Survey (QCRI LLM Lab)](https://github.com/llm-lab-org/Multimodal-RAG-Survey) | [![GitHub Repo stars](https://img.shields.io/github/stars/llm-lab-org/Multimodal-RAG-Survey?style=social)](https://github.com/llm-lab-org/Multimodal-RAG-Survey) | Academic lab / survey | Cites WFGY as a practical diagnostic resource for multimodal RAG. | [PR #4](https://github.com/llm-lab-org/Multimodal-RAG-Survey/pull/4) |

For the complete 20+ project list (frameworks, benchmarks, curated lists), see the 👉 **[WFGY Recognition Map](https://github.com/onestardao/WFGY/blob/main/recognition/README.md)**

> If your project uses the WFGY ProblemMap and you would like to be listed,
> feel free to open an issue or pull request in this repository.

---

</details>

A production-first failure map for RAG / agent pipelines, compressed into one portable image.
The poster defines objects, metrics, ΔS zones, failure types, and mode patterns in a single unified view.

Feed a failing run `(Q, E, P, A)` plus this card to any LLM.
It returns `type → mode(s) → fixes → verification tests`.

No external framework required.

---

<details>
<summary><b>How to use (60 seconds)</b></summary>

<br>

1) Download the **full-resolution** Debug Card from this repository.
2) Upload the image to any strong LLM.
3) Paste your failing run context:
   - `Q` = user question
   - `E` = top-k retrieved evidence
   - `P` = final prompt sent to the model
   - `A` = model output
   - plus logs/metrics if available
4) Ask the model to diagnose using the **16-Problem Map** and propose fixes with one test per fix.

Expected output:
- ΔS zones (or best-effort estimate)
- failure type: `R / P / S / I`
- 1–3 matching modes (1–16)
- structural fixes + verification tests

</details>

---

![WFGY RAG 16 Problem Map Global Debug Card](./WFGY_RAG_16_Problem_Map_Global_Debug_Card.jpeg)

---

📥 Download the original full-resolution image directly from this repository.  
If this helps you, consider leaving a ⭐ — it helps more developers discover this project. [![GitHub Repo stars](https://img.shields.io/github/stars/onestardao/WFGY?style=social)](https://github.com/onestardao/WFGY)

---

<details>
<summary><b>Colab MVP · Wave 0 (one-click runnable)</b></summary>

<br>

Wave 0 is the first executable form of the Global Debug Card protocol.

It loads the machine-readable specs, parses one debug packet,
and renders a structured triage summary in a single Colab cell.
No LLM. No local setup.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/ProblemMap/GlobalDebugCardExamples/wfgy_rag16_wave0_colab_mvp.ipynb)

**What it demonstrates**

- JSON problem catalog can be consumed programmatically
- Debug packet structure is tool-friendly and stable
- Triage output can be reproduced deterministically

**Wave 0 scope**

- Modes: **No.1, No.2, No.5, No.8**
- Single synthetic failure case
- Single-cell execution

This is the minimal proof that the Global Debug Card can run as code,
not just as a human-readable poster.

</details>

---

<details>
<summary><b>Machine-Readable JSON Specs · Wave 0 (live)</b></summary>

<br>

This page has a Wave 0 version of the machine-readable protocol for the Global Debug Card.
The goal is simple:

> The same debugging logic that lives on the poster should also exist as a stable JSON contract.

Wave 0 ships two JSON specs, both already used by the Colab MVP.

**1. Problem catalog**

- File path:
  `ProblemMap/specs/wfgy_problem_catalog_v1.json`
- Direct link:
  [`wfgy_problem_catalog_v1.json`](https://github.com/onestardao/WFGY/raw/main/ProblemMap/specs/wfgy_problem_catalog_v1.json)

What it contains:

- version and description fields
- timestamp of last update
- lane definitions:
  - `IN` = input / retrieval
  - `RE` = reasoning / planning
  - `ST` = state / memory
  - `OP` = infra / deploy
- type definitions:
  - `R` / `P` / `S` / `I` as the main failure families
- a `wave0_scope` block that documents:
  - Wave 0 focuses on modes **1, 2, 5, 8**
  - the catalog is expected to grow in future waves
- a `modes` array, where each mode includes:
  - `id` and short code (for example `IN-1`)
  - lane
  - default failure type
  - title and short symptom text
  - primary and secondary signals
  - high-level fix focus

This catalog is meant to be **read-only** for tools.
New modes or fields may be added in the future, but existing keys should remain compatible.

**2. Debug packet**

- File path:
  `ProblemMap/specs/wfgy_debug_packet_v1.json`
- Direct link:
  [`wfgy_debug_packet_v1.json`](https://github.com/onestardao/WFGY/raw/main/ProblemMap/specs/wfgy_debug_packet_v1.json)

What it contains:

- version and description
- top-level metadata such as `last_updated_utc`
- a `required_fields` section, defining the minimal keys a packet must include:
  - `id`
  - `created_utc`
  - `environment`
  - `q`
  - `e`
  - `p`
  - `a`
- `optional_fields`, including:
  - `metrics`
  - `labels`
  - `triage_notes`
  - `fix_plan`
- `field_specs` that describe:
  - the type of each field
  - a short description
  - examples where helpful
- an `example_packet` which shows:
  - a realistic RAG failure around a support-ticket summary
  - concrete values for `q`, `e`, `p`, `a`
  - a small metrics block
  - lane / mode labels for Wave 0
  - a compact fix plan and verification tests

The debug packet spec is designed so that:

- any tool can emit one JSON object that follows this shape
- the Colab MVP, or a future agent, can read the object and:
  - infer mode information
  - print a triage summary
  - compare before vs after

**Relationship to the poster**

The JSON layer does **not** replace the image.
Instead, it mirrors the same structure in a way that software can consume:

- the poster is the fastest way for a human and an LLM to triage a new failure
- the JSON specs are the way for tools to replay and track those failures over time

Wave 0 is intentionally minimal but fully working.
Later waves are expected to:

- broaden mode coverage
- add richer metrics and thresholds
- align with concrete ΔS computation recipes
- document versioning and compatibility guarantees

</details>

---

## Environment Coverage

- **[MLflow](https://github.com/mlflow/mlflow)** · Experiment tracking & RAG debugging · [Medium Article](https://psbigbig.medium.com/the-16-problem-rag-map-how-to-debug-failing-mlflow-runs-with-a-single-screenshot-6563f5bee003?postPublishedType=repub)
- **[Dask](https://github.com/dask/dask)** · Distributed execution & task orchestration · [Medium Article](https://psbigbig.medium.com/your-dask-dashboard-is-green-your-rag-answers-are-wrong-here-is-a-16-problem-map-to-debug-them-f8a96c71cbf1)
- **[Kedro](https://github.com/kedro-org/kedro)** · Pipeline structuring & ML workflow management · [Medium Article](https://medium.com/@psbigbig/your-kedro-pipelines-are-reproducible-ae42f775bfde)

---

## FAQ

<details>
<summary><b>Do I need all four objects `(Q, E, P, A)` to use the Global Debug Card?</b></summary>

<br>

The best results come from having all four objects:

- `Q` = user question
- `E` = retrieved evidence
- `P` = final prompt sent to the model
- `A` = model output

This gives the card the full diagnostic chain from intent to evidence to prompt to answer.

If one object is missing, the card can still be used for partial triage:

- missing `P` usually means rough classification is still possible
- missing `E` often points to observability or infra-side issues
- missing both `E` and `P` reduces accuracy, but the card can still help identify likely failure families

In short: all four objects are ideal, but partial inputs can still be useful for first-pass diagnosis.

</details>

---

<details>
<summary><b>Can the Global Debug Card partially automate RAG debugging?</b></summary>

<br>

Yes, partially.

The card is well suited for:

- structured triage
- first-pass failure classification
- matching likely problem modes
- proposing repair directions
- defining one verification test per fix

This means it can help automate the early part of debugging very well.

What it does **not** guarantee is a one-click, fully automatic repair for every RAG failure.
Some cases still require human review, domain context, or deeper system changes.

The current design goal is not "magic auto-fix."
The goal is to turn messy debugging into a repeatable protocol.

</details>

---

<details>
<summary><b>Can tools like OpenClaw use this card to automatically resolve RAG issues?</b></summary>

<br>

Yes, for some classes of issues.

A tool like OpenClaw can use the Global Debug Card as a diagnostic layer:

1. collect `(Q, E, P, A)`
2. run classification
3. emit a structured debug packet
4. apply one constrained repair action
5. re-run a verification check

This is most realistic for problems where the repair loop is narrow and testable.

Best early targets include:

- **No.1** retrieval wrong or off-topic
- **No.5** semantic vs embedding mismatch
- **No.8** missing evidence visibility
- parts of **No.2** interpretation collapse

These are good candidates because they often respond to:

- retrieval parameter changes
- query rewrite
- re-ranking
- logging and observability upgrades
- constrained prompt repair

Harder cases, such as long-horizon reasoning errors or deep architectural flaws, usually should not be treated as fully automatic fixes in the first wave.

</details>

---

<details>
<summary><b>What can the first Colab MVP actually automate?</b></summary>

<br>

The first Colab MVP is designed as a **first-pass repair loop**, not a full autonomous debugger.

Its planned job is:

1. accept one failing case from `(Q, E, P, A)`
2. compute or estimate the diagnostic structure
3. emit a machine-readable debug packet
4. apply one constrained patch
5. re-check one or more verification signals

This makes the first public notebook useful for:

- reproducible triage
- small repair experiments
- before/after comparisons
- documenting how one failure was improved

The first Colab MVP is intended to prove the protocol works in practice.
It is not meant to solve every failure mode automatically on day one.

</details>

---

<details>
<summary><b>Which problem modes are best suited for automated debugging first?</b></summary>

<br>

The best first-wave targets are the modes that are both:

- easy to observe
- narrow enough to repair with a constrained loop

The strongest early candidates are:

- **No.1** retrieval wrong or off-topic  
  Good for top-k sweeps, query rewrite, filter tightening, and re-ranking.

- **No.5** semantic vs embedding mismatch  
  Good for embedding checks, chunking review, normalization review, and retrieval alignment tests.

- **No.8** missing evidence visibility  
  Good for observability upgrades, evidence logging, and packet completeness checks.

- **No.2** interpretation collapse  
  Good for constrained prompt repair, evidence-first answer patterns, and citation-before-claim checks.

These modes are ideal for Wave 0 because they can often be improved without rebuilding the entire stack.

</details>

---

<details>
<summary><b>What will the machine-readable JSON MVP be used for?</b></summary>

<br>

The JSON MVP is the protocol layer for tools.

It is meant to make the card usable by:

- agent runners
- CI workflows
- internal debugging tools
- replay and comparison pipelines

The planned JSON layer has two main roles:

1. **Problem catalog JSON**  
   A machine-readable version of the 16-mode map, including mode IDs, signals, and default repair directions.

2. **Debug packet JSON**  
   A stable result format for one diagnosis run, including the detected type, likely modes, fixes, and verification steps.

The JSON layer does not replace the image workflow.
It makes the same logic consumable by software.

</details>

---

<details>
<summary><b>Can I plug this into my own agent runner, CI, or internal tooling?</b></summary>

<br>

Yes, that is one of the intended directions.

If your system can provide a minimal case record such as:

- `Q`
- `E`
- `P`
- `A`

then it can likely be adapted to this protocol.

Additional metadata can improve results, for example:

- retrieval scores
- model name
- chunk IDs
- timing logs
- prompt template version
- index configuration

The final goal is simple:

your system emits one case, the protocol emits one debug packet.

That makes the card easier to integrate into real workflows than a free-form debugging conversation.

</details>

---

<details>
<summary><b>Is this meant to replace human debugging?</b></summary>

<br>

No.

The purpose of the Global Debug Card is to improve the **first stage** of debugging:

- shared vocabulary
- structured triage
- clearer diagnosis
- repeatable verification steps

It is not meant to remove human judgment.

Human review is still important for:

- high-risk changes
- domain-specific correctness
- architecture-level redesign
- policy or safety decisions
- ambiguous multi-cause failures

A good way to think about it is:

this card reduces debugging chaos, but humans still decide the final repair strategy.

</details>

---

<details>
<summary><b>Do I need embeddings to use this page?</b></summary>

<br>

No, but embeddings make the protocol stronger.

The full diagnostic model uses structured similarity and boundary reasoning.
That works best when a fixed embedding model is available.

However, the card is still useful without embeddings:

- a strong LLM can estimate likely drift patterns from the visible objects
- the image workflow can still guide manual or semi-structured triage
- rough type and mode guesses can still be generated from the failure pattern

So there are two valid usage modes:

- **image + reasoning workflow** for fast manual triage
- **embedding + packet workflow** for stronger, machine-runnable diagnosis

</details>

---

<details>
<summary><b>What is the difference between the image workflow and the JSON workflow?</b></summary>

<br>

They use the same logic, but they serve different users.

**Image workflow**
- optimized for humans
- easy to use immediately
- works by uploading the card and pasting `(Q, E, P, A)`
- good for fast triage with any strong LLM

**JSON workflow**
- optimized for tools
- intended for automation and integration
- produces stable, machine-readable outputs
- good for replay, comparison, and agent orchestration

In short:

- the image workflow is the human entry point
- the JSON workflow is the machine entry point

Both are two views of the same protocol.

</details>

---

<details>
<summary><b>Why not just paste logs into any strong LLM and ask it to debug?</b></summary>

<br>

You can do that, and sometimes it helps.
But without a shared protocol, the output is often inconsistent.

Raw free-form debugging usually has these problems:

- no shared object model
- no fixed failure vocabulary
- no stable mapping from symptoms to modes
- no required verification step
- hard to compare two runs consistently

The Global Debug Card adds structure:

- the same four objects
- the same failure families
- the same mode vocabulary
- the same output expectation
- the same repair-and-test pattern

That makes debugging more reproducible and much easier to turn into automation.

</details>

---

<details>
<summary><b>How far can the Global Debug Card be pushed?</b></summary>

<br>

The short answer is: much further than a static poster.

At minimum, it is already useful as:

- an image-based triage layer
- a shared RAG debugging vocabulary
- a structured prompt for diagnosis

With the next layers added, it can grow into:

- a Colab-based repair loop
- a machine-readable incident format
- a replayable before/after comparison tool
- an agent-facing debug protocol
- a lightweight regression-check layer for RAG systems

So the long-term direction is not "just a card."

The long-term direction is:

- from image prompt
- to structured diagnosis
- to partial automation
- to reproducible repair loops
- to a reusable protocol for RAG debugging

</details>

---

<details>
<summary><b>Can this help reduce hallucinations without changing the whole stack?</b></summary>

<br>

Often, yes.

One of the main strengths of the card is that it works as a **diagnostic layer**, not a full replacement stack.

That means teams can often improve reliability by first identifying:

- whether the problem is retrieval
- whether the prompt is the main source of drift
- whether evidence visibility is missing
- whether the issue is state or infra-related

This allows smaller, more targeted fixes:

- retrieval tuning
- prompt repair
- re-ranking
- observability upgrades
- packet completeness checks

In many real cases, that is much cheaper than rebuilding the whole system.

</details>

---

<details>
<summary><b>Can this support replay, A/B comparison, and before/after repair loops?</b></summary>

<br>

Yes, and that is one of the strongest next-step directions.

Once a failure case is captured in a structured form, the same case can be replayed under different settings:

- different top-k values
- different retrievers
- different chunking strategies
- different prompt templates
- different repair actions

This makes it possible to compare:

- before vs after
- setup A vs setup B
- manual fix vs automated fix

That is one reason the Colab MVP and JSON MVP matter.
They move the card from "diagnostic poster" toward "replayable debugging protocol."

</details>

---

<details>
<summary><b>What should I submit if I want my failing case to become a reproducible example?</b></summary>

<br>

The best submission is a minimal but complete failure packet.

Recommended input:

- `Q` = the original user question
- `E` = retrieved evidence or top-k chunks
- `P` = the final prompt sent to the model
- `A` = the model output
- any relevant logs or metrics
- optional notes about the expected correct behavior

You should remove private or sensitive data before sharing.

A good reproducible example does not need to be large.
It just needs to preserve the failure pattern clearly enough for the protocol to analyze.

That kind of example is ideal for future Colab demos, test cases, and repair-loop comparisons.

</details>

<!--
RAG ΔS CLINIC · GLOBAL DEBUG CARD

OBJECTS
Q = user question
E = top-k retrieved docs (small k, e.g., 3–5), concatenated with a consistent separator
P = final user-side prompt string sent to model (template wrapping Q + E)
A = model answer

EMBEDDING + METRIC
I(X) = embedding of text X from one fixed model checkpoint
cos_sim(u,v) = cosine similarity in [0,1]
ΔS(X,Y) = 1 − cos_sim(I(X), I(Y))        // hence 0 ≤ ΔS ≤ 1

BOUNDARY SCORES
ΔS_QE = ΔS(Q,E)
ΔS_EP = ΔS(E,P)
ΔS_PA = ΔS(P,A)
ΔS_QA = ΔS(Q,A)

ZONES
safe:    0.00 ≤ ΔS < 0.40
transit: 0.40 ≤ ΔS < 0.60
risk:    0.60 ≤ ΔS < 0.85
danger:  0.85 ≤ ΔS ≤ 1.00

zone(ΔS) ∈ {safe, transit, risk, danger}
zone_order: safe < transit < risk < danger
“X is not worse than Y” means zone_order(X) ≤ zone_order(Y).

16 RAG MODES

No lane name                symptom
1  IN  hallucination/drift  E wrong or off-topic
2  RE  misread evidence     E ok, reasoning wrong
3  RE  chain drift          multi-step plan drifts away from Q/E
4  RE  bluff                confident, unsupported
5  IN  embed false pos      sim high, relevance low
6  RE  logic collapse       dead-end, no recovery
7  ST  broken memory        loses story / state
8  IN  no E visibility      cannot inspect E content
9  ST  entropy collapse     long context turns into noise
10 RE  creative freeze      flat, literal, blocked
11 RE  symbol fail          code / math / symbols fail
12 RE  self-loop            recursion or paradox loop
13 ST  agent chaos          agents overwrite or fight
14 OP  bootstrap            called before deps ready
15 OP  deadlock             circular wait
16 OP  bad deploy           wrong version or config

LANES
IN = input / retrieval
RE = reasoning / planning
ST = state / context
OP = infra / deploy

PATTERNS → TYPE → FIX FOCUS

If several types match, prefer I > S > R > P.

Let Z_QE = zone(ΔS_QE), Z_EP = zone(ΔS_EP),
    Z_PA = zone(ΔS_PA), Z_QA = zone(ΔS_QA).

Type R (retrieval)
Cond:
( Z_QE ∈ {risk,danger} and Z_QA ∈ {risk,danger}
  and Z_EP, Z_PA are not worse than Z_QE )
or
( Z_QE = safe and Z_EP ∈ {safe,transit} and Z_QA ∈ {risk,danger} )

Typical modes: {1,5,8}

Type P (prompt / reasoning)
Cond:
Z_QE, Z_EP ∈ {safe,transit} and Z_PA, Z_QA ∈ {risk,danger}

Typical modes: {2,3,4,6,10,11,12}

Type S (state / memory)
Multi-run:
Z_QE stable, Z_QA changes zones.

Single-run heuristic:
matches modes {7,9,13}.

Typical modes: {7,9,13}

Type I (infra)
Cond:
E empty, placeholder, mismatching Q,
or inconsistent/unobservable across runs.

If Type I holds:
ΔS unreliable; treat ΔS_QE as 1.0 by convention.

Typical modes: {14,15,16,8}

LLM TASK

Given Q, E, P, A:

1. Compute or estimate ΔS_QE, ΔS_EP, ΔS_PA, ΔS_QA.
2. Assign zones.
3. Choose type ∈ {R,P,S,I}.
4. Choose 1–3 modes.
5. Propose structural fixes.
6. Define 1 verification test per fix.

REQUIRED OUTPUT

ΔS + zones
type
modes
fixes
tests

github onestardao · WFGY
-->
