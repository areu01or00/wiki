---
title: "ChartWalker: Benchmarking the Cross-Chart RAG Task with Hierarchical Knowledge Graphs"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [multimodal-rag, retrieval-augmented-generation, chart-reasoning, hierarchical-knowledge-graphs, benchmark]
sources: ["https://arxiv.org/abs/2606.23997"]
---

# ChartWalker: Benchmarking the Cross-Chart RAG Task with Hierarchical Knowledge Graphs

## Overview
ChartWalker introduces a benchmark for **cross-chart retrieval-augmented generation** — multi-modal analytical tasks where the question spans multiple related charts (rather than a single chart or table) — and constructs a hierarchical knowledge graph over chart collections to support grounded, multi-hop reasoning. Existing benchmarks either focus on well-structured tables or generate cross-chart questions by simply extracting rows/columns, missing the synthesis problem that real multi-chart dashboards pose. The paper shows that naively applying single-chart RAG methods collapses on cross-chart tasks and that a chart-aware hierarchical KG is necessary to recover meaningful accuracy.

## Key Facts
- **Authors**: Tang, Ning; Xie, Chenghan; Yuan, Hanyang; Li, Yi; Huang, Renhong; et al.
- **Year**: 2026 (revised 2026-06-22)
- **arXiv**: [2606.23997](https://arxiv.org/abs/2606.23997)
- **Subjects**: cs.IR

## Key Contributions
- Introduces the Cross-Chart RAG task formulation and ChartWalker benchmark, distinguishing it from single-chart QA and from text-table RAG.
- Constructs a hierarchical knowledge graph linking charts via shared entities, themes, and visual-semantic relations, enabling multi-hop evidence aggregation.
- Demonstrates that chart-aware hierarchical KG retrieval substantially outperforms naive single-chart RAG on cross-chart analytical questions, isolating the contribution of cross-document reasoning.
- Releases evaluation harness with both automated metrics and human-judged faithfulness/accuracy splits to disentangle retrieval failures from generation failures.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain that led to this discovery (HF daily+monthly emergent-concept run on 2026-06-25).
- [[dream-dense-retrieval-embeddings-via-autoregressive-modeling-2606.24667]] — Complementary unification of retrieval and generation inside a single autoregressive LM; ChartWalker attacks the *cross-document* side, DREAM attacks the *model-architecture* side.
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — Both papers extend retrieval beyond flat semantic search; EvoEmbedding evolves the embedding representation, ChartWalker evolves the index structure.