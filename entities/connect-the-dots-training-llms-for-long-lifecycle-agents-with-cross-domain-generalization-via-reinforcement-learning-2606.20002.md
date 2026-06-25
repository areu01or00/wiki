---
title: "Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [long-horizon-agents, reinforcement-learning, cross-domain-generalization, agent-training, meta-capability]
sources: ["https://arxiv.org/abs/2606.20002"]
---

# Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning

## Overview
Connect the Dots (CoD) frames a meta-capability that long-lifecycle LLM agents need: as a deployed agent solves a long sequence of tasks while exploring its environment, it must accumulate and reuse cross-task knowledge without losing it to context drift or per-domain overfitting. The paper presents a general RL training framework that teaches an LLM to "connect the dots" across sequential tasks in multiple environments, with explicit regularization for cross-domain generalization. The empirical result is that an agent trained under the CoD framework transfers competently to held-out task domains rather than collapsing to in-distribution performance — a property prior long-horizon agent training pipelines lacked.

## Key Facts
- **Authors**: Chen, Yanxi; Shi, Weijie; Xie, Yuexiang; Hu, Boyi; Li, Yaliang; et al.
- **Year**: 2026 (revised 2026-06-18)
- **arXiv**: [2606.20002](https://arxiv.org/abs/2606.20002)
- **Subjects**: cs.LG

## Key Contributions
- Formulates long-lifecycle agent training as a cross-domain RL problem, isolating the "connect the dots" meta-capability (cross-task knowledge accumulation with cross-domain transfer) from single-task proficiency.
- Proposes a training framework with explicit cross-domain generalization regularization, addressing the failure mode where long-lifecycle agents overfit to their training environment distribution.
- Demonstrates empirical transfer to held-out task domains — the trained agent retains competence rather than collapsing to in-distribution performance, the canonical long-horizon-agent generalization failure.
- Bridges the long-horizon-agent literature (plan persistence, memory management, tool retrieval) with the cross-domain RL literature, providing a unified training recipe that subsumes prior single-domain approaches.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain that led to this discovery (HF daily+monthly emergent-concept run on 2026-06-25).
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — PlanBench-XL measures the long-horizon-tool-use axis; CoD trains for the long-horizon-cross-domain axis. Together they characterize the failure surface of long-lifecycle agents from both evaluation and training sides.
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist identifies the *retention* failure mode at the trace level; CoD addresses the *transfer* failure mode at the training level. Complements the inference-time plan-aware eviction policy with a training-time cross-domain RL recipe.