---
title: "ManimAgent: Self-Evolving Multimodal Agents for Visual Education"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multimodal-agents, self-evolution, code-generation, visual-education, reflection]
sources: ["https://arxiv.org/abs/2606.30296"]
---

# ManimAgent: Self-Evolving Multimodal Agents for Visual Education

## Overview
ManimAgent tackles the problem of episodic forgetting in multi-round reflection-based LLM agents: each task is solved in isolation and lessons from prior reflection rounds are discarded before the next task begins. The paper studies this on a compelling task — generating Python animations via the Manim library from scientific paper sections — and introduces a self-evolving agent that carries forward implicit activation patterns across reflection rounds on different tasks.

## Key Facts
- **Authors**: Wenjia Jiang, Zongyuan Cai, Yuanhang Shao, Chenru Wang, Boyan Han, Zhixue Song, Keyu Chen, Shengwei An, Xu Yang, Zhou Yang
- **Year**: 2026
- **arXiv**: [2606.30296](https://arxiv.org/abs/2606.30296)

## Key Contributions
- Self-evolving multimodal agent for visual education via code generation (Manim library)
- Implicit activation steering across reflection rounds —学到 knowledge/patterns transfer between tasks
- Multi-round reflection recovers from failures within a task, but ManimAgent extends this to cross-task evolution
- Procedural memory: implicit activation patterns (not just explicit plan的记忆) carried forward across episodes
- Scientific animation generation as a compelling testbed for multimodal self-evolution

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts wiki
