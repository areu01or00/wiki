---
title: "TMAS: Scaling Test-Time Compute via Multi-Agent Synergy"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [test-time-compute, multi-agent, inference-scaling, reasoning]
sources: ["https://arxiv.org/abs/2605.10344"]
---

# TMAS: Scaling Test-Time Compute via Multi-Agent Synergy

## Overview
Test-time scaling has become an effective paradigm for improving LLM reasoning by allocating additional computation during inference. This paper proposes TMAS, a framework that organizes inference as a collaborative process among specialized agents with hierarchical memories: an experience bank reuses low-level reliable intermediate conclusions and local feedback, while a guideline bank records previously explored high-level strategies to steer subsequent rollouts away from redundant reasoning patterns. TMAS introduces a hybrid reward RL scheme that jointly preserves basic reasoning capability, enhances experience utilization, and encourages exploration beyond previously attempted solution strategies.

## Key Facts
- **Authors**: George Wu, Nan Jing, Qing Yi, Chuan Hao, Ming Yang, Feng Chang, Yuan Wei, Jian Yang, Ran Tao, Bryan Dai
- **Year**: 2026
- **arXiv**: [2605.10344](https://arxiv.org/abs/2605.10344)
- **Subjects**: Artificial Intelligence (cs.AI)
- **Submitted**: 2026-05-11 (v1), revised 2026-05-19 (v2)

## Key Contributions
- Hierarchical memory architecture: experience bank (low-level intermediate conclusions) + guideline bank (high-level strategies)
- Hybrid reward RL scheme jointly preserving reasoning capability, experience utilization, and exploration
- Stronger iterative scaling than existing test-time scaling baselines on challenging reasoning benchmarks
- Hierarchical collaboration structure enables effective cross-trajectory information flow not present in single-agent test-time scaling
- Multi-agent synergy approach to test-time compute allocation — fundamentally different from single-agent scaling methods

## Related Papers
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — Different axis: TMAS is multi-agent collaborative scaling (hierarchical memories, experience/guideline banks); When More Thinking Hurts is single-model overthinking collapse
- [[self-improvement-can-self-regress-rise-and-collapse-llm-self-training-2606.21090]] — Different axis: TMAS is test-time (inference) scaling; Self-Improvement Can Self-Regress is training-time self-training collapse
- [[selective-forgetting-for-large-reasoning-models-2604.03571]] — Sibling from same run — LRM-specific selective forgetting
