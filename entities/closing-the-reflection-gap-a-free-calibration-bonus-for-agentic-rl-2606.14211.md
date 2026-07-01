---
title: "Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [LLM agents, self-reflection, calibration, reinforcement learning, agentic RL, self-assessment]
sources: ["https://arxiv.org/abs/2606.14211"]
---

# Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL

## Overview
LLM agents deployed in external environments observe concrete feedback (execution results, error messages, tool outputs) but tend to mis-assess their own outputs after observing this feedback — even for questions they answered correctly. This "reflection gap" persists because standard RL barely helps due to a credit-assignment mismatch. RefGRPO fixes this with two ingredients: a free calibration bonus computed by contrasting the agent's own reflection with the actual outcome, and a dynamic coefficient schedule. Result: reduces underconfidence rate from 44.4% to 7.7% while improving task accuracy from 75.1% to 76.5% on text-to-SQL across five benchmarks.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.14211](https://arxiv.org/abs/2606.14211)

## Key Contributions
- Identifies and measures the reflection gap in LLM agents: mis-assessment of own outputs after environment feedback
- RefGRPO: free calibration bonus (contrast reflection with outcome, no extra reward model/LLM judge needed) + dynamic coefficient schedule
- Reduces underconfidence rate by 44.4% → 7.7% on text-to-SQL benchmarks
- Improves task accuracy by 75.1% → 76.5% simultaneously with better reflection calibration
- Enables calibrated reflection as pseudo-reward for self-improvement without outcome supervision
- Enables effective test-time selective prediction: commit only to rollouts flagged as correct

## Related Papers
- [[clustered-self-assessment-uncertainty-quantification-llms-2606.03846]] — Clustered self-assessment via representation clustering for LLM UQ (orthogonal: RefGRPO uses environment-outcome-contrast for calibration; clustered self-assessment uses representation analysis)
- [[latent-confidence-alignment-for-llm-self-assessment-2606.21937]] — Latent confidence alignment for LLM self-assessment (orthogonal: RefGRPO addresses reflection gap via outcome contrast; latent confidence alignment trains via representation-based confidence signals)
- [[teaching-large-reasoning-models-effective-reflection-2601.12720]] — Teaching large reasoning models effective reflection (orthogonal: focuses on reasoning models; RefGRPO addresses general agentic RL setting with environment feedback)
