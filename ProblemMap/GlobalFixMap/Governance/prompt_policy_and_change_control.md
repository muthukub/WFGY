# Prompt Policy and Change Control — Guardrails and Fix Patterns

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Governance**.  
  > To reorient, go back here:  
  >
  > - [**Governance** — policy enforcement and compliance controls](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


A governance fix page for **prompt stability, approval flows, and change control**.  
Use this page when uncontrolled prompt edits, hidden overrides, or missing approval gates destabilize your RAG or reasoning pipeline.

---

## When to use this page
- Prompts are edited directly in production without sign-off.  
- Fine-tuned prompts drift from documented baseline.  
- Multi-agent pipelines apply different prompt rules with no central approval.  
- No version history or rollback path exists for prompt changes.  
- Waivers for unsafe prompt edits lack expiry or owner.  

---

## Acceptance targets
- **Prompt policy coverage ≥ 0.95** across live agents, RAG steps, and evaluation sets.  
- **ΔS(question, retrieved) ≤ 0.45** after prompt edits (no semantic drift).  
- **λ_observe remains convergent** across 3 paraphrases and 2 seeds.  
- Each prompt edit has **recorded owner, approval, and expiry date**.  
- Version rollback possible in under 60 seconds.  

---

## Typical breakpoints and WFGY fix

- **Live edits destabilize outputs**  
  → [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
  Require citation schema and provenance anchors before prompt rollout.

- **Hidden prompt injection bypasses control**  
  → [prompt-injection.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)  
  Enforce structural schema locks to prevent drift into unsafe states.

- **Baseline prompts vanish after fine-tuning**  
  → [policy_baseline.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Governance/policy_baseline.md)  
  Require reference to immutable baseline for audit and rollback.

- **Conflicts between agents** (different policies in orchestration)  
  → [Multi-Agent Problems](https://github.com/onestardao/WFGY/blob/main/ProblemMap/Multi-Agent_Problems.md)  
  Use role namespaces and explicit prompt slots to enforce alignment.

- **No audit trail for prompt changes**  
  → [audit_and_logging.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Governance/audit_and_logging.md)  
  Require immutable logging of who changed what, when, and why.

---

## Minimal governance checklist
1. **Immutable baselines** — Store canonical prompt versions in a controlled repo.  
2. **Approval required** — Every change must be signed off before rollout.  
3. **Waivers expire** — Unsafe or experimental prompts must auto-expire.  
4. **Rollback path** — 1-click restore of previous prompt version.  
5. **Drift checks** — Run ΔS/λ probes after every edit; block rollout if drift > 0.45.  
6. **Audit logs** — Immutable records joinable to governance lineage.  

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

