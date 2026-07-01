---
title: "TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [context-management, memory, long-horizon, inference-efficiency, llm]
sources: ["https://arxiv.org/abs/2606.06337"]
---

# TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management

## Overview
TokenMizer addresses the fundamental context-window constraint in long-horizon LLM deployments by modeling session history as a typed knowledge graph rather than flat text. The schema defines 14 node types and 7 edge types, with a hybrid extraction pipeline that populates the graph incrementally and a three-tier checkpoint system that serializes it into compact resume blocks.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.06337](https://arxiv.org/abs/2606.06337)

## Key Contributions
- Typed knowledge graph schema (14 node types, 7 edge types) modeling session structure
- Hybrid extraction pipeline populates graph incrementally from LLM session history
- Three-tier checkpoint system serializes graph into 78-token average resume blocks (2x smaller than 159-170 token baselines)
- 8-layer compression pipeline reduces context overhead; semantic cache reduces repeated-query latency
- Higher decision recall (+9-17pp) and file recall (58.7%) vs flat-text retention baselines

## Related Papers
- [[hmars-hierarchical-multi-agent-memory-long-context-2606.28349]] — Hierarchical multi-agent memory architecture (different axis: multi-agent vs single-session graph structure)
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Context management as load-bearing for agents
- [[memlearner-learning-to-query-context-memory-for-video-world-models-2606.31734]] — Learned query-based context memory for video world models
