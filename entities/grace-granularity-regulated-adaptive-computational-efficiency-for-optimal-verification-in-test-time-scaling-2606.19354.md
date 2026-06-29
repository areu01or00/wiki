---
title: "GRACE: Granularity-Regulated Adaptive Computational Efficiency for Optimal Verification in Test-Time Scaling"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, test-time-compute, verification, llm]
sources: ["https://arxiv.org/abs/2606.19354"]
---

# GRACE: Granularity-Regulated Adaptive Computational Efficiency for Optimal Verification in Test-Time Scaling

## Overview
GRACE establishes a unified theoretical framework characterizing optimal verification granularity as an explicit function of problem difficulty, verifier accuracy, and compute budget. The key insight is a phase transition: fine-grained verification dominates when compute budget is large or problems are hard; coarse-grained verification is preferred in the low-budget, easy-problem regime. The theory unifies Best-of-N, beam search, and step-level MCTS within a single Pareto-optimality framework.

## Key Facts
- **Authors**: Ardit Krasniqi, Luan Vejsiu, Elira Dervishi
- **Year**: 2026
- **arXiv**: [2606.19354](https://arxiv.org/abs/2606.19354)
- **Submitted**: 28 April 2026 (originally announced June 2026)
- **Subjects**: Computation and Language (cs.CL); Machine Learning (cs.LG)

## Key Contributions
- Phase transition theory: fine-grained vs coarse-grained verification governed by problem difficulty + compute budget
- Unified framework connecting Best-of-N, beam search, and step-level MCTS as Pareto-optimal special cases
- Adaptive granularity strategy achieving compute-performance Pareto frontier
- Empirical validation on MATH-500, GSM8K, AIME: up to 3.1% accuracy gain at matched compute

## Related Papers
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — Unified test-time scaling framework (sibling test-time compute paper; GRACE provides the theoretical basis for optimal verification granularity that ThinkBooster's empirical framework operates within)
- [[maxproof-scaling-mathematical-proof-with-generative-verifier-rl-and-population-level-test-time-scaling-2606.13473]] — Generative verifier RL for proof synthesis (complementary verification approach; GRACE's granularity theory explains why adaptive verification granularity matters for proof verification)
- [[nabla-reasoner-llm-reasoning-via-test-time-gradient-descent-in-latent-space-2603.04948]] — Test-time gradient descent in latent space (Run 113 pick; GRACE extends the test-time compute allocation question to the verification granularity dimension)
