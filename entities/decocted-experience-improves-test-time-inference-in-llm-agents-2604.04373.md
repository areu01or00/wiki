---
title: "Decocted Experience Improves Test-Time Inference in LLM Agents"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [test-time-computing, inference-efficiency, llm-agents, context-augmentation]
sources: ["https://arxiv.org/abs/2604.04373"]
---

# Decoacted Experience Improves Test-Time Inference in LLM Agents

## Overview
This paper addresses the inefficiency of naive test-time scaling for complex reasoning and agentic tasks. The proposed Decoacted Experience method uses context as a complementary scaling axis for improving LLM performance at test time, systematically studying how to construct and leverage context to improve inference without updating model parameters. The work shows that context construction strategies matter significantly for test-time compute efficiency.

## Key Facts
- **Authors**: (from arXiv abstract — see paper)
- **Year**: 2026
- **arXiv**: [2604.04373](https://arxiv.org/abs/2604.04373)

## Key Contributions
- Introduces context as a complementary scaling axis for test-time LLM improvement
- Systematically studies context construction strategies for agentic and reasoning tasks
- Demonstrates that naive test-time compute scaling is inefficient compared to targeted context augmentation
- Load-bearing axis: test-time context augmentation without parameter updates

## Related Papers
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — Overthinking in LLM test-time compute
- [[q-evolve-self-evolving-llm-agents-with-in-distribution-optimization-2606.07367]] — Self-evolving LLM agents
- [[maxproof-scaling-mathematical-proof-with-generative-verifier-rl-and-population-level-test-time-scaling-2606.13473]] — Test-time scaling for mathematical proof
