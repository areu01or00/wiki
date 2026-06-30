---
title: "Experience Augmented Policy Optimization for LLM Reasoning"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [reinforcement-learning, reasoning, llm]
sources: ["https://arxiv.org/abs/2606.30420"]
---

# Experience Augmented Policy Optimization for LLM Reasoning

## Overview
RLVR (Reinforcement Learning with Verifiable Rewards) is a powerful paradigm for improving LLM reasoning, but existing methods rely on on-policy optimization from scratch, resulting in high sampling costs and inefficient use of accumulated experience. This paper introduces Experience Augmented Policy Optimization (EAPO), which reuses historical reasoning trajectories to reduce sample complexity while maintaining policy improvement.

## Key Facts
- **Authors**: Unknown
- **Year**: 2026
- **arXiv**: [2606.30420](https://arxiv.org/abs/2606.30420)

## Key Contributions
- Experience replay mechanism for RLVR that conditions on the agent's own acquired skills, providing dense token-level supervision without external retrieval
- Reduces sampling cost by reusing high-quality reasoning traces from prior policy versions
- Maintains policy improvement guarantees while significantly improving data efficiency

## Related Papers
- [[self-improvement-can-self-regress-rise-and-collapse-llm-self-training-2606.21090]] — Prior self-improvement via experience replay in LLM RL training
- [[beyond-reward-engineering-a-data-recipe-for-long-context-reinforcement-learning-2606.18831]] — Data recipe for long-context RL relevant to experience reuse
