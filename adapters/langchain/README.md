# WFGY LangChain Adapter (Semantic Firewall)

This adapter provides a `WFGYSemanticFirewall` callback handler for LangChain, enabling real-time monitoring of semantic tension (ΔS) to prevent hallucinations and perception drift.

## Quick Start

```python
from wfgy.adapters.langchain.firewall import WFGYSemanticFirewall
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# Initialize embeddings (must be consistent)
embeddings = OpenAIEmbeddings()

# Initialize WFGY Firewall
firewall = WFGYSemanticFirewall(embedding_model=embeddings)

# Plug into any LangChain object or chain
llm = ChatOpenAI(callbacks=[firewall])

# or use it in a chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=your_retriever,
    callbacks=[firewall]
)

qa_chain.run("How does WFGY work?")
```

## Metrics Tracked

- **ΔS (Query <-> Context)**: Measures how well the retrieved documents match the user's intent. High ΔS indicates "Perception Drift".
- **ΔS (Final Answer)**: Measures how well the LLM's response stays within the semantic bounds of the query.

## Zones
- **Safe**: ΔS < 0.4
- **Risk**: 0.6 < ΔS < 0.85
- **Danger**: ΔS ≥ 0.85 (Triggers alerts)
```
