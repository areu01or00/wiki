---
title: "∇-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, test-time-compute, latent-space, optimization]
sources: ["https://arxiv.org/abs/2603.04948"]
---

# ∇-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space

## Overview
Proposes ∇-Reasoner, an iterative generation framework that integrates differentiable optimization over token logits into the decoding loop to refine the policy on-the-fly at test time. The core component, Differentiable Textual Optimization (DTO), leverages gradient signals from both the LLM's likelihood and a reward model. Theoretically shows that inference-time gradient descent in sample space to maximize reward is dual to KL-regularized RL alignment. Empirically achieves 20%+ accuracy improvement on math reasoning with 10-40% fewer model calls versus strong baselines.

## Key Facts
- **Authors**: Peihao Wang, Ruisi Cai, Zhen Wang, Hongyuan Mei, Qiang Liu, Pan Li, Zhangyang Wang
- **Year**: 2026
- **arXiv**: [2603.04948](https://arxiv.org/abs/2603.04948)
- **Submitted**: 5 Mar 2026
- **Venue**: ICLR 2026

## Key Contributions
- First-order (gradient-based) optimization paradigm for test-time reasoning scaling, replacing zeroth-order search (beam search, majority voting)
- Differentiable Textual Optimization (DTO): backpropagates through LLM decoding to refine token representations using reward model gradients
- Rejection sampling + acceleration design for robust and faster decoding
- Theoretical duality: test-time gradient descent in sample space ≡ KL-regularized RL alignment
- Results: 20%+ accuracy on math reasoning benchmarks; 10-40% fewer model calls vs baseline

## Related Papers
- [[llm-reasoning-is-latent-not-the-chain-of-thought-2604.15726]] — Position paper arguing latent-state dynamics are the primary medium of LLM reasoning
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Latent computational mode in LLMs as a reasoning substrate
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Test-time compute allocation for reasoning LLMs
