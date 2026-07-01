---
title: "GRADE: Graph Representation of LLM Agent Dependency and Execution"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm-agents, graph-representation, dependency-modeling, trace-analysis]
sources: ["https://arxiv.org/abs/2606.22741"]
---

# GRADE: Graph Representation of LLM Agent Dependency and Execution

## Overview
GRADE proposes a unified graph representation for LLM agent execution traces that models both execution order (what ran when) and dependency relationships (what each step relied on). The key insight is that standard agent traces log execution but not the dependency edges between steps — GRADE recovers this missing layer, enabling failure prediction and fault localization that execution-only metrics miss.

## Key Facts
- **arXiv**: [2606.22741](https://arxiv.org/abs/2606.22741)
- **Year**: 2026
- **Theme**: graph-representation / dependency-modeling / agent-trace

## Key Contributions
- Introduces a dual-layer graph representation for LLM agent runs: execution edges (what ran in what order, read from trace) and dependency edges (what each step relied on, rarely logged — graded by how each is known: observed, declared, or inferred)
- Shows the dependency layer can predict failure where run-size metrics are weak; under leave-one-corpus-out transfer, the dependency layer stays above chance on every held-out class while run-size fails
- Provides a feature-based alternative to generic graph neural networks, which may misread the dependency layer
- Enables fault localization in failed multi-agent runs via the execution layer
- Opens further applications: efficiency and robustness optimization at scale

## Related Papers
- [[from-agent-traces-to-trust-a-survey-of-evidence-tracing-and-execution-provenance-in-llm-agents-2606.04990]] — Parent survey on evidence tracing and execution provenance in LLM agents
- [[cognitive-episodes-in-llm-reasoning-traces-enable-interpretable-human-item-diffi-2606.28186]] — Reasoning trace analysis for interpretability
- [[hidden-thoughts-are-not-secret-reasoning-trace-exposure-in-llms-2606.00642]] — Reasoning trace exposure/security
