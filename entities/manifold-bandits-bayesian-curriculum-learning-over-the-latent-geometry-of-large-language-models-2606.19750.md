---
title: "Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [reinforcement-learning, curriculum-learning, llm-reasoning, bandit-algorithms, training-efficiency]
sources: ["https://arxiv.org/abs/2606.19750"]
---

# Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models

## Overview
A curriculum-learning framework for LLM reinforcement learning that replaces standard adaptive sampling — which treats prompts as independent bandit arms — with a Bayesian model over the latent geometry of problem difficulty. By exploiting geometric structure in the embedding space of problems, Manifold Bandits improves sample efficiency on reasoning-RL tasks and avoids the exploration pathologies that arise when difficulty is treated as a scalar decoupled from related problems.

## Key Facts
- **Authors**: McKenzie, Darrien; Hansen, Nicklas; Wang, Xiaolong
- **Year**: 2026
- **arXiv**: [2606.19750](https://arxiv.org/abs/2606.19750)
- **Subjects**: cs.LG; cs.CL; stat.ML

## Key Contributions
- Reformulation of LLM RL curriculum learning as Bayesian optimization over a learned manifold of problem difficulty, replacing the standard "each prompt is an independent arm" formulation with a Gaussian-process-style posterior that shares statistical strength across geometrically similar problems — yielding substantially better sample efficiency on reasoning-RL benchmarks.
- Empirical isolation of the geometric-priors effect: shows that on reasoning tasks where problems cluster meaningfully in embedding space, curriculum learning that exploits the manifold structure reaches a target reasoning accuracy with materially fewer environment steps than independent-arm bandit baselines, and that the gains are concentrated in the early- and mid-training regime where exploration matters most.
- A bridge between the bandit-optimization literature and the LLM-RL training literature: prior curriculum-learning work treated prompt sampling as a multi-armed bandit with independent arms; this paper shows the assumption is empirically false for LLM reasoning tasks (problem embeddings are informative) and provides a drop-in replacement that respects the geometric structure.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this entity was first indexed via emergent-concept search on 2026-06-25 (LLM RL training efficiency / curriculum-learning geometry theme).
- [[holistic-data-scheduler-for-llm-pre-training-via-multi-objective-reinforcement-learning-2606.24133]] — Complementary RL-for-data work: Holistic Data Scheduler uses multi-objective RL for data mixing, Manifold Bandits uses Bayesian optimization over problem geometry for prompt sampling — both attack the LLM-training stack at the curriculum/allocation layer rather than the model-architecture layer.
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Complementary data-allocation framing: AC-ODM optimizes pretraining data mixing via actor-critic RL, Manifold Bandits optimizes RL-prompt sampling via Bayesian optimization over latent difficulty geometry — both improve training efficiency by replacing scalar heuristics with structured sampling policies.
- [[beyond-reward-engineering-a-data-recipe-for-long-context-reinforcement-learning-2606.18831]] — Both are RL-training-efficiency contributions; Beyond Reward Engineering shows that data-recipe design dominates reward-shaping for long-context RL, and Manifold Bandits shows that curriculum-geometry structure dominates independent-arm sampling for reasoning RL — together framing "what to sample" as the load-bearing RL training decision.
