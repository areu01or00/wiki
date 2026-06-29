---
title: "Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, self-correction, reinforcement-learning, multi-agent, policy-optimization]
sources: ["https://arxiv.org/abs/2604.07165"]
---

# Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization

## Overview
Proposes T-STAR (Tree-structured Self-Taught Agent Rectification), a framework that recovers the latent tree structure underlying multi-step LLM agent trajectories and assigns credit based on critical steps that disproportionately impact reasoning outcomes — addressing the sparse-reward problem in RL for LLM agents that treat sampled trajectories as independent chains.

## Key Facts
- **Authors**: Li, Yu; Tang, Sizhe; Lan, Tian
- **Year**: 2026
- **arXiv**: [2604.07165](https://arxiv.org/abs/2604.07165)

## Key Contributions
- Tree-structured self-rectification (T-STAR) for multi-turn LLM agent policy optimization
- Addresses sparse-reward failure mode of GRPO treating chains as independent uniform-credit steps
- Identifies and upweights critical steps that disproportionately impact reasoning outcome
- Latent tree structure recovery enables more granular credit assignment than chain-based approaches

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept page for arxiv LLM-research discovery
