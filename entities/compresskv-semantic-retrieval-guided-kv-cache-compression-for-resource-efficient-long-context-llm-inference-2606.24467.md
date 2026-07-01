---
title: "CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, KV-cache, long-context, compression, GQA, memory-optimization]
sources: ["https://arxiv.org/abs/2606.24467"]
---

# CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference

## Overview
CompressKV addresses the memory footprint and decoding cost bottleneck of KV caches in long-context LLM inference on resource-constrained hardware. Unlike prior heuristic token scoring across all heads, CompressKV identifies Semantic Retrieval Heads (SRHs) that capture both initial/final tokens and semantically important mid-context evidence, using them to selectively retain KV pairs. Allocates cache budgets across layers via offline layer-wise eviction error estimates. Preserves over 97% of full-cache performance using only 3% of KV cache on LongBench.

## Key Facts
- **Authors**: CompressKV team
- **Year**: 2026
- **arXiv**: [2606.24467](https://arxiv.org/abs/2606.24467)

## Key Contributions
- Semantic Retrieval Heads (SRHs): attention heads that capture initial tokens, final tokens, and semantically important mid-context evidence
- Per-layer cache budget allocation via offline layer-wise eviction error estimates
- 97% of full-cache performance with only 3% KV cache on LongBench QA tasks
- 90% accuracy with 0.7% KV storage on Needle-in-a-Haystack
- Improved resource-performance trade-off for long-context LLM inference vs. all prior KV cache eviction methods

## Related Papers
- [[context-recycling-for-long-horizon-llm-inference-2606.26105]] — Context Recycling for Long-Horizon LLM Inference (complementary: both address long-context inference efficiency)
- [[coverage-driven-kv-cache-eviction-kvec-2606.29563]] — KVEC: Coverage-Driven KV-Cache Eviction (related axis: both KV cache compression for inference efficiency)
- [[crystal-kv-efficient-kv-cache-management-chain-thought-2601.16986]] — Crystal-KV: KV cache management for chain-of-thought (related axis: KV cache optimization for multi-step reasoning)
