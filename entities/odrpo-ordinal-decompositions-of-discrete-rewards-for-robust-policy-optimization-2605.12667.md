---
title: "ODRPO: Ordinal Decompositions of Discrete Rewards for Robust Policy Optimization"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reward-shaping, policy-optimization, rlhf, stochastic-rater, ordinal-decomposition]
sources: ["https://arxiv.org/abs/2605.12667"]
arxiv_id: "2605.12667"
---

# ODRPO: Ordinal Decompositions of Discrete Rewards for Robust Policy Optimization

## Overview
ODRPO addresses the stochasticity of LLM auto-raters in RLAIF pipelines for non-verifiable domains (long-form QA, instruction-following). By decomposing discrete rewards into a sequence of ordinal binary indicators and computing advantages independently across success thresholds, ODRPO prevents outlier auto-rater evaluations from corrupting the global policy update and establishes an implicit variance-aware learning curriculum.

## Key Facts
- **Authors**: Nirmal Patel, Fei Wang
- **Year**: 2026
- **arXiv**: [2605.12667](https://arxiv.org/abs/2605.12667)

## Key Contributions
- **Empirical diagnosis** of auto-rater stochasticity propagation through standard advantage estimators (GRPO, MaxRL) — noisy reward samples skew normalization statistics and degrade the global learning signal.
- **Ordinal decomposition framework** that structurally isolates evaluation noise by decomposing discrete rewards into a sequence of ordinal binary indicators representing progressively challenging success thresholds.
- **Independent advantage computation** across ordinal levels with accumulation, transforming single-reward optimization into a multi-reward formulation that prevents outlier corruption of global updates.
- **Implicit variance-aware learning curriculum** — easier ordinal thresholds provide dense early signal, harder thresholds provide refinement signal — without explicit curriculum scheduling.
- **Empirical validation** on Qwen2.5-7B and Qwen3-4B with up to 14.8% relative improvement over baselines; computes effectively at the same per-step cost as scalar reward GRPO since the ordinal decomposition is parallelizable.
- **First framework to structurally isolate auto-rater noise** rather than filtering it post-hoc, addressing the load-bearing problem that RLAIF's reliance on stochastic LLM-raters introduces irreducible noise that corrupts RL training signal.

## Related Papers
- [[discretizing-reward-models-2606.21795]] — Sibling paper on reward-model oversensitivity as structural failure mode; ODRPO addresses the same axis (reward quality) with an orthogonal mechanism (ordinal decomposition vs discretization).
- [[a-survey-of-on-policy-distillation-for-large-language-models-2604.00626]] — Adjacent paper on on-policy distillation as capability-transfer primitive; ODRPO's advantage estimation can be combined with on-policy distillation for cleaner gradient signal.
- [[beyond-reward-engineering-a-data-recipe-for-long-context-reinforcement-learning-2606.18831]] — Sibling paper on data recipe for long-context RL; ODRPO's variance-aware ordinal decomposition addresses reward-quality issues that Beyond-Reward-Engineering addresses from the data side.
- [[efficientrollout-system-aware-self-speculative-decoding-for-rl-rollouts-2606.18967]] — Sibling paper on inference-side acceleration for RL rollouts; ODRPO's ordinal decomposition is inference-orthogonal (it changes the reward signal itself, not the rollout cost).