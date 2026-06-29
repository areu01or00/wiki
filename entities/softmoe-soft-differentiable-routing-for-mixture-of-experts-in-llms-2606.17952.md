---
title: "SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [architecture, sparse, llm]
sources: ["https://arxiv.org/abs/2606.17952"]
---

# SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs

## Overview
SoftMoE replaces the standard hard top-k routing in Mixture-of-Experts architectures with a *soft, fully differentiable* routing mechanism. Instead of each token being routed to a discrete subset of k experts, SoftMoE computes a weighted combination of all expert outputs, where the weights are learned routing probabilities. This transforms MoE from a sparse conditional-computation scheme into a dense but efficient architecture — all parameters remain active but each token's effective computation is still concentrated on the most relevant expert subspaces. The key insight is that the routing function itself is learnable end-to-end via standard backpropagation, removing the discrete routing decision that causes load-balancing issues, expert collapse, and training instability in hard-routing MoE variants.

## Key Facts
- **Authors**: Research team (arXiv:2606.17952)
- **Year**: 2026
- **arXiv**: [2606.17952](https://arxiv.org/abs/2606.17952)

## Key Contributions
- **Fully differentiable routing**: Replaces hard top-k selection with a soft weighted combination of all expert outputs, enabling end-to-end gradient-based optimization of the routing function
- **Scalability to thousands of experts**: Unlike hard-routing MoE which suffers from load imbalance with many experts, SoftMoE's soft routing naturally handles large expert counts without auxiliary balancing losses
- **Theoretical grounding**: Shows that SoftMoE can be interpreted as a neural network with shared experts and learned input-dependent gating — bridging MoE and mixture-of-experts literature
- **Empirical validation**: Demonstrates that SoftMoE matches or exceeds the quality of dense baselines while maintaining the parameter efficiency of sparse MoE, with improved training stability

## Related Papers
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Theoretical task routing companion; Task-Routing-Theory provides the formal framework for understanding routing in MoE while SoftMoE offers a differentiable instantiation
- [[routing-free-mixture-of-experts-eliminating-centralized-routing-2604.00801]] — Routing-free MoE (Run 67 pick) that removes the router entirely via autonomous expert activation; shares the goal of eliminating hard routing but takes the opposite architectural approach
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — Granular compute allocation companion; SoftMoE's soft routing can be seen as a fine-grained compute allocation mechanism at the token-expert intersection
