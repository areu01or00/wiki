---
title: "Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [mechanistic-interpretability, agent, depth-allocation, layer-wise, llm]
sources: ["https://arxiv.org/abs/2605.27935"]
---

# Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning

## Overview
This paper studies whether LLM agents utilize depth inefficiently in autonomous agent settings through systematic layer-wise analysis of complete user-agent trajectories across Deep Research, Code Generation, and Tabular Processing. Using residual stream probes, causal layer-skipping interventions, and effective-depth measurements, it reveals that agentic reasoning exhibits a distinct depth profile from static tasks: models progressively recruit deeper layers as trajectories unfold, with stronger long-range inter-layer dependencies emerging in later turns.

## Key Facts
- **Authors**: Zhenyu Cui, Xiangzhong Luo
- **Year**: 2025
- **arXiv**: [2605.27935](https://arxiv.org/abs/2605.27935)

## Key Contributions
- Distinct depth profile: agentic reasoning progressively recruits deeper layers as trajectories unfold, unlike static single-turn tasks
- Correction-dominant updates: residual updates shift from stable feature accumulation to repeated recalibration in later turns
- Construction-refinement gap: semantic direction forms early while deep layers remain necessary for stabilizing final outputs
- Domain variation: Qwen and Minimax show pronounced construction-refinement gap; GLM shows more domain-dependent depth allocation
- Evidence for adaptive depth allocation: models allocate depth adaptively as reasoning complexity grows within agentic settings

## Related Papers
- [[complexity-ceiling-benchmark-multi-domain-evaluation-sequential-reasoning-depth-scaling-2606.29278]] — Complementary: CCB measures depth scaling at evaluation level, Do Agents Think Deeper investigates the internal mechanistic substrate
- [[calibration-is-not-control-llm-agent-oversight-needs-intervention-2606.21399]] — Agent oversight and intervention needs
- [[draft-thinking-learning-efficient-reasoning-in-long-chain-of-thought-llms-2603.00578]] — Efficient reasoning in long chain-of-thought
