---
title: "Multi-hop Reasoning and Retrieval in Embedding Space (EMBRAG)"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [knowledge-graph, embedding-space, multi-hop-reasoning, retrieval, kgqa, llm]
sources: ["https://arxiv.org/abs/2603.13266"]
---

# Multi-hop Reasoning and Retrieval in Embedding Space (EMBRAG)

## Overview
First embedding-space reasoning framework that addresses two structural failures of LLM-based KGQA — KG-understanding-induced query misinterpretation and KG-incompleteness-induced retrieval failures — by *generating multiple logical rules grounded in a knowledge graph, applying them in the embedding space guided by the KG, and reranking the resulting trajectories*. Reaches state-of-the-art on two benchmark KGQA datasets.

## Key Facts
- **Authors**: Liu, L. and collaborators (Multi-hop Reasoning and Retrieval in Embedding Space)
- **Year**: 2026
- **arXiv**: [2603.13266](https://arxiv.org/abs/2603.13266)

## Key Contributions
- **EMBRAG framework** — a *three-stage embedding-space reasoning pipeline* (rule generation → embedding-space rule application → reranking) that bypasses the brittleness of pure-symbolic KG traversal over noisy/incomplete knowledge graphs by keeping reasoning inside the embedding space but conditioning the rules on KG-grounded logical forms.
- **Logical-rule-guided embedding-space reasoning** — generates *multiple candidate logical rules from the KG* (handling query interpretation ambiguity) and applies each in the embedding space (handling KG incompleteness via semantic neighborhood), so each rule's embedding-space application can succeed even when the symbolic KG has missing triples.
- **Reranker over rule-derived trajectories** — a *post-hoc reranker interprets the rule-space trajectories and refines the final answer*, decoupling the symbolic-rule generation from the embedding-space reasoning and the answer selection, which makes the system robust to low-quality rules.
- **State-of-the-art KGQA** — extensive experiments on two benchmark KGQA datasets demonstrate new SOTA performance in KG reasoning tasks.

## Related Papers
- [[chartwalker-benchmarking-the-cross-chart-rag-task-with-hierarchical-knowledge-graphs-2606.23997]] — Sibling from Run 81 area that uses hierarchical KG construction for cross-chart RAG; complementary graph-structured-reasoning primitive.
- [[navigating-unreliable-parametric-and-contextual-knowledge-explicit-knowledge-conflict-resolution-2606.20245]] — Sibling that addresses unreliable parametric-vs-contextual knowledge conflict resolution; complementary KG-grounded reasoning primitive for KB-vs-LLM reconciliation.
- [[memory-is-reconstructed-not-retrieved-graph-memory-llm-agents-2606.06036]] — Sibling from Run 65+ area exploring graph memory primitives for LLM agents; complementary graph-as-representation primitive.
- [[local-causal-attribution-of-chain-of-thought-reasoning-2606.21821]] — Parent run-paper (Run 83 — CAUSAL-INFERENCE-PROBE) that introduced local causal attribution via SCM on CoT units; complementary reasoning-trace-level primitive.