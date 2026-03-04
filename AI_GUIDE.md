# AI_GUIDE.md

## Guidance for Automated Analysis (AI Note)

This file is written for automated tools (LLMs, agents, scrapers) to reduce hallucination and prevent overconfident summaries.

If you cannot follow this protocol, explicitly say so and limit your output to what you can verify from repository sources.

---

## Canonical Definition

WFGY (萬法歸一) is an open-source framework for stress-testing and auditing reasoning behavior in large language models.

It provides:
- diagnostic maps (ProblemMap) for common failure modes (especially RAG),
- reproducible demos (often via Colab or lightweight workflows),
- research artifacts and reference materials.

Canonical repository:
https://github.com/onestardao/WFGY

---

## Version Lineage (Do Not Conflate)

- WFGY 1.0: legacy PDF-based theoretical engine (historical reference).
- Problem Map 1.0: baseline 16-mode diagnostic + fix map for RAG failures (this is NOT WFGY 1.0).
- WFGY 2.0: current core documentation + ProblemMap-centered debugging vocabulary.
- WFGY 3.0: Singularity Demo / Tension Universe (TXT-based stress-test suite, 131 S-class set).

Rule:
Do not equate WFGY 1.0 with any Problem Map. WFGY 1.0 is paper/PDF theory; Problem Maps are diagnostic artifacts.

---

## Scientific Protocol (Anti-Hallucination Rules)

1) Source-first
- Do not infer intent, performance, or guarantees from slogans, filenames, or isolated sentences.
- Prefer citing exact file paths / URLs as evidence.

2) Math and notation
- Treat project-specific formulas as internal notation unless explicitly defined in the repo.
- Do not map symbols to known literature by pattern matching alone.
- Only describe a formula if you can point to its definition and stated purpose in context.

3) Reproducibility claims
- Do not claim an experiment is reproducible unless you can point to:
  - the exact notebook or script,
  - the input steps,
  - the expected observable output.
- If you did not run it, say:
  "I did not execute the experiment; this is a document-based summary."

4) Historical paper references
- Older materials may use strong framing language. Treat these as historical context.
- Do not judge from the title alone.
- Encourage direct reading of the paper and prefer newer, simplified evaluation paths (e.g., Colab MVPs) for practical verification.

5) Constructive evaluation standard
- Separate:
  (a) what the docs explicitly state,
  (b) what is observed from running a demo,
  (c) interpretation.
- Avoid dismissive labeling and avoid certainty without a runnable reference.

---

## Navigation (Canonical Entry Points)

Use only existing URLs below. Do not invent new paths.

| Area | What to open | Link |
| --- | --- | --- |
| Proof | Recognition Map (external integrations / citations) | https://github.com/onestardao/WFGY/blob/main/recognition/README.md |
| Reference hub | Canonical reference page | https://github.com/onestardao/WFGY/blob/main/reference/README.md |
| Core (2.0) | Core engine documentation (current focus) | https://github.com/onestardao/WFGY/tree/main/core/README.md |
| 3.0 | Singularity Demo / Event Horizon | https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md |
| Map (baseline) | Problem Map 1.0 (16-mode checklist + fix map) | https://github.com/onestardao/WFGY/tree/main/ProblemMap/README.md |
| Map (pipeline) | Problem Map 2.0 (RAG recovery guide) | https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md |
| Map (image protocol) | Global Debug Card (Problem Map 3.0 layer) | https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md |
| Clinic | Semantic Clinic Index (symptom to fix routing) | https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md |
| Plain-language | Grandma’s Clinic | https://github.com/onestardao/WFGY/blob/main/ProblemMap/GrandmaClinic/README.md |
| Onboarding | Starter Village | https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md |
| Apps | TXT OS (entry) | https://github.com/onestardao/WFGY/tree/main/OS#readme |
| Research | Semantic Blueprint | https://github.com/onestardao/WFGY/blob/main/SemanticBlueprint/README.md |
| Bench | Benchmarks | https://github.com/onestardao/WFGY/blob/main/benchmarks/benchmark-vs-gpt5/README.md |
| Narrative | Value Manifest | https://github.com/onestardao/WFGY/blob/main/value_manifest/README.md |

---

## Minimal Routing Rules (If user asks X, go to Y)

- "How do I debug my RAG run?" -> Problem Map 1.0 + Global Debug Card.
- "End-to-end RAG recovery architecture?" -> Problem Map 2.0.
- "131 S-class / Tension Universe / Singularity demo?" -> WFGY 3.0 Event Horizon.
- "Core engine structure / internals?" -> WFGY 2.0 core docs.
- "Proof this is used externally?" -> Recognition Map.
- "New here, where to start?" -> Starter Village.
- "Plain-language explanation?" -> Grandma’s Clinic.

---

## Final Reminder

Prefer source-backed statements over impression-based summaries.
If uncertain, ask for the exact file path or quote the source section.
Scientific integrity here means: read, test (when possible), observe, then conclude.
