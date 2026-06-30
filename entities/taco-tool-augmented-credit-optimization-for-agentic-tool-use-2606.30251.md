---
title: "TACO: Tool-Augmented Credit Optimization for Agentic Tool Use"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [agentic-ai, reinforcement-learning, tool-use, credit-assignment]
sources: ["https://arxiv.org/abs/2606.30251"]
---

# TACO: Tool-Augmented Credit Optimization for Agentic Tool Use

## Overview
TACO (Tool-Augmented Credit Optimization) addresses the credit assignment problem in agentic multimodal models that perform operations on images via code. When operations can be useful, redundant, or misleading, outcome-only rewards fail and existing process rewards either don't attribute correctness to individual tool calls or require external judges. TACO introduces a GRPO variant for code-tool agents using two coupled advantage channels: DAPR (Differential Answer-Probe Reward) and a probe-token mechanism for self-supervised, judge-free tool-contribution attribution.

## Key Facts
- **Authors**: Mingkuan Feng, Jinyang Wu, Hao Gu, et al.
- **Year**: 2026
- **arXiv**: [2606.30251](https://arxiv.org/abs/2606.30251)

## Key Contributions
- **Differential Answer-Probe Reward (DAPR)**: self-supervised, judge-free advantage channel that credits each tool call by its own effect on answering correctly
- **Probe tokens**: inserted to enable self-supervised tool-contribution attribution without external judge model
- **GRPO variant** for code-tool agents with dual advantage channels
- Solves the tool-use credit assignment problem in agentic multimodal settings

## Related Papers
- [[scaling-the-horizon-not-the-parameters-reaching-trillion-parameter-performance-with-a-35b-agent-2606.30616]] — Agents-A1: agent-horizon scaling via long-horizon trajectories
- [[agentodyssey-open-ended-long-horizon-text-game-generation-for-test-time-continual-learning-agents-2606.24893]] — AgentOdyssey: test-time continual learning evaluation
- [[self-improvement-can-self-regress-rise-and-collapse-llm-self-training-2606.21090]] — Self-Improvement Can Self-Regress: RL self-training collapse
