---
title: "ABot-M0.5: Unified Mobility-and-Manipulation World Action Model"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [embodied-ai, robotics, world-model]
sources: ["https://arxiv.org/abs/2607.00678"]
---

# ABot-M0.5: Unified Mobility-and-Manipulation World Action Model

## Overview
ABot-M0.5 is a World Action Model (WAM) built for mobile manipulation — the combination of robot navigation and arm manipulation tasks. It addresses three fundamental misalignments in prior WAMs: temporal granularity mismatch (coarse video chunks vs. fine contact dynamics), action space entanglement (navigation-manipulation混杂), and train-test inconsistency (supervised inverse dynamics that don't match autoregressive inference). ABot-M0.5 introduces intermediate latent actions for temporal alignment, a dual-level Mixture-of-Transformers architecture for action disentanglement, and dream-forcing training for inference-consistent dynamics. Achieves state-of-the-art on long-horizon task success and fine-grained control accuracy benchmarks.

## Key Facts
- **Authors**: Chen, Ronghan; Yang, Yandan; Tang, Zuojin + 18
- **Year**: 2026
- **arXiv**: [2607.00678](https://arxiv.org/abs/2607.00678)

## Key Contributions
- **Three-level alignment theory**: Temporal granularity, action space, and train-test consistency — the three axes that make mobile manipulation uniquely hard for WAMs
- **Intermediate latent actions**: Bridge action space between video latents and embodiment-specific controls, capturing local visual state transitions
- **Dual-level MoT architecture**: Mixture-of-Transformers disentangles both modality representations and heterogeneous action subspaces (base movement + arm manipulation)
- **Dream-forcing training strategy**: Progressively trains inverse dynamics on model-predicted videos, improving train-test alignment and robustness during autoregressive prediction
- **Benchmark performance**: State-of-the-art on challenging mobile manipulation and fine-grained control accuracy benchmarks

## Related Papers
- [[does-vla-even-know-the-basics-measuring-commonsense-and-world-knowledge-retention-in-vision-language-action-models-2606.19297]] — VLA commonsense retention analysis; ABot-M0.5 addresses world modeling failures by explicitly aligning temporal and action granularity across embodiments
- [[ebench-elemental-diagnosis-of-generalist-mobile-manipulation-policies-2606.18239]] — EBench provides diagnostic benchmarks for mobile manipulation; ABot-M0.5's three-level alignment framework is motivated by similar failure mode analysis
- [[eventvla-event-driven-visual-evidence-memory-for-long-horizon-vision-language-action-policies-2606.20092]] — EventVLA uses event-driven memory for long-horizon VLA policies; ABot-M0.5's latent action mechanism provides complementary temporal alignment for event-driven control
