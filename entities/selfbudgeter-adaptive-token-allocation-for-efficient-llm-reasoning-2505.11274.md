---
title: "SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [inference-efficiency, reasoning, token-budgeting]
sources: ["https://arxiv.org/abs/2505.11274"]
---

# SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning

## Overview
SelfBudgeter addresses the problem of excessive token consumption in large reasoning models by training models to self-estimate the required reasoning budget based on query difficulty. The model learns to allocate fewer tokens for simple queries and more for complex ones, achieving adaptive token efficiency without sacrificing quality.

## Key Facts
- **Authors**: Li, Zheng; Dong, Qingxiu; Ma, Jingyuan + 3 others
- **Year**: 2025
- **arXiv**: [2505.11274](https://arxiv.org/abs/2505.11274)

## Key Contributions
- Self-adaptive reasoning budget estimation based on query difficulty
- Trains the model to self-estimate required tokens before generating
- Achieves comparable quality with significantly fewer tokens on simple queries
- First self-budgeting primitive for LLM token allocation

## Related Papers
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Constrained policy optimization for test-time compute allocation
- [[when-less-is-enough-efficient-inference-via-collaborative-reasoning-2605.01111]] — Collaborative dual-model reasoning
- [[bagen-are-llm-agents-budget-aware-2606.00198]] — Benchmark for LLM budget awareness
