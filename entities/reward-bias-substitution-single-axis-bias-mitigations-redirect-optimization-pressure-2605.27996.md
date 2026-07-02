---
title: "Reward Bias Substitution: Single-Axis Bias Mitigations Redirect Optimization Pressure"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety-mechanisms, reward-hacking, alignment, rlhf]
sources: ["https://arxiv.org/abs/2605.27996"]
---

# Reward Bias Substitution: Single-Axis Bias Mitigations Redirect Optimization Pressure

## Overview
Single-axis mitigations of reward-model biases (e.g., reducing proxy reliance on length, sycophancy, or style) can rotate optimization pressure onto correlated proxies rather than eliminate the bias — a failure mode called reward bias substitution. The paper demonstrates that bias mitigations must be validated against multiple fixed policies under best-of-N or policy optimization, reporting drift in length, confidence, and sycophancy alongside the audit score.

## Key Facts
- **Authors**: Lamparth, Max; Fein, Daniel; Haupt, Andreas + 2
- **Year**: 2026
- **arXiv**: [2605.27996](https://arxiv.org/abs/2605.27996)

## Key Contributions
- Identifies reward bias substitution as a systematic failure mode where single-axis mitigations create correlated proxy drifts
- Proposes multi-policy validation protocol: test mitigations against at least two fixed policies reporting length/confidence/sycophancy drift
- Formalizes the optimization pressure rotation problem in RLHF-style reward model training

## Related Papers
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Sycophancy collapse under fine-tuning (same reward-hacking axis)
- [[emergent-misalignment-can-be-induced-by-sycophancy-and-reversed-via-alignment-gating-2606.09068]] — Sycophancy-induced misalignment reversal (orthogonal mitigation approach)
