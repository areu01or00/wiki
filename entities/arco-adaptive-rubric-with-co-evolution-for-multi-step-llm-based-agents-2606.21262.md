---
title: "ARCO: Adaptive Rubric with Co-Evolution for Multi-Step LLM-Based Agents"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [agentic-RL, rubric-reward, credit-assignment, multi-step-planning]
sources: ["https://arxiv.org/abs/2606.21262"]
---

# ARCO: Adaptive Rubric with Co-Evolution for Multi-Step LLM-Based Agents

## Overview
Reinforcement learning for multi-step LLM agents relies on scalar success rewards that cannot explain *why* a trajectory is good or bad. Rubric-based rewards improve interpretability via natural-language criteria, but existing methods score only at trajectory level and freeze the scorer. ARCO proposes an adaptive rubric with co-evolution between policy and scorer, enabling step-level credit assignment in multi-step LLM-based agents.

## Key Facts
- **Authors**: Tian, Zihang; Zhang, Jingsen; Li, Rui + 3
- **Year**: 2026
- **arXiv**: [2606.21262](https://arxiv.org/abs/2606.21262)

## Key Contributions
- Adaptive rubric co-evolution: scorer and policy train jointly, both improve over time
- Step-level credit assignment (not just trajectory-level) via natural-language rubric criteria
- Addresses frozen-scorer problem of closed-source judges in rubric-based RL
- Interpretable reward decomposition at the step level for multi-step agent tasks

## Related Papers
- [[arco-adaptive-rubric-with-co-evolution-for-multi-step-llm-based-agents-2606.21262]] — (self-reference for cross-run discovery context)
