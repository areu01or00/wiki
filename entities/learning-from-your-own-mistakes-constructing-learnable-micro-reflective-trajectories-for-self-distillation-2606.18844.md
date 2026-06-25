---
title: "Learning from Your Own Mistakes: Constructing Learnable Micro-Reflective Trajectories for Self-Distillation"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [reasoning, rl, self-distillation, llm-research, training-method]
sources: ["https://arxiv.org/abs/2606.18844"]
---

# Learning from Your Own Mistakes: Constructing Learnable Micro-Reflective Trajectories for Self-Distillation

## Overview
The paper introduces Trajectory-Augmented Policy Optimization (TAPO), a self-distillation method that replaces implicit logit-level KL alignment with explicit trajectory construction: during RL training the model produces both correct and incorrect rollouts to the same query, and TAPO builds micro-reflective corrections that retain the model's own erroneous prefix and then insert a natural-language diagnosis plus corrected reasoning anchored to a correct reference from the same sampling group. On AIME 2024/2025 and HMMT 2025, TAPO achieves consistent improvements over GRPO under matched training steps while strengthening both first-pass reasoning and error-correction effectiveness.

## Key Facts
- **Authors**: Huang, Zhilin; Gao, Hang; Dong, Ziqiang; Chen, Yuan; Luo, Yifeng; Qin, Chujun; Wang, Jingyi; Yang, Yang; Jiang, Guanjun
- **Year**: 2026
- **Date**: 2026-06-17
- **arXiv**: [2606.18844](https://arxiv.org/abs/2606.18844)
- **Subjects**: Machine Learning (cs.LG)

## Key Contributions
- TAPO formulation: self-distillation advanced from implicit KL-based distributional alignment to explicit trajectory construction with contrastive micro-reflective corrections anchored in the learner's own prefix
- Difficulty-aware candidate selection at the model's capability boundary plus decoupled advantage estimation that prevents gradient contamination between the on-policy self-distillation signal and the RL reward signal
- Consistent gains over GRPO on AIME 2024, AIME 2025, and HMMT 2025 at matched training-step budgets, with separate first-pass and error-correction improvements
- Theoretical / empirical argument that on-policy trajectory-anchored corrections preserve the learner's distribution better than position-wise KL alignment, which can drift toward a privileged target distribution the model never reaches
- A reusable recipe for any RL-trained reasoning model: contrastive same-prompt sampling, error-preserving prefix construction, and capability-boundary-difficulty filtering are all modular components that compose with standard PPO/GRPO trainers

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[beyond-reward-engineering-a-data-recipe-for-long-context-reinforcement-learning-2606.18831]] — Companion data-recipe perspective on long-context RL; together they suggest the next-generation reasoning-RL frontier is in *training signal construction* rather than reward shaping
