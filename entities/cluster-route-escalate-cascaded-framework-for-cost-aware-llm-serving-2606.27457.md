---
title: "Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [serving, inference, cost-efficiency, cascaded-inference, query-routing]
sources: ["https://arxiv.org/abs/2606.27457"]
---

# Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving

## Overview
A two-stage cascaded LLM serving framework that clusters incoming queries by difficulty and assigns cost-effective models, with a quality-estimation cascade that escalates low-quality outputs to stronger models. Achieves 97-99% of the strongest model's accuracy at significantly reduced inference cost.

## Key Facts
- **Authors**: 
- **Year**: 2026
- **arXiv**: [2606.27457](https://arxiv.org/abs/2606.27457)
- **Online Date**: 2026-06-25

## Key Contributions
- Two-stage cascaded serving: Stage 1 query clustering assigns each cluster to its most cost-effective model; Stage 2 quality estimation cascade escalates low-quality outputs to stronger models
- Interpretable cost budget hyperparameter tuned offline; adapts to model pool changes without manual reconfiguration
- Retains 97-99% of strongest model's accuracy while reducing Time Per Output Token (TPOT)
- Requires only task-correctness labels (no human labels or reference outputs)

## Related Papers
- [[declarative-router-policy-compilation-from-inference-routing-to-agent-orchestration-cross-layer-verification-2603.27299]] — Routing and orchestration (sibling routing work)
- [[gbc-gradient-based-connections-for-optimizing-multi-agent-systems-2606.28187]] — Multi-agent system optimization (sibling resource management work)
- [[emergent-concepts]] — Parent meta-page for emergent concept discoveries
