---
title: "ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [instruction-tuning, on-policy-distillation, llm-reasoning, self-distillation]
sources: ["https://arxiv.org/abs/2605.28014"]
---

# ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains

## Overview
On-policy self-distillation (OPSD) improves LLM reasoning by providing dense token-level supervision for on-policy rollouts. However, existing OPSD methods yield limited in-domain gains and generalize poorly out-of-domain. ROSD identifies two key failure modes: conditioning the self-teacher on a verified solution creates confirmation bias, and the self-teacher lacks task-specific adaptation signals. The paper proposes reflective conditioning and domain-aware adaptation to address both.

## Key Facts
- **Authors**: Zhao, Ziqi; Ma, Xinyu; Yang, Liu + 6
- **Year**: 2026
- **arXiv**: [2605.28014](https://arxiv.org/abs/2605.28014)

## Key Contributions
- Identifies two failure modes in OPSD: confirmed-solution conditioning bias and lack of task-specific adaptation
- Proposes reflective conditioning: self-teacher receives the student's own reasoning trajectory, not the ground truth
- Domain-aware adaptation layer that injects task-specific distributional signals into the self-teacher
- Evaluates across 8 reasoning domains showing +12% average improvement over prior OPSD methods

## Related Papers
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — OPID (concurrent work): on-policy distillation for agentic RL, complementary to ROSD's domain-general reasoning framing
