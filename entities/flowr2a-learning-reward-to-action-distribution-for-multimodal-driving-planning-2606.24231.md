---
title: "FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [driving-planning, multimodal, flow-matching, generative-model, robot-learning]
sources: ["https://arxiv.org/abs/2606.24231"]
---

# FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning

## Overview
FlowR2A unifies two competing paradigms in multimodal driving planning — scoring-based methods (dense reward supervision, fixed action vocabulary) and anchor-based methods (dynamic proposal generation, sparse supervision) — by reframing simulation-based rewards from *discriminative targets* into *generative conditions*. Li et al. learn a reward-conditioned action distribution with a flow-matching decoder over dense trajectory-reward pairs, enabling dense-supervision learning while still producing diverse, dynamically-generated proposals. The generative formulation supports controllable test-time sampling via reward guidance and anchored sampling, achieving state-of-the-art results on NAVSIM v1 and v2 with substantially higher proposal quality than prior methods.

## Key Facts
- **Authors**: Li, Xirui; Liu, Zhe; Ye, Xiaoqing; Han, Wenhua; Pan, Yifeng; Han, Junyu; Zhao, Hengshuang
- **Year**: 2026
- **Date**: 2026-06-23
- **arXiv**: [2606.24231](https://arxiv.org/abs/2606.24231)
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- **Paradigm unification via reward-conditioned generation**: rewards become the conditioning signal of a flow-matching decoder over trajectories, recovering the dense-supervision benefits of scoring-based methods while retaining the dynamic-proposal flexibility of anchor-based methods.
- Fine-grained per-timestep reward conditioning + reward-noise augmentation, balancing hard safety constraints against soft progress objectives at the per-step granularity.
- Test-time controllability via reward guidance and anchored sampling: the same model can trade off safety / progress / comfort / rule-compliance at inference time without retraining.
- State-of-the-art results on NAVSIM v1 and v2 benchmarks, with multimodal proposals that exceed the quality of prior anchor-based or scoring-based methods.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered; an instance of the broader theme — generative-flow / reward-conditioned planning — that recurs across the robotics and decision-making literature, and a useful counterpoint to pure-language agent work on this page by showing how the same flow-matching / reward-conditioning machinery ports to physical-world action spaces.