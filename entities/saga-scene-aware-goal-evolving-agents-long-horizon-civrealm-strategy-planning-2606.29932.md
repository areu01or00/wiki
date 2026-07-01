---
title: "SAGA: Scene-Aware, Goal-Evolving Agents for Long-Horizon CivRealm Strategy Planning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent-planning, strategy, multi-agent, scene-understanding, llm]
sources: ["https://arxiv.org/abs/2606.29932"]
---

# SAGA: Scene-Aware, Goal-Evolving Agents for Long-Horizon CivRealm Strategy Planning

## Overview
SAGA addresses three systematic failures in LLM agents for long-horizon strategy games: scene blindness from raw tile coordinates, context overflow from monolithic state dumps, and shallow cross-game learning. It introduces a Map-Semantic Scene Graph for typed spatial reasoning, a goal-evolving mechanism for hierarchical planning, and cross-game generalization via RL.

## Key Facts
- **Authors**: Tianyu Jin, Shuo Chen, Yida Wang, Liuyu Xiang, Yingzhuo Liu, Zhiyao Jiang, Yexin Li, Zhaofeng He
- **Year**: 2026
- **arXiv**: [2606.29932](https://arxiv.org/abs/2606.29932)

## Key Contributions
- Map-Semantic Scene Graph encoding typed spatial relations among game entities — resolves scene blindness from raw tile coordinates
- Goal-evolving mechanism for hierarchical planning across multiple decision domains under imperfect information
- Cross-game RL training enabling generalization beyond single-episode isolation
- CivRealm strategy benchmark evaluation demonstrating superior long-horizon task success vs. monolithic state-dump baselines

## Related Papers
- [[worldevolver-self-evolving-world-models-for-llm-agent-planning-2606.30639]] — WorldEvolver: self-evolving world models for LLM agent planning with foresight (same-day submission, complementary world-model vs scene-graph approaches)
- [[agents-last-exam-2606.05405]] — Agents' Last Exam: LLM agent benchmarking methodology
