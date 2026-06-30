---
title: "AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [agent, continual-learning, evaluation]
sources: ["https://arxiv.org/abs/2606.24893"]
---

# AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents

## Overview
AgentOdyssey introduces a procedural text game generation framework for evaluating test-time continual learning agents. The key insight is that genuine continual learning requires interleaving learning and inference throughout deployment — a setting that standard benchmarks miss by treating test time as inference-only. AgentOdyssey generates open-ended text games with rich world dynamics, long-horizon tasks, and automatic evaluation of world knowledge acquisition, episodic memory, exploration diversity, and model cost.

## Key Facts
- **Authors**: Zheyuan Zhang, Zehao Wen, Alvin Zhang, Andrew Wang, Jianwen Xie, Daniel Khashabi, Tianmin Shu
- **Year**: 2026
- **arXiv**: [2606.24893](https://arxiv.org/abs/2606.24893)

## Key Contributions
- Procedural text game generator that produces open-ended environments with rich entities and world dynamics
- Multi-faceted evaluation measuring game progress plus diagnostic tests on world knowledge acquisition, episodic memory, exploration diversity, and model cost
- Reveals that short-term memory benefits multiple agent paradigms and is a critical component of agent test-time training
- Finds that even top agents remain far below human performance on long-horizon tasks despite scaling with stronger base models

## Related Papers
- [[agentic-world-modeling-foundations-capabilities-laws-and-beyond-2604.22748]] — foundational world modeling taxonomy; AgentOdyssey extends this to procedural open-ended evaluation
- [[attribution-guided-continual-learning-for-llms-2605.05285]] — another continual learning primitive; AgentOdyssey focuses on test-time vs. training-time distinction
- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — test-time compute scaling; AgentOdyssey reframes test time as learning, not just compute allocation
