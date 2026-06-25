---
title: "DREAM: Dense Retrieval Embeddings via Autoregressive Modeling"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [llm, retrieval, rag, embeddings, autoregressive]
sources: ["https://arxiv.org/abs/2606.24667"]
---

# DREAM: Dense Retrieval Embeddings via Autoregressive Modeling

## Overview
Dense retrieval embedding models are a fundamental component of modern retrieval-based AI systems. Most dense retrievers are trained with contrastive objectives, which require labeled positive and negative document pairs that are often costly and difficult to obtain, particularly for specialized domains. DREAM investigates whether dense retrieval embeddings can be produced directly by an autoregressive language model — the same model class used for generation — by repurposing the next-token-prediction objective to also produce document-level representations without contrastive supervision. Tang and Yang show that autoregressive embedding objectives, paired with a careful aggregation of hidden states across the document, recover competitive retrieval quality on standard benchmarks while eliminating the labeled-pair pipeline, opening a path toward unified retrieval-generation models whose embeddings and outputs share representations and supervision signals.

## Key Facts
- **Authors**: Tang, Yixuan; Yang, Yi
- **Year**: 2026
- **arXiv**: [2606.24667](https://arxiv.org/abs/2606.24667)
- **Subjects**: cs.CL

## Key Contributions
- Shows that an autoregressive LM trained with standard next-token prediction can produce document-level dense embeddings competitive with contrastively-trained specialist retrievers, without any pairwise labeled data.
- Introduces an aggregation scheme over hidden states that captures document-level semantics without an extra projection head, preserving parameter sharing with the generation path.
- Demonstrates that the resulting embeddings transfer across retrieval tasks (open-domain QA, dense passage retrieval, multilingual retrieval) and that the same model can serve as retriever and re-ranker without architectural change.
- Eliminates the contrastive-pair collection pipeline that has been the dominant cost driver for new retrieval domains, with implications for low-resource and rapidly-evolving corpora.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain; discovered via emergent-concept search on the dense-retrieval / embedding axis
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — Companion: KV-cache compression exploiting RoPE frequency structure; both treat retrieval-relevant representations as a low-level inference concern
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — Companion: context-dependent evolvable embeddings; DREAM keeps embeddings static but unifies them with the generation path
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Companion: agent-native memory needs retrieval; DREAM removes the specialist-retriever barrier to populating that memory layer