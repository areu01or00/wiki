---
title: "AsyncOPD: How Stale Can On-Policy Distillation Be?"
created: 2026-06-01
updated: 2026-06-01
type: entity
tags: [llm, post-training]
sources: ["https://arxiv.org/abs/2606.24143"]
---

# AsyncOPD: How Stale Can On-Policy Distillation Be?

## Overview
On-policy distillation (OPD) trains a student LLM on its own rollouts guided by teacher feedback, decoupled via asynchronous pipelines to overcome the systems bottleneck of synchronous rollout generation. This paper systematically studies the staleness problem in OPD — how stale-policy data affects training dynamics and final student quality — and provides the first empirical characterization of the staleness-quality tradeoff curve for LLM post-training.

## Key Facts
- **arXiv**: [2606.24143](https://arxiv.org/abs/2606.24143)
- **Date**: 2026-06-01

## Key Contributions
- First systematic study of stale-policy data effects in on-policy distillation for LLMs
- Staleness-quality tradeoff curve: characterizes how delay between rollout and update affects student model quality
- Analysis of which tasks/domains are most sensitive to staleness (reasoning workloads vs. knowledge tasks)
- Findings: reasoning-heavy workloads suffer more from staleness than knowledge distillation tasks


## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent concept discoveries

## Theme Framing
**Axis**: RLHF/post-training — on-policy distillation staleness as a training dynamics problem
