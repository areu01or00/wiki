---
title: "CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [agentic-RL, credit-assignment, self-distillation, reinforcement-learning]
sources: ["https://arxiv.org/abs/2606.29476"]
---

# CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning

## Overview
Self-distilled agentic RL augments trajectory-level reward with token-level distillation loss, using the same policy conditioned on privileged context as teacher. CRAFT addresses the key limitation that the prevailing single-scalar gating (teacher-student logprob gap) is retrospective and only scores realized rollouts — never the counterfactual alternatives. By generating free sibling rollouts under modified contexts, CRAFT enables counterfactual credit assignment at the token level.

## Key Facts
- **Authors**: Meng, Zibin; Chen, Kani
- **Year**: 2026
- **arXiv**: [2606.29476](https://arxiv.org/abs/2606.29476)

## Key Contributions
- Counterfactual credit assignment via free sibling rollouts — scores what the policy *would have* done under different context
- Token-level distillation loss conditioned on privileged context, not just realized trajectory
- Self-distilled agentic RL with dual signal: trajectory reward + token-level distillation
- Addresses retrospective limitation of single-scalar teacher-student gap gating

## Related Papers
- [[craft-counterfactual-credit-assignment-from-free-sibling-rollouts-for-self-distilled-agentic-reinforcement-learning-2606.29476]] — (self-reference for cross-run discovery context)
