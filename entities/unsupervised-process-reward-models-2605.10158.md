---
title: "Unsupervised Process Reward Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [process-reward-model, unsupervised-learning, self-supervised, reasoning, llm, step-level-supervision]
sources: ["https://arxiv.org/abs/2605.10158"]
---

# Unsupervised Process Reward Models

## Overview
uPRM (Unsupervised PRM) trains Process Reward Models without any human step-level annotations — it requires neither ground-truth reasoning steps nor ground-truth final answers. Instead, it uses a novel contrastive self-supervised objective that leverages the structure of LLM-generated reasoning chains: positive pairs are semantically-similar reasoning steps from correct trajectories, negative pairs are steps from incorrect trajectories or random chunks. This eliminates the most expensive component of PRM data collection while maintaining competitive performance on MATH and other reasoning benchmarks.

## Key Facts
- **Authors**: Artyom Gadetsky, Maxim Kodryan, Siba Smarak Panigrahi, Hang Guo, Maria Brbic
- **Year**: 2026
- **arXiv**: [2605.10158](https://arxiv.org/abs/2605.10158)
- **Online date**: 2026-05-11

## Key Contributions
- **Zero-annotation PRM training** — contrastive self-supervised objective that learns step-level quality signals from raw LLM reasoning trajectories without any human step labels or ground-truth answer verification. The key insight is that correctness signal can be extracted from trajectory structure alone.
- **Positive-negative pair construction** — positive pairs: steps from trajectories that reach correct answers; negative pairs: steps from incorrect trajectories or random spans. The contrastive loss drives the model to embed step quality signals in its representation space.
- **Competitive with supervised PRMs** — achieves 94% of Math-Shepherd (fully-supervised PRM) performance on MATH benchmark with zero step-level annotations, demonstrating that the step-level signal is learnable without explicit supervision.
- **Scalability analysis** — shows uPRM performance scales with the diversity and quality of reasoning trajectories used for contrastive pairs, suggesting that better LLMs for trajectory generation produce better uPRMs without additional annotation cost.

## Related Papers
- [[off-the-shelf-llms-as-process-scorers-training-free-prm-alternative-chunk-level-guided-generation-2606.01682]] — Training-free PRM alternative via off-the-shelf LLM likelihood scoring; both eliminate the annotation cost of PRM training but uPRM still trains a model while Off-the-Shelf uses fixed LLM likelihoods as the scorer.
- [[est-prm-stress-testing-process-reward-models-before-they-become-load-bearing-2606.00437]] — Stress-tests existing PRMs; uPRM's contrastive self-supervised objective sidesteps some of EST-PRM's identified brittleness modes by not relying on label-preserving annotations at all.
- [[veribound-pac-bayesian-generalization-bounds-for-process-reward-models-trained-with-formal-verification-tools-2606.20740]] — PAC-Bayesian theory for PRMs trained with formal verification annotations; uPRM provides a complementary unsupervised pathway that could be analyzed via similar generalization theory.
