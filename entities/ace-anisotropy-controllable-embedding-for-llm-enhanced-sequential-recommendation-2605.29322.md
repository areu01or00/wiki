---
title: "ACE: Anisotropy-Controllable Embedding for LLM-enhanced Sequential Recommendation"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [embedding, representation-geometry, recommendation, model-architecture]
sources: ["https://arxiv.org/abs/2605.29322"]
---

# ACE: Anisotropy-Controllable Embedding for LLM-enhanced Sequential Recommendation

## Overview
Addresses the anisotropy problem in LLM-generated embeddings for sequential recommendation. LLM-generated embeddings suffer from strong anisotropy — vectors concentrate in similar directions, creating geometric imbalance that degrades fine-tuning stability and retrieval quality. ACE proposes an anisotropy-controllable embedding method that balances geometric uniformity and semantic preservation via a regularization term controlling embedding dimension dispersion.

## Key Facts
- **Authors**: Lee, Dongcheol; Kim, Hye-young; Lee, Jongwuk
- **Year**: 2026
- **arXiv**: [2605.29322](https://arxiv.org/abs/2605.29322)

## Key Contributions
- First method to explicitly control anisotropy in LLM-generated embeddings via a dispersion regularization term
- Preserves semantic relationships among items while improving geometric uniformity of the embedding space
- Demonstrates improved fine-tuning stability for sequential recommendation backbones
- Provides diagnostic framework for relating embedding geometry to downstream retrieval robustness

## Related Papers
- [[dream-dense-retrieval-embeddings-via-autoregressive-modeling-2606.24667]] — DREAM: dense retrieval embeddings via autoregressive modeling (alternative embedding approach)
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — EvoEmbedding: evolvable representations for long-context retrieval and agentic memory
