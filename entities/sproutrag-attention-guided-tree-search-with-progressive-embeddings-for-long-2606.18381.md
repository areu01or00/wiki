---
title: "SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [rag, retrieval, hierarchical, attention, long-context]
sources: ["https://arxiv.org/abs/2606.18381"]
---

# SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG

## Overview
Retrieval-augmented generation systems must balance retrieval granularity with contextual coherence — a trade-off existing methods address via LLM-guided chunking (costly indexing), single-level context expansion (fixed granularity), or hierarchical summarization (information loss). SproutRAG introduces an attention-guided hierarchical RAG framework that organizes sentence-level chunks into progressively larger but semantically coherent units, applying tree search guided by attention-derived signals to avoid the cost of LLM calls during indexing/retrieval and the information loss of summarization.

## Key Facts
- **Authors**: Abaskohi, Amirhossein; Laradji, Issam H.; West, Peter; +1 more
- **Year**: 2026
- **arXiv**: [2606.18381](https://arxiv.org/abs/2606.18381)

## Key Contributions
- Introduces **SproutRAG**, an attention-guided hierarchical RAG framework that scales chunks progressively without summarization.
- Avoids costly LLM calls during indexing/retrieval — uses attention-derived signals instead of LLM-guided chunking.
- Avoids information loss inherent in hierarchical summarization by composing semantically-coherent progressive units via tree search.

## Related Papers
- [[emergent-concepts]] — Parent topic: LLM agent evaluation / RAG / memory governance
