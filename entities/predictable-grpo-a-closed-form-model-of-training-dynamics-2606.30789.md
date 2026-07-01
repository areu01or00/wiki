---
title: "Predictable GRPO: A Closed-Form Model of Training Dynamics"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, RL, training-dynamics, theory]
sources: ["https://arxiv.org/abs/2606.30789"]
---

# Predictable GRPO: A Closed-Form Model of Training Dynamics

## Overview
GRPO (Group Relative Policy Optimization) has become a standard RL post-training method for improving LLM reasoning, but its training dynamics were previously described only empirically. This paper derives closed-form expressions for GRPO training trajectories, enabling prediction of divergence thresholds and the effects of refresh interval on training stability. The key finding: past a sharp refresh-interval threshold, stale-policy training becomes unstable — a phenomenon previously observed but not predicted.

## Key Facts
- **Authors**: Ghosh, Rajat; Nimmaturi, Datta; Singhal, Aryan + 4
- **Year**: 2026
- **arXiv**: [2606.30789](https://arxiv.org/abs/2606.30789)
- **Date**: 2026-06-29

## Key Contributions
- First closed-form model of GRPO training dynamics, predicting policy evolution without empirical simulation
- Proves divergence past a sharp refresh-interval threshold (stale-policy instability)
- Derives conditions under which GRPO reward trajectories are predictable from initial policy state
- Provides theoretical grounding for the widely observed instability of long-interval RL post-training runs

## Related Papers
- [[iapo-information-aware-policy-optimization-for-token-efficient-reasoning-2602.19049]] — Related policy optimization theory (token-efficient reasoning)
- [[cfpo-counterfactual-policy-optimization-multimodal-reasoning-2606.23206]] — Counterfactual policy optimization for multimodal reasoning
