---
title: "Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [reasoning, inference-efficiency, test-time-compute, chain-of-thought]
sources: ["https://arxiv.org/abs/2606.15070"]
---

# Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models

## Overview
Large reasoning models (LRMs) solve complex problems via explicit chain-of-thought (CoT) reasoning, but suffer from overthinking — redundant tokens that degrade accuracy. This paper introduces an attention-state adaptive generation mechanism that lets the model learn when to stop reasoning, rather than always generating a fixed-length CoT trace.

## Key Facts
- **Authors**: Jiakai Li, Ke Qin, Rongzheng Wang, Yizhuo Ma, Qizhi Chen, Muquan Li, Shuang Liang
- **Year**: 2026
- **arXiv**: [2606.15070](https://arxiv.org/abs/2606.15070)

## Key Contributions
- Attention-state based stopping criterion that monitors internal representation drift during CoT generation
- Learns a decision boundary for when additional reasoning steps will hurt rather than help
- Reduces token count while improving accuracy on math/reasoning benchmarks (GSM8K, MATH)
- First "learned stopping" approach that doesn't require training a separate binary classifier

## Related Papers
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — Grace: granularity-regulated adaptive computation for optimal verification in test-time scaling
- [[self-verified-distillation-your-language-model-is-secretly-its-own-synthetic-data-pipeline-2605.26132]] — Self-supervised refinement algorithm for LLM post-training
