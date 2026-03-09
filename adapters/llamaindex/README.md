# WFGY LlamaIndex Adapter (Semantic Firewall)

This adapter provides a wrapper for LlamaIndex QueryEngines to enable semantic tension (ΔS) monitoring.

## Usage

```python
from wfgy.adapters.llamaindex.firewall import WFGYSemanticFirewallLlama
from llama_index.embeddings.openai import OpenAIEmbedding

# Initialize embeddings
embed_model = OpenAIEmbedding()

# Initialize Firewall
firewall = WFGYSemanticFirewallLlama(embedding_model=embed_model)

# Create your engine
query_engine = index.as_query_engine()

# Wrap it
firewall_engine = firewall.wrap_query_engine(query_engine)

# Use it as normal
response = firewall_engine.query("What is semantic tension?")
```
