---
title: "HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [benchmark, retrieval, rag, embedding, information-retrieval, evaluation, efficiency]
sources: ["https://arxiv.org/abs/2606.22778"]
---

# HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions

## Overview
HAKARI-Bench is a lightweight benchmark purpose-built for comparing retrieval architectures and efficiency settings under unified conditions, addressing the gap between heavyweight retrieval benchmarks (comprehensive but slow) and ad-hoc production comparisons. It provides standardized infrastructure for evaluating dimensionality reduction, quantization, and reranking configurations across many embedding and retrieval models, enabling rapid iteration on retrieval-augmented generation pipelines during development.

## Key Facts
- **Authors**: Tateno, Yuichi et al.
- **Year**: 2026
- **Date**: 2026-06-22
- **arXiv**: [2606.22778](https://arxiv.org/abs/2606.22778)
- **Subjects**: Information Retrieval (cs.IR)

## Key Contributions
- A lightweight retrieval benchmark designed to be rerunnable during development, addressing the heavyweight nature of existing comprehensive retrieval benchmarks
- Unified-condition evaluation infrastructure for comparing retrieval configurations (dimensionality reduction, quantization, reranking) across many models, eliminating the apples-to-oranges comparisons that plague production retrieval comparisons
- Empirical comparison of contemporary embedding and retrieval architectures under matched efficiency settings, surfacing which combinations deliver the best accuracy/cost tradeoffs for RAG pipelines
- Practical tooling for RAG engineers to benchmark their specific retrieval stack against standardized configurations, lowering the barrier to principled retrieval-pipeline choices

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[dream-dense-retrieval-embeddings-via-autoregressive-modeling-2606.24667]] — Companion retrieval theme on dense embeddings via autoregressive modeling
