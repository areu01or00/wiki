---
title: "DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [t2v, subject-driven-generation, open-domain-generation, video-generation]
sources: ["https://arxiv.org/abs/2606.26058"]
---

# DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation

## Overview
Distinguishes *in-domain* from *cross-domain* subject-driven text-to-video (S2V) generation and proposes DomainShuttle, a framework that explicitly shuttles between the two regimes so that the reference subject can be preserved while subject-irrelevant properties (background, lighting, pose, action) vary freely according to the text prompt. Targets the open-domain S2V regime where existing methods over-optimize subject fidelity at the cost of cross-domain editability and adaptability.

## Key Facts
- **Authors**: Chen, Nan; Cai, Yiyang; Xie, Rongchang; Pan, Junwen; Chen, Cheng; Jia, Weinan
- **Year**: 2026
- **arXiv**: [2606.26058](https://arxiv.org/abs/2606.26058)
- **Date**: 2026-06-24

## Key Contributions
- Frames open-domain S2V as a **two-mode problem** (in-domain fidelity vs cross-domain editability) and proposes an explicit domain-shuttle mechanism so that a single model can serve both regimes instead of specializing to one
- Surfaces **subject-irrelevant properties** (background, lighting, pose, action) as a first-class axis that should vary flexibly under cross-domain prompts — the structural complement to subject-fidelity maximization
- Provides a unified recipe for freeform open-domain S2V that lifts prior methods out of the "preserve subject at all costs" local optimum

## Related Papers
- [[emergent-concepts]] — Parent meta-page; discovered via emergent-concept search on 2026-06-25
- [[physics-question-scene-graph-fine-grained-evaluation-physical-plausibility-text-to-video-2606.25306]] — Sibling T2V evaluation work extending the eval-as-discipline wave into the T2V surface (physical-plausibility scene graphs)
- [[multi-turn-reflective-masking-elicits-reasoning-mask-diffusion-2606.16700]] — Sibling non-AR reasoning work in the diffusion-language-modeling surface
