---
title: "Making Expert Reasoning Learnable with Self-Distillation"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [reasoning, self-distillation, training, llm]
sources: ["https://arxiv.org/abs/2602.02405"]
---

# Making Expert Reasoning Learnable with Self-Distillation

## Overview
Improving LLM reasoning typically requires either the ability to sample correct solutions or a stronger teacher model. When both are unavailable — the common case for frontier-level problems — naive expert solution imitation fails because human explanations are didactic and out-of-distribution for LLMs. This paper introduces Distribution Aligned Imitation Learning (DAIL), a two-step self-distillation method that transforms expert solutions into in-distribution reasoning traces and uses contrastive learning to extract generalizable reasoning methodologies.

## Key Facts
- **Authors**: Unnamed (arXiv 2602.02405)
- **Year**: 2026
- **arXiv**: [2602.02405](https://arxiv.org/abs/2602.02405)

## Key Contributions
- DAIL transforms expert solutions into detailed, in-distribution reasoning traces via a two-step bridging process
- Contrastive objective focuses learning on expert reasoning insights and methodologies rather than surface-level patterns
- Achieves up to 31% pass@128 gains on Qwen2.5-Instruct and Qwen3 with fewer than 1000 expert solutions
- Enables out-of-domain generalization without requiring a stronger teacher model

## Related Papers
- [[learning-from-your-own-mistakes-constructing-learnable-micro-reflective-trajectories-for-self-distillation-2606.18844]] — Complementary self-distillation approach constructing reflective micro-trajectories from the model's own mistakes
- [[rethinking-reward-supervision-rubric-conditioned-self-distillation-2606.19327]] — Rubric-conditioned self-distillation framing related to DAIL's distribution alignment objective
