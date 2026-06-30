---
title: "UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [inference-efficiency, test-time-scaling, llm]
sources: ["https://arxiv.org/abs/2605.30898"]
---

# UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling

## Overview
In real-world deployments of large language models (LLMs), balancing inference quality and computational cost has become a central challenge. Existing approaches tackle this trade-off along two largely independent dimensions: model routing, which switches among models of different scales, and test-time scaling, which allocates more compute within a single forward pass. This paper proposes UniScale, a unified inference scaling framework that jointly optimizes model routing and test-time scaling via online contextual multi-armed bandits.

## Key Facts
- **Authors**: Kaiyu Huang, Xingyu Wang, Mingze Kong, Zhubo Shi, Yuqian Hou, Hong Xu, Zhongxiang Dai, Minchen Yu, Qingjiang Shi
- **Year**: 2026
- **arXiv**: [2605.30898](https://arxiv.org/abs/2605.30898)

## Key Contributions
- Proposes the Unified Inference Scaling (UIS) paradigm that integrates model routing and Test-Time Scaling (TTS) into a unified decision space
- Designs UniScale, an adaptive framework based on contextual multi-armed bandits that jointly optimizes both dimensions online
- Casts the joint optimization as a combinatorial bandit with knapsack constraints, achieving Pareto-optimal quality-cost trade-offs without offline training
- Orthogonal to prior test-time scaling papers (Grace, MARS, MaxProof, EfficientBranchRouting) which focus on single-model allocation rather than cross-model routing

## Related Papers
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — Granularity-regulated adaptive computational efficiency for single-model verification; orthogonal to UniScale's cross-model routing approach
- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — Local branch routing for single-model test-time scaling; orthogonal to UniScale's joint model-routing + test-time-compute optimization
