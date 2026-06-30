---
title: "Reformulate LLM Reinforcement Learning for Efficient Training under Black-box Discrepancy"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [reinforcement-learning, training-efficiency, llm-post-training]
sources: ["https://arxiv.org/abs/2606.08779"]
---

# Reformulate LLM Reinforcement Learning for Efficient Training under Black-box Discrepancy

## Overview
DCMDP (Discrepancy-Constrained Markov Decision Process) addresses RL training collapses in LLMs caused by train-inference discrepancy — the mismatch between high-fidelity training engines and low-cost deployment engines. It formulates dual-objective optimization coupling reward maximization with discrepancy constraint, using Lagrangian relaxation for adaptive balancing.

## Key Facts
- **Authors**: 
- **Year**: 2026
- **arXiv**: [2606.08779](https://arxiv.org/abs/2606.08779)

## Key Contributions
- Discrepancy tolerance region characterization for LLM RL post-training
- DCMDP formulation coupling reward maximization with training-inference alignment
- Lagrangian relaxation mechanism for adaptive discrepancy control
- Validated on Qwen-3-8B and Qwen-3-30bA3B (MoE) — enables heterogeneous training-deployment paradigm

## Related Papers
- [[learning-from-own-solutions-self-conditioned-credit-assignment-for-reinforcement-learning-with-verifiable-rewards-2606.18810]] — Self-conditioned credit assignment for RLVR with verifiable rewards
