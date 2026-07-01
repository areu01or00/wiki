---
title: "Reducing Hallucinations in Complex Question Answering using Simple Graph-based Retrieval-Augmented Generation"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [RAG, hallucination, retrieval, safety]
sources: ["https://arxiv.org/abs/2606.05901"]
---

# Reducing Hallucinations in Complex Question Answering using Simple Graph-based Retrieval-Augmented Generation

## Overview
A graph-based RAG approach that reduces hallucinations in complex question answering by structuring retrieval around entity-relationship graphs rather than flat document chunks. Shows that simple graph normalization outperforms complex multi-hop retrieval pipelines.

## Key Facts
- **Authors**: Wedge, Christopher J.; Stutter, Joshua; Dixon, Danny + 1
- **Year**: 2026
- **arXiv**: [2606.05901](https://arxiv.org/abs/2606.05901)

## Key Contributions
- Graph-based document structuring for RAG reduces hallucination by 11.1% on TriviaQA
- Cuts retrieval frequency from 45.2% (flat chunk RAG) to much lower while improving accuracy
- Self-correction loop integrated with graph traversal validates retrieved context before generation
- Simple approach outperforms complex multi-hop pipelines on hallucination metrics

## Related Papers
- [[world-action-models-a-survey-2606.20781]] — Survey of world models in agents; complementary context on agent memory vs retrieval grounding
