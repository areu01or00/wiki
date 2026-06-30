---
title: "Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [uncertainty-quantification, computer-use-agents, vision-language-models, llm]
sources: ["https://arxiv.org/abs/2606.25760"]
---

# Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models

## Overview
Computer-use agents (e.g., Claude, GPT-4V-based agents that click through GUIs) translate vision-language model predictions into executable actions. A misclick can cascade into failed tasks, so calibrated uncertainty estimates are essential for rejection: the agent should abstain when uncertain rather than act confidently on a wrong prediction. This paper presents a benchmark evaluating post-hoc uncertainty quantification (UQ) methods across VLM-based computer-use agents, measuring whether UQ rankings transfer across agents, benchmarks, and observable interfaces.

## Key Facts
- **Authors**: [arXiv 2606.25760](https://arxiv.org/abs/2606.25760)
- **Year**: 2026
- **arXiv**: [2606.25760](https://arxiv.org/abs/2606.25760)

## Key Contributions
- **Computer-Use UQ Benchmark**: First benchmark measuring uncertainty calibration for VLM-based GUI agents across rejection-rate curves, calibration plots, and miss-severity ranking — showing that UQ methods that work well for classification fail to rank miss-severity in sequential GUI navigation
- **Cross-agent UQ instability**: Demonstrates that UQ rankings (e.g., which method best identifies high-risk misclicks) are not stable across different VLM backends or task distributions — a significant gap for deployment reliability
- **Practical recommendations**: Identifies which UQ methods (entropy, mutual information, ensemble disagreement) are most deployment-appropriate for computer-use agents operating in high-stakes environments

## Related Papers
- [[uncertainty-quantification-in-llm-agents-foundations-emerging-challenges-opportunities-2602.05073]] — Related Papers: Foundational UQ challenges for LLM agents
- [[origins-of-stochasticity-comprehensive-investigations-on-uncertainty-quantification-for-llms-2606.22792]] — Related Papers: Comprehensive UQ investigations for LLMs
