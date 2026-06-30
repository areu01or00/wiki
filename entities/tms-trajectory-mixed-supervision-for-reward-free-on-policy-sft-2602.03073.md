---
title: "TMS: Trajectory-Mixed Supervision for Reward-Free, On-Policy SFT"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [fine-tuning, rl, sft, training-methodology]
sources: ["https://arxiv.org/abs/2602.03073"]
---

# TMS: Trajectory-Mixed Supervision for Reward-Free, On-Policy SFT

## Overview
TMS (Trajectory-Mixed Supervision) addresses a key asymmetry between RL and SFT for LLM post-training: RL better preserves model capabilities (retention) but requires complex reward engineering and expensive on-policy sampling, while SFT is efficient but suffers from "Supervision Mismatch" — training on static high-quality outputs that don't reflect the distribution the model actually produces at inference time. TMS bridges this gap by mixing trajectories from the current policy with expert trajectories, enabling on-policy SFT without requiring a reward model.

## Key Facts
- **Authors**: TMS Authors
- **Year**: 2026
- **arXiv**: [2602.03073](https://arxiv.org/abs/2602.03073)

## Key Contributions
- Trajectory-mixed supervision: mixes current-policy and expert trajectories during SFT, enabling on-policy training without reward models
- Addresses Supervision Mismatch — SFT's core brittleness is that static expert data doesn't match the model's actual inference distribution
- Eliminates need for reward engineering while retaining RL-like retention benefits — on-policy mixing keeps the model close to its base distribution
- Demonstrates catastrophic forgetting mitigation: training signal stays anchored to the model's own outputs, reducing distributional drift

## Related Papers
- [[supervised-fine-tuning-versus-reinforcement-learning-a-study-of-post-training-methods-for-large-language-models-2603.13985]] — SFT vs RL comparison study — empirically benchmarks the retention vs. training-efficiency tradeoff; TMS directly addresses the SFT side of this tradeoff via trajectory mixing
- [[school-of-reward-hacks-hacking-harmless-tasks-generalizes-to-misaligned-behavior-in-llms-2508.17511]] — School of Reward Hacks — RLHF reward hacking vulnerability; TMS sidesteps the reward model entirely, removing the substrate for reward hacking
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Calibration Collapse — sycophancy fine-tuning reward hacking; TMS's reward-free approach eliminates the reward signal that drives sycophancy amplification
