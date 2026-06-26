---
title: "DanceOPD: On-Policy Generative Field Distillation"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [flow-matching, distillation, image-generation, multi-capability, on-policy]
sources: ["https://arxiv.org/abs/2606.27377"]
---

# DanceOPD: On-Policy Generative Field Distillation

## Overview
Addresses the structural challenge in modern image generation where a single model must unify diverse capabilities — text-to-image (T2I), local editing, and global editing — that rarely naturally align and often conflict (e.g., editing degrades T2I performance while global and local editing interfere with each other). Proposes DanceOPD, an on-policy generative field distillation framework for flow-matching models that routes each sample to one capability field, queries one low-noise student-induced state, and trains with a simple velocity MSE objective.

## Key Facts
- **Authors**: Zhou, Wei; Zhu, Xiongwei; Xu, Zelin; Dong, Bo; Gong, Lixue; Liang, Yongyuan; Chu, Meng; Qu, Leigang; Kong, Lingdong; Liu, Wei
- **Year**: 2026
- **arXiv**: [2606.27377](https://arxiv.org/abs/2606.27377)

## Key Contributions
- **Capability-routing-as-distillation-target**: Each capability source is a velocity field over the shared flow state space, and the student learns from fields queried on its own rollout states to compose expert capabilities.
- **Absorbs operator-defined fields**: The formulation also absorbs operator-defined fields such as classifier-free guidance (CFG) into the same distillation framework.
- **Improves multi-capability composition**: Strengthens target capabilities while preserving anchor generation quality across T2I, editing, realism-field absorption, and CFG absorption.

## Related Papers
- [[emergent-concepts]] — Parent wiki page