---
title: "Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [video-diffusion, autoregressive-video, diffusion-distillation, world-models, streaming]
sources: ["https://arxiv.org/abs/2606.25473"]
---

# Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models

## Overview
Extends rCM (a recent diffusion-distillation framework based on the complementarity of consistency models and distribution-matching distillation) from the standard (non-autoregressive) video setting into the **autoregressive causal-diffusion-transformer** setting required for real-time streaming video generation and action-conditioned interactive world models. Provides a unified open recipe that supports both **teacher-forcing** (teacher-rollout supervision) and **self-forcing** (model-rollout supervision) regimes under one distillation objective.

## Key Facts
- **Authors**: Zheng, Kaiwen; He, Guande; Zhao, Min; Zhang, Jintao; Chen, Huayu; Chen, Jianfei
- **Year**: 2026
- **arXiv**: [2606.25473](https://arxiv.org/abs/2606.25473)
- **Date**: 2026-06-24

## Key Contributions
- Port of the **CM + DMD complementarity** to the autoregressive diffusion setting, demonstrating that the forward/reverse divergence complementarity that powers rCM in the static setting survives chunkwise rollout
- Unifies **teacher-forcing** and **self-forcing** distillation under one open recipe — eliminating the need for two separate distillation pipelines depending on whether the supervision comes from a frozen teacher rollout or a self-rollout
- Targets the **streaming / interactive-world-model** deployment regime where causal attention is required for low-latency frame-by-frame generation and action conditioning, complementing the broader autoregressive-video-diffusion paradigm

## Related Papers
- [[emergent-concepts]] — Parent meta-page; discovered via emergent-concept search on 2026-06-25
- [[world-action-models-a-survey-2606.20781]] — Sibling embodied world-model / predictive-action survey
- [[world-value-models-robotic-manipulation-2606.24742]] — Sibling value-estimation world-model work in the manipulation surface
