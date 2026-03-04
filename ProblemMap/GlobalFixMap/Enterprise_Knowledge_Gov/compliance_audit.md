# Compliance Audit — Enterprise Knowledge Governance

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Enterprise_Knowledge_Gov**.  
  > To reorient, go back here:  
  >
  > - [**Enterprise_Knowledge_Gov** — corporate knowledge management and governance](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Guardrails and patterns to enforce **compliance-ready audits** in AI pipelines.  
Use this page when enterprise policies or regulators require **auditability, traceability, and repeatable evidence** for AI knowledge usage.

---

## When to use this page
- Internal or external auditors require proof of AI outputs.  
- You need to show exactly which documents were cited and how they were retrieved.  
- Enterprise standards mandate **compliance trails** (ISO, SOC2, GDPR, HIPAA, etc).  
- Users ask "why did the model say this?" and you must replay the answer deterministically.  

---

## Core acceptance targets
- Every AI output must be linked to **retrieval evidence** (doc_id, section_id, offsets).  
- **ΔS(question,retrieved)** logged per query, with thresholds verified.  
- **λ_observe** states stored for all runs (paraphrase, rerun, seeds).  
- Full **audit trail exportable** (JSON, CSV, signed logs).  

---

## Typical audit failures → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| Missing or inconsistent citations | No schema enforcement on retrieval | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| Evidence cannot be reproduced | No deterministic ΔS/λ logs | [retrieval-playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md) |
| Multiple outputs differ for same input | λ flips or entropy collapse | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md), [entropy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md) |
| No visibility into expired docs | Missing expiry field in audit logs | [knowledge_expiry.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Enterprise_Knowledge_Gov/knowledge_expiry.md) |
| Incomplete audit trails | Storage not aligned to contracts | [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |

---

## Fix in 60 seconds
1. **Enforce snippet schema**:  
   Each retrieval must return `doc_id`, `section_id`, `offsets`, `tokens`, `expiry_date`.  

2. **Log ΔS and λ** per step:  
   Store values for retrieval, assembly, reasoning.  

3. **Export audit logs**:  
   JSON or CSV export at end of run.  
   Example:  
   ```json
   {
     "question": "What is policy X?",
     "ΔS": 0.38,
     "λ": "→",
     "citations": ["doc123#section5"],
     "timestamp": "2025-08-28T12:34:00Z"
   }
````

4. **Replay capability**:
   Store retriever seed + config for deterministic reruns.

---

## Copy-paste compliance probe

```txt
You have TXTOS and WFGY Problem Map loaded.

My compliance audit requirement:
- Audit log must contain {ΔS, λ_state, citations, expiry_flag}
- Logs must be exportable to JSON/CSV

Task:
1. Verify schema presence in retrieval.
2. Re-run with same seed and compare logs.
3. If mismatch, cite the exact WFGY page that explains the fix.
```

---

## Escalate when

* Audit log missing ΔS or λ.
* Same seed replay yields different citations.
* Expired documents appear in logs as valid.

Escalation fix: apply [ops/debug\_playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md) and [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md) to enforce deterministic ordering.

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

要繼續幫你生嗎？
