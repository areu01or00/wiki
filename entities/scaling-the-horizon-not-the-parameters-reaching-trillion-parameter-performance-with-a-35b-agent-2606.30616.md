---
title: "Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [agentic-ai, moe, test-time-compute, inference-efficiency]
sources: ["https://arxiv.org/abs/2606.30616"]
---

# Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent

## Overview
Agents-A1 is a 35B Mixture-of-Experts agentic model that achieves trillion-parameter-level performance by scaling the agent horizon rather than model parameters. The key insight is that agent capability scales with long-horizon trajectory length and heterogeneous agent ability diversity, not raw parameter count. Built on a long-horizon knowledge-action infrastructure producing ~45K-token average trajectories.

## Key Facts
- **Authors**: Lei Bai, Zongsheng Cao, Yang Chen, et al.
- **Year**: 2026
- **arXiv**: [2606.30616](https://arxiv.org/abs/2606.30616)

## Key Contributions
- **Agent-horizon scaling** as a new axis orthogonal to parameter scaling: capability scales with trajectory length and ability diversity, not parameter count
- **Long-horizon knowledge-action infrastructure** connecting external knowledge, actions, observations, and verifier outcomes
- **Three-stage training recipe**: full-domain SFT, domain-level teacher models, and mu-... (continues)
- 35B MoE achieving trillion-parameter-level performance via horizon scaling alone

## Related Papers
- [[agentodyssey-open-ended-long-horizon-text-game-generation-for-test-time-continual-learning-agents-2606.24893]] — AgentOdyssey: procedural text game generation for test-time continual learning evaluation
- [[memobench-benchmarking-world-modeling-in-dynamically-changing-environments-2606.27537]] — MemoBench: world model memory consistency benchmark
- [[self-improvement-can-self-regress-rise-and-collapse-llm-self-training-2606.21090]] — Self-Improvement Can Self-Regress: rise-and-collapse failure mode in LLM self-training
