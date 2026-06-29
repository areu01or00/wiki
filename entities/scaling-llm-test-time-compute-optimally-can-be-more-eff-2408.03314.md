---
title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Parameters"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [test-time-compute, scaling-laws, inference-optimization, llm]
sources: ["https://arxiv.org/abs/2408.03314"]
---

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Parameters

## Overview
This paper studies how LLMs can improve their outputs by using more test-time (inference-time) computation. The authors analyze two primary mechanisms: (1) searching against dense process-based verifier reward models and (2) updating the LLM itself during inference. They introduce compute-optimal test-time scaling strategies that dynamically allocate inference compute based on prompt difficulty, demonstrating that test-time computation can outperform simply scaling up model parameters.

## Key Facts
- **Authors**: Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar
- **Year**: 2024
- **arXiv**: [2408.03314](https://arxiv.org/abs/2408.03314)

## Key Contributions
- First systematic analysis of test-time compute scaling mechanisms in LLMs
- Proposer-Verifier framework: distinguishes between proposing (LLM generates candidates) and verifying (process-based reward models score each step)
- Compute-optimal test-time scaling: dynamically allocates inference compute proportional to prompt difficulty
- Demonstrates that for many tasks, test-time compute scaling outperforms training-time parameter scaling
- Opens direction of generally self-improving agents that operate on open-ended natural language

## Related Papers
- [[test-time-scaling-makes-overtraining-compute-optimal-2604.01411]] — T2 scaling laws jointly optimize pretraining + test-time compute; companion framework extending this work
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — Documents failure modes of test-time compute scaling (overthinking/underthinking)
