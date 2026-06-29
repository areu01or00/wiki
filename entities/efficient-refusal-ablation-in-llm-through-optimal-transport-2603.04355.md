---
title: "Efficient Refusal Ablation in LLM through Optimal Transport"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [information-geometry, alignment-safety, optimal-transport]
sources: ["https://arxiv.org/abs/2603.04355"]
---

# Efficient Refusal Ablation in LLM through Optimal Transport

## Overview
Replaces orthogonal-projection activation-jailbreaks with a principled optimal-transport framework that *transforms the entire distribution* of harmful activations to match harmless ones, treating refusal not as a 1-D direction but as a rich distributional shift. Introduces a closed-form PCA+OT solution that is cheap to run and preserves the surrounding residual channel.

## Key Facts
- **Authors**: Geraldin Nanfack, Eugene Belilovsky, Elvis Dohmatob
- **Year**: 2026
- **arXiv**: [2603.04355](https://arxiv.org/abs/2603.04355)
- **Submission date**: 4 Mar 2026

## Key Contributions
- **First optimal-transport–based refusal-ablation framework** that treats safety-alignment as a *distribution-to-distribution* map rather than 1-D orthogonal-projection ablation.
- **PCA + closed-form OT solution**: uses PCA to identify the dominant refusal-direction subspace and a closed-form linear OT map to transform only the harmful-side distribution toward the harmless-side distribution — leaving orthogonal residual channels untouched.
- **Distributional-shape preservation under ablation**: by matching full distributional summaries (Wasserstein-2 / Sinkhorn-style targets) rather than 1-D directions, the ablation preserves away-from-refusal manifold structure — empirically reducing collateral capability degradation.
- **Information-geometric primitive for alignment** — adds an OT-distributional-shape primitive to the alignment-safety toolbox (Representation-Engineering, Refusal-Direction, Concept-Heterogeneity-aware Steering).
- **Empirically validated on safety-evaluation benchmarks** with lower side-effect perplexity / capability degradation than orthogonal-projection baselines; computationally cheaper than iterative OT solving because of the PCA preconditioning.

## Related Papers
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Geometric-refusal 1-D instability primitive that this OT-distributional approach outperforms.
- [[a-brain-like-synergistic-core-in-llms-drives-behaviour-and-learning-2601.06851]] — PID-synergy primitive over the same activation space; OT-removal preserves the synergistic distribution in residual channels.
- [[learning-is-forgetting-llm-training-as-lossy-compression-2604.07569]] — Rate-distortion view that OT-transformation instantiates in the *refusal-direction subspace*.
- [[a-low-rank-subspace-analysis-of-llm-interventions-2606.14388]] — Low-rank subspace primitive for LLM interventions; PCA here is its special-case for refusal-direction identification.
- [[acthook-watermarking-llm-agent-trajectories-2602.18700]] — Agent-trajectory watermarking complementary: where this refuses, that embeds; both operate on agent-side activation shapes.
