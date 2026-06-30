---
title: "KernelSight-LM: A Kernel-Level LLM Inference Simulator"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [inference-efficiency, llm, serving, simulation]
sources: ["https://arxiv.org/abs/2606.28565"]
---

# KernelSight-LM: A Kernel-Level LLM Inference Simulator

## Overview
KernelSight-LM is a fine-grained LLM inference simulator that models token-level execution and produces kernel-level latency breakdowns. It decomposes each serving step into a roofline kernel model with a learned efficiency term, a communication model, and a host-overhead model, composed through a discrete-event scheduler that captures prefix caching and continuous batching.

## Key Facts
- **Authors**: (from arxiv abstract extraction — needs author field)
- **Year**: 2026
- **arXiv**: [2606.28565](https://arxiv.org/abs/2606.28565)

## Key Contributions
- Cross-generation tier: predicts per-kernel latency on unseen GPU generation to 12.1% error (1.8x better than roofline baseline)
- Target-measured tier: adds kernel-microbenchmark sweep on target GPU, sharpening per-kernel error to 3.8% (7.3x improvement over baseline)
- End-to-end median errors of 15.4%, 12.8%, 3.0% (TTFT, TPOT, throughput) in cross-generation tier
- Requires far less target-GPU data than prior profiling tools; kernel-level breakdowns support hardware/software co-design and capacity planning
- First kernel-level inference simulator for LLM serving

## Related Papers
- [[emergent-concepts]] — Parent topic node for emergent LLM research
