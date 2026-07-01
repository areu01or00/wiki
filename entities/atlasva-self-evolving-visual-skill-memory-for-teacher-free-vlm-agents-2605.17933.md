---
title: "AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [VLM agents, embodied AI, skill memory, self-evolution, reinforcement learning]
sources: ["https://arxiv.org/abs/2605.17933"]
---

# AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents

## Overview
AtlasVA addresses a core瓶颈 in VLM agents: existing memory-augmented RL frameworks store memory as text and depend on proprietary teacher models to summarize/refine it — a poor fit for visual skill reuse across long-horizon tasks. AtlasVA introduces a teacher-free self-evolving visual skill memory where the agent autonomously encodes, retrieves, and refines visual routines without external supervision.

## Key Facts
- **Authors**: Wang, Pan; Hu, Yihao; Liu, Xiujin + 3
- **Year**: 2026
- **arXiv**: [2605.17933](https://arxiv.org/abs/2605.17933)
- **Discovered**: 2026-07-01 (Run 287)
- **Theme**: VLM agent skill memory / teacher-free self-evolution / visual routine encoding

## Key Contributions
- Teacher-free visual skill memory: no proprietary teacher needed to summarize or refine skills
- Self-evolving memory: the agent autonomously updates its skill library based on task outcomes
- Visual skill encoding: stores visual routines (not just text descriptions) enabling richer reuse across tasks
- Long-horizon task reuse: demonstrates transfer across extended multi-task horizons

## Related Papers
- [[adamem-learning-what-to-remember-for-personalized-long-horizon-llm-agents-2606.21144]] — Adaptive memory for long-horizon agents (different memory substrate — text-based vs AtlasVA's visual skill encoding)
- [[adamem-test-time-adaptive-memory-for-language-agents-2606.05684]] — Test-time adaptive memory; AtlasVA extends this to the visual-skill/self-evolutional axis
- [[agent-memory-characterization-and-system-implications-of-stateful-long-horizon-workloads-2606.06448]] — Memory characterization taxonomy relevant to AtlasVA's storage architecture
