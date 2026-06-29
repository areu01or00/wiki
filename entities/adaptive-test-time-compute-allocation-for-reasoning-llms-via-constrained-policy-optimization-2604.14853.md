---
title: "Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [test-time-compute, constrained-optimization, compute-allocation, lagrangian-relaxation, llm-reasoning, primitive]
sources: ["https://arxiv.org/abs/2604.14853"]
---

# Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization

## Overview
Formalizes per-instance test-time compute allocation as a constrained optimization problem (maximize expected accuracy subject to an average compute budget) and solves it with a two-stage **Solve-then-Learn** pipeline. In the solve stage, Lagrangian relaxation decomposes the global constraint into per-instance sub-problems with closed-form oracle actions that optimally price accuracy against cost; in the learn stage, a lightweight classifier predicts oracle actions from cheap input features to amortize the rule for real-time deployment. Establishes task-level regret bounds and demonstrates up to 12.8% relative accuracy improvement on MATH under matched budget constraints across DeepSeek-V3, GPT-4o-mini, and Qwen2.5-7B.

## Key Facts
- **Authors**: Zhai, Zhiyuan; Li, Bingcong; Xiao, Bingnan; Li, Ming; Wang, Xin
- **Year**: 2026
- **arXiv**: [2604.14853](https://arxiv.org/abs/2604.14853)
- **Citation date**: 2026-04-16 (online 2026-04-16)
- **First author affiliation**: (not extracted)

## Key Contributions
- **Constrained-optimization formulation of test-time compute allocation**: replaces ad hoc heuristic compute schedules with a formal max-accuracy-under-budget objective decomposed via Lagrangian relaxation into per-instance sub-problems with closed-form oracle actions.
- **Solve-then-Learn pipeline**: stage 1 solves the Lagrangian relaxation exactly (monotone-cost property enables binary search for exact budget targeting); stage 2 amortizes the allocation rule via a lightweight classifier trained on cheap input features.
- **Task-level regret bound**: proves the learned policy's task-level regret is bounded by its imitation error times the worst-case per-instance gap, yielding a clean reduction from constrained inference to supervised classification.
- **Empirical validation**: 12.8% relative accuracy improvement on MATH under matched budget, 91%+ imitation accuracy to the Lagrangian oracle, with consistent gains across three LLMs.

## Related Papers
- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — Sibling test-time-scaling primitive operating at the local-branch-routing layer
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — Sibling test-time-scaling framework unified across sequential/parallel modes
- [[maxproof-scaling-mathematical-proof-with-generative-verifier-rl-and-population-level-test-time-scaling-2606.13473]] — Sibling verifier-driven test-time-scaling in mathematical-proof domain