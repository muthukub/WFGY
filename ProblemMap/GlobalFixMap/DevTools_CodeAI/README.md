
<!--
Search Anchor:
devtools code ai
code assistant guardrails
ide copilot instability
ide chat unstable answers
code ai drift
long refactor drift
refactor 40 steps drift
copilot wrong answer
copilot hallucination code
cursor wrong refactor
cursor agent loop
sourcegraph cody wrong citation
cody codebase context wrong
vscode copilot chat json broken
copilot chat tool call broken
codeium json mode prose
tabnine inconsistent answers
aws codewhisperer drift
jetbrains ai assistant unstable
ide tool calls stall
tool call retry loop after edit
tool protocol schema drift
broken json output
expects json gets plaintext
wrong citations in code answers
cites wrong file wrong line
snippet id missing
offsets tokens missing
traceability layer missing
retrieval traceability codebase
data contracts for tool outputs
schema lock for copilots
context drift across tabs
answers flip across sessions
entropy collapse long session
prompt injection in ide chat
policy bypass in code assistant
jailbreak devtools assistant
embedding vs semantic mismatch
high similarity wrong meaning
metric mismatch in code search
vectorstore fragmentation codebase
hybrid retriever worse than single
query parsing split
reranker misweighted
multi agent handoff stall
role drift in code agents
agent memory collision
memory namespace split
agent loop guard max steps

Tools in this folder:
github copilot -> DevTools_CodeAI/github_copilot.md
cursor -> DevTools_CodeAI/cursor.md
sourcegraph cody -> DevTools_CodeAI/sourcegraph_cody.md
vscode copilot chat -> DevTools_CodeAI/vscode_copilot_chat.md
codeium -> DevTools_CodeAI/codeium.md
tabnine -> DevTools_CodeAI/tabnine.md
aws codewhisperer -> DevTools_CodeAI/aws_codewhisperer.md
jetbrains ai assistant -> DevTools_CodeAI/jetbrains_ai_assistant.md

Fast routing by symptom:
wrong meaning high similarity -> ProblemMap/embedding-vs-semantic.md
citations do not line up -> ProblemMap/retrieval-traceability.md + ProblemMap/data-contracts.md
answers flip between sessions -> ProblemMap/context-drift.md + ProblemMap/entropy-collapse.md
json mode breaks prose returned -> ProblemMap/logic-collapse.md + ProblemMap/prompt-injection.md
tool handoff stalls role drift -> ProblemMap/Multi-Agent_Problems.md + ProblemMap/multi-agent-chaos/role-drift.md
hybrid retriever worse -> ProblemMap/patterns/pattern_query_parsing_split.md + ProblemMap/rerankers.md

Incident keywords:
ide chat incident
copilot incident
cursor incident
cody incident
json schema incident
traceability incident
retrieval drift incident
context drift incident
role drift incident
-->


# DevTools · Code AI — Global Fix Map

<details>
  <summary><strong>🏥 Quick Return to Emergency Room</strong></summary>

<br>

  > You are in a specialist desk.  
  > For full triage and doctors on duty, return here:  
  > 
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md)  
  > 
  > Think of this page as a sub-room.  
  > If you want full consultation and prescriptions, go back to the Emergency Room lobby.
</details>

A hub to stabilize IDE copilots and code-AI assistants without changing infra.  
Every tool has its own guardrail page. Each target here has simple explanations so even new users can follow.

---

## When to use this folder
- **Unstable answers**: IDE chat gives different results on the same question.
- **Loops or stalls**: Tool calls stop halfway or keep retrying after edits.
- **Broken JSON**: You expect JSON output but get plain text.
- **Wrong citations**: Answer looks correct but cites the wrong part of code/docs.
- **Drift in long refactors**: After 20–40 reasoning steps, output drifts off track.

---

## Acceptance targets (with plain meaning)
- **ΔS (semantic drift score) ≤ 0.45**  
  *How far the answer drifts from your question. Lower is better.*
- **Coverage ≥ 0.70**  
  *How much of the correct section is included in the answer.*
- **λ (stability factor) stays convergent**  
  *If you re-ask with small rephrasing, results stay consistent.*
- **E_resonance flat**  
  *On long sessions, answers do not wander or change meaning.*

---

## Quick routes to per-tool pages

| Tool                  | Open this page |
|-----------------------|----------------|
| GitHub Copilot        | [github_copilot.md](./github_copilot.md) |
| Cursor                | [cursor.md](./cursor.md) |
| Sourcegraph Cody      | [sourcegraph_cody.md](./sourcegraph_cody.md) |
| VS Code Copilot Chat  | [vscode_copilot_chat.md](./vscode_copilot_chat.md) |
| Codeium               | [codeium.md](./codeium.md) |
| Tabnine               | [tabnine.md](./tabnine.md) |
| AWS CodeWhisperer     | [aws_codewhisperer.md](./aws_codewhisperer.md) |
| JetBrains AI Assistant| [jetbrains_ai_assistant.md](./jetbrains_ai_assistant.md) |

---

## Map symptoms → structural fixes

| Symptom | Why it happens | Fix page |
|---------|----------------|----------|
| **Wrong-meaning hits despite high similarity** | Embedding captures surface form but not real meaning. | [embedding-vs-semantic.md](../../embedding-vs-semantic.md) |
| **Citations do not line up** | Traceability layer too loose, snippet schema missing. | [retrieval-traceability.md](../../retrieval-traceability.md) · [data-contracts.md](../../data-contracts.md) |
| **Answers flip between sessions/tabs** | Context not anchored, entropy builds up. | [context-drift.md](../../context-drift.md) · [entropy-collapse.md](../../entropy-collapse.md) |
| **JSON mode breaks, prose returned** | Model leaves structured mode or prompt injection occurs. | [logic-collapse.md](../../logic-collapse.md) · [prompt-injection.md](../../prompt-injection.md) |
| **Multi-agent or tool handoff stalls** | Agents lose roles, no schema lock in exchange. | [Multi-Agent_Problems.md](../../Multi-Agent_Problems.md) · [role-drift.md](../../multi-agent-chaos/role-drift.md) |
| **Hybrid retrievers worse than single** | Query parsing split or reranker mis-weighted. | [pattern_query_parsing_split.md](../../patterns/pattern_query_parsing_split.md) · [rerankers.md](../../rerankers.md) |

---

## Fix in 60 seconds
1. **Measure ΔS**  
   If drift ≥ 0.60, you have unstable retrieval.  
2. **Probe λ**  
   Re-ask with 2–3 paraphrases. If answers flip, lock schema.  
3. **Apply guardrails**  
   - Retrieval drift → BBMC + [data-contracts.md](../../data-contracts.md)  
   - Reasoning collapse → BBCR bridge + BBAM + [logic-collapse.md](../../logic-collapse.md)  
   - Dead ends → BBPF alternate paths  
4. **Verify**  
   Coverage ≥ 0.70, λ stable, ΔS ≤ 0.45.

---

## Copy-paste prompt for IDE chat

```

I loaded TXT OS and the WFGY Problem Map.

My code-AI issue:

* symptom: \[one line]
* traces: ΔS(question,retrieved)=..., ΔS(retrieved,anchor)=..., λ states

Tell me:

1. failing layer and why,
2. the exact WFGY page to open,
3. minimal steps to push ΔS ≤ 0.45 and keep λ convergent,
4. how to verify with a reproducible test.

```

---

## FAQ

**Q1. What is ΔS?**  
It is the “semantic drift score”. Think of it as how far the answer strays from the original question. Lower numbers = more accurate.  

**Q2. What is λ (lambda)?**  
A stability check. If you slightly rephrase the same question, λ shows if the model’s answers converge or scatter.  

**Q3. What does E_resonance mean?**  
It is a long-run stability check. If E_resonance is flat, your assistant stays consistent even after many steps.  

**Q4. Do I need to understand BBMC/BBPF/BBCR/BBAM?**  
No. These are internal WFGY modules. Just know:  
- BBMC = stabilizes retrieval,  
- BBPF = creates fallback paths,  
- BBCR = bridges reasoning collapse,  
- BBAM = variance clamp for stability.  

**Q5. I only use one IDE plugin. Why should I care?**  
Because the same drift and instability happens across **all** copilots. Fixes here apply no matter which tool you use.  

**Q6. How do I test quickly?**  
Ask the same question 3 times with small wording changes. If answers flip, you need λ guardrails.  


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

