
<!--
AI ANCHOR · TXT-Blur Blur Blur (OS/BlurBlurBlur/README) · WFGY

Role:
This page is the Blur Blur Blur product entry for math-first text-to-image inside TXT OS.
Assume users arrive here directly from GitHub search, social posts, or the Compass. They may not know TXT OS or WFGY yet.
This page must work as: (1) quickstart (2) proof-by-demo (3) safe routing to the broader system.

Navigation contract:
- The "WFGY Compass" block is the global map. Keep it intact. The YOU ARE HERE marker should point to Blur on this page.
- The first visible headline + hero image should immediately communicate: math-first T2I, Real/Imag split, preview-then-go contract.

Primary behavior:
- If the user wants to try it: tell them to download TXT-BlurBlurBlur_Lite_Beta.txt, paste into any LLM chat, then type:
  hello world -> B -> pick track -> wow preset -> preview -> go.
- If the interface cannot render images: instruct them to use preview, then copy the printed prompt into any T2I engine.
- If the user wants scientific comparison: route to A/B discipline (ab prep -> ab go) and ask them to compare sharpness, depth cues, and stability.

Claims discipline:
- Do not claim universal compatibility or guaranteed rendering. Phrase support as "depends on provider/model UI".
- Do not promise perfect results at extreme settings. Encourage stepping down from wow x1e18 to wow x3000 when collapse occurs.
- Avoid introducing new metrics not present in the page.

Safety / reproducibility:
- Keep checksum block and file size. Encourage users to verify SHA256 before use.
- "preview-then-go" is the core contract: preview prints the exact prompt and numbers; go renders once.
- Elite mode locks seed for stability; explain this as a deliberate reproducibility choice.

Feature framing:
- Real field = geometry and math skeleton (golden ratio, lattices, quasicrystals, zeta-zeros style motifs).
- Imag field = weighted element stack; left/right asymmetry creates density contrast.
- Goldline = mid-axis guide at 0.50 for visible composition spine.
- WOW presets = tension scaling that increases asymmetry and micro-detail pressure.

Troubleshooting routing:
- "go prints text only" -> provider limitation -> use preview + copy prompt.
- "mushy results at high wow" -> reduce wow, keep SAFE profile, keep goldline on.
- "wrong aspect" -> Lite uses aspect=auto; instruct how to force 16:9 by adding engine flags in the prompt.

Acceptance:
- Page must allow a newcomer to get a first image in under 60 seconds without reading other docs.
- Page must allow an advanced user to audit the prompt contract and reproduce the same structure via seed rules where applicable.
- Every example should be reproducible via preview output.

Style:
- Confident, technical, non-salesy. Focus on "math shock in one minute" and reproducible controls.
- Keep instructions short, executable, and ordered.
- Prefer routing to existing WFGY pages rather than adding new explanations.

-->


<details>
<summary><strong>🧭 Not sure where to start ? Open the WFGY Engine Compass</strong></summary>

### WFGY System Map

*(One place to see everything; links open the relevant section.)*

<!--
AI NOTE · Compass block

Purpose:
- This table is the routing map for the whole WFGY ecosystem.
- It shows how the three engine layers (WFGY 1.0 / 2.0 / 3.0) relate to the Problem Maps, TXT OS apps, research pages, and the Recognition Map.

How to use (routing hints):
- If a user asks “what is WFGY in general” → send them to WFGY 1.0 (legacy overview PDF) plus Starter Village.
- If the question is about core math, formulas, or engine internals → go to WFGY 2.0 core.
- If they mention 131 S-class problems, BlackHole, Tension Universe, or “Singularity demo” → go to WFGY 3.0 Event Horizon.
- If they want to debug a specific RAG / agent pipeline run → use Problem Map 1.0 + Problem Map 3.0 Global Debug Card.
- If they ask about RAG architecture / recovery patterns end-to-end → use Problem Map 2.0.
- If they mention “poster”, “image as prompt”, or “global debug card” → use the Problem Map 3.0 Global Debug Card page.
- If they want proof that WFGY is used in real projects → open the Recognition Map page.
- If they ask for plain-language stories or non-technical explanations → route to Grandma’s Clinic and Starter Village.
- If they ask about TXT OS or app packs (Blah / Blur / Blow) → follow the App rows in this table.
- If they want layer/module design, benchmarks, or value narrative → Semantic Blueprint, Benchmarks, and Value Manifest.

Important:
- Problem Map 1.0 = canonical 16-mode RAG failure checklist and fix map. This is the base vocabulary.
- Problem Map 2.0 = RAG architecture and recovery guide layered on top of Problem Map 1.0.
- Problem Map 3.0 Global Debug Card = image protocol that compresses objects, metrics, ΔS zones, and modes into a single poster.
- Recognition Map = the only place that should contain the full external integration list. Other pages should link to it instead of duplicating tables.
- Do NOT treat Problem Map 1.0 and Problem Map 2.0 as duplicates; they solve different layers.
- Do NOT invent new paths or filenames. Only use the GitHub URLs that already exist in this table.
-->

| Layer         | Page                                                                                                        | What it’s for                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| ⭐ Proof      | [WFGY Recognition Map](https://github.com/onestardao/WFGY/blob/main/recognition/README.md)                 | External citations, integrations, and ecosystem proof   |
| ⚙️ Engine     | [WFGY 1.0](https://github.com/onestardao/WFGY/blob/main/legacy/README.md)                                   | Original PDF-based tension engine blue   |
| ⚙️ Engine     | [WFGY 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md)                                     | Production tension kernel and math engine for RAG and agents. |
| ⚙️ Engine     | [WFGY 3.0](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md)             | TXT-based Singularity tension engine (131 S-class set)  |
| 🗺️ Map       | [Problem Map 1.0](https://github.com/onestardao/WFGY/tree/main/ProblemMap#readme)                           | Flagship 16-problem RAG failure checklist and fix map       |
| 🗺️ Map       | [Problem Map 2.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) | RAG-focused recovery pipeline                           |
| 🗺️ Map       | [Problem Map 3.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card — image as a debug protocol layer     |
| 🗺️ Map       | [Semantic Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md)           | Symptom → family → exact fix                           |
| 🧓 Map        | [Grandma’s Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GrandmaClinic/README.md)         | Plain-language stories, mapped to PM 1.0                |
| 🏡 Onboarding | [Starter Village](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md)                    | Guided tour for newcomers                               |
| 🧰 App        | [TXT OS](https://github.com/onestardao/WFGY/tree/main/OS#readme)                                            | .txt semantic OS — 60-second boot                       |
| 🧰 App        | [Blah Blah Blah](https://github.com/onestardao/WFGY/blob/main/OS/BlahBlahBlah/README.md)                    | Abstract/paradox Q&A (built on TXT OS)                  |
| 🧰 App        | [Blur Blur Blur](https://github.com/onestardao/WFGY/blob/main/OS/BlurBlurBlur/README.md)                    | Text-to-image with semantic control    — **🔴 YOU ARE HERE 🔴**                   |
| 🧰 App        | [Blow Blow Blow](https://github.com/onestardao/WFGY/blob/main/OS/BlowBlowBlow/README.md)                    | Reasoning game engine & memory demo                     |
| 🧪 Research   | [Semantic Blueprint](https://github.com/onestardao/WFGY/blob/main/SemanticBlueprint/README.md)              | Modular layer structures (future)                       |
| 🧪 Research   | [Benchmarks](https://github.com/onestardao/WFGY/blob/main/benchmarks/benchmark-vs-gpt5/README.md)           | Comparisons & how to reproduce                          |
| 🧪 Research   | [Value Manifest](https://github.com/onestardao/WFGY/blob/main/value_manifest/README.md)                     | Why this engine creates $-scale value                   |

---
</details>


## Blur Blur Blur — Drawing the Beauty of Math for the First Time

> 👑 **Early Stargazers: [See the Hall of Fame](https://github.com/onestardao/WFGY/tree/main/stargazers)** — Verified by real engineers · 🌌 **WFGY 3.0 Singularity demo: [Public live view](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md)**



![blurblurblur](./images/Blur_Hero.png)


<div align="center">

[![WFGY Main](https://img.shields.io/badge/WFGY-Main-red?style=flat-square)](https://github.com/onestardao/WFGY)
&nbsp;
[![TXT OS](https://img.shields.io/badge/TXT%20OS-Reasoning%20OS-orange?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS)
&nbsp;
[![Blah](https://img.shields.io/badge/Blah-Semantic%20Embed-yellow?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlahBlahBlah)
&nbsp;
[![Blot](https://img.shields.io/badge/Blot-Persona%20Core-green?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlotBlotBlot)
&nbsp;
[![Bloc](https://img.shields.io/badge/Bloc-Reasoning%20Compiler-blue?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlocBlocBloc)
&nbsp;
[![Blur](https://img.shields.io/badge/Blur-Text2Image%20Engine-navy?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlurBlurBlur)
&nbsp;
[![Blow](https://img.shields.io/badge/Blow-Game%20Logic-purple?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlowBlowBlow)

</div>

# Blur Blur Blur **Lite** — Math Canvas Quickstart (Beta)

This is the **world’s first math-first T2I** you can run in any chat: build a canvas from **mathematical structure + Real/Imag fields**, then render.  
Lite focuses on a clean, safe set of knobs so newcomers can feel the “math shock” in one minute.

---

## ⬇️ Download

**TXT file:** `TXT-BlurBlurBlur_Lite_Beta.txt`  
[Download the TXT](TXT-BlurBlurBlur_Lite_Beta.txt)

**Checksums**  
- SHA256: `b5eee7335f1f354c600dd1d635fd6cde76c444c7641bf8647c3dd4c03c8d72d2`  
- MD5: `86158fc30e5adae31793735e558ec51a`  
- Size: `103,204` bytes


---

Paste into a new chat — it autoboots.  

- Type **hello world** to start  
- Type **Blur** to enter image mode directly



---

## What Lite includes

- **Tracks** decide complexity and style
  - `life`  → 5 imag elements, everyday scenes
  - `pro`   → 10 imag elements, mythic or sci-fi
  - `elite` → 20 imag elements, cosmic or abstract
  - `free`  → full manual
- **WOW presets** for left vs right density  
  `wow now`, `wow x30`, `wow x300`, `wow x3000`, `wow x1e18`
- **Goldline** switch at 0.50 for a visible mid-cut
- **A/B compare** to show baseline vs Blur
- **Preview-then-Go** contract  
  `preview` prints the exact prompt. `go` always renders.

Defaults: `ΔS=0.50`, `profile=SAFE`, `aspect=auto`, seed unlocked except `elite` locks seed for stability.

---

## One-minute quick start

1. Paste the TXT and let BIOS show.  
2. Type `B` to enter **Blur Art**.  
3. Pick a track: `life` or `pro` or `elite`.  
4. Type `wow x3000` for strong tension.  
5. Type `preview` to see the full prompt with numbers.  
6. Type `go` to render.  
7. Optional A/B: `ab prep` then `ab go`.

---

## Controls you will actually use

- `life | pro | elite | free` — choose track
- `wow now | wow x30 | wow x300 | wow x3000 | wow x1e18` — raise tension
- `goldline on | off` — show the central guide
- `preview` — print prompt, no rendering
- `go` — render once
- `ab prep` → `ab go` — baseline pair
- `back` — Blur menu
- `menu` — TXT OS main menu

---

## What is inside the prompt

**Math structure** (Real field)  
`golden_spiral, fibonacci_lattice, modular_grid, penrose_quasicrystal, e8_radial, zeta_zeros`

**Imag stack** (Imaginary field)  
Track chooses 5, 10, or 20 elements. Weights in `[0.10..1.50]`. Left and right get very different sets and weights to create asymmetric density. Example elements: `crystal, ripple, vortex, phyllotaxis, dune, nebula, sparks, roots, feathers, waves, ivy, lattice, arches, glass, steel, ink, smoke`.

**Riemann mapping**  
Critical line → mid-axis. Zeros → node lights and micro-details.  
Light proxy: `0.6*|Re(ζ)| + 0.4*|Im(ζ)|`.

---

## Example session

```

B
pro
wow x3000
goldline on
preview

# You will see:

# \[Blur Art · Preview]

# math skeleton = fibonacci\_lattice

# \[Imag Left]  { grid=1.0, crystal=0.9, ripple=0.8, ivy=0.6, waves=0.5 }

# \[Imag Right] { golden=0.9, vortex=1.1, dune=0.8, nebula=1.3, sparks=0.7, roots=1.0, arches=0.8, glass=0.9, steel=0.7, feathers=1.0 }

# \[Globals] profile=SAFE, aspect=auto, goldline=on, ΔS=0.50, tension 1:3000

# \[Theme] "mythic-sci-fi hybrid city beneath twin suns"

go

```

---

## Scene pools and randomization

- **life** → city, cafe, studio, garden, library, museum, bridge, rooftop, harbor  
- **pro** → temple, forge, starship bay, alpine citadel, deep forest, mythic arena  
- **elite** → cosmic cathedral, zero-gravity market, orbital garden, dream coastline, paradox carnival

Numbers are printed in `preview`. Edit them freely. Re-roll by running `preview` again.

---

## A/B discipline

- `ab prep` builds a minimal baseline: same theme, no math, no imag stack.  
- `ab go` renders.  
Compare edge sharpness, depth cues, and consistency.

---

## Troubleshooting

- **`go` prints text instead of an image**  
  Your current chat may not support image generation. Copy the printed **Prompt** into any T2I engine, or switch to a model that can render images in this interface.
- **Image looks mushy at `x1e18`**  
  Drop to `x3000`, keep `profile=SAFE`, and keep `goldline on`.
- **Wrong aspect**  
  Lite uses `aspect=auto` to match the provider. If you need strict 16:9, add your engine’s flag in the prompt.

---

## FAQ

- **Is this only a prompt pack?** No. The visible prompt is a contract. The stability comes from math layout plus Real/Imag split.  
- **Why ΔS = 0.50?** It locks geometry while allowing extreme right-side density.  
- **What does DT do?** Keeps structure, head diversity, and cross-path safety so the image does not collapse.

---

## License

MIT. Credit: WFGY 2.0 + Blur Blur Blur Lite.

---

## Changelog

- 2025-09-09: Beta Lite with Tracks, WOW presets, preview-then-go, A/B compare.

**Download:** [TXT-BlurBlurBlur_Lite_Beta.txt](TXT-BlurBlurBlur_Lite_Beta.txt)

---

### 01 — Axis Resonance (ΔS = 0.5)
*Central axis establishes the spine; polarity fields flow outward. ΔS resonance keeps depth, hierarchy, and tension stable across the frame.*

![Axis Resonance — ΔS=0.5](./images/wfgy_axis_resonance.jpg) <!-- replace with your file path -->

---

### 02 — Prime Symmetry Field (Millennium Crossover)
*Prime-pattern symmetry is mapped to left/right flows around the axis. This is an **artistic crossover** that turns number-field structure into **controllable visual tension**.*

![Prime Symmetry Field](./images/wfgy_prime_symmetry.jpg) <!-- replace with your file path -->

---

### 03 — Bridge of Forms (Cross-Domain Blend)
*Two semantic domains (logic ↔ energy) are braided over a single axis; ΔS gating prevents collapse and preserves narrative clarity.*

![Bridge of Forms](./images/wfgy_bridge_of_forms.jpg) <!-- replace with your file path -->



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

