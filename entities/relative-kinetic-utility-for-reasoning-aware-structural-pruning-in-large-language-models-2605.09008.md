---
title: "Relative Kinetic Utility for Reasoning-Aware Structural Pruning in Large Language Models"
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [architecture, llm, inference-efficiency, pruning]
sources: ["https://arxiv.org/abs/2605.09008"]
---

# Relative Kinetic Utility for Reasoning-Aware Structural Pruning in Large Language Models

## Overview
Chain-of-Thought (CoT) prompting introduced major reasoning improvements in LLMs but scaling test-time computation produces extensive CoT sequences with severe KV cache memory bottlenecks. This paper proposes Reasoning-Aware Structural Pruning (RASP) — a pruning approach that preserves neurons critical for chain-of-thought reasoning while removing cross-entropic redundant parameters, using a novel Relative Kinetic Utility (RKU) metric that measures per-neuron contribution to reasoning path propagation.

## Key Facts
- **Authors**: Tianhao Qian
- **Year**: 2026 (arXiv 2605.09008, submitted May 2026)
- **arXiv**: [2605.09008](https://arxiv.org/abs/2605.09008)

## Key Contributions
- **Relative Kinetic Utility (RKU) metric**: Novel per-neuron utility measurement capturing contribution to reasoning path propagation — distinguishes pruning targets from CoT-critical neurons that magnitude-based methods incorrectly cut
- **Reasoning-Aware Structural Pruning (RASP)**: Hardware-aware structural pruning framework using RKU to identify and remove CoT-redundant neurons while preserving reasoning-critical attention heads and MLP layers
- **KV Cache Efficiency**: Achieves 2.1x KV cache reduction with <1.5% reasoning accuracy degradation on GSM8K and MATH benchmarks; 3.4x reduction with <3% degradation on multi-step logical deduction tasks
- **Benchmark results**: Outperforms magnitude-based pruning baselines (SparseGPT, Wanda) on CoT reasoning tasks by 12-18 accuracy points at equivalent sparsity ratios

## Related Papers
- [[emergent-concepts]] — Parent page for emergent-concept discoveries
