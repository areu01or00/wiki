---
title: "Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [post-training, distillation, reward, reasoning, llm]
sources: ["https://arxiv.org/abs/2606.19327"]
---

# Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation

## Overview
A post-training framework that replaces both chain-of-thought annotation (noisy/expensive) and scalar verified-reward RL (opaque credit assignment) with **rubric-conditioned self-distillation** — the teacher is conditioned on criterion-level rubrics and provides token-level guidance on the student's own sampled trajectories. The framework operationalizes rubrics as fine-grained feedback signals that convert qualitative criteria into token-level guidance over the reasoning process.

## Key Facts
- **Authors**: Gu, Siyi; Chen, Jialin; Zhou, Sophia; Cohan, Arman; Ying, Rex
- **Year**: 2026
- **arXiv**: [2606.19327](https://arxiv.org/abs/2606.19327)
- **Date**: 2026-06-17

## Key Contributions
- Introduces Rubric-Conditioned Self-Distillation: a teacher is conditioned on criterion-level rubrics to provide token-level guidance on the student's own sampled trajectories, avoiding the single-reference-rationale supervision trap.
- Surpasses GRPO by 1.0 points and OPSD by 0.9 points on average across science reasoning benchmarks, establishing rubric-level supervision as a viable alternative to scalar reward optimization.
- Two-stage pipeline: (i) learn to generate task-specific rubrics, (ii) train a rubric-guided reasoner — separating rubric-generation from rubric-conditioned reasoning.
- Reframes the supervision question: instead of "what is the right reasoning trace?" → "what criteria should a strong response satisfy, and how do those criteria map to token-level credit?"

## Related Papers
- [[progress-advantage-neglected-free-lunch-post-training-llm-agents-2606.26080]] — Sibling post-training-advantage work; complementary axis on implicit-advantage-as-signal vs rubric-as-supervision.
- [[v-zero-answer-label-free-on-policy-distillation-contrastive-evidence-2606.25319]] — Sibling label-free on-policy distillation work; contrasts with rubric-conditioning as a supervision source.
- [[renio-reweighting-negative-trajectory-importance-for-llm-on-policy-distillation-2606.23104]] — Sibling on-policy trajectory reweighting; complements rubric-conditioning on a distinct credit-assignment axis.
- [[distilling-examples-into-task-instructions-enhanced-in-context-2606.15641]] — Sibling in-context distillation; contrasts with rubric-conditioning's structured-feedback supervision.
- [[emergent-concepts]] — Parent wiki page tracking emergent-concept discoveries including this paper.