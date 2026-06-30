---
title: "SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent, reinforcement-learning, uncertainty, self-evolution]
sources: ["https://arxiv.org/abs/2602.21158"]
---

# SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards

## Overview
SELAUR addresses a key gap in reward design for multi-step LLM decision-making agents: the intrinsic uncertainty of LLMs. Uncertainty reflects model confidence, reveals where exploration is needed, and offers valuable learning cues even in failed trajectories. SELAUR uses this uncertainty signal as a self-supervised reward for agent self-evolution without requiring external reward engineering.

## Key Facts
- **Authors**: Dengjia Zhang, Xiaoou Liu, Lu Cheng, Yaqing Wang, Kenton Murray, Hua Wei
- **Year**: 2026
- **arXiv**: [2602.21158](https://arxiv.org/abs/2602.21158)

## Key Contributions
- Intrinsic LLM uncertainty as a learnable self-supervised reward signal
- Uncertainty-aware exploration guidance without external reward engineering
- Step-level credit assignment via uncertainty signals in failed trajectories
- Agent self-evolution framework requiring no human-designed rewards

## Related Papers
- [[worldevolver-self-evolving-world-models-for-llm-agent-planning-2606.30639]] — WorldEvolver's self-evolving world models; both explore self-evolution without external supervision
- [[q-evolve-self-evolving-llm-agents-with-in-distribution-optimization-2606.07367]] — Q-Evolve's IDROptimization complements SELAUR's uncertainty-based approach
- [[rise-reliable-improvement-in-self-evolving-vision-language-models-2605.20914]] — Rise's VLM self-evolution reliability; orthogonal to SELAUR's uncertainty-driven RL framework
