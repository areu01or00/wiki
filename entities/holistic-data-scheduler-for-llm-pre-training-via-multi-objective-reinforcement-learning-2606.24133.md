---
title: "Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [pretraining, data-mixing, reinforcement-learning, llm, training]
sources: ["https://arxiv.org/abs/2606.24133"]
---

# Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning

## Overview
Holistic Data Scheduler reframes online data mixing for LLM pretraining as a multi-objective reinforcement learning problem, replacing single-scalar objectives with a Pareto-style trade-off across competing pre-training desiderata. Where prior Online Data Mixing (ODM) methods optimize one proxy at a time, this work trains a scheduler that adaptively reweights heterogeneous sources so the corpus simultaneously respects diversity, domain balance, and downstream signal distributions. The result is a drop-in data scheduler that improves pretraining efficiency and downstream evaluation without per-domain manual re-tuning.

## Key Facts
- **Authors**: Dang, Chenhao; Ma, Jing; Liao, Mingjie
- **Year**: 2026 (2026-06-23)
- **arXiv**: [2606.24133](https://arxiv.org/abs/2606.24133)
- **Subjects**: cs.LG

## Key Contributions
- Formalizes online data mixing as a multi-objective RL problem, exposing the Pareto trade-off between data quality, diversity, and downstream-task balance that single-objective ODM methods hide.
- Introduces a scheduler that adaptively reweights data sources during pretraining with a holistic reward signal rather than per-source scalar rewards.
- Demonstrates empirical gains in pretraining efficiency and downstream benchmarks vs. existing ODM baselines, with reduced sensitivity to manual mixing hyperparameters.
- Provides ablations isolating the contribution of multi-objective framing vs. the underlying RL machinery.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on the data-mixing/pretraining-efficiency theme cluster.
