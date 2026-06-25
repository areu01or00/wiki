---
title: "The Hitchhiker's Guide to Agentic AI: From Foundations to Systems"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agentic-ai, survey, systems, practitioner-reference, llm-architecture]
sources: ["https://arxiv.org/abs/2606.24937"]
---

# The Hitchhiker's Guide to Agentic AI: From Foundations to Systems

## Overview
A comprehensive practitioner's reference for building autonomous AI systems, organized around a central thesis that building great agentic systems requires understanding every layer of the pipeline — not just one. The book opens with the LLM substrate (transformer architecture, GPU scheduling, inference optimization) and walks upward through tool integration, planning, memory, multi-agent coordination, evaluation, safety, and production deployment, treating each layer as a first-class engineering concern rather than an implementation detail.

## Key Facts
- **Authors**: Roitman, Haggai
- **Year**: 2026
- **arXiv**: [2606.24937](https://arxiv.org/abs/2606.24937)
- **Subjects**: cs.AI; cs.CL; cs.LG

## Key Contributions
- End-to-end vertical treatment of agentic systems spanning model substrate through production deployment, in contrast to most prior literature that focuses on one layer (planning, memory, or evaluation) in isolation.
- Layer-by-layer engineering playbook — covering inference optimization, tool integration, planning architectures, memory subsystems, multi-agent orchestration, evaluation harnesses, safety guardrails, and deployment topology — with explicit cross-layer interaction notes.
- Practitioner-oriented reference framing: positions agentic AI as a systems engineering discipline rather than a research frontier, an angle that complements the academic surveys on individual components like the CLI-Universe task-synthesis work and the Are-We-Ready-for-Agent-Native-Memory systems-substrate paper.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this entity was first indexed via emergent-concept search on 2026-06-25 (agentic-systems practitioner reference theme).
- [[cli-universe-towards-verifiable-task-synthesis-engine-for-terminal-agents-2606.22883]] — Complementary training-data-side view of terminal agents; while this entry frames the systems layer, CLI-Universe addresses the executable-task synthesis pipeline.
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Substrate-level (memory systems) treatment that aligns with this paper's emphasis on memory as a first-class engineering concern.