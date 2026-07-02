---
title: "Beyond Compaction: Structured Context Eviction for Long-Horizon Agents"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [agent, context-management, long-horizon-planning, memory]
sources: ["https://arxiv.org/abs/2606.11213"]
---

# Beyond Compaction: Structured Context Eviction for Long-Horizon Agents

## Overview
Presents Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon. Built around three primitives: typed episodes, an explicit dependency graph authored by the agent, and a graduated eviction policy that is deterministic and LLM-free. Sessions accumulate history and CWL selectively evicts tokens while preserving structural dependencies.

## Key Facts
- **Authors**: Semenov, Andrew; Dorofeev, Svyatoslav
- **Year**: 2026
- **arXiv**: [2606.11213](https://arxiv.org/abs/2606.11213)

## Key Contributions
- Typed episodes: structured memory units that carry semantic type information for selective eviction
- Explicit dependency graph: agent-authored graph of inter-episode relationships enabling principled eviction decisions
- Graduated eviction policy: deterministic and LLM-free — avoids the cost and latency of calling the LLM to decide what to forget
- Effectively unbounded working horizon for long-horizon agentic tasks

## Related Papers
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist: context management is load-bearing for LLM agents
- [[memprobe-probing-longterm-agent-memory-via-hidden-userstate-recovery-2606.24595]] — MEMPROBE: probing long-term agent memory via hidden user-state recovery
- [[agents-last-exam-2606.05405]] — Agents' Last Exam: agent benchmarking methodology
