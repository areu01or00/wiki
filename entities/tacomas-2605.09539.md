---
title: "TacoMAS: Test-Time Co-Evolution of Topology and Capability in LLM-based Multi-Agent Systems"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [multi-agent-systems, test-time-scaling, llm]
sources: ["https://arxiv.org/abs/2605.09539"]
---

# TacoMAS: Test-Time Co-Evolution of Topology and Capability in LLM-based Multi-Agent Systems

## Overview
Multi-agent systems (MAS) have emerged as a promising paradigm for solving complex tasks. Recent work has explored self-evolving MAS that automatically optimize agent capabilities or communication topologies. However, existing methods either learn a fixed topology and then optimize capabilities, or vice versa — treating these as sequential rather than joint problems. This paper proposes TacoMAS, a test-time co-evolution framework that simultaneously optimizes both agent topology and individual agent capabilities. TacoMAS formulates MAS inference as online graph adaptation where agent roles and inter-agent connections co-evolve based on task demands, and jointly optimizes a graph neural network controller and per-agent capability parameters via meta-learning.

## Key Facts
- **Authors**: Chen Xu, Yicheng Hu, Ruizi Wang, Xinyu Lin, Wenjie Wang, Dongrui Liu, Fuli Feng
- **Year**: 2026
- **arXiv**: [2605.09539](https://arxiv.org/abs/2605.09539)

## Key Contributions
- Proposes TacoMAS, the first test-time co-evolution framework that jointly optimizes both agent topology and individual agent capabilities simultaneously
- Formulates MAS inference as online graph adaptation where agent roles and inter-agent connections co-evolve based on task demands
- Jointly optimizes a graph neural network controller and per-agent capability parameters via meta-learning
- Outperforms state-of-the-art single-aspect methods (topology-only or capability-only) across diverse multi-agent benchmarks
- Orthogonal to GenEnv (difficulty-aligned environment-agent co-evolution) and TMAS (multi-agent synergy via test-time compute) by treating topology and capability as coupled rather than independent

## Related Papers
- [[tmas-scaling-test-time-compute-via-multi-agent-synergy-2605.10344]] — TMAS organizes multi-agent inference as collaborative process with hierarchical memories; orthogonal to TacoMAS's graph neural network topology optimization
- [[genenv-difficulty-aligned-co-evolution-between-llm-agents-and-environment-simulators-2512.19682]] — GenEnv co-evolves agent and environment difficulty; orthogonal to TacoMAS's agent-agent topology co-evolution
