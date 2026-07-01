---
title: "Selective Memory Retention for Long-Horizon LLM Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm-agents, memory-systems, long-horizon-planning, agentic-llm]
sources: ["https://arxiv.org/abs/2606.29178"]
---

# Selective Memory Retention for Long-Horizon LLM Agents

## Overview
Studies when external memory retention actually helps vs. hurts long-horizon LLM agents. Introduces TraceRetain, a lightweight bounded-memory framework scoring entries by interpretable features (success, age, access frequency, redundancy, specificity, similarity, downstream utility) and evicting the lowest-scoring ones at capacity. Finds bounded retention improves memory/step efficiency on saturated clean benchmarks at no task-success cost.

## Key Facts
- **Authors**: Pranath Reddy
- **Year**: 2026
- **arXiv**: [2606.29178](https://arxiv.org/abs/2606.29178)

## Key Contributions
- **TraceRetain**: Bounded external memory scoring framework with interpretable eviction features
- **When retention matters**: Bounded retention buys memory efficiency on clean benchmarks; differentiates from cache heuristics only when task requires selective recall
- **Interpretable eviction signals**: Success rate, age, access frequency, redundancy, specificity, similarity, downstream utility
- **First bounded-memory eviction scoring framework with explicit downstream utility signal in the wiki**

## Related Papers
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Agent-native memory systems context (related memory eviction theme)
- [[adamem-learning-what-to-remember-for-personalized-long-horizon-llm-agents-2606.21144]] — AdaMem adaptive memory for long-horizon agents (memory management theme)
