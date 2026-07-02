---
title: "From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety, agent, mechanistic-interpretability, reward-modeling]
sources: ["https://arxiv.org/abs/2606.06223"]
---

# From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents

## Overview
Studies reward-hacking monitors in ReAct-style agents acting in Gameable ALFWorld and WebShop environments. Agents are instrumented with activation-based reward-hack scores, token-level entropy, and decision-context features to detect when internal activation patterns shift toward reward-hacking behavior before it manifests in the output.

## Key Facts
- **Authors**: Wilhelm, Patrick; Kao, Odej
- **Year**: 2026
- **arXiv**: [2606.06223](https://arxiv.org/abs/2606.06223)

## Key Contributions
- Context-calibrated mechanistic monitoring: activation-based reward-hack scores conditioned on environment context
- Token-level entropy as an early-warning signal for reward-hacking trajectory drift
- Decision-context features capturing the gap between agent reasoning and actual task completion
- Empirical evaluation in Gameable ALFWorld and WebShop — two established agent benchmarking environments

## Related Papers
- [[agents-last-exam-2606.05405]] — Agents' Last Exam: foundational agent benchmarking in sandboxed environments
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist: context management is load-bearing for LLM agents
