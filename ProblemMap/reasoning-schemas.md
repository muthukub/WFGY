# 🗂️ Reasoning Schemas — Designing Prompt Layouts That Survive Long Chains  
_A practical guide to structuring system + retrieval + task prompts so LLMs keep thinking instead of drifting_

---

## 1  What is a “Reasoning Schema” ?

A **reasoning schema** is the formal layout that dictates **where** each piece of context goes and **how** an LLM must traverse it:

```

System  →  Task  →  Constraints  →  Context  →  Question  →  Answer

````

If any segment is missing, reordered, or over-written, the logic graph collapses and hallucinations slip in.

---

## 2  Why Most Ad-hoc Layouts Fail

| Failure Mode | Trigger | Effect |
|--------------|---------|--------|
| **Context Flood** | Dumping 20 k tokens of raw text | λ_observe flips to chaotic; model stops planning |
| **Constraint Drift** | Constraints after context | Model “forgets” to cite or guard sensitive data |
| **Role Blending** | User text inserted before task | System tone and policy overridden |
| **Evidence → Answer inversion** | Asking for answer *before* citations | Model fabricates then cites random lines |

---

## 3  WFGY Canonical Schema (Stable Version v1.2)

| Segment | Purpose | Size (tokens) | WFGY Guard |
|---------|---------|---------------|------------|
| **System** | Identity, ethics, safety | ≤ 50 | Role tag `<sys>` + BBAM weight lock |
| **Task** | Specific action required | 1 sentence | ΔS anchor to System ≤ 0.25 |
| **Constraints** | Format, style, rules | bullets ≤ 80 | BBMC residue check |
| **Context** | Retrieved or uploaded text | sliding window ≤ 2 k | λ_observe must stay convergent |
| **Question** | User’s query | raw | stored separately for ΔS probes |
| **Answer Slot** | “Write here” placeholder | n/a | BBCR collapse-rebirth if answer starts early |

Placeholders are literal; the LLM fills only the *Answer Slot*.

---

## 4  Templates You Can Copy

<details><summary><strong>Single-Shot QA</strong></summary>

```text
<sys>
You are DataGuardian-L, a licensed legal research assistant. Cite section numbers.
</sys>

<task>
Answer strictly in bullet points; cite every claim.
</task>

<constraints>
- Tone: formal
- No speculation
- Use original terminology
</constraints>

<context>
{retrieved_sections}
</context>

<question>
{user_question}
</question>

<answer>
````

</details>

<details><summary><strong>Multi-Step Chain (analysis → plan → answer)</strong></summary>

```text
<sys> … </sys>
<task> … </task>
<constraints> … </constraints>
<context> … </context>
<question> … </question>

<scratchpad>
Think step-by-step. Output JSON:
{
  "analysis": "...",
  "plan": "...",
  "answer": "..."
}
</scratchpad>
```

</details>

---

## 5  Common Pitfalls & Fixes

| Pitfall                                 | Symptom              | Fix                                                     |
| --------------------------------------- | -------------------- | ------------------------------------------------------- |
| Forgetting closing tags                 | Model merges roles   | Validate tag balance; λ diverges instantly              |
| Placing context after question          | Retrieval ignored    | Keep schema order; run ΔS(question, context) test       |
| Over-long constraints                   | Answer truncated     | Compress with BBMC until ΔS(system, constraints) ≤ 0.25 |
| Mixing code + docs in one context block | Embedding collisions | Split into typed sub-blocks; separate vector stores     |

---

## 6  Automated Validation Pipeline

1. **Schema Linter** – Regex check for tag order.
2. **ΔS Probes** –

   * ΔS(system, task) ≤ 0.30
   * ΔS(task, answer) ≤ 0.45
3. **λ\_observe** – Must stay convergent from task → answer.
4. **Round-trip Check** – Paraphrase user question 2×; answer variance < 0.15.

If any test fails, trigger **BBCR** to rebuild prompt with compacted segments.

---

## 7  FAQ

**Q:** *Do I need tags if I use OpenAI’s `messages` array?*
**A:** Yes for long chains. Tags persist after retrieval merges; arrays don’t survive copy-paste workflows.

**Q:** *Can I merge Task + Constraints?*
**A:** Possible if total ≤ 120 tokens and ΔS stays low, but separation improves editability.

**Q:** *What about JSON-only prompts?*
**A:** Ensure keys mirror schema order; add dummy key `"__guard": "DO NOT MODIFY"` to catch injections.

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

