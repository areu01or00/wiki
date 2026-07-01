---
title: "Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [robotics, VLA, sim-to-real, reinforcement-learning, zero-shot-transfer]
sources: ["https://arxiv.org/abs/2606.18953"]
---

# Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

## Overview
Vision-Language-Action (VLA) models pre-trained on large robot datasets face a sim-to-real gap when deployed in new physical environments. This paper introduces object-centric residual RL to close that gap: a sim-side residual policy is trained with pose noise injection and dropout to capture object-level deviations between simulation and reality, then distilled back into the VLA for zero-shot real-robot transfer without any real-world fine-tuning. Results: simulation success rates improve from 49% to 87%, real-robot from 42% to 76% across 5 manipulation tasks.

## Key Facts
- **Authors**: Kim, Kinam; Saito, Namiko; Kim, Heecheol + 3
- **Year**: 2026
- **arXiv**: [2606.18953](https://arxiv.org/abs/2606.18953)

## Key Contributions
- Object-centric residual RL: separate residual policy for per-object deviation between sim and real
- Zero-shot sim-to-real transfer for VLA models via residual distillation — no real-robot fine-tuning needed
- Pose noise injection and dropout to simulate domain shift in simulation
- Strong empirical gains across 5 manipulation tasks: sim 49%→87%, real 42%→76%

## Related Papers
- [[scaling-the-horizon-not-the-parameters-reaching-trillion-parameter-performance-with-a-35b-agent-2606.30616]] — Trillion-parameter scaling for agents, relevant to large VLA pre-training
- [[toward-secure-and-reliable-pddl-formalization-of-large-language-models-with-planner-in-the-loop-feedback-2606.29700]] — PDDL formalization for agent planning, complementary to VLA action-level reasoning
