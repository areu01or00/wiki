---
title: "Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for Least-Privilege LLM Agents"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety, LLM agents, least-privilege, capability control, causal gating]
sources: ["https://arxiv.org/abs/2606.13884"]
---

# Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for Least-Privilege LLM Agents

## Overview
Modern decision systems increasingly rely on learned components whose outputs may be confident yet wrong, exposing downstream actions to costly errors. This paper introduces Risk-Aware Causal Gating (RACG), a framework that decides whether to act on, defer, or abstain from a model's prediction based on causal confidence estimation. The least-privilege principle is operationalized through capability minimization — deliberately restricting when the agent exercises its full capabilities, using uncertainty as the gating signal. This represents the first formal framework treating model capability suppression as a first-class safety primitive rather than an afterthought.

## Key Facts
- **Authors**: Iyer, Laxmipriya Ganesh; Babu, Rahul Suresh
- **Year**: 2026
- **arXiv**: [2606.13884](https://arxiv.org/abs/2606.13884)

## Key Contributions
- First framework treating capability minimization as a safety primitive (not just alignment training)
- Risk-Aware Causal Gating (RACG) uses causal confidence to gate model outputs — defer or abstain when confidence is low
- Least-privilege principle for LLM agents: agents should exercise only the minimum capabilities required for each specific task
- Demonstrates significant reduction in downstream error rates compared to always-acting baselines

## Related Papers
- [[calibrating-the-evaluator-does-probability-calibration-mitigate-preference-coupling-in-llm-agent-feedback-loops-2606.31371]] — Probability calibration for LLM agent feedback loops, complementary to risk-aware gating
- [[a-systematic-evaluation-of-black-box-uncertainty-estimation-methods-for-large-language-models-2606.19868]] — Black-box uncertainty estimation for LLMs, relevant to confidence-gating infrastructure
