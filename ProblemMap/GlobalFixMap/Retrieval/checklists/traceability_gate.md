# Traceability Gate Checklist

Purpose: enforce cite then explain with a minimal, verifiable payload contract.

---

## Required fields per snippet

- [ ] `snippet_id` unique within the corpus
- [ ] `section_id` stable anchor for the document
- [ ] `source_url` resolvable or a content hash if private
- [ ] `offsets` byte or char range within the source
- [ ] `tokens` token range used by the model

Contract details:  
[Retrieval traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) ·
[Data contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

---

## Schema example

```json
{
  "snippet_id": "sn_9f3a",
  "section_id": "sec_2.3_hydraulics",
  "source_url": "https://example.org/handbook/2024/chap2#sec-3",
  "offsets": {"start": 18342, "end": 18897},
  "tokens": {"start": 1205, "end": 1248}
}
````

---

## Gate checks

* [ ] Each answer references at least one snippet with all required fields.
* [ ] Offsets resolve back to exactly the cited text.
* [ ] Section anchors stable across builds. Hash or ID diff is logged.
* [ ] Duplicate or near duplicate snippets collapsed before ranking.
* [ ] Formatter and export steps do not rename required fields.
* [ ] On failure, publish is blocked and the pipeline returns a structured error.

Refs:
[Duplication and near duplicate collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/RAG_VectorDB/duplication_and_near_duplicate_collapse.md)

---

## Acceptance targets

* 100 percent of published answers pass the schema check.
* For the gold set, human spot check of 20 answers finds zero broken citations.
* ΔS(question, cited\_snippet) ≤ 0.45 on average.

---

## Minimal policy snippet

```txt
Policy:
- Answer only after citing snippets with {snippet_id, section_id, source_url, offsets, tokens}.
- If no snippet qualifies, return "insufficient evidence" with the top 3 candidate snippets and exit.
```



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

