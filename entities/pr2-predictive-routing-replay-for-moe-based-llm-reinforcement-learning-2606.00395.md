---
title: "PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [moe, reinforcement-learning, router-drift, importance-sampling, llm, mixture-of-experts, ppo, routing, stability]
sources: ["https://arxiv.org/abs/2606.00395"]
---

# PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning

## Overview
Introduces **Predictive Routing Replay (PR2)**, a method for stabilizing reinforcement learning on Mixture-of-Experts LLMs by augmenting each expert router with a lightweight evolution predictor that anticipates short-horizon router drift across model updates. The predictor's distribution is used during rollout to apply top-k routing that exposes experts *likely to become active after the next update*, and the resulting predicted route is replayed during the training phase for stable importance estimation. The paper targets the root cause of MoE-RL instability — **router drift** between disaggregated rollout and training phases that produces large rollout–training mismatch and unstable importance sampling weights in PPO-style algorithms — and provides a theoretically-grounded alternative to vanilla routing replay, which freezes the replay route within a trajectory but ignores how the router evolves off-policy.

## Key Facts
- **Authors**: Dong, Daize; Chen, Junlin; Jia, Haolong; Liu, Jiang; Wu, Jiawei; Di, Huanwei; Wu, Jialian; Liu, Zhengzhong; Liu, Zicheng; Barsoum, Emad; Metaxas, Dimitris N.; Wang, Hongyi
- **Year**: 2026
- **arXiv**: [2606.00395](https://arxiv.org/abs/2606.00395)
- **Submission Date**: 2026-05-29 (cs.LG / cs.CL)

## Key Contributions
- **Identifies router drift as the structural root cause** of MoE-RL training instability: expert activations change drastically across model updates and differ between rollout and training phases, producing unstable importance sampling weights that propagate through PPO-style policy gradients.
- **Introduces a learned evolution predictor** per router — a lightweight module that learns to anticipate short-horizon router evolution — yielding a predictive routing distribution used in two distinct phases.
- **Asymmetric dual-phase design**: during rollout, top-k routing uses the *predictive* distribution so gradients reach experts likely to become active after updates; during training, the *predicted route* (computed at rollout time) is replayed to retain consistency for stable importance estimation — this is the load-bearing primitive that distinguishes PR2 from vanilla routing replay.
- **Theoretical analysis** showing that PR2 reduces routing-induced mismatch and improves RL stability; experiments across reasoning benchmarks confirm stronger downstream performance than routing-replay baselines.
- **Surfaces predict-router-drift-instead-of-removing-router as the axis-inverted primitive** for MoE-RL: rather than removing the router (Run 67 routing-free MoE), PR2 *predicts the router's evolution* — an architectural-intelligence primitive that turns router drift from a liability into a learnable signal.

## Related Papers
- [[routing-free-mixture-of-experts-eliminating-centralized-routing-2604.00801]] — Run 67 inverse-axis sibling — Routing-Free MoE removes the router entirely, PR2 *predicts the router's evolution* to track drift — together they bracket the MoE-RL-stability surface between *router-removal-as-architectural-elimination* and *router-drift-prediction-as-architectural-intelligence* primitives.
- [[discretizing-reward-models-2606.21795]] — Run 59 RL-post-training sibling — Discretizing Reward Models addresses *reward-signal-quality collapse*, PR2 addresses *router-induced-importance-sampling-collapse* — together they bracket the RL-post-training failure-mode space between reward-time signal pathology and rollout-time importance-weighting pathology.
- [[efficientrollout-system-aware-self-speculative-decoding-for-rl-rollouts-2606.18967]] — Run 59 RL-rollout sibling — EfficientRollout optimizes the *rollout-latency* dimension assuming the model is non-stationary, PR2 optimizes the *rollout-training-consistency* dimension of non-stationarity — together they bracket the RL-rollout engineering surface between latency-reduction and importance-sampling-stability primitives.
- [[why-multi-step-tool-use-reinforcement-learning-collapses-and-how-supervisory-signals-fix-it-2606.26027]] — Run 60 sibling agentic-RL paper — Multi-Step-Tool-Use-RL diagnoses *training-time format-distribution collapse*, PR2 diagnoses *router-induced-training-collapse* — together they bracket the RL failure-mode space between format-distribution and router-distribution pathologies.
- [[supervised-fine-tuning-versus-reinforcement-learning-a-study-of-post-training-methods-for-large-language-models-2603.13985]] — Run 65 sibling SFT-vs-RL post-training paper — SFT-vs-RL provides the *SFT/DPO/PPO/GRPO/KTO/ORPO unified-objective-family framework*, PR2 provides the *router-side-stability primitive that any PPO-family algorithm must address when applied to MoE models* — together they bracket the post-training surface between unified-objective-family and architecture-side-stability primitives.
- [[emergent-concepts]] — parent wiki page