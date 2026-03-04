# Roles and Access (RBAC / ABAC) — Guardrails and Fix Pattern

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


This page defines **role-based access control (RBAC)** and **attribute-based access control (ABAC)** guardrails for AI pipelines.  
Without explicit access boundaries, LLMs may read from unintended sources, leak sensitive data, or bypass audit policy.

---

## When to use this page
- Your RAG or agent stack integrates multiple data stores with different sensitivity levels.  
- You cannot trace **who accessed what** across prompts, embeddings, or tool calls.  
- Evaluation runs fail because different users see different knowledge bases.  
- Compliance requires proof of **least privilege** but no policy schema exists.  

---

## Acceptance targets
- 100% of RAG data calls tagged with `role` or `attribute` context.  
- Coverage ≥ 0.95 of sensitive datasets behind access boundaries.  
- Audit trails record `who`, `what`, `when`, `ΔS`, `λ_state`.  
- Role drift probes show λ remains convergent across 3 paraphrases.  
- Exceptions logged with owner and expiry date.  

---

## Common failures → exact fixes

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| Agents fetch data beyond allowed scope | missing RBAC fences | [policy_baseline.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Governance/policy_baseline.md) |
| Two users get different citations | inconsistent ABAC checks | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| Logs don’t show who triggered retrieval | no role injection | [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| Role drift causes schema injection | misplaced role attributes | [prompt-injection.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md) |
| Sensitive snippets leak in chains | missing attribute check | [pii_handling_and_minimization.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Governance/pii_handling_and_minimization.md) |

---

## Fix in 60 seconds

1. **Attach context**  
   Every retrieval call carries `{role, attribute_set, index_hash, ΔS, λ_state}`.  

2. **Enforce least privilege**  
   Roles map to dataset groups. Attributes refine down (e.g. geography, project).  

3. **Log every decision**  
   Audit trail logs query, ΔS, λ state, role, attributes, and snippet ids.  

4. **Probe role drift**  
   Run 3 paraphrases per role. If λ flips, enforce schema lock.  

---

## Minimal copy-paste checklist

- [ ] Define roles (admin, annotator, auditor, agent).  
- [ ] Define attributes (region, dataset sensitivity, project scope).  
- [ ] Attach `{role, attr}` to all tool and retrieval calls.  
- [ ] Enforce least privilege at ingestion and retrieval.  
- [ ] Log ΔS and λ_state by role.  
- [ ] Review and expire waivers.  

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

要我直接繼續幫你生出來嗎？
