---
title: "SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [benchmark, agentic-eval, smart-home, environment-grounded, llm-agents]
sources: ["https://arxiv.org/abs/2606.01912"]
---

# SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes

## Overview
SMH-Bench evaluates whether LLM agents can reason, interact, and act reliably in realistic state-dependent smart-home environments, where success requires reasoning over user intent, preferences, multi-device interactions, and evolving world state — beyond static instruction-to-API mapping or simplified simulations. The benchmark fills a structural gap in agentic evaluation: most existing benchmarks measure single-turn task completion rather than sustained environment-grounded agency.

## Key Facts
- **Authors**: Li, Kuan; Zhang, Shuo; Wang, Huacan; et al.
- **Year**: 2026
- **arXiv**: [2606.01912](https://arxiv.org/abs/2606.01912)
- **Date**: 2026/06/01

## Key Contributions
- Identifies that prior smart-home benchmarks focus on static instruction-to-API mapping or limited simulations and fail to capture whether LLMs can reliably reason, interact, and act in evolving household environments.
- Introduces SMH-Bench as a benchmark for sustained environment-grounded agency over user intent, device preferences, and multi-device interactions.
- Surfaces the smart-home environment as a structurally distinct evaluation surface for LLM agents — one that requires world-state tracking, preference learning, and dynamic action selection simultaneously.

## Related Papers
- [[evoarena-tracking-memory-evolution-robust-llm-agents-dynamic-environments-2606.13681]] — sibling dynamic-environment LLM agent benchmark with memory-evolution focus
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — sibling real-session agent benchmark for enterprise workspaces
- [[memtoolagent-leveraging-memory-tool-using-agents-environment-user-feedback-2606.07909]] — sibling environment+user-feedback-grounded memory-tool agent surface
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — sibling long-horizon tool-use planning benchmark
