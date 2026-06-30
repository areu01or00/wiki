---
title: "PEAR: Permutation-Equivariant Adaptive Routing Multi-Agent Debate"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [llm, multi-agent, debate, reasoning, routing]
sources: ["https://arxiv.org/abs/2606.20621"]
---

# PEAR: Permutation-Equivariant Adaptive Routing Multi-Agent Debate

## Overview
PEAR (Permutation-Equivariant Adaptive Routing Multi-Agent Debate) is an inference-time protocol for multi-agent LLM debate that dynamically reconfigures communication roles and sparse topologies across consecutive debate rounds. It eliminates positional bias through strategic agent position switching and selective agent activation, while maintaining productive debate dynamics.

## Key Facts
- **Authors**: (to be filled from paper)
- **Year**: 2026
- **arXiv**: [2606.20621](https://arxiv.org/abs/2606.20621)

## Key Contributions
- Permutation-equivariant architecture ensuring debate outcomes are independent of agent ordering — fair evaluation regardless of initial role assignment
- Dynamic sparse topology reconfiguration across consecutive debate rounds; 40% fewer active agents while improving accuracy
- State-of-the-art results on reasoning, math, and code generation tasks with reduced compute cost

## Related Papers
- [[sequential-consensus-for-multi-agent-llm-debates-a-wald-sprt-compute-governor-with-calibration-based-failure-detection-2605.19193]] — Sequential Consensus: Compute-governor controlled multi-agent debate — PEAR extends this with adaptive topology reconfiguration
- [[the-value-of-variance-mitigating-debate-collapse-in-multi-agent-systems-via-uncertainty-driven-policy-optimization-2602.07186]] — Value of Variance: Uncertainty-driven policy to prevent debate collapse — PEAR adds permutation-equivariant routing to avoid positional bias
- [[democratic-icai-debate-steering-principles-preferences-2606.28294]] — Democratic ICAI Debate: Principled preference aggregation for multi-agent debate — orthogonal to PEAR's routing architecture
