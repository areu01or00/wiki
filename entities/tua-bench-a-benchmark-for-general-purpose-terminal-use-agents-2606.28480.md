---
title: "TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [benchmark, agent, terminal, computer-use, evaluation]
sources: ["https://arxiv.org/abs/2606.28480"]
---

# TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents

## Overview
TUA-Bench introduces a general-purpose benchmark for terminal-use agents (TUAs) — LLMs operating in terminal environments beyond coding. It covers 120 real-world tasks across five families: document editing, email management, live-web information seeking, and scientific/engineering workflows co-designed with PhD-level domain experts requiring specialized software. Evaluated via deterministic setup scripts and execution-based scoring, TUA-Bench finds the strongest frontier agent (Claude Code with Claude Opus 4.8) achieves 65.8% overall performance, revealing substantial gaps in general-purpose terminal capability.

## Key Facts
- **Authors**: Shoufa Chen, Luyuan Wang, Xuan Yang, Zhiheng Liu, Yuren Cong, Yuanfeng Ji, Feiyan Zhou, Xiao [et al.]
- **Year**: 2026
- **arXiv**: [2606.28480](https://arxiv.org/abs/2606.28480)

## Key Contributions
- First general-purpose terminal-use agent benchmark covering non-programming digital activities (document editing, email, live-web search)
- Five task families including domain-expert co-designed scientific workflows requiring specialized software
- Deterministic execution-based evaluation with real terminal setup scripts — not synthetic/simulated environments
- 120 manually designed real-world tasks across routine and specialized domains
- Claude Code + Opus 4.8 max reasoning effort achieves 65.8% — significant headroom for improvement

## Related Papers
- [[cli-universe-towards-verifiable-task-synthesis-engine-for-terminal-agents-2606.22883]] — Verifiable task synthesis for terminal agents
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — Computer-use agent evaluation and contextual integrity
- [[how-much-coordination-gain-is-real-a-paired-noise-floor-protocol-for-multi-agent-llm-benchmarks-2606.20695]] — Paired noise floor protocol for multi-agent LLM benchmarks
