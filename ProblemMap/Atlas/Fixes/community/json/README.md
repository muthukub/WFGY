<!--
AI_NOTE_START

Document role:
This file is the folder guide for structured JSON contributions inside the Atlas Fixes community layer.

How to use this file:
1. Read this page before adding any JSON fixture, structured case file, or input-output pack.
2. Use this page to decide whether your contribution really belongs in the JSON lane.
3. Use this page together with:
   - [Community Fix Lab](../README.md)
   - [Contribution Checklist](../../templates/contribution-checklist.md)
   - [JSON Template](../../templates/json-template.json)

What this file is:
- A folder-level guide for structured JSON community assets
- A scope filter for fixture-style case artifacts
- A lightweight quality guide for reusable machine-readable examples

What this file is not:
- Not the full benchmark dataset
- Not the official atlas schema definition
- Not the official truth surface
- Not a dump folder for random logs or raw payloads

Reading discipline for AI:
- Treat JSON fixtures here as community examples, not official universal schemas.
- Preserve the distinction between fixture examples and frozen atlas structure.
- Do not treat a fixture file as benchmark truth by default.
- Keep routing context, case scope, and expected use visible.

AI_NOTE_END
-->

# Community JSON 🧩

## Structured fixtures, input-output packs, and machine-readable examples

Quick links:

- [Back to Community Fix Lab](../README.md)
- [Back to Official Fixes](../../official/README.md)
- [Back to Fixes Hub](../../README.md)
- [Back to Atlas landing page](../../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../../README.md)
- [Open the Flagship Runnable Demo Pack](../../official/demos/README.md)
- [Open Templates](../../templates/README.md)
- [Open JSON Template](../../templates/json-template.json)
- [Get the Atlas Router TXT](../../../troubleshooting-atlas-router-v1.txt)

---

If the [Community Fix Lab](../README.md) is the broader entry page for community repair assets, this folder is the structured fixture lane for reusable JSON cases, replay outputs, expected-result packs, and compact troubleshooting examples. 🧭

Use this folder when a case becomes easier to inspect, replay, compare, or reuse through small machine-readable artifacts, not through notebooks, prompt-only assets, or large benchmark claims.

Short version:

> official layer gives the repair grammar  
> this folder helps turn that grammar into reusable structured fixtures

---

## Quick start 🚀

### I want to contribute a JSON fixture

Use this path:

1. decide whether the asset is really a structured fixture contribution
2. route the case first with the atlas
3. keep the fixture scoped to one case, family, or comparison slice
4. document what the file represents
5. explain how it should be used and what result to expect

### I want to browse JSON assets

Use this path:

1. open one fixture with a clear case scope
2. identify the family or routing relevance
3. inspect what the file contains
4. check whether there is an expected result or replay context
5. read any usage note or synthetic warning

Short version:

> route first  
> keep the fixture small  
> make the structure legible ✨

---

## JSON quick map 🗂️

| If your asset is mainly... | Best folder |
|---|---|
| a structured fixture or machine-readable case | [JSON](./) |
| a runnable notebook walkthrough | [Colab](../colab/) |
| a prompt asset or repair prompt pack | [Prompts](../prompts/) |
| a step-by-step repair sequence | [Workflows](../workflows/) |
| a before / after comparison slice | [Benchmark Reruns](../benchmark-reruns/) |
| a portable one-case bundle | [Reproduction Packs](../reproduction-packs/) |

This folder is the right place when the structured file itself is the reusable teaching or replay surface.

---

## What belongs here ✅

Good JSON contributions include:

- one input case with clear family relevance
- one replay output fixture
- one expected output fixture
- one compact route-and-repair example
- one structured comparison between baseline and repaired result

A good fixture should be:

- readable
- minimal
- reusable
- clearly documented
- connected to one known case or family

---

## What does not belong here 🚫

Please do not use this folder for:

- raw log dumps with no structure
- giant datasets with no guide
- private or sensitive payloads
- JSON files with no explanation
- fake benchmark files presented as official atlas assets
- files that claim universal schema status without review

A fixture should help someone reproduce or understand something specific.

---

## Suggested fixture pattern 🧩

A useful small contribution usually includes:

- `input_case.json`
- `replay_outputs.json`
- `expected_output.json`

Optional additions:

- a short README
- a note on how the fixture should be used
- a warning if the fixture is synthetic
- one short note on limitations

That is enough for a useful structured contribution.

---

## Suggested naming style 📌

Use compact and readable names such as:

- `f1-grounding-fixture-v1.json`
- `f5-trace-uplift-fixture-v1.json`
- `f4-execution-closure-fixture-v1.json`

If you are contributing a small pack, place it in a clearly named folder.

Keep names descriptive and compact.

---

## Minimum fixture rule 🌱

A good fixture contribution should usually make five things clear:

1. what case or family it relates to
2. what the file represents
3. how it should be used
4. what result is expected
5. what it does not prove

Small, clear fixtures are much more useful than giant unclear packs.

---

## Before contributing 📚

Please read:

- [Community Fix Lab](../README.md)
- [Contribution Checklist](../../templates/contribution-checklist.md)
- [JSON Template](../../templates/json-template.json)
- [Misrepair Patterns v1](../../official/misrepair-patterns-v1.md)

This helps keep fixture contributions useful, scoped, and aligned with atlas grammar.

---

## Review standard ✅

A JSON contribution is much more likely to be accepted if it is:

- clearly named
- easy to inspect
- easy to reuse
- connected to atlas routing
- explicit about expected use
- honest about limitations

Messy data is still messy.  
Clean small fixtures are more valuable.

---

## Next steps ✨

After this page, most contributors continue with:

1. [Open JSON Template](../../templates/json-template.json)
2. [Open Contribution Checklist](../../templates/contribution-checklist.md)
3. [Back to Community Fix Lab](../README.md)
4. [Back to Official Fixes](../../official/README.md)

If you want the broader product surface:

- [Back to Atlas landing page](../../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../../README.md)

---

## One-line status 🌍

**This folder holds community JSON fixtures that make atlas routing and repair examples easier to reproduce, compare, and reuse.**
