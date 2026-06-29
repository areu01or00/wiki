---
title: "Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, llm-pruning, benchmarking, optimization]
sources: ["https://arxiv.org/abs/2606.09080"]
---

# Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy

## Overview
Beyond FLOPs exposes the gap between theoretical FLOP reduction and actual wall-clock inference speedup from LLM pruning. Using a GEMM-centric taxonomy that maps pruning patterns to actual matrix multiplication efficiency, the paper demonstrates that many established pruning methods fail to deliver proportional speedups in practice due to hardware-aware considerations like memory bandwidth, cache behavior, and irregular access patterns.

## Key Facts
- **Authors**: [arXiv 2606.09080](https://arxiv.org/abs/2606.09080)
- **Year**: 2026
- **arXiv**: [2606.09080](https://arxiv.org/abs/2606.09080)
- **Online Date**: 2026/06/08

## Key Contributions
- GEMM-centric pruning taxonomy that maps structural pruning to actual hardware efficiency
- Systematic benchmarking showing FLOP reduction ≠ actual speedup for many pruning methods
- Identifies memory bandwidth and irregular access as primary bottlenecks for non-structural pruning
- Evaluation framework for assessing pruning methods on real hardware, not just theoretical metrics

## Related Papers
- [[emergent-concepts]] — Parent emergent concept discovery chain
