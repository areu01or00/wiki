---
title: "IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, kv-cache, long-context, llm]
sources: ["https://arxiv.org/abs/2605.25475"]
---

# IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference

## Overview
IndexMem replaces heuristic KV-cache eviction policies with a learnable indexer that predicts KV-token importance, enabling selective retention of high-value activations during long-context LLM inference. Unlike prior eviction methods (H~2O, KVCate, StreamingLLM) that rely on static or shallow signals, IndexMem trains an indexer to score token importance from the evolving attention context, reducing memory footprint while preserving model quality.

## Key Facts
- **Authors**: (from arxiv 2605.25475)
- **Year**: 2025
- **arXiv**: [2605.25475](https://arxiv.org/abs/2605.25475)

## Key Contributions
- Learnable KV-cache eviction framework with latent memory module that predicts token importance scores
- Indexer trained to identify which KV entries to retain vs evict based on downstream utility
- Reduces KV-cache memory footprint significantly while maintaining model output quality on long-context tasks
- Orthogonal to prior eviction methods — uses learned importance rather than recency or attention-weight heuristics

## Related Papers
- [[coverage-driven-kv-cache-eviction-kvec-2606.29563]] — KVEC: Coverage-Driven KV-Cache Eviction (different eviction strategy, same problem domain)
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — RoPE-Aware Bit Allocation for KV-Cache Quantization (compression axis, orthogonal to eviction)
