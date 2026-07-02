---
title: "CausalMix: Data Mixture as Causal Inference for Language Model Training"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [training-data, causal-inference, data-mixture, llm-pretraining]
sources: ["https://arxiv.org/abs/2607.01104"]
---

# CausalMix: Data Mixture as Causal Inference for Language Model Training

## Overview
CausalMix frames data mixture optimization for LLM training as a causal inference problem. Rather than treating data pool shift as a static distribution problem, it models the causal relationship between data mixture weights and downstream model performance under dynamic distribution shifts, enabling seamless scaling from small to large data pools without costly full retraining.

## Key Facts
- **Authors**: Tang, Zinan; Zhang, Yukun; Zheng, Shaomian + 6
- **Year**: 2026
- **arXiv**: [2607.01104](https://arxiv.org/abs/2607.01104)

## Key Contributions
- Causal framing of data mixture optimization as counterfactual inference over mixture weights
- Handles dynamic data pool shift without full retraining from scratch
- Scalable from small settings to large data pools and model sizes
- First causal-inference-based data mixture framework that generalizes across distribution shifts

## Related Papers
- [[holistic-data-scheduler-for-llm-pre-training-via-multi-objective-reinforcement-learning-2606.24133]] — Multi-objective RL data scheduling; complementary to CausalMix's causal framing of mixture optimization
- [[fastmix-fast-data-mixture-optimization-via-gradient-descent-2606.14971]] — Gradient-based data mixture optimization; alternative approach to the same problem space
