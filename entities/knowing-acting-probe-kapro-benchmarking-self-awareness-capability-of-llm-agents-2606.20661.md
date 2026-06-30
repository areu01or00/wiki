---
title: "From Knowing to Acting: Benchmarking Self-Awareness Capability of LLM Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent, benchmarking, self-awareness, metacognition]
sources: ["https://arxiv.org/abs/2606.20661"]
---

# From Knowing to Acting: Benchmarking Self-Awareness Capability of LLM Agents

## Overview
This paper introduces KAPRO (Knowing-Acting Quadrant PRObe), a framework that evaluates cognitive-behavioral alignment in LLM agents by assessing their ability to discern whether a problem can be solved via internal parametric knowledge or requires external resources (tools, information). The benchmark addresses a critical gap: existing agent evaluations prioritize execution success while ignoring self-awareness — the metacognitive capacity to know what one knows and doesn't know.

## Key Facts
- **Authors**: Yifan Li, Shengbin Yue, Boyu Feng, Jinhu Qi, Bo Ke, Zixing Song, Hongru Wang, Zhongyu Wei, Irwin King
- **Year**: 2026
- **arXiv**: [2606.20661](https://arxiv.org/abs/2606.20661)

## Key Contributions
- **KAPRO framework**: Knowing-Acting Quadrant PRObe — evaluates agents across 4 quadrants based on whether they correctly identify problems as solvable internally or requiring external resources
- **Cognitive-behavioral alignment metric**: Measures the gap between an agent's self-assessment of knowledge and its actual capability to solve problems
- **Self-awareness taxonomy**: Categorizes agent failures into overconfident internalization (claiming knowledge that isn't in parameters) and underconfident delegation (requesting tools for solvable internal problems)
- **Findings**: Current frontier models exhibit systematic self-awareness failures in tool-use scenarios, particularly overestimating internal parametric knowledge

## Related Papers
- [[the-metacognitive-monitoring-battery-a-cross-domain-benchmark-for-llm-self-monitoring-2604.15702]] — Cross-domain benchmark for LLM self-monitoring (companion benchmark paper, different scope: task-general metacognition vs. tool-specific KAPRO)
- [[metis-learning-to-jailbreak-llms-via-self-evolving-metacognitive-policy-optimization-2605.10067]] — Metacognitive policy optimization for adversarial robustness (different axis: self-awareness applied to security vs. KAPRO's knowledge-resource discernment)
- [[goal-autopilot-a-verifiable-anti-fabrication-firewall-for-unattended-long-horizon-agents-2606.11688]] — Verifiable honesty firewall for agents (complementary: both probe agent self-knowledge limitations, KAPRO at capability-assessment level, Goal-Autopilot at honest-termination level)
