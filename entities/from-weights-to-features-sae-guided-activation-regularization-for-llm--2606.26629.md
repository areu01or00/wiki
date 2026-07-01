---
title: "From Weights to Features: SAE-Guided Activation Regularization for LLM Continual Learning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [continual-learning, catastrophic-forgetting, llm, regularization, sae]
sources: ["https://arxiv.org/abs/2606.26629"]
---

# From Weights to Features: SAE-Guided Activation Regularization for LLM Continual Learning

## Overview
Weight-space regularization methods like Elastic Weight Consolidation (EWC) are the standard approach to catastrophic forgetting in continual learning, but they underperform on large language models. This paper argues this gap stems from the polysemantic nature of LLMs — per-weight importance estimates collapse when individual weights encode multiple overlapping features. The authors propose SAE-Guided Activation Regularization, which uses Sparse Autoencoder (SAE) decompositions to regularize at the feature level instead of the weight level, preserving task-specific activations without being disrupted by weight polysemanticity.

## Key Facts
- **Authors**: Ning, Evan; Xue, Wei; Lou, Dong; Guo, Yike
- **Year**: 2026
- **arXiv**: [2606.26629](https://arxiv.org/abs/2606.26629)
- **Date**: 2026-06-25

## Key Contributions
- Diagnoses why EWC-style weight-space regularization underperforms on LLMs (polysemanticity → collapsed per-weight importance)
- Proposes SAE-Guided Activation Regularization: regularize at the feature activation level rather than weight level
- Demonstrates that SAE features provide more stable task-similarity signals than individual weights
- First paper to use SAE decomposition as a *regularization target* for continual learning in LLMs, not just for interpretability

## Related Papers
- [[learning-is-forgetting-llm-training-as-lossy-compression-2604.07569]] — Complementary framing: "learning is forgetting" as lossy compression; this paper provides the regularization mechanism to mitigate that phenomenon
- [[robust-uncertainty-quantification-for-self-evolving-llms-via-continual-domain-pretraining-2510.22931]] — Continual domain pretraining with uncertainty quantification; SAE-Reg adds a complementary feature-level regularization layer to CL pipelines
- [[safety-alignment-as-continual-learning-mitigating-the-alignment-tax-via-orthogonal-gradient-projection-2602.07892]] — Safety alignment as continual learning; both papers treat CL as the load-bearing framework for LLM deployment lifecycle
