---
title: "KbSD: Knowledge Boundary aware Self-Distillation for Behavioral Calibration in Agentic Search"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agentic-ai, retrieval-augmented-generation, knowledge-distillation, calibration, reasoning]
sources: ["https://arxiv.org/abs/2606.29863"]
---

# KbSD: Knowledge Boundary aware Self-Distillation for Behavioral Calibration in Agentic Search

## Overview
KbSD addresses a critical gap in agentic search systems: the inability to calibrate when an LLM should trust its parametric memory versus retrieved external evidence. The paper identifies that binary RL rewards provide sparse supervision for the knowledge-boundary calibration decision itself, and introduces a self-distillation framework where the agent learns to model its own knowledge boundaries across different query types.

## Key Facts
- **Authors**: Tao Feng, Xinke Jiang, Chao Wu
- **Year**: 2026
- **arXiv**: [2606.29863](https://arxiv.org/abs/2606.29863)

## Key Contributions
- Knowledge Boundary Self-Distillation (KbSD) framework for behavioral calibration in agentic search
- Addresses reward sparsity problem in RL-based agentic systems — binary rewards don't guide the calibration reasoning process
- Decision taxonomy: trust parametric memory vs. rely on retrieved evidence vs. abstain — each requiring different reasoning strategies
- Self-distillation approach where the agent learns from its own calibration decisions across diverse knowledge states
- Behavioral calibration via self-distillation rather than external supervision signals

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts wiki
