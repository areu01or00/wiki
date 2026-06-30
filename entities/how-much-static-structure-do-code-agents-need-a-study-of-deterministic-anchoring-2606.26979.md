---
title: "How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [code-agents, benchmarking, llm-agents]
sources: ["https://arxiv.org/abs/2606.26979"]
---

# How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring

## Overview
LLM-based code agents navigate repositories through keyword search but miss structural relationships (call graphs, inheritance hierarchies, configuration dependencies). This paper investigates lightweight static analysis as deterministic anchors: stable structural facts injected as plain-text comments that constrain probabilistic exploration and make navigation more predictable. The key finding is the deterministic anchoring effect: static structure helps less by making agents "smarter" and more by making their navigation disciplined and reproducible.

## Key Facts
- **Authors**: Zhihao Lin, Mingyi Zhou, Yizhuo Yang, Li Li
- **Year**: 2026
- **arXiv**: [2606.26979](https://arxiv.org/abs/2606.26979)

## Key Contributions
- Codex baseline + lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds)
- Scale-sensitive: denser semantics show diminishing returns; hub-heavy projects benefit from inverse-only "who-calls-me" links
- Tags raise link-following rate from 0.15-0.18 to 0.21-0.24, halve run-to-run variance, improve Pass@1 +3.4pp at ~10% more input tokens
- Practical guidelines: default to lightweight topology on medium projects; prune forward edges in large repos; reserve dense tags for implicit-dependency cases

## Related Papers
- [[codeteam-an-llm-powered-multi-agent-framework-for-repository-level-cod-2606.22082]] — Multi-agent repository-level code understanding
- [[v-zero-answer-label-free-on-policy-distillation-contrastive-evidence-2606.25319]] — On-policy distillation for LLM agents
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — Verifier telemetry for agentic knowledge-intensive tasks
