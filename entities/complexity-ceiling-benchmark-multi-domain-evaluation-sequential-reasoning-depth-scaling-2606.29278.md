---
title: "The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [benchmark, reasoning, evaluation, depth-scaling, llm]
sources: ["https://arxiv.org/abs/2606.29278"]
---

# The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling

## Overview
CCB introduces a controlled evaluation of how language-model reasoning decays as the number of required sequential steps grows, across three structurally distinct regimes: grounded spatial state-tracking, abstract symbolic pointer manipulation, and transitive relational inference. The key finding is a geometric per-step decay pattern with widely separated domain ceilings — on transitive relational inference every model collapses by N=5 despite strong performance on the other two regimes.

## Key Facts
- **Authors**: Chapra, Kumar, Mandal, Sinha
- **Year**: 2026
- **arXiv**: [2606.29278](https://arxiv.org/abs/2606.29278)

## Key Contributions
- Geometric per-step decay model: reasoning accuracy decays predictably as sequential depth N grows from 5 to 50
- Domain ceilings: strongest models retain pd>0.92 across N=50 on spatial/symbolic regimes but every model collapses on transitive relational inference by N=5
- TFBC trace-level metric: 14.5% of correct answers across the benchmark are reached via incorrect intermediate reasoning
- k* (mean step at which reasoning first diverges) predicts within-domain accuracy better than parameter count
- Forced verbose state-tracking does not move the ceiling (McNemar p=1.000)

## Related Papers
- [[agentic-reasoning-for-large-language-models-2601.12538]] — Agentic reasoning taxonomy and depth requirements
- [[draft-thinking-learning-efficient-reasoning-in-long-chain-of-thought-llms-2603.00578]] — Efficient reasoning in long chain-of-thought
- [[why-reasoning-fails-to-plan-a-planning-centric-analysis-of-long-horizon-decision-making-in-llm-agents-2601.22311]] — Long-horizon decision making failures in LLM agents
