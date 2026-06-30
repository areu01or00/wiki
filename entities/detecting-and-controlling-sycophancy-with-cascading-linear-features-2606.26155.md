---
title: "Detecting and Controlling Sycophancy with Cascading Linear Features"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [safety, interpretability, sycophancy, activation-steering, llm-alignment]
sources: ["https://arxiv.org/abs/2606.26155"]
---

# Detecting and Controlling Sycophancy with Cascading Linear Features

## Overview
This paper presents an iterative data generation pipeline that isolates cascading linear features responsible for sycophancy — the tendency of LLMs to prioritize user validation over truth. The key innovation is moving beyond simple binary pairs of contrastive samples and instead isolating samples showing degrees of features that scale linearly with behavior, enabling better feature disentanglement. Sycophancy features discovered through cascading samples form linearly separable subspaces that allow selection of model activations more corresponding to desired behavior than LLM-as-a-judge and system prompting baselines.

## Key Facts
- **arXiv**: [2606.26155](https://arxiv.org/abs/2606.26155)
- **Key Subject**: Activation steering via cascading linear feature subspaces for sycophancy control

## Key Contributions
- Introduces cascading linear feature discovery via iterative data generation pipeline
- Shows sycophancy features form linearly separable subspaces enabling interpretable detection and steering
- Demonstrates deterministic scoring and robust steering matching or outperforming LLM-as-a-judge baselines
- Provides lower computational demand and more interpretability guarantees than baseline approaches
- Surfaces *cascading-linear-feature-space* and *sycophancy-as-linearly-separable-subspace* as load-bearing INTERPRETABILITY-SAFETY primitives

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent LLM research discoveries
