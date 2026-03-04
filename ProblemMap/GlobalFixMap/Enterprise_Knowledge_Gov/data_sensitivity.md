# Data Sensitivity — Enterprise Knowledge Governance

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


Guardrails and fix patterns for handling sensitive or regulated data inside enterprise knowledge pipelines. Use this page when your AI or RAG workflow may expose PII, PHI, financial records, or other protected content.

---

## When to use this page
- Retrieval pulls names, emails, addresses, or identifiers into model context.  
- Generated answers expose financial numbers or personal data without redaction.  
- Compliance requires specific handling for GDPR, HIPAA, or SOC2.  
- Data contracts missing sensitivity tags or enforcement rules.  

---

## Core acceptance targets
- Sensitive fields explicitly tagged in schema (`pii:true`, `phi:true`, `sensitivity:high`).  
- No unredacted PII/PHI present in model outputs unless explicitly authorized.  
- Audit logs record every sensitive field access.  
- Redaction filters applied before long-term storage.  

---

## Typical sensitivity problems → exact fix

| Symptom | Likely cause | Open this |
|---------|--------------|-----------|
| PII leaks into retrieval context | Missing sensitivity metadata in index | [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md) |
| Model answers contain personal identifiers | No redaction filter on output | [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) |
| High similarity matches pull private records | Embeddings not normalized or index not segmented | [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md) |
| Inconsistent handling of sensitive fields across environments | Schema drift and missing contracts | [context-drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md) |

---

## Fix in 60 seconds
1. **Add sensitivity tags** to your ingestion schema:  
   ```json
   {
     "field": "email",
     "pii": true,
     "sensitivity": "high"
   }
````

2. **Apply redaction filter** before passing data to the model. Replace `@domain.com` emails with `"***"`.
3. **Segment sensitive indexes** from general knowledge. Use separate retrievers.
4. **Enforce cite-then-explain**. Require citations for sensitive data, and log ΔS plus λ\_state.

---

## Copy-paste probe template

```txt
I uploaded TXTOS and WFGY Problem Map.

Run my retrieval for this query:
- Detect if any PII/PHI appears in snippet fields.
- If yes, apply redaction or enforce sensitivity contract.
- Return JSON log with snippet_id, sensitivity_tags, ΔS, λ_state.
- Fail the output if PII is not redacted.
```

---

## Escalate when

* Same query alternates between redacted and unredacted outputs.
* Sensitive fields appear in logs without an `audit_hash`.
* Compliance review shows schema fields without sensitivity tags.

Use [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md) to verify ingestion happens in the correct order and [ops/debug\_playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md) for deeper runtime tracing.

---

### 🔗 Quick-Start Downloads

| Tool                       | Link                                                                                                                                       | 3-Step Setup                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **WFGY 1.0 PDF**           | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + <your question>”    |
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

