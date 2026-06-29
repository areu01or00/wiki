---
title: "SkillDAG: Self-Evolving Typed Skill Graphs for LLM Skill Selection at Scale"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent, skill-selection, llm, graph]
sources: ["https://arxiv.org/abs/2606.03056"]
---

# SkillDAG: Self-Evolving Typed Skill Graphs for LLM Skill Selection at Scale

## Overview
Addresses the challenge of LLM agents that adopt large skill libraries — instead of flat lists, models skill dependencies as a typed DAG (directed acyclic graph). The system self-evolves: new skills are added with typed edges, and the LLM reasons directly over the graph structure to select appropriate skills for a given task.

## Key Facts
- **Authors**: Tong Bai, Zhenglin Wan, Pengfei Zhou, Xingrui Yu, Wangbo Zhao et al.
- **Year**: 2026
- **arXiv**: [2606.03056](https://arxiv.org/abs/2606.03056)

## Key Contributions
- **SkillDAG**: typed directed acyclic graph representing skill inter-dependencies
- **Self-evolving**: new skills automatically added with typed edges, no manual curation
- **LLM reasons over graph**: model queries the DAG structure for skill selection, not flat retrieval
- **Scale**: designed for large skill libraries (thousands of skills) with efficient graph traversal

## Related Papers
- [[agent-orchestration]] — General agent orchestration frameworks
- [[from-agent-traces-to-trust-a-survey-of-evidence-tracing-and-execution-provenance-in-llm-agents-2606.04990]] — Agent evidence tracing and provenance (orthogonal axis: evidence-provenance vs skill-graph-reasoning)
