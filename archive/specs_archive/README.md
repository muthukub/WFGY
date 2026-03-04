
# WFGY – Public API Specs & ONNX Graphs
*Version 1.0 · last updated 2025-06-12*

WFGY is open by design.  
To guarantee that each module can be inspected, audited, or re-implemented,
we publish (1) a concise API spec and (2) a lightweight ONNX graph for every
core component.  
Download the `.onnx` files and open them in **[Netron](https://netron.app)**
or any ONNX viewer to see the exact computation graph—no black box, no
hidden layers.

| Module | API spec | ONNX graph |
|--------|----------|-----------|
| **BBMC**<br>_Semantic Residue_ | [`bbmc_api.md`](bbmc_api.md) | [`onnx/bbmc.onnx`](onnx/bbmc.onnx) |
| **BBPF**<br>_Progression Flow_ | [`bbpf_api.md`](bbpf_api.md) | [`onnx/bbpf.onnx`](onnx/bbpf.onnx) |
| **BBCR**<br>_Collapse–Rebirth_ | [`bbcr_api.md`](bbcr_api.md) | [`onnx/bbcr.onnx`](onnx/bbcr.onnx) |
| **BBAM**<br>_Attention Modulator_ | [`bbam_api.md`](bbam_api.md) | [`onnx/bbam.onnx`](onnx/bbam.onnx) |

---

## Re-exporting the graphs

All four graphs are intentionally **tiny** (~20 KB each) so they build in
seconds and reveal the tensor flow without shipping proprietary weights.

```bash
# in repo root
python export_onnx.py
````

This script recreates the folder structure:

```
specs/
├── onnx/
│   ├── bbam.onnx
│   ├── bbcr.onnx
│   ├── bbmc.onnx
│   └── bbpf.onnx
└── *.md               # human-readable API specs
```

Feel free to replace these dummy graphs with full-precision weights
if you need exact numerical reproduction.

---

## License & Citation

The API descriptions and ONNX graphs are released under the MIT license.
If you use WFGY in research, please cite the Zenodo release:

```
PSBigBig, “WFGY 1.0: A Self-Healing Variance Gate for LLMs,”
```

> Any issue / PR is welcome—open science thrives on transparency.

```

---

### Will Colab runs change after adding this folder?

No. `specs/` is pure documentation.  
All examples (`example_01`–`08`), tests, and the SDK itself remain identical,
so you can keep running the original Colab notebook without any modification.
```

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

