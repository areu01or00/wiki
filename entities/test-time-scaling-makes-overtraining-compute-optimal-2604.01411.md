---
title: "Test-Time Scaling Makes Overtraining Compute-Optimal"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [test-time-scaling, inference-scaling, scaling-laws, compute-optimal, pretraining, training-time-compute, reasoning]
sources: ["https://arxiv.org/abs/2604.01411"]
---

# Test-Time Scaling Makes Overtraining Compute-Optimal

## Overview
T² (Train-to-Test) scaling laws are the first joint optimization framework that simultaneously determines optimal model size, training token count, AND number of inference samples under a fixed end-to-end compute budget. Unlike classical Chinchilla scaling laws which only optimize pretraining, and unlike test-time scaling papers that treat the model as fixed, T² jointly balances all three dimensions. The key insight is that when inference compute is expensive (repeated sampling, beam search, agency workflows), the optimal model is systematically smaller and trained on fewer tokens than Chinchilla predicts — because you want to allocate more compute budget to inference-time sampling.

## Key Facts
- **Authors**: Nicholas Roberts, Sungjun Cho, Zhiqi Gao, Tzu-Heng Huang, Albert Wu, Gabriel Orlanski, Avi Trost, Kelly Buchanan, Aws Albarghouthi, Frederic Sala
- **Year**: 2026
- **arXiv**: [2604.01411](https://arxiv.org/abs/2604.01411)
- **Online date**: 2026-04-01

## Key Contributions
- **Joint Train+Test compute optimization** — T² scaling laws simultaneously optimize model size N, training tokens D, and inference samples K under fixed compute budget C = N*D + K*N_inference. The optimal (N*, D*, K*) triple systematically deviates from Chinchilla-optimal (N_chinchilla, D_chinchilla) when inference compute is non-trivial.
- **Compute-optimal frontier surfaces** — for a given total compute budget, the T² frontier identifies the Pareto-optimal operating point across all three dimensions. The gap between Chinchilla-optimal and T²-optimal grows as inference costs increase (reasoning tasks, multi-agent rollouts, synthetic data generation).
- **Overtraining is sometimes optimal** — under T² framework, "overtraining" (training past Chinchilla-optimal tokens) can be compute-optimal when the saved inference compute from a slightly larger model is reallocated to more samples. This inverts the standard Chinchilla framing.
- **Implications for reasoning models** — reasoning models that use many inference samples (self-consistency, Best-of-N, agentic rollouts) should be trained on fewer tokens and kept smaller than Chinchilla predicts, because the inference compute savings dominate pretraining efficiency losses.

## Related Papers
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — Unified test-time scaling framework; sibling survey that contextualizes T² among the broader test-time scaling landscape.
- [[linguistic-generalizability-of-test-time-scaling-in-mathematical-reasoning-2502.17407]] — Tests whether test-time scaling gains generalize across languages; T²'s language-agnostic compute framework explains why generalization patterns vary by linguistic feature.
- [[maxproof-scaling-mathematical-proof-with-generative-verifier-rl-and-population-level-test-time-scaling-2606.13473]] — Population-level test-time scaling for theorem proving; both papers study scaling inference compute for math reasoning but T² focuses on the joint optimization theory while MAXProof focuses on the empirical scaling application.
- [[query-conditioned-test-time-self-training-quest-per-query-adaptation-2605.13369]] — Per-query test-time adaptation framework; both papers address test-time parameter efficiency but T² optimizes the full train+test compute budget while Quest optimizes per-sample adaptation.
