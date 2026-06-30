---
title: "PersuasiveToM: A Benchmark for Evaluating Machine Theory of Mind in Persuasive Dialogues"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [theory-of-mind, benchmarking, persuasion, llm-agents]
sources: ["https://arxiv.org/abs/2502.21017"]
---

# PersuasiveToM: A Benchmark for Evaluating Machine Theory of Mind in Persuasive Dialogues

## Overview
PersuasiveToM addresses a critical gap in ToM evaluation: existing benchmarks use simplified settings (Sally-Anne tasks) that miss the complexity of real-world persuasion. The framework has two core tasks — ToM Reasoning (tracking evolving desires, beliefs, and intentions) and ToM Application (using inferred mental states to predict persuasion strategies). Experiments across 8 leading LLMs show models struggle with dynamic mental state tracking and comprehensive dialogue-level understanding.

## Key Facts
- **Authors**: Fangxu Yu, Lai Jiang, Shenyi Huang, Zhen Wu, Xinyu Dai
- **Year**: 2025
- **arXiv**: [2502.21017](https://arxiv.org/abs/2502.21017)

## Key Contributions
- First ToM benchmark specifically for persuasive dialogue contexts
- Two-task framework: ToM Reasoning + ToM Application
- Reveals that even leading LLMs struggle with dynamic mental state tracking in extended dialogues
- First persuasion-context ToM benchmark in the wiki
- Orthogonal to simplified-style ToM benchmarks (Sally-Anne, ExploreToM)

## Related Papers
- [[decompose-tom-enhancing-theory-mind-reasoning-through-simulation-and-task-decomposition-2501.09056]] — Simulation-theory-driven ToM enhancement via task decomposition (prior simpler ToM methodology)
- [[osctom-rl-guided-adversarial-generation-for-high-order-theory-of-mind-2605.20423]] — RL-guided adversarial ToM generation for nested belief conflicts
- [[think2-grounded-metacognitive-reasoning-in-large-language-models-2602.18806]] — Metacognitive regulatory prompting for adaptive effort allocation
