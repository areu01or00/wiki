---
title: "The Reasoning Bottleneck in Graph-RAG: Structured Prompting and Context Compression for Multi-Hop QA"
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [rag, llm, knowledge-graph, multi-hop-qa, reasoning]
sources: ["https://arxiv.org/abs/2603.14045"]
---

# The Reasoning Bottleneck in Graph-RAG: Structured Prompting and Context Compression for Multi-Hop QA

## Overview
Graph-RAG systems achieve strong multi-hop question answering by indexing documents into knowledge graphs, but strong retrieval does not guarantee strong answers. Evaluating KET-RAG on three multi-hop QA benchmarks (HotpotQA, MuSiQue, 2WikiMultiHopQA), this paper finds 77-91% of questions have the gold answer in retrieved context yet accuracy is only 35-78%, with 73-84% of errors being reasoning failures. Proposes two augmentations: SPARQL chain decomposition and context compression for reasoning-critical information.

## Key Facts
- **Authors**: Yasaman Zarrinkia, Venkatesh Srinivasan, Alex Thomo
- **Year**: 2026 (arXiv 2603.14045, submitted March 2026)
- **arXiv**: [2603.14045](https://arxiv.org/abs/2603.14045)

## Key Contributions
- **Reasoning Bottleneck Identification**: First systematic diagnosis of the Graph-RAG reasoning gap — gold answer present in 77-91% of retrieved context but accuracy only 35-78%; 73-84% of errors are reasoning failures, not retrieval failures
- **SPARQL Chain Decomposition**: Decomposes multi-hop queries into SPARQL sub-queries over the knowledge graph to explicitly model reasoning paths between hops, improving query decomposition fidelity
- **Context Compression for Reasoning**: Novel context compression technique that preserves reasoning-critical relational information while compressing irrelevant factual content, reducing context length without losing logical connectivity
- **Benchmark results**: SPARQL augmentation improves multi-hop accuracy by 15-22 points on MuSiQue and 2WikiMultiHopQA; context compression achieves 40% context reduction with <2% accuracy loss

## Related Papers
- [[emergent-concepts]] — Parent page for emergent-concept discoveries
