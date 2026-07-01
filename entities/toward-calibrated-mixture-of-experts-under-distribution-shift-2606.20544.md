---
title: "Toward Calibrated Mixture-of-Experts Under Distribution Shift"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [calibration, mixture-of-experts, distribution-shift, moe, reliability]
sources: ["https://arxiv.org/abs/2606.20544"]
---

# Toward Calibrated Mixture-of-Experts Under Distribution Shift

## Overview
This paper studies how Mixture-of-Experts (MoE) models behave under distribution shift, focusing on the interaction between routing mechanisms and expert-level calibration. The key finding is that expert calibration is sufficient to ensure overall model calibration under a broad class of distribution shifts for hard-routed MoEs, but insufficient for soft-routed models. The paper proposes adversarial reweighting to penalize calibration errors of the routed aggregate under distribution shift, improving the accuracy-calibration tradeoff.

## Key Facts
- **Authors**: Wong, Gina; Prinster, Drew; Saria, Suchi + 2
- **Year**: 2026
- **arXiv**: [2606.20544](https://arxiv.org/abs/2606.20544)
- **Date**: 2026-06-18

## Key Contributions
- Establishes theoretical conditions under which expert calibration ensures overall MoE calibration under distribution shift
- Demonstrates that soft-routed MoEs break the sufficiency condition that holds for hard-routed models
- Proposes adversarial reweighting penalizing calibration errors of the routed aggregate under distribution shift
- Shows improvements on both average and difficult data subsets across model classes, tasks, and distribution shifts

## Related Papers
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Task routing in MoE (orthogonal: routing theory vs. calibration under shift)
