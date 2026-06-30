---
title: "On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [llm, distillation, self-training, diversity, on-policy]
sources: ["https://arxiv.org/abs/2606.26091"]
---

# On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity

## Overview
This paper reveals a fundamental diversity-accuracy tradeoff in on-policy self-distillation. While achieving strong pass@1 accuracy by using a single model as both teacher and student, the approach causes rollout diversity to decrease and pass@k curves to flatten — generating more rollouts fails to improve accuracy. The root cause is compounding biases where the teacher scores each student rollout while conditioned on a sampled correct rollout, channeling feedback through the model's own biases.

## Key Facts
- **Authors**: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
- **Year**: 2026
- **arXiv**: [2606.26091](https://arxiv.org/abs/2606.26091)

## Key Contributions
-

## Related Papers
- [[v-zero-answer-label-free-on-policy-distillation-contrastive-evidence-2606.25319]] — On-policy distillation contrastive evidence; shares self-distillation methodology theme
- [[heal-hindsight-entropy-assisted-learning-reasoning-distillation-2603.10359]] — Hindsight entropy reasoning distillation; shares diversity-reduction concern in distillation
- [[learning-from-your-own-mistakes-constructing-learnable-micro-reflective-trajectories-for-self-distillation-2606.18844]] — Self-distillation via micro-reflective trajectories; related methodology
