---
title: "Anisotropy Decides Cosine vs. Rank Metrics for Text Embeddings"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [embeddings, evaluation, representation, llm]
sources: ["https://arxiv.org/abs/2606.29571"]
---

# Anisotropy Decides Cosine vs. Rank Metrics for Text Embeddings

## Overview
The standard way to compare two text embeddings is cosine similarity — but scattered prior work reports that rank-based metrics sometimes outperform it, without ever pinning down the geometric condition that decides when and why. This paper resolves the debate with a comprehensive empirical study across 19 parameter-free similarity metrics and a theoretical analysis linking the geometry of embedding anisotropy to metric selection.

## Key Facts
- **Authors**: Parupudi, V. S. Raghu
- **Year**: 2026
- **arXiv**: [2606.29571](https://arxiv.org/abs/2606.29571)

## Key Contributions
- Identifies embedding anisotropy as the fundamental geometric property that determines whether cosine similarity or rank-based metrics perform better
- 19-metric empirical study establishing a decision boundary based on the anisotropy-spectrum structure of the embedding space
- Practical guideline: if embedding directions are clustered (high anisotropy), rank metrics dominate; if uniformly distributed (low anisotropy), cosine similarity is optimal
- Explains why prior work gave conflicting results — they sampled embeddings with different anisotropy profiles

## Related Papers
- [[from-reasoning-traces-to-reusable-modules-understanding-compositional-generalization-in-language-model-reasoning-2606.18089]] — Compositional generalization and embedding anisotropy are both representation-structure properties; this paper provides the metric selection lens for the same geometric phenomenon
