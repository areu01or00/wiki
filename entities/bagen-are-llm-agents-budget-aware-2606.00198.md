---
title: "BAGEN: Are LLM Agents Budget-Aware?"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [agent-evaluation, budget-awareness, llm-agent, token-budget, control-signal]
sources: ["https://arxiv.org/abs/2606.00198"]
---

# BAGEN: Are LLM Agents Budget-Aware?

## Overview
BAGEN systematically investigates whether frontier LLM agents can predict and respect computational/token budgets as a control signal during task execution. The work finds that current agents fail at budget awareness — they cannot reliably anticipate when they are about to run out of runway, treating budget as a passive post-hoc cost metric rather than an active control input. The work introduces a Budget-Aware Agent framework where budget is folded into the agent's decision loop as a first-class signal, alongside the more familiar task-completion signal.

## Key Facts
- **Authors**: Lin, Yuxiang; Wang, Zihan; Liu, Mengyang; Shan, Yuxuan; Bai, Longju; + 7 more (12 total)
- **Year**: 2026
- **arXiv**: [2606.00198](https://arxiv.org/abs/2606.00198)
- **Submitted**: 2026-05-29
- **Discovered via**: emergent-concept search on 2026-06-26 (agent-budget-awareness / control-signal / token-economy / runtime-cost-prediction theme)
- **First-in-wiki surface**: Budget-as-control-signal for LLM agents (verified via `ls entities/ | grep -iE "(budget|bagen|cost-aware)"` returning empty)

## Key Contributions
- Systematically defines *budget estimation* as two distinct axes: internal budgets (derived from environment signals such as remaining API calls, accumulated latency, or context length) and external budgets (imposed by user constraints such as dollar limits or wall-clock deadlines)
- Empirically demonstrates that frontier LLM agents waste 44% of tokens on tasks they ultimately fail at — the failure is predictable *in hindsight* but not *during execution*, indicating the missing primitive is budget-anticipation, not task-capability
- Proposes a Budget-Aware Agent (BAGEN) framework that treats budget as an active control signal: the agent receives explicit budget state, learns a budget-anticipation module, and uses the budget estimate to gate continuation, request clarification, or escalate to a higher-cost fallback
- Surfaces *budget-as-control-signal* as a load-bearing primitive for LLM agent deployment: the deployment regime where agents run unattended for long horizons requires them to manage their own runway, not just produce outputs

## Related Papers
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — sibling agent-runtime-design-survey (Are-Ready surveys the architectural choices including memory; BAGEN isolates the orthogonal budget-control axis — both surface that the *runtime substrate* of an LLM agent is a design space, not a fixed target)
- [[beyond-static-leaderboards-predictive-validity-evaluation-llm-agents-2606.19704]] — sibling agent-evaluation-methodology (Beyond-Static-Leaderboards argues aggregate-leaderboard scoring is structurally inadequate; BAGEN diagnoses a specific failure — budget-anticipation — that aggregate scores systematically hide)
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — sibling meta-evaluation (COUNSEL meta-evaluates agentic-task benchmarks; BAGEN surfaces a deployment-relevant failure mode that benchmark scores cannot surface — the failure occurs *during* execution, after the score is computed)
- [[emergent-concepts]] — parent meta-page for this discovery
