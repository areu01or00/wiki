---
title: "REAR: Test-time Preference Realignment through Reward Decomposition"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [alignment, preference-learning, test-time-scaling, reward-decomposition, inference-efficiency]
sources: ["https://arxiv.org/abs/2606.30339"]
---

# REAR: Test-time Preference Realignment through Reward Decomposition

## Overview
REAR extends test-time scaling (TTS) beyond verifiable domains (math/coding) to preference alignment by decomposing the underlying reward function into a question-related component and a preference-information component. The derived REAlignment Reward (REAR) selectively rescales the proportions of these two reward terms, formulated as a linear combination of token-level policy log-probabilities for computational efficiency. Integrates with best-of-N sampling and tree search TTS algorithms.

## Key Facts
- **Authors**: Zhang, Fuxiang; Wang, Pengcheng; Li, Chenran + 6
- **Year**: 2026
- **arXiv**: [2606.30339](https://arxiv.org/abs/2606.30339)

## Key Contributions
- Decomposes reward function into question-related and preference-related components for test-time preference realignment
- Derives REAR as linear combination of token-level policy log-probabilities — computationally efficient and algorithm-agnostic
- Enables training-free test-time scaling for preference alignment tasks (previously limited to math/coding)
- Generalizes to mathematical and visual tasks under appropriate preference settings
- **First reward-decomposition-based test-time preference realignment framework in the wiki.**

## Related Papers
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — On-policy skill distillation for agentic RL (parallel test-time scaling for agentic RL)
- [[renio-reweighting-negative-trajectory-importance-for-llm-on-policy-distillation-2606.23104]] — On-policy distillation with trajectory reweighting (RL post-training primitive)
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — Structured output constraints (alignment primitive — orthogonal to REAR's preference decomposition)
