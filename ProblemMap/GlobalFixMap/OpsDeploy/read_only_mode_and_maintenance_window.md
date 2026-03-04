# Read-Only Mode and Maintenance Window — OpsDeploy

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


Freeze writes quickly and communicate clearly during incidents, migrations, or index rebuilds. Keep retrieval online while protecting data integrity and user trust.

## Open these first
- Ordering and cold boots: [Bootstrap Ordering](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [Pre-Deploy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)
- Idempotency and dedupe: [Idempotency & Dedupe](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/idempotency_dedupe.md)
- Incident comms: [Incident Comms & Statuspage](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/incident_comms_and_statuspage.md)
- Cache and warmup: [Cache Warmup & Invalidation](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/cache_warmup_invalidation.md)

## Acceptance targets
- All write endpoints return 423 or 503 with `Retry-After`
- No production writes in storage audit during the window
- Read paths healthy: error budget unaffected
- Banner or Statuspage posted before and after with exact times
- ΔS and λ trends flat during the window for read requests

## 60-second checklist
1) **Flip read-only flag**  
   Global feature flag `read_only=true`. Middleware blocks writes, tool calls that mutate state, and ingestion jobs.
2) **Communicate**  
   Post Statuspage and in-product banner with start and end times. Include contact and rollback plan.
3) **Queue writes**  
   Buffer allowed write intents to a durable queue with idempotency keys. Drop non-critical writes.
4) **Headers**  
   Write endpoints respond with `Retry-After: <seconds>` and a stable error code for clients to respect.
5) **Drains**  
   Stop background writers, disable compaction and long migrations during the window.

## Minimal playbook
- **Scope**: enumerate write surfaces including embeddings backfills, vector upserts, tool call side effects, KV mutations.  
- **Guard**: enforce in API gateway and service layer. Return machine-readable errors.  
- **Observe**: track blocked write count, queue depth, read latency, ΔS and λ.  
- **End**: re-enable writes, run a short soak, publish closure notice, then backfill the queued intents.

## Common pitfalls → fix
- A background job keeps writing  
  → include job scheduler in the flag check and stop crons.  
- Clients spin on retries  
  → add jittered backoff and a max-retry budget. See [Retry Backoff](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/retry_backoff.md).  
- Cached stale banners  
  → set short TTL and purge caches on start and end.

## Escalate
If read errors or ΔS spikes appear, extend the window and execute a limited [Rollback & Fast Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/rollback_and_fast_recovery.md).

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

