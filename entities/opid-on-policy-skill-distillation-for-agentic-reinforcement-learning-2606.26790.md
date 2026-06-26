---
title: "OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [post-training, agentic-rl, skill-distillation, on-policy, llm-agents]
sources: ["https://arxiv.org/abs/2606.26790"]
---

# OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning

## Overview
OPID addresses the credit-assignment weakness of outcome-based agentic RL by introducing a token-level, on-policy self-distillation signal conditioned on the agent's own acquired skills, removing dependence on external skill memories or retrieved privileged context. The approach replaces sparse trajectory-level reward with dense per-token guidance that stays matched to the agent's current state distribution.

## Key Facts
- **Authors**: Yang, Shuo; Wu, Jinyang; Lu, Zhengxi; Shen, Yuhao; et al.
- **Year**: 2026
- **arXiv**: [2606.26790](https://arxiv.org/abs/2606.26790)
- **Date**: 2026/06/25

## Key Contributions
- Identifies two structural failures of existing skill-conditioned on-policy distillation: (1) reliance on costly external skill memories and (2) mismatch between retrieved skills and the agent's current state distribution.
- Proposes on-policy distillation directly conditioned on the agent's own acquired skills, eliminating both external retrieval and state-distribution shift.
- Provides dense token-level supervision on top of outcome-based RL, replacing sparse trajectory-level rewards with fine-grained per-step guidance.

## Related Papers
- [[escaping-the-self-confirmation-trap-an-execute-distill-verify-paradigm-for-agentic-experience-learning-2606.24428]] — sibling on-policy agentic distillation addressing self-confirmation failure
- [[renio-reweighting-negative-trajectory-importance-for-llm-on-policy-distillation-2606.23104]] — sibling reweighting negative-trajectory importance for on-policy LLM distillation
- [[v-zero-answer-label-free-on-policy-distillation-contrastive-evidence-2606.25319]] — sibling label-free on-policy distillation with contrastive evidence
- [[rethinking-reward-supervision-rubric-conditioned-self-distillation-2606.19327]] — sibling replacing scalar rewards with rubric-conditioned dense supervision
- [[progress-advantage-neglected-free-lunch-post-training-llm-agents-2606.26080]] — sibling post-training signal surface for LLM agents
