---
title: "Not All Queries Need Deep Thought: CoFiCot for Adaptive Coarse-to-fine Stateful Refinement"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [test-time-compute, adaptive-inference, reasoning, llm-efficiency]
sources: ["https://arxiv.org/abs/2603.08251"]
---

# Not All Queries Need Deep Thought: CoFiCot for Adaptive Coarse-to-fine Stateful Refinement

## Overview
Scaling test-time computation enhances LLM reasoning but faces a uniform computation paradox: allocating identical resources leads to over-correction on simple tasks and insufficient refinement on complex ones. CoFiCot (Coarse-to-Fine with Stateful Refinement) addresses this by dynamically tailoring inference strategies to problem difficulty — using a coarse-to-fine adaptive framework that decides how much compute to invest based on the perceived difficulty of each query, achieving better accuracy-efficiency tradeoffs than uniform allocation.

## Key Facts
- **Authors**: Dongxu Zhang, Hongqiang Lin, Yiding Sun, Pengyu Wang, Qirui Wang, Ning Yang, Jihua Zhu
- **Year**: 2026
- **arXiv**: [2603.08251](https://arxiv.org/abs/2603.08251)

## Key Contributions
- **Coarse-to-fine adaptive inference**: Dynamically tailors inference strategies (coarse vs fine-grained refinement) to the difficulty of each query
- **Uniform computation paradox resolution**: Avoids both over-correction on simple tasks and under-refinement on complex ones
- **Stateful refinement**: Maintains refinement state across tokens/steps to decide when to escalate or de-escalate computation
- **First in wiki**: First coarse-to-fine adaptive test-time compute allocation framework that resolves the uniform allocation paradox

## Related Papers
- [[process-supervision-of-confidence-margin-for-calibrated-llm-reasoning-2604.23333]] — Calibrated confidence margins for compute allocation (orthogonal: explicit margin signals vs CoFiCot difficulty-based routing)
- [[scatr-simple-calibrated-test-time-ranking-2604.16535]] — Calibrated test-time ranking for BoN selection (orthogonal: per-candidate ranking vs CoFiCot difficulty-driven compute scaling)
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Adaptive test-time compute allocation via constrained policy optimization (orthogonal: CoFiCot difficulty-driven vs C-PPO constrained-optimization)
