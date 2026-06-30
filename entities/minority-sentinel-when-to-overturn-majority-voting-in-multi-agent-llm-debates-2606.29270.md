---
title: "Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [multi-agent, reasoning, llm, evaluation]
sources: ["https://arxiv.org/abs/2606.29270"]
---

# Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates

## Overview
Multi-Agent Debate (MAD) with Majority Voting is a dominant paradigm for improving LLM reasoning, but its effectiveness rests on the Condorcet Jury Theorem's assumption of independent errors. Since contemporary LLMs share similar pretraining corpora, their errors are strongly correlated, causing the majority to systematically suppress correct minority opinions. This paper identifies when to overturn majority voting and surfaces the minority sentinel mechanism.

## Key Facts
- **Authors**: Unknown
- **Year**: 2026
- **arXiv**: [2606.29270](https://arxiv.org/abs/2606.29270)

## Key Contributions
- Identifies correlated error problem in multi-agent LLM debates — majority suppresses minority correct opinions
- Proposes minority sentinel mechanism to detect when to overturn majority voting
- First paper in wiki to address the Condorcet failure mode for LLM multi-agent reasoning

## Related Papers
- [[consensus-is-strategically-insufficient-reasoning-trace-disagreement-as-a-knowledge-representation-signal-2606.04223]] — Prior work on reasoning trace disagreement as signal (shared theme of LLM disagreement)
- [[aura-adaptive-uncertainty-aware-refinement-llm-judge-2606.19714]] — LLM-as-Judge evaluation for multi-agent settings
