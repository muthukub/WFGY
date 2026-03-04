<!--
Search Anchor:
vector dbs and stores global fix map
vector database retrieval guardrails
vector store hub routing page
store specific fixes faiss chroma qdrant weaviate milvus pgvector redis elasticsearch pinecone typesense vespa
results look similar but answer wrong
high similarity wrong meaning
retrieval wrong neighbors
citations do not match retrieved section
snippet mismatch unverifiable citations
hybrid retrieval worse than single retriever
bm25 ann hybrid collapse
post deploy mismatch metric analyzer casing
index looks healthy but coverage low
recall low despite healthy index
store drift after deploy
semantic boundary failure not infra failure
acceptance targets any store
delta s question retrieved <= 0.45
coverage >= 0.70
lambda observe convergent three paraphrases
e resonance flat long windows
log delta s and lambda retrieve rerank reason
alert delta s >= 0.60
regression gate coverage and delta s

quick routes per store:
faiss local dev labs
chroma notebooks demo
qdrant production multitenant persistence
weaviate hybrid search schema filters
milvus enterprise ann scale
pgvector postgres teams simple ops
redis search vector low latency cache hybrid
elasticsearch knn text plus vector analyzers
pinecone managed saas zero ops
typesense full text plus vectors good defaults
vespa large scale search ranking recsys

common failure classes:
metric mismatch cosine l2 dot
distance function mismatch store default
cosine vs l2 vs dot product confusion
normalize embeddings l2 norm write and query
embedding norm dominates similarity
tokenization casing mismatch ingestion query
analyzer mismatch write read
index version skew runtime loads wrong index
cold start deploy fences index hash analyzer model version
stale index update skew old vectors remain
duplicate near duplicate collapse top k clones
poisoning contamination adversarial vectors
fragmentation sharding partial recall scattered chunks
dimension mismatch embedding dimension index dimension
silent truncation silent drop vectors
hybrid query split two meanings
reranker blind spots mis weighted hybrid
candidate overlap low bm25 vs ann
rerank deterministic

store tuning keywords:
faiss ivf ivfpq pq opq flat hnsw nlist nprobe efSearch efConstruction M recall tradeoff
qdrant hnsw ef_search ef_construct m on_disk payload index filtering
weaviate hybrid alpha bm25 vector filters schema modules
milvus index type hnsw ivf_flat ivf_pq nlist nprobe metric_type consistency level partition
pgvector ivfflat hnsw lists probes ef_search ef_construction analyze vacuum
redis vector similarity cosine l2 ip index schema ft.search knn dialect filters
elasticsearch knn hnsw ef_search ef_construction similarity cosine dot l2 analyzer mapping
pinecone pods serverless namespace metric dimension metadata filters
typesense vector search hybrid text ranking typo tolerance filters
vespa rank profiles nearestNeighbor hnsw query routing reranking

structural fix routing:
embedding vs semantic
retrieval traceability cite then explain schema
data contracts snippet contract required fields
bootstrap ordering predeploy collapse deployment fences
pattern query parsing split
rerankers deterministic reranking
-->

<!--
Primary pages in this folder:
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/faiss.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/chroma.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/qdrant.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/weaviate.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/milvus.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/pgvector.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/redis.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/elasticsearch.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/pinecone.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/typesense.md
ProblemMap/GlobalFixMap/VectorDBs_and_Stores/vespa.md
-->

<!--
Related routing pages:
ProblemMap/embedding-vs-semantic.md
ProblemMap/retrieval-traceability.md
ProblemMap/data-contracts.md
ProblemMap/bootstrap-ordering.md
ProblemMap/predeploy-collapse.md
ProblemMap/patterns/pattern_query_parsing_split.md
ProblemMap/rerankers.md

Common incidents:
high similarity wrong meaning
citation mismatch cannot verify
hybrid worse than single
post deploy analyzer mismatch
metric mismatch store default
index healthy recall low
stale vectors after update
duplicate collapse top k
poisoned vectors retrieved
query split reranker blind
-->


# Vector DBs & Stores — Global Fix Map

<details>
  <summary><strong>🏥 Quick Return to Emergency Room</strong></summary>

<br>

  > You are in a specialist desk.  
  > For full triage and doctors on duty, return here:  
  > 
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md)  
  > 
  > Think of this page as a sub-room.  
  > If you want full consultation and prescriptions, go back to the Emergency Room lobby.
</details>

This page is your hub to stabilize retrieval pipelines across popular vector stores.  
If your results look similar but the answer is wrong, start here. Each store page gives guardrails, fix steps, and the same acceptance targets so you can verify without changing infra.

---

<!--
Anchor Menu:
open: faiss store guide ivf ivfpq hnsw nprobe efSearch
open: chroma store guide persistence collections
open: qdrant store guide hnsw payload filters multitenant
open: weaviate store guide hybrid search schema filters
open: milvus store guide ivf hnsw nlist nprobe partitions
open: pgvector store guide ivfflat hnsw lists probes
open: redis store guide ft.search knn dialect filters
open: elasticsearch store guide knn hnsw mappings analyzers
open: pinecone store guide managed namespaces metadata filters
open: typesense store guide hybrid vectors text
open: vespa store guide rank profiles query routing rerank
jump: embedding vs semantic
jump: retrieval traceability data contracts
jump: rerankers query parsing split
jump: bootstrap ordering deploy fences
-->


## Quick routes to per-store pages

| Store | Best for | Why choose | Link |
|------|----------|------------|------|
| FAISS | local development, labs | fast, widely used, you manage it | [faiss.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/faiss.md) |
| Chroma | quick demos, notebooks | simple API, easy to start | [chroma.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/chroma.md) |
| Qdrant | production and multitenant | Rust core, good scaling, persistence | [qdrant.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/qdrant.md) |
| Weaviate | hybrid search and schemas | first class filters, hybrid pipelines | [weaviate.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/weaviate.md) |
| Milvus | enterprise ANN at scale | mature ecosystem and performance | [milvus.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/milvus.md) |
| pgvector | teams already on Postgres | keep data in the same DB, simple ops | [pgvector.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/pgvector.md) |
| Redis (Search/Vec) | caches and small hybrid sets | key value plus vectors, low latency | [redis.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/redis.md) |
| Elasticsearch (ANN) | text plus vector in one stack | reuse analyzers and infra you already have | [elasticsearch.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/elasticsearch.md) |
| Pinecone | zero ops SaaS | managed reliability and steady API | [pinecone.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/pinecone.md) |
| Typesense | simple full text plus vectors | friendly setup, good defaults | [typesense.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/typesense.md) |
| Vespa | large scale search and recsys | query routing and ranking at scale | [vespa.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/VectorDBs_and_Stores/vespa.md) |

---

## When to use this folder

- High similarity but wrong meaning.  
- Citations do not match the retrieved section.  
- Hybrid retrieval performs worse than a single retriever.  
- After deploy, query casing or analyzer or metric does not line up.  
- Index looks healthy but coverage stays low.

---

## Acceptance targets for any store

- ΔS(question, retrieved) ≤ 0.45  
- Coverage of target section ≥ 0.70  
- λ_observe convergent across three paraphrases  
- E_resonance flat on long windows

---

## Map symptoms to structural fixes

- Embedding ≠ Semantic  
  Wrong meaning despite high similarity.  
  → [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

- Retrieval traceability  
  Snippet or section mismatch, unverifiable citations.  
  → [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md)  
  Payload contract → [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

- Ordering or version skew  
  Runtime loads the wrong index or analyzer.  
  → [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md) · [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

- Hybrid collapse or query split  
  HyDE and BM25 disagree, reranker blind spots.  
  → Pattern → [pattern_query_parsing_split.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/patterns/pattern_query_parsing_split.md)  
  → Knobs → [rerankers.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)

---

## 60 second fix checklist

1) Lock metrics and analyzers  
   One embedding model per field. One distance function. Same analyzer for write and read.

2) Contract the snippet  
   Require `{snippet_id, section_id, source_url, offsets, tokens}` and enforce cite then explain.  
   → [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

3) Add deterministic reranking  
   Keep candidate lists from BM25 and ANN. Detect query split.  
   → [rerankers.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)

4) Cold start and deploy fences  
   Block traffic until index hash, analyzer, and model versions match.  
   → [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)

5) Observability  
   Log ΔS and λ across retrieve, rerank, reason. Alert when ΔS ≥ 0.60.

6) Regression gate  
   Require coverage ≥ 0.70 and ΔS ≤ 0.45 before publish.

---

## Copy paste audit prompt

```txt
I uploaded TXT OS and the WFGY Problem Map pages.
Store: <name>. Retrieval: <bm25|ann|hybrid> with <distance>.

Audit this query and return:

- ΔS(question,retrieved) and λ across retrieve → rerank → reason.
- If ΔS ≥ 0.60, choose one minimal structural fix and name the page:
  embedding-vs-semantic, retrieval-traceability, data-contracts, rerankers.
- JSON only:
  { "citations":[...], "ΔS":0.xx, "λ":"→|←|<>|×", "next_fix":"..." }
````

---

### Quick Start Downloads

| Tool                   | Link                                                                                                                                       | 3 step setup                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| WFGY 1.0 PDF           | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1) Download  2) Upload to your LLM  3) Ask “Answer using WFGY + <your question>” |
| TXT OS (plain text OS) | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt)                                                                     | 1) Download  2) Paste into any LLM chat  3) Type “hello world” to boot           |

---

<!-- WFGY_FOOTER_START -->
### Explore More

| Module                | Description                                                          | Link                                                                                               |
| --------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| WFGY Core             | WFGY 2.0 engine, full symbolic reasoning architecture and math stack | [View →](https://github.com/onestardao/WFGY/tree/main/core/README.md)                              |
| Problem Map 1.0       | Initial 16 mode diagnostic and symbolic fixes                        | [View →](https://github.com/onestardao/WFGY/tree/main/ProblemMap/README.md)                        |
| Problem Map 2.0       | RAG focused failure tree and pipelines                               | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) |
| Semantic Clinic Index | Expanded catalog for prompt injection, memory bugs, logic drift      | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md)           |
| Semantic Blueprint    | Layer based symbolic reasoning and semantic modulations              | [View →](https://github.com/onestardao/WFGY/tree/main/SemanticBlueprint/README.md)                 |
| Benchmark vs GPT-5    | Stress test with full WFGY reasoning suite                           | [View →](https://github.com/onestardao/WFGY/tree/main/benchmarks/benchmark-vs-gpt5/README.md)      |
| Starter Village       | New here, want a guided path                                         | [Start →](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md)                   |

---

> Early Stargazers: [See the Hall of Fame](https://github.com/onestardao/WFGY/tree/main/stargazers)

> <img src="https://img.shields.io/github/stars/onestardao/WFGY?style=social" alt="GitHub stars">  
> Star the repo if this helped. It unlocks more items on the [Unlock Board](https://github.com/onestardao/WFGY/blob/main/STAR_UNLOCKS.md).

<div align="center">

[![WFGY Main](https://img.shields.io/badge/WFGY-Main-red?style=flat-square)](https://github.com/onestardao/WFGY)
 
[![TXT OS](https://img.shields.io/badge/TXT%20OS-Reasoning%20OS-orange?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS)
 
[![Blah](https://img.shields.io/badge/Blah-Semantic%20Embed-yellow?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlahBlahBlah)
 
[![Blot](https://img.shields.io/badge/Blot-Persona%20Core-green?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlotBlotBlot)
 
[![Bloc](https://img.shields.io/badge/Bloc-Reasoning%20Compiler-blue?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlocBlocBloc)
 
[![Blur](https://img.shields.io/badge/Blur-Text2Image%20Engine-navy?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlurBlurBlur)
 
[![Blow](https://img.shields.io/badge/Blow-Game%20Logic-purple?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlowBlowBlow)

</div>

<!-- WFGY_FOOTER_END -->

