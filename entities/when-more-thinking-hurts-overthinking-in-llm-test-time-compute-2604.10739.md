---
title: "When More Thinking Hurts: Overthinking in LLM Test-Time Compute"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [inference-efficiency, reasoning, test-time-compute, llm]
sources: ["https://arxiv.org/abs/2604.10739"]
---

# When More Thinking Hurts: Overthinking in LLM Test-Time Compute

## Overview
Scaling test-time compute through extended chains of thought has become a dominant paradigm for improving LLM reasoning. However, existing research implicitly assumes that longer thinking always yields better results. This paper systematically investigates how the marginal utility of additional reasoning tokens changes as compute budgets increase — finding that marginal returns diminish substantially at higher budgets and that models exhibit "overthinking," abandoning previously correct answers. Optimal thinking length varies across problem difficulty, making uniform compute allocation suboptimal.

## Key Facts
- **Authors**: Zhou, Shu; Ling, Rui; Chen, Junan; Wang, Xin; Fan, Tao + 1 more
- **Year**: 2026
- **arXiv**: [2604.10739](https://arxiv.org/abs/2604.10739)

## Key Contributions
- First paper to systematically document **overthinking** as a failure mode in LLM test-time compute scaling — extended reasoning is associated with *abandoning previously correct answers*
- **Cost-aware evaluation framework** revealing that the optimal stopping point varies by problem difficulty — uniform compute allocation is structurally suboptimal
- **Marginal utility curve** of additional reasoning tokens: diminishing returns at high budgets, with a regime where more thinking actively hurts
- Establishes *overthinking-as-a-structural-failure-mode* distinct from *underthinking* (too few reasoning tokens to reach the answer)
- *Optimal-thinking-length-variation-by-problem-difficulty* primitive: problems have a task-specific optimal compute budget; exceeding it causes regression
- *Diminishing-marginal-returns-at-high-compute* primitive: the test-time compute scaling curve is not monotonic
- Cost-benefit framework for test-time compute deployment: stopping at the optimal point outperforms both fixed short and fixed long thinking

## Related Papers
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Adaptive Test-Time Compute Allocation (related: adaptive compute routing — different axis: this paper focuses on when MORE thinking hurts, that paper focuses on WHEN to allocate compute)
- [[reasoning-about-reasoning-bapo-bounds-on-chain-of-thought-token-complexity-in-llms-2602.02909]] — BAPO Bounds on CoT Complexity (related: complexity bounds on reasoning tokens)
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — Self-reference (this paper)
