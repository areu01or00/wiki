---
title: "AC-ODM: Actor--Critic Online Data Mixing for Sample-Efficient LLM Pretraining"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [pretraining, data-mixing, actor-critic, online-learning, llm-research]
sources: ["https://arxiv.org/abs/2505.23878"]
---

# AC-ODM: Actor--Critic Online Data Mixing for Sample-Efficient LLM Pretraining

## Overview
AC-ODM is an online data mixing framework for LLM pretraining that combines actor--critic reinforcement learning with a quality-aware reward signal to adaptively reweight heterogeneous pretraining corpora. The method addresses the failure mode of static or single-objective online data mixing (ODM) by jointly optimizing a mixing policy and a value baseline, yielding sample-efficient pretraining on fixed compute budgets.

## Key Facts
- **Authors**: Ma, Jing, Dang, Chenhao, Liao, Mingjie
- **Year**: 2026
- **Date**: 2026-06-23
- **arXiv**: [2505.23878](https://arxiv.org/abs/2505.23878)
- **Subjects**: Machine Learning (cs.LG)

## Key Contributions
- Actor--critic formulation for online data mixing that separates the mixing policy (actor) from the value estimator (critic), enabling stable training under shifting pretraining distributions
- Quality-aware reward signal that combines downstream evaluation proxies with corpus-level statistics, avoiding the brittleness of single-scalar ODM objectives
- Empirical demonstration of sample-efficient pretraining: matches or exceeds static-mixing baselines on standard language modeling benchmarks at matched token budgets
- A plug-in design compatible with existing LLM pretraining pipelines (no architectural changes to the model)

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[holistic-data-scheduler-for-llm-pre-training-via-multi-objective-reinforcement-learning-2606.24133]] — Complementary multi-objective-RL pretraining scheduler