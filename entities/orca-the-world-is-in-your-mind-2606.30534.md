---
title: "Orca: The World is in Your Mind"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [world-model, foundation-model, multimodal, embodiment, agent]
sources: ["https://arxiv.org/abs/2606.30534"]
---

# Orca: The World is in Your Mind

## Overview
Orca is a general world foundation model that learns a unified world latent space from multimodal world signals. Rather than optimizing isolated next-token, next-frame, or next-action prediction, Orca centers on Next-State-Prediction modeling, learning through two complementary paradigms: unconscious learning from dense natural state transitions in continuous video, and conscious learning from sparse meaningful state transitions via language-described events and VQA supervision. Pre-trained on 125K hours of video and 160M event annotations, Orca's frozen backbone with lightweight modality-specific decoders achieves strong scalability and outperforms similar-sized specialized baselines across text generation, image prediction, and embodied action generation.

## Key Facts
- **Authors**: Yihao Wang, Yuheng Ji, Mingyu Cao, Yanqing Shen, Runze Xiao, Huaihai Lyu, Senwei Xie, Euan [et al.]
- **Year**: 2026
- **arXiv**: [2606.30534](https://arxiv.org/abs/2606.30534)

## Key Contributions
- First general world foundation model using unified Next-State-Prediction (NSP) as the modeling objective — unifying token/frame/action prediction into a single framework
- Dual-paradigm learning: unconscious (dense video state transitions) + conscious (language-described sparse events + VQA)
- 125K hours of video + 160M event annotations — largest world-learning inventory dataset to date
- Frozen backbone with trainable modality-specific decoders — scalable to new modalities without full retraining
- Outperforms same-sized specialized baselines on text generation, image prediction, and embodied action generation
- Stronger world latent enables stronger downstream readouts — verifying world latent space quality as the key bottleneck

## Related Papers
- [[agentic-world-modeling-foundations-capabilities-laws-and-beyond-2604.22748]] — Agentic world modeling survey and framework taxonomy
- [[causal-reward-world-models-zero-shot-skill-generation-2606.23280]] — Causal reward world models for zero-shot skill generation
- [[causal-rcm-a-unified-teacher-forcing-and-self-forcing-open-recipe-for-autoregressive-diffusion-distillation-in-streaming-video-generation-and-interactive-world-models-2606.25473]] — Diffusion distillation for interactive world models
