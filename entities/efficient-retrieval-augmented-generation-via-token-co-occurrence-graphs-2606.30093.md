---
title: "Efficient Retrieval-Augmented Generation via Token Co-occurrence Graphs"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [rag, retrieval, llm, inference]
sources: ["https://arxiv.org/abs/2606.30093"]
---

# Efficient Retrieval-Augmented Generation via Token Co-occurrence Graphs

## Overview
Standard RAG approaches struggle with multi-hop reasoning, and existing graph-based RAG methods rely on computationally expensive and error-prone LLM-based extraction pipelines. This paper proposes TIGRAG (Token-Induced GraphRAG), which builds token co-occurrence graphs from document collections as a lightweight structural backbone for efficient multi-hop retrieval — avoiding LLM-based extraction while preserving graph-based reasoning benefits.

## Key Facts
- **Authors**: N/A (from abstract)
- **Year**: 2026
- **arXiv**: [2606.30093](https://arxiv.org/abs/2606.30093)

## Key Contributions
- Token co-occurrence graph as a lightweight structural retrieval backbone for RAG (TIGRAG)
- Eliminates expensive LLM-based graph extraction used by prior GraphRAG approaches
- Improves multi-hop reasoning in RAG systems while reducing computational overhead
- Orthogonal to prior Graph-RAG reasoning bottleneck paper (Run 215) — addresses efficiency vs. diagnosis

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts chain
