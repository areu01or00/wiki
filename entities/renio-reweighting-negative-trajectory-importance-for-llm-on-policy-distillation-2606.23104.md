---
title: "ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [llm, distillation, on-policy, reasoning, reinforcement-learning, training]
sources: ["https://arxiv.org/abs/2606.23104"]
---

# ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation

## Overview
ReNIO revisits on-policy distillation (OPD) for LLM reasoning — where a student is trained on its own generated outputs — and observes that standard OPD treats all student-generated outputs equally, including low-quality or off-trajectory samples that *hurt* the student. The paper proposes a trajectory-importance reweighting scheme (Negative Trajectory Importance Optimization, ReNIO) that down-weights or filters harmful negatives during on-policy rollouts, yielding measurable improvements in reasoning benchmarks. The core contribution is reframing "negative" trajectories not as uniform supervision noise but as a heterogeneous population that requires importance estimation.

## Key Facts
- **Authors**: Lin, Chen; Chen, Kedi; Zhang, Wei
- **Year**: 2026 (revised 2026-06-22)
- **arXiv**: [2606.23104](https://arxiv.org/abs/2606.23104)
- **Subjects**: cs.LG

## Key Contributions
- Identifies that standard on-policy distillation treats all student-generated outputs uniformly, including low-quality negatives that can degrade rather than improve student reasoning.
- Proposes ReNIO, a negative-trajectory importance reweighting mechanism that explicitly estimates per-rollout importance for on-policy distillation, filtering or down-weighting harmful samples.
- Reports empirical gains on standard reasoning benchmarks, demonstrating that reweighting is a load-bearing component of OPD rather than an optional refinement.
- Connects on-policy distillation to the broader literature on negative-sample handling in preference/RL training (RLHF/DPO family), reframing it as a *trajectory-importance* problem rather than a *reward-modeling* problem.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 as a fresh 2026 contribution to LLM distillation / on-policy training for reasoning.