---
title: "Training Transformers for KV Cache Compressibility"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, kv-cache, training, long-context, architecture]
sources: ["https://arxiv.org/abs/2605.05971"]
---

# Training Transformers for KV Cache Compressibility

## Overview
Formalizes KV compressibility as a property of learned representations rather than context alone. Proves that almost any sequence-to-vector function admits both highly compressible and inherently non-compressible transformer implementations. Proposes KV-CAT (KV-Compression Aware Training): a continued pretraining procedure using a train-time KV sparsification policy that masks KV slots during training, forcing the model to learn compressible representations. Improves quality-budget tradeoff for downstream compression methods across retrieval, long-context QA, and perplexity benchmarks.

## Key Facts
- **Authors**: To be confirmed
- **Year**: 2026
- **arXiv**: [2605.05971](https://arxiv.org/abs/2605.05971)

## Key Contributions
- Formal theoretical framework for KV compressibility as a representation property
- Proof that compressible vs non-compressible implementations exist for same function
- KV-CAT continued pretraining procedure with train-time KV slot masking
- Improves quality-budget tradeoff of downstream post-hoc compression methods
- Evaluated on retrieval, LongBench, and perplexity benchmarks

## Related Papers
- [[coverage-driven-kv-cache-eviction-kvec-2606.29563]] — Complementary: both optimize inference efficiency via KV cache management
- [[compresskv-semantic-retrieval-guided-kv-cache-compression-for-resource-efficient-long-context-llm-inference-2606.24467]] — Complementary: both address KV cache compression for long-context inference
