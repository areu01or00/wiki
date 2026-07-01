---
title: "HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, kv-cache, long-context, llm]
sources: ["https://arxiv.org/abs/2606.28831"]
---

# HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression

## Overview
HARD-KV resolves the "Static-Dynamic mismatch" in long-context LLM inference: head-adaptive compression algorithms offer superior accuracy but modern inference engines (vLLM) require rigid static memory patterns for CUDA Graphs and PagedAttention. HARD-KV introduces a Cascade Cache hierarchy with dense/sparse/condensed tiers, a Logits Calibration mechanism that normalizes heterogeneous head-importance metrics into a unified probability space, and a system-level index rewriting pass that produces contiguous physical layouts. Result: up to 2× throughput improvement while maintaining high-fidelity generation in 10k+ token scenarios.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.28831](https://arxiv.org/abs/2606.28831)

## Key Contributions
- Cascade Cache hierarchy: dense → sparse → condensed token lifecycle management across heterogeneous attention heads
- Logits Calibration: normalizes diverse importance metrics (Top-p dynamics) into unified probability space for consistent budgeting
- System-level index rewriting: fragments dynamic indices into contiguous physical layouts compatible with vLLM's PagedAttention + CUDA Graphs
- 2× throughput improvement on math-reasoning benchmarks (AIME, U-Math) at 10k+ token context lengths

## Related Papers
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — KV-cache quantization with rope awareness; complementary compression axis
- [[refreekv-towards-threshold-free-kv-cache-compression-2502.16886]] — Threshold-free KV-cache compression; HARD-KV's head-adaptive budgeting extends this line
- [[kernelsight-lm-a-kernel-level-llm-inference-simulator-2606.28565]] — LLM inference kernel-level simulation; HARD-KV's system-level optimization complements the simulation perspective
