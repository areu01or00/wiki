---
title: "Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [robotics, manipulation, failure-detection, world-models, conformal-prediction, deployment-monitoring]
sources: ["https://arxiv.org/abs/2606.23085"]
---

# Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents

## Overview
Zhang, Lu, Wang, Kang, Kuo, Cheng, Wang, and Jenkins address the underexplored problem of failure detection in long-horizon robotic manipulation — where failure onset is ambiguous and dense temporal annotations are typically unavailable — by proposing Foresight, a failure-detection framework that monitors manipulation trajectories using latent representations from an action-conditioned world model, trained on only final task-level success or failure labels and calibrated via functional conformal prediction for adaptive detection thresholds, evaluated across LIBERO-Long, ManiSkill-Long, and BEHAVIOR-1K with SOTA vision-language-action policies and validated on real ReactorX-200 and Franka arms.

## Key Facts
- **Authors**: Zhang, Haoran; Lu, Yifu; Wang, Boyang; Kang, Xuhui; Kuo, Yen-Ling; Cheng, Zezhou; Wang, Mengdi; Jenkins, Odest Chadwicke
- **Year**: 2026
- **arXiv**: [2606.23085](https://arxiv.org/abs/2606.23085)
- **Date**: 2026-06-22

## Key Contributions
- Identifies the deployment-monitoring gap in long-horizon robotic manipulation: existing policies produce trajectories that may fail mid-execution, but failure onset is ambiguous, dense temporal annotations are typically unavailable, and per-step ground-truth verifiers do not exist — leaving real-world deployments without a reliable safety overlay.
- Proposes Foresight, a failure-detection framework that monitors manipulation trajectories using latent representations from an action-conditioned world model — leveraging the world model's predictive embeddings as a unified representation that captures both task-relevant state and forward-look-ahead signals, replacing per-step supervision with end-of-trajectory labels only.
- Designs a functional conformal prediction (FCP) calibration procedure that adapts detection thresholds based on the policy's predictive uncertainty distribution, yielding a calibrated failure detector that generalizes across policies without per-policy threshold tuning.
- Validates across SOTA vision-language-action policies on LIBERO-Long, ManiSkill-Long, and BEHAVIOR-1K simulation benchmarks and on real-robot long-horizon tasks (ReactorX-200 and Franka arms) — surfacing action-conditioned world-model embeddings as a scalable, policy-agnostic representation for reliable failure monitoring.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[world-value-models-robotic-manipulation-2606.24742]] — Sibling robotics world-model work targeting the data-selection axis (using value models to filter non-expert manipulation data); Foresight complements WVM by surfacing world-model embeddings as the right substrate for *deployment-time* failure monitoring — together they frame the world-model backbone as the load-bearing primitive for both the training-data-filter and the runtime-safety surfaces of manipulation policy deployment.
- [[worldlines-benchmarking-and-modeling-long-horizon-stateful-2606.18847]] — Sibling long-horizon household-assistance benchmark with ObsMem memory framework; Foresight complements WorldLines by isolating the missing failure-detection axis of long-horizon embodied deployment — where WorldLines asks "can the agent remember the household state?" and Foresight asks "can the deployment system detect when the manipulation policy is failing mid-trajectory?"
- [[world-action-models-a-survey-2606.20781]] — Sibling WAM survey; Foresight's world-model-as-monitoring-substrate pattern is the runtime-monitoring complement to the survey's deployment-regime axis, showing that the same predictive representations useful for action generation are also the right basis for safety monitoring.
- [[ebench-elemental-diagnosis-of-generalist-mobile-manipulation-policies-2606.18239]] — Sibling multi-axis diagnostic benchmark; Foresight complements EBench by isolating the *runtime* failure-detection axis that the diagnostic benchmark surfaces only statistically — EBench measures aggregate capability profiles while Foresight detects per-trajectory failures during deployment.