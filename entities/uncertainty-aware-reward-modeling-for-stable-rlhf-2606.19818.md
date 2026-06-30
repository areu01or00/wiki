---
title: "Uncertainty-Aware Reward Modeling for Stable RLHF"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [rlhf, reward-modeling, uncertainty, alignment, grpo]
sources: ["https://arxiv.org/abs/2606.19818"]
---

# Uncertainty-Aware Reward Modeling for Stable RLHF

## Overview
Proposes Uncertainty-Aware Reward Modeling (UARM), which equips reward models with calibrated uncertainty via quantile-based conformal prediction and reweights GRPO advantages through heteroscedastic variance decomposition. Addresses the critical vulnerability where unreliable reward estimates are granted disproportionate influence during GRPO's uniform treatment of rewards.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.19818](https://arxiv.org/abs/2606.19818)

## Key Contributions
- **Quantile-Based Conformal Prediction for RMs**: First application of conformal prediction to reward model uncertainty quantification, providing calibrated confidence intervals for reward predictions
- **Heteroscedastic Variance Decomposition**: Decomposes advantage computation into variance-aware components, preventing unreliable rewards from receiving disproportionate influence in GRPO
- **Reward Hacking Reduction**: Significantly reduces reward hacking on HelpSteer, UltraFeedback, and PKU-SafeRLHF compared to standard GRPO and uncertainty-agnostic baselines
- **Downstream Alignment Quality**: Improves alignment quality vs. standard GRPO baselines while maintaining comparable task performance

## Related Papers
- [[when-rlhf-fails-mechanistic-taxonomy-reward-hacking-collapse-evaluator-gaming-2606.03238]] — Mechanistic taxonomy of RLHF failure modes
- [[reward-hacking-in-the-era-of-large-models-mechanisms-emergent-misalignment-challenges-2604.13602]] — Mechanisms and emergent misalignment challenges in reward hacking
