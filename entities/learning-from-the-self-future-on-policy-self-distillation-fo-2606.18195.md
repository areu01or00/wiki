---
title: "Learning from the Self-future: On-policy Self-distillation for dLLMs"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [diffusion-llm, distillation, training, post-training, reasoning]
sources: ["https://arxiv.org/abs/2606.18195"]
---

# Learning from the Self-future: On-policy Self-distillation for dLLMs

## Overview
d-OPSD is the first On-Policy Self-distillation (OPSD) framework specifically designed for diffusion LLMs (dLLMs). Unlike autoregressive OPSD which uses left-to-right prefix conditioning, d-OPSD reframes self-teacher construction using self-generated answers as suffix conditioning — enabling the student to learn from "self future-experience" rather than privileged prefixes. Shifts supervision from token-level to step-level, aligned with dLLM iterative denoising. Achieves superior sample efficiency on four reasoning benchmarks.

## Key Facts
- **Authors**: To be confirmed
- **Year**: 2026
- **arXiv**: [2606.18195](https://arxiv.org/abs/2606.18195)

## Key Contributions
- First OPSD framework tailored for diffusion LLMs (d-OPSD)
- Suffix conditioning via self-generated answers instead of left-to-right prefixes
- Step-level supervision aligned with iterative denoising process
- ~10% of optimization steps needed vs RLVR baselines
- Consistent improvement across four reasoning benchmarks

## Related Papers
- [[compresskv-semantic-retrieval-guided-kv-cache-compression-for-resource-efficient-long-context-llm-inference-2606.24467]] — Complementary: both address KV cache optimization for long-context inference
- [[coverage-driven-kv-cache-eviction-kvec-2606.29563]] — Complementary: both optimize inference efficiency via KV cache management
