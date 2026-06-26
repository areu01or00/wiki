---
title: "In-Context World Modeling for Robotic Control"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [robotics, vla, in-context-learning, world-model, system-identification, adaptation]
sources: ["https://arxiv.org/abs/2606.26025"]
---

# In-Context World Modeling for Robotic Control

## Overview
Identifies a structural failure mode in modern Vision-Language-Action (VLA) models — they fail to generalize to novel setups (altered camera viewpoints, robot morphologies) because they are conditioned only on current observations and language instructions, implicitly assuming a fixed execution context — and proposes In-Context World Modeling (ICWM), a framework that treats system identification as an in-context adaptation problem. The policy autonomously infers essential system variables from a short history of self-generated, task-agnostic interactions before task execution, capturing world dynamics of the current system without parameter updates.

## Key Facts
- **Authors**: Wang, Siyin; Shi, Junhao; Fei, Senyu; Fu, Zhaoyang; Ji, Li; Gong, Jingjing; Qiu, Xipeng
- **Year**: 2026
- **arXiv**: [2606.26025](https://arxiv.org/abs/2606.26025)

## Key Contributions
- **System identification as in-context adaptation**: Unlike traditional In-Context Learning where demonstrations specify *what task to perform*, ICWM leverages the context window to understand *how the system operates* — inferred from task-agnostic interactions.
- **Implicit world-dynamics capture**: A short history of self-generated interactions encodes system variables before task execution, enabling adaptation to novel configurations without parameter updates.
- **Significant gains over VLA baselines on novel camera viewpoints**: Validated in simulation and on real-world robot platforms.

## Related Papers
- [[emergent-concepts]] — Parent wiki page