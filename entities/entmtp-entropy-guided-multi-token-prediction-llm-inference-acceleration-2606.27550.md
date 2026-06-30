---
title: "EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, multi-token-prediction, speculative-decoding, llm]
sources: ["https://arxiv.org/abs/2606.27550"]
---

# EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction

## Overview
EntMTP addresses the mismatch between static speculative decoding topology and variable entropy of natural language. Existing multi-token prediction (MTP) heads use fixed tree-based attention throughout generation, meaning speculation depth stays constant regardless of context. EntMTP is a training-free scheduler that dynamically toggles between tree-based attention topologies conditioned on local generation entropy — matching speculation depth to context predictability to maximize accepted-token throughput.

## Key Facts
- **arXiv**: [2606.27550](https://arxiv.org/abs/2606.27550)
- **Year**: 2026
- **Theme**: inference efficiency / speculative decoding / multi-token prediction

## Key Contributions
- **Entropy-guided topology switching**: Dynamically selects between Pareto-optimal tree attention topologies based on running entropy estimates
- **Training-free**: Works with existing MTP heads without retraining; only the scheduling policy changes
- **Low-entropy regions** (predictable text): Deeper speculation enabled for fast drafting
- **High-entropy regions** (uncertain text): More conservative speculation to avoid error accumulation
- **Results**: 1.15x speedup against Hydra, peak 1.36x against Medusa baselines on Humaneval, ShareGPT, GSM8k, Litbench

## Related Papers
- [[beyond-multi-token-prediction-pretraining-llms-with-future-summaries-2510.14751]] — Multi-token prediction pretraining (prior art)
- [[jetspec-breaking-the-scaling-ceiling-of-speculative-decoding-with-parallel-tree-2606.18394]] — Parallel tree speculative decoding
- [[dart-diffusion-inspired-speculative-decoding-for-fast-llm-inference-2601.19278]] — Diffusion-inspired speculative decoding
- [[dustin-draft-augmented-sparse-verification-for-efficient-long-context-generation-with-speculative-decoding-2606.24957]] — Sparse verification for speculative decoding
