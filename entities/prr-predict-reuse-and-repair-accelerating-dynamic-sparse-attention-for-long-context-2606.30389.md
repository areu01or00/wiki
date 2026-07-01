---
title: "Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, long-context, sparse-attention, speculative-decoding, kv-cache]
sources: ["https://arxiv.org/abs/2606.30389"]
---

# Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding

## Overview
PRR is a speculate-reuse-repair runtime that addresses the serialized selection-to-attention dependency bottleneck introduced by dynamic sparse attention (DSA) in long-context LLM decoding. DSA attend to only top-K KV blocks per query, but the selection is the bottleneck. PRR exploits temporal locality in DSA selections via EMA-based prediction, speculative execution, and an incremental repair kernel using FlashAttention-based repair with online-softmax statistics. Reduces per-token decoding latency by up to 40% while preserving downstream accuracy.

## Key Facts
- **Authors**: Tianyu Wang, Gourav Rattihalli, Aditya Dhakal, Junbo Li, Zhiwei Ren, Dejan Milojicic, Longfei Shangguan
- **Year**: 2026
- **arXiv**: [2606.30389](https://arxiv.org/abs/2606.30389)

## Key Contributions
- **EMA-based temporal locality predictor** — lightweight exponential moving average predictor exploits temporal locality in DSA block selections to predict likely blocks before selection completes
- **Speculative execution off critical path** — profiling-guided speculation budget keeps speculative work off the critical path while waiting for serialized selection
- **FlashAttention-based incremental repair kernel** — folds missed blocks into partial attention state using online-softmax statistics; integrates missed blocks incrementally rather than recomputing
- **40% latency reduction** on long-context benchmarks and DSA methods while preserving task accuracy

## Related Papers
- [[dustin-draft-augmented-sparse-verification-for-efficient-long-context-generation-with-speculative-decoding-2606.24957]] — sibling on sparse verification for speculative decoding (different verification axis — PRR uses repair, Dustin uses draft-augmented verification)
- [[jetspec-breaking-the-scaling-ceiling-of-speculative-decoding-with-parallel-tree-2606.18394]] — related speculative decoding efficiency
- [[dart-diffusion-inspired-speculative-decoding-for-fast-llm-inference-2601.19278]] — related speculative decoding
