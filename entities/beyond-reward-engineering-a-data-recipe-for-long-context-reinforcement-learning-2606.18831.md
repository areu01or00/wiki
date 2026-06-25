---
title: "Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [reinforcement-learning, long-context, data-centric, agentic, llm-training, llm-research]
sources: ["https://arxiv.org/abs/2606.18831"]
---

# Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning

## Overview
This paper argues that the long-context RL bottleneck for LLMs is data diversity rather than reward engineering, and demonstrates that a simple outcome-based GRPO setup paired with a curated ~14K-example data recipe — spanning retrieval, multi-evidence synthesis, and reasoning task families — is sufficient to substantially improve long-context reasoning. The gains transfer to agentic workloads (GAIA +4.8, BrowseComp +7.0 when continuing RL on an agent-tuned model), showing that long-context RL data and agentic RL are not separable concerns.

## Key Facts
- **Authors**: Xu, Xiaoyue; Zhang, Sikui; Wang, Xiaorong; Han, Xu; Xiao, Chaojun
- **Year**: 2026
- **Date**: 2026-06-17
- **arXiv**: [2606.18831](https://arxiv.org/abs/2606.18831)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- Data-centric framing: long-context RL improvements are dominated by data recipe diversity rather than reward engineering, inverting the field's recent reward-engineering focus
- Constructs and curates eight datasets (~14K examples) across three complementary task families — retrieval, multi-evidence synthesis, and reasoning — for long-context RL training
- Achieves +7.2/+3.2/+6.4 average point gains on seven long-context benchmarks across Qwen3-4B/8B/30B-A3B with a minimal outcome-based GRPO setup, surpassing prior RL training sets
- Demonstrates direct transfer to agentic tasks: continuing RL training on an agent-tuned model with the same data recipe improves GAIA by +4.8 and BrowseComp by +7.0
- Argues for releasing long-context RL datasets alongside training recipes so that long-context and agentic RL research can iterate on data quality rather than reward design

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Data-mixing for pretraining sample efficiency
- [[holistic-data-scheduler-for-llm-pre-training-via-multi-objective-reinforcement-learning-2606.24133]] — Multi-objective data scheduling
- [[renio-reweighting-negative-trajectory-importance-for-llm-on-policy-distillation-2606.23104]] — On-policy distillation RL
- [[look-light-think-heavy-what-multimodal-chain-of-thought-reasoning-can-and-cannot-do-2606.22565]] — Multimodal CoT reasoning