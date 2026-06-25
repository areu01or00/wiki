---
title: "GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agent, memory, benchmark, access-control, governance]
sources: ["https://arxiv.org/abs/2606.18829"]
---

# GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents

## Overview
Memory benchmarks for LLM agents have largely assumed single-user settings, leaving shared assistants in hospitals, workplaces, campuses, and households understudied. GateMem introduces a benchmark for multi-principal shared-memory agents that jointly evaluates utility for legitimate long-horizon requests with state updates, access control across contextual authorization boundaries, and agent-facing actions — a regime where multiple principals write to a common memory pool and query it under different roles, scopes, and relationships, making memory quality require governance as well as recall.

## Key Facts
- **Authors**: Ren, Zhe; Yang, Yibo; Chen, Yimeng; +7 more
- **Year**: 2026
- **arXiv**: [2606.18829](https://arxiv.org/abs/2606.18829)

## Key Contributions
- Introduces **GateMem**, the first benchmark targeting multi-principal shared-memory LLM agent deployments.
- Formalizes three-axis evaluation: long-horizon utility with state updates, access control across contextual authorization boundaries, and agent-facing actions under governance constraints.
- Targets the deployment regime missing from existing memory benchmarks (single-user assumptions), specifically shared assistants across hospitals/workplaces/campuses/households.

## Related Papers
- [[emergent-concepts]] — Parent topic: LLM agent evaluation / RAG / memory governance
