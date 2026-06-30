---
title: "Draft-Thinking: Learning Efficient Reasoning in Long Chain-of-Thought LLMs"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [architecture, llm, inference-efficiency, reasoning]
sources: ["https://arxiv.org/abs/2603.00578"]
---

# Draft-Thinking: Learning Efficient Reasoning in Long Chain-of-Thought LLMs

## Overview
Draft-Thinking addresses the systematic overthinking problem in long chain-of-thought reasoning models, where performance gains come with substantially increased reasoning budgets. Rather than post-hoc token compression or truncation, Draft-Thinking guides models to learn a concise draft-style reasoning structure that retains only critical reasoning steps.

## Key Facts
- **Authors**: Jie Cao, Tianwei Lin, Zhenxuan Fan, Bo Yuan, Ziyuan Zhao, Rolan Yan, Wenqiao Zhang, Siliang Tang
- **Year**: 2025
- **arXiv**: [2603.00578](https://arxiv.org/abs/2603.00578)

## Key Contributions
- Proposes learning a draft-style reasoning structure for LRMs
- Retains only critical reasoning steps, discarding unnecessary tokens
- Decouples reasoning capability from reasoning cost
- Addresses systematic overthinking in existing CoT paradigms

## Related Papers
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — "When More Thinking Hurts": overthinking in test-time compute scaling (same reasoning-efficiency family)
