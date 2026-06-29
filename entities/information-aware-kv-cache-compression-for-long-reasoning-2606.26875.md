---
title: "Information-Aware KV Cache Compression for Long Reasoning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [inference-efficiency, kv-cache-compression, long-reasoning]
sources: ["https://arxiv.org/abs/2606.26875"]
---

# Information-Aware KV Cache Compression for Long Reasoning

## Overview
First paper in the wiki to introduce a **information-theoretic KV cache compression framework** that periodically compresses the KV cache for generated tokens during long-decoding reasoning — selecting eviction candidates by an information-content score that respects both the per-token semantic contribution and the cumulative decay in the reasoning trace.

## Key Facts
- **Authors**: not extracted
- **Year**: 2026
- **arXiv**: [2606.26875](https://arxiv.org/abs/2606.26875)
- **Date (online)**: 2026-06-28
- **Submission**: 2026-06 (cs.CL)

## Key Contributions
- Periodic KV cache compression during decoding — not only at prefill — keeps long-reasoning traces bounded in memory while preserving reasoning fidelity.
- Information-aware eviction score balances per-token semantic contribution against cumulative decay in the chain-of-thought, surfacing *information-theoretic-eviction-primitive* as the correct retention primitive rather than recency or attention magnitude.
- Extensive experiments on long prefilling and long decoding benchmarks demonstrate that the framework consistently beats recency/attention-magnitude baselines while keeping reasoning accuracy within a narrow margin of the uncompressed baseline.
- Distinguishes itself from recency-window-attention primitives (sliding-window) by using *information-content-driven-eviction*; from attention-magnitude-pruning primitives by using *downstream-decoding-fidelity-loss* as the objective rather than static attention scores.

## Related Papers
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — sibling on KV-cache inference-efficiency primitive (Run 85)
- [[vericache-turning-lossy-kv-cache-into-lossless-llm-inference-2605.17613]] — sibling on lossy/lossless KV-cache compression primitive (Run 59)
- [[efficientrollout-system-aware-self-speculative-decoding-for-rl-rollouts-2606.18967]] — sibling on inference-side efficiency for long rollouts (Run 59)
