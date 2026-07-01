---
title: "MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm-training, distillation, reinforcement-learning, post-training]
sources: ["https://arxiv.org/abs/2606.30406"]
---

# MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training

## Overview
Modern LLMs rely on RL during post-training to push specific capabilities, but integrating multiple capabilities into a single model remains difficult. Off-Policy Finetune and Mix-RL methods are either inefficient or lose performance. MOPD introduces Multi-Teacher On-Policy Distillation, where multiple specialized teacher models provide on-policy signal simultaneously, enabling efficient integration of diverse capabilities (reasoning, safety, instruction-following) into a single student model without capability regression.

## Key Facts
- **Authors**: Ma, Wenhan; Wei, Jianyu; Zhao, Liang + 10
- **Year**: 2026
- **arXiv**: [2606.30406](https://arxiv.org/abs/2606.30406)

## Key Contributions
- **On-policy multi-teacher distillation**: First framework to use multiple specialized teachers simultaneously in on-policy RL loop, preserving sample efficiency while avoiding capability regression
- **Capability integration without forgetting**: Student model retains all teacher capabilities post-distillation, addressing the catastrophic forgetting problem in multi-capability integration
- **Efficient rollouts**: Novel teacher routing and advantage estimation that reduces compute overhead vs. running each teacher independently
- **Strong empirical results**: Outperforms Mix-RL and Off-Policy Finetune on MATH, GSM8K, and safety benchmarks simultaneously

## Related Papers
- [[renio-reweighting-negative-trajectory-importance-for-llm-on-policy-distillation-2606.23104]] — ReNIO: negative trajectory importance for on-policy LLM distillation (prior wiki entry)
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — Structured output constraints in open-weight LLMs (prior wiki entry on tool calling)
