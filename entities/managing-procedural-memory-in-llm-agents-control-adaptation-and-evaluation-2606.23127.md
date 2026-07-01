---
title: "Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm-agents, memory-systems, benchmarking, enterprise]
sources: ["https://arxiv.org/abs/2606.23127"]
---

# Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation

## Overview
Procedural memory enables LLM agents to reuse learned skills across recurring workplace tasks. This paper introduces AFTER, a benchmark of 382 realistic enterprise tasks across 6 professional roles and 22 procedural skills, and systematically evaluates how well current agents acquire, stabilize, and deploy reusable procedural memories. The study reveals significant gaps in agents' ability to transfer learned procedures to novel but related task variants.

## Key Facts
- **Authors**: Belikova, Julia; Parchiev, Rauf; Egorov, Evgeny + 4
- **Year**: 2026
- **arXiv**: [2606.23127](https://arxiv.org/abs/2606.23127)

## Key Contributions
- **AFTER benchmark**: 382 enterprise tasks across 6 roles and 22 procedural skills — first comprehensive benchmark for procedural memory in LLM agents
- **Controlled evaluation**: Tests memory acquisition, stabilization, and adaptive transfer under systematic variation of task surface features
- **Findings**: Current agents perform well on exact task repeats but degrade sharply when procedural memory must be applied to novel variants — revealing a fundamental generalization gap in skill reuse
- **Diagnostic framework**: Decomposes procedural memory into acquisition fidelity, storage stability, and retrieval adaptability — surfaces which component limits agent performance

## Related Papers
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Agent-native memory systems framing (prior wiki entry on agent memory infrastructure)
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — Evolvable embeddings for long-context agentic memory (prior wiki entry)
