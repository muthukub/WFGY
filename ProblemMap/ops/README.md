# Ops — Deploy & Runbook (Problem Map)

**Purpose:** this folder contains operational runbooks, checklists and playbooks for deploying, observing, debugging and failing-over RAG pipelines and their surrounding infra.  
Target audience: SREs and engineers responsible for production RAG services. Newbie friendly — each section has a checklist and exact commands.

---

## Quick nav
- **Deployment checklist** → [deployment_checklist.md](./deployment_checklist.md)  
- **Live monitoring & alerts (RAG)** → [live_monitoring_rag.md](./live_monitoring_rag.md)  
- **Debug playbook (step-by-step)** → [debug_playbook.md](./debug_playbook.md)  
- **Failover & recovery** → [failover_and_recovery.md](./failover_and_recovery.md)

---

## Scope & assumptions
- Production topology: API gateway → RAG service (retriever + generator + guard) → Vector DB + Source storage.  
- Infra: Kubernetes (Helm) or docker-compose for small envs. Prometheus + Grafana for metrics; centralized logs (ELK/Fluentd/Vector).  
- Safety-first: ops steps favor **read-only** diagnostic commands until root cause is clear.

---

## How to use these runbooks
1. Read the **deployment checklist** before you deploy.  
2. Use **live monitoring** to ensure SLOs after deploy.  
3. If incident happens, follow **debug_playbook** (triage → isolate → mitigate → fix).  
4. If controller/broker or core services fail, follow **failover_and_recovery**.

---

## Quick operator checks (first 60s)
- Is service responding? `curl -fsS http://$SERVICE/healthz || true`  
- Are pods healthy? `kubectl get pods -n $NS`  
- Any obvious error spikes in logs (last 1 minute): `kubectl logs -n $NS -l app=$APP --since=1m | tail -n 200`  
- Check key metrics in Prometheus (latency/p95, error rate, retriever QPS).

---

## Where patterns & examples map here
- If retrieval bad → see `ProblemMap/retrieval-collapse.md` and [examples for vector-store repair](../examples/example_05_vectorstore_repair.md).  
- If bootstrap ordering failures on start → see `ProblemMap/bootstrap-ordering.md` & [pattern_bootstrap_deadlock.md](../patterns/pattern_bootstrap_deadlock.md).  
- For memory/state issues → `ProblemMap/patterns/pattern_memory_desync.md`.

---

> If you want me to also generate ready-to-apply Kubernetes manifests or Prometheus alerts for your environment (Helm values), I can produce them next — tell me cluster flavor (k8s / k3s / kind / docker-compose) and I’ll adapt.

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

