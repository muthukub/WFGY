# PII Handling and Minimization — Guardrails and Fix Patterns

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


A governance fix page for when **personally identifiable information (PII)** leaks, handling is unclear, or minimization principles are violated.  
Use this page when data pipelines, embeddings, or RAG outputs contain sensitive fields that cannot be justified or audited.

---

## When to use this page
- Retrieval responses contain raw PII that was not required for the task.  
- Embeddings or chunks accidentally ingest names, emails, IDs, or financial data.  
- Redaction or anonymization rules are inconsistently applied.  
- No audit trail exists for who accessed or approved PII exposure.  
- Waivers for PII usage lack expiry, owner, or justification.  

---

## Acceptance targets
- PII fields are **redacted, hashed, or minimized** in ≥ 0.98 of stored embeddings.  
- Retrieval outputs contain no raw identifiers unless explicitly approved.  
- ΔS(question, retrieved) ≤ 0.45 for governed answers (no drift into unapproved fields).  
- All PII queries pass through policy checks with logging enabled.  
- Every waiver or override has an accountable owner and time-bound expiry.  

---

## Typical breakpoints and WFGY fix

- **Embedding or vector ingestion leaks PII**  
  → [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)  
  Enforce PII scrub before embedding. Validate with spot-checks against gold set.

- **Chunking preserves identifiers across splits**  
  → [chunking-checklist.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/chunking-checklist.md)  
  Require token-level scrub of identifiers, then re-chunk.

- **Answers expose sensitive spans without approval**  
  → [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
  Enforce citation schema, ensure only approved snippets are surfaced.

- **Policy bypass in orchestration or tools**  
  → [prompt-injection.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/prompt-injection.md)  
  Guard against malicious queries that try to extract hidden PII.

- **Audit trail gaps**  
  → [audit_and_logging.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Governance/audit_and_logging.md)  
  Require immutable logs of every PII access and minimization check.

---

## Minimal governance checklist
1. **Redact on ingest** — Apply regex/sensitive data detection before storing text or embeddings.  
2. **Schema enforce** — Store `doc_id`, `pii_flag`, `redacted_text` side by side for traceability.  
3. **Chunk validation** — Randomly sample and confirm PII scrubbed before index build.  
4. **Policy in LLM prompts** — Require “no PII unless approved waiver” as hard guardrail.  
5. **Audit logs** — Track every waiver, approval, and override. Immutable and joinable to lineage.  
6. **Expiry enforcement** — Waivers expire automatically; extension requires re-approval.  

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

