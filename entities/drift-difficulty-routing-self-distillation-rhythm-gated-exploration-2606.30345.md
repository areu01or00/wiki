---
title: "DRIFT: Difficulty Routing Self-DIstillation with Rhythm-Gated Exploration and Success BuFfer Training"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, self-distillation, reinforcement-learning, llm]
sources: ["https://arxiv.org/abs/2606.30345"]
---

# DRIFT: Difficulty Routing Self-DIstillation with Rhythm-Gated Exploration and Success BuFfer Training

## Overview
DRIFT enables large language models to achieve stable self-improvement without external expert supervision in complex reasoning tasks. It combines difficulty-guided sample routing with a success-buffered self-distillation loss and a rhythm-gated exploration mechanism that modulates the balance between confident and uncertain tokens during training.

## Key Facts
- **Authors**: Luo, Haisen; Liu, Yiwei; Wang, Haoning + 13
- **Year**: 2026
- **arXiv**: [2606.30345](https://arxiv.org/abs/2606.30345)

## Key Contributions
- Difficulty Routing: dynamically selects training samples based on estimated model confidence, focusing on tokens near the decision boundary
- Rhythm Gating: modulates exploration vs exploitation by gating token-level loss contributions based on a learned "rhythm" signal
- Success Buffer: accumulates high-confidence, successful reasoning traces as stable distillation targets, preventing regression on already-mastered tasks
- Stable self-improvement loop without external reward signals or expert demonstrations

## Related Papers
- [[learning-from-your-own-mistakes-constructing-learnable-micro-reflective-trajectories-for-self-distillation-2606.18844]] — Prior self-distillation with micro-reflective trajectories; DRIFT differs by using difficulty routing and success buffer instead of failure-focused trajectories
- [[on-policy-self-distillation-sampled-demonstrations-reduces-output-diversity-2606.26091]] — On-policy self-distillation; DRIFT addresses the output diversity collapse via rhythm gating
