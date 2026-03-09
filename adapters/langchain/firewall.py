import math
from typing import Any, Dict, List, Optional
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult

class WFGYSemanticFirewall(BaseCallbackHandler):
    """
    WFGY Semantic Firewall Adapter for LangChain.
    Implements ΔS (Semantic Tension) monitoring and λ_observe tracking.
    """

    def __init__(self, 
                 embedding_model: Any, 
                 threshold_risk: float = 0.6, 
                 threshold_danger: float = 0.85,
                 verbose: bool = True):
        self.embedding_model = embedding_model
        self.threshold_risk = threshold_risk
        self.threshold_danger = threshold_danger
        self.verbose = verbose
        self.last_query_embedding = None
        self.last_context_embeddings = []

    def _calculate_delta_s(self, vec_a, vec_b) -> float:
        """Calculates ΔS = 1 - cos(theta)"""
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0 or norm_b == 0:
            return 1.0
        cos_theta = dot_product / (norm_a * norm_b)
        return 1.0 - cos_theta

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> Any:
        # Cache query embedding for ΔS calculation later
        if prompts:
            self.last_query_embedding = self.embedding_model.embed_query(prompts[0])

    def on_retriever_end(self, documents: List[Any], **kwargs: Any) -> Any:
        """Monitor ΔS between query and retrieved documents."""
        if not self.last_query_embedding or not documents:
            return

        doc_texts = [doc.page_content for doc in documents]
        doc_embeddings = self.embedding_model.embed_documents(doc_texts)
        self.last_context_embeddings = doc_embeddings

        delta_s_scores = [self._calculate_delta_s(self.last_query_embedding, doc_emb) for doc_emb in doc_embeddings]
        avg_delta_s = sum(delta_s_scores) / len(delta_s_scores)

        if self.verbose:
            print(f"[WFGY] Avg ΔS (Query <-> Context): {avg_delta_s:.4f}")

        if avg_delta_s >= self.threshold_danger:
            print(f"⚠️ [WFGY] DANGER ZONE: Perception Drift detected (ΔS={avg_delta_s:.4f})")
            # In a production version, we might raise an error here to stop the chain.

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Monitor ΔS between answer and context/query."""
        if not response.generations or not self.last_query_embedding:
            return

        answer_text = response.generations[0][0].text
        answer_embedding = self.embedding_model.embed_query(answer_text)

        delta_s_answer = self._calculate_delta_s(self.last_query_embedding, answer_embedding)
        
        if self.verbose:
            print(f"[WFGY] Final Answer ΔS: {delta_s_answer:.4f}")

        if delta_s_answer >= self.threshold_risk:
             print(f"🚨 [WFGY] RISK ZONE: Potential Hallucination detected (ΔS={delta_s_answer:.4f})")
