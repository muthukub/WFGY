# Shadow Traffic Mirroring — OpsDeploy

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **OpsDeploy**.  
  > To reorient, go back here:  
  >
  > - [**OpsDeploy** — operations automation and deployment pipelines](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


Safely mirror real production requests to a new model or service without affecting users. Use this page to validate output drift, latency, rate limits, and side-effect isolation before any canary or switchover.

## Open these first
- Visual map and recovery: [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)
- End to end retrieval knobs: [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)
- Live ops: [Live Monitoring for RAG](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/live_monitoring_rag.md), [Debug Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md)
- Safe rollouts nearby: [Staged Canary](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/staged_rollout_canary.md), [Blue-Green Switchovers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/blue_green_switchovers.md)
- Backpressure and retries: [Rate Limit Backpressure](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/rate_limit_backpressure.md), [Retry Backoff](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/retry_backoff.md)

## Acceptance targets
- ΔS(prod_answer, shadow_answer) ≤ 0.45 on three paraphrases
- λ remains convergent across two seeds
- P99 added latency from mirroring ≤ 5 percent of end-to-end
- Zero side effects from shadow path: writes blocked or redirected
- Sampling accuracy within ±2 percent of configured shadow ratio

## 60-second checklist
1) **Mirror only reads**  
   Route the same request payload to the shadow service. Strip tokens and secrets not required for read paths. Block tool calls and any writes.
2) **Tag and store**  
   Append `shadow_id`, `req_hash`, `model_rev`, `index_hash`. Persist both prod and shadow outputs with ΔS and λ.
3) **Throttles**  
   Apply a hard cap on mirror QPS. Respect provider limits. Enable backpressure guards.
4) **Drift gates**  
   Alert when mean ΔS exceeds 0.45 or when λ flips on harmless paraphrases.

## Minimal playbook
- **Ingress**: duplicate the request at the edge or gateway. Never await the shadow response on the user path.  
- **Sanitize**: remove side-effect headers, redact PII fields that the shadow does not need.  
- **Observe**: log `ΔS`, `λ_state`, `shadow_latency_ms`, HTTP codes, rate-limit headers.  
- **Compare**: evaluate citation alignment with [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) and snippet schema from [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md).  
- **Decide**: graduate to canary if drift stays within target for 24 hours and error budget is untouched.

## Common pitfalls → fix
- Shadow answers write or call tools  
  → run in read-only mode and stub tool responses. See [Idempotency & Dedupe](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/idempotency_dedupe.md).
- Cache pollution from shadow  
  → segregate caches by `shadow=true` key segment. See [Cache Warmup & Invalidation](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/cache_warmup_invalidation.md).
- Latency spikes  
  → apply sample ratio caps and separate thread pools. Add [Backpressure](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/rate_limit_backpressure.md).
- Unreliable comparisons  
  → normalize prompts and headers, align indexes with [Vector Index Build & Swap](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/vector_index_build_and_swap.md).

## Escalate
Promote to [Staged Canary](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/staged_rollout_canary.md) when drift and error rates meet targets for a full diurnal cycle and shadow P95 latency increase is under 3 percent.

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

