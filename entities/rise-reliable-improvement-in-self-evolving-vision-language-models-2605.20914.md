---
title: "RISE: Reliable Improvement in Self-Evolving Vision-Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [self-evolving, vlm, multimodal, dual-role, closed-loop, questioner-solver, mode-collapse]
sources: ["https://arxiv.org/abs/2605.20914"]
---

# RISE: Reliable Improvement in Self-Evolving Vision-Language Models

## Overview
Diagnoses three failure modes in prior VLM self-evolving pipelines — coarse-grained role alternation, progressive question-quality degradation, and mode collapse toward a narrow question distribution — and proposes a reliable self-evolving framework with fine-grained role alternation, a quality supervisor, and skill-aware dynamic balancing. Demonstrates that unlabeled-image self-evolution can match the gains of human-supervised VLM post-training when the closed-loop primitives are designed to keep question generation and solver adaptation tightly coupled.

## Key Facts
- **Authors**: Xu, Chaoran; Miao, Yingmao; Zhang, Pengfei (and co-authors)
- **Year**: 2026
- **arXiv**: [2605.20914](https://arxiv.org/abs/2605.20914)
- **Online Date**: 2026-05-26

## Key Contributions
- **Dual-role closed-loop taxonomy for VLM self-evolution**: identifies three coupled failure modes — coarse role alternation, question-quality degradation, and mode collapse — that prior VLM self-evolving pipelines exhibit and that LLM-only self-evolution pipelines do not surface (because VLMs lack a strong textual prior to anchor question generation).
- **Fine-grained role alternation primitive**: shortens the feedback loop between the questioner and the solver by interleaving their updates at a higher cadence than full-epoch alternation, giving the solver immediate signal on each new question batch.
- **Quality supervisor for pseudo-label reliability**: introduces a learned supervisor that filters generated questions and pseudo-labels for validity, addressing the question-degradation pathology that breaks earlier VLM self-evolving systems.
- **Skill-aware dynamic balancing for mode-collapse mitigation**: tracks which reasoning skills are exercised across the question stream and rebalances generation to cover under-sampled skills, preventing the question distribution from collapsing toward a narrow subset during long evolution runs.

## Related Papers
- [[density-ridge-selective-prediction-for-llm-and-vlm-hallucination-detection-via-kinematic-feature-density-of-hidden-state-trajectories-2606.10198]] — Density-ridge selective prediction for LLM and VLM hallucination detection — complementary hallucination-control primitive: density-ridge surfaces out-of-distribution VLM outputs while RISE prevents the closed-loop from producing them in the first place via skill-aware question balancing.
- [[pathreasoner-r1-instilling-structured-reasoning-into-pathology-vision-language-models-2601.21617]] — Pathology VLM structured reasoning (Run 84 sibling) — same VLM primitive class but applied to a single vertical (pathology) with static reasoning supervision; RISE is the self-evolving analog that learns the supervision from the model itself.
- [[eventvla-event-driven-visual-evidence-memory-for-long-horizon-vision-language-action-policies-2606.20092]] — Event-driven visual-evidence memory for VLA policies — complementary memory primitive for long-horizon VLM/VLAs: EventVLA supplies episodic memory, RISE supplies the closed-loop self-improvement primitive that operates on the memory's outputs.