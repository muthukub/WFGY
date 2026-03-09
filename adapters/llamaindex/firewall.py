import math
from typing import Any, List, Optional
from llama_index.core.query_engine import BaseQueryEngine
from llama_index.core.response.schema import Response

class WFGYSemanticFirewallLlama:
    """
    WFGY Semantic Firewall Wrapper for LlamaIndex.
    Adds ΔS monitoring to any QueryEngine.
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

    def _calculate_delta_s(self, vec_a, vec_b) -> float:
        """Calculates ΔS = 1 - cos(theta)"""
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0 or norm_b == 0:
            return 1.0
        cos_theta = dot_product / (norm_a * norm_b)
        return 1.0 - cos_theta

    def wrap_query_engine(self, query_engine: BaseQueryEngine) -> BaseQueryEngine:
        """Wraps a LlamaIndex query engine to monitor semantics."""
        original_query = query_engine.query

        def wrapped_query(str_or_query_bundle: Any) -> Response:
            query_str = str(str_or_query_bundle)
            query_embedding = self.embedding_model.get_query_embedding(query_str)
            
            # Execute original query
            response = original_query(str_or_query_bundle)
            
            # Analyze DeltaS between Answer and Query
            answer_text = response.response
            answer_embedding = self.embedding_model.get_query_embedding(answer_text)
            
            delta_s = self._calculate_delta_s(query_embedding, answer_embedding)
            
            if self.verbose:
                print(f"[WFGY-LlamaIndex] Answer ΔS: {delta_s:.4f}")

            # Analyze Source Nodes
            if hasattr(response, 'source_nodes'):
                source_delta_s = []
                for node in response.source_nodes:
                    node_text = node.node.get_content()
                    node_embedding = self.embedding_model.get_text_embedding(node_text)
                    source_delta_s.append(self._calculate_delta_s(query_embedding, node_embedding))
                
                avg_source_delta_s = sum(source_delta_s) / len(source_delta_s)
                if self.verbose:
                    print(f"[WFGY-LlamaIndex] Avg Source ΔS: {avg_source_delta_s:.4f}")

                if avg_source_delta_s >= self.threshold_danger:
                    print(f"⚠️ [WFGY] DANGER ZONE: Source Drift (ΔS={avg_source_delta_s:.4f})")

            return response

        query_engine.query = wrapped_query
        return query_engine
