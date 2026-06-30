---
title: "Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System"
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [robotics, navigation, vla, agentic, qwen, perception-planning, inference-time]
sources: ["https://arxiv.org/abs/2606.18112"]
---

# Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System

## Overview
This technical report presents Qwen-RobotNav, a scalable navigation model for agentic navigation systems. The key insight is that diverse navigation tasks (instruction following, object search, target tracking, autonomous driving) share the same perception-planning backbone but require fundamentally different observation strategies. Qwen-RobotNav addresses this through a parameterized interface with multiple task modes and controllable observation parameters.

## Key Facts
- **Authors**: Qwen Team (from arxiv 2606.18112)
- **Year**: 2026
- **arXiv**: [2606.18112](https://arxiv.org/abs/2606.18112)

## Key Contributions
- Presents Qwen-RobotNav: a scalable navigation model with parameterized interface for diverse agentic navigation tasks
- Introduces multiple task modes that select navigation behavior at inference time
- Introduces controllable observation parameters (token budget, per-camera weights) governing visual history encoding
- Training-time randomization over all parameters enables robustness to any inference-time configuration

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept discovery chain
