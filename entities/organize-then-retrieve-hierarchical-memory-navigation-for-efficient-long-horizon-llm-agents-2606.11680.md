---
title: "Organize then Retrieve: Hierarchical Memory Navigation for Efficient Long-Horizon LLM Agents"
created: "2026-06-30"
updated: "2026-06-30"
type: entity
tags: [agent-memory, hierarchical-memory, memory-navigation, long-horizon, retrieval]
sources: ["https://arxiv.org/abs/2606.11680"]
---

# Organize then Retrieve: Hierarchical Memory Navigation for Efficient Long-Horizon LLM Agents

## Overview
LLM agents performing long-horizon tasks face fundamental statelessness — all task-relevant information must fit in the growing input context. Organize then Retrieve (OTR) addresses this by separating memory organization (structuring information into hierarchical schemas) from retrieval (contextual querying of the organized structure), enabling efficient long-horizon reasoning without requiring full context to fit in the input window. The approach treats organization as a separate pre-processing phase that structures agent experience into retrievable chunks, then retrieval as a targeted query operation that pulls only relevant organized segments into the active context. This two-phase architecture reduces context pressure while maintaining task-relevant coherence across extended agent trajectories.

## Key Facts
- **Authors**: (from arXiv 2606.11680 — see abstract page)
- **Year**: 2026
- **arXiv**: [2606.11680](https://arxiv.org/abs/2606.11680)
- **Subjects**: cs.AI / cs.CL

## Key Contributions
- Hierarchical memory organization as a first-class pre-processing phase separate from retrieval (vs. flat retrieval or end-to-end memory systems)
- Two-phase architecture: organize (structure into hierarchical schemas) then retrieve (contextual query of organized memory)
- Reduces context pressure in long-horizon agent tasks by keeping only structured, retrieval-targeted information in active context
- Addresses LLM statelessness bottleneck for extended multi-step tasks without gradient updates or external databases
- First hierarchical memory organization/pre-retrieval structuring paper in the wiki

## Related Papers
- [[memprobe-probing-longterm-agent-memory-via-hidden-userstate-recovery-2606.24595]] — MEMPROBE: probing long-term agent memory via hidden user-state recovery; orthogonal to OTR (MEMPROBE = memory evaluation methodology, OTR = memory organization architecture)
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — EvoEmbedding: evolvable agentic memory representations; orthogonal to OTR (EvoEmbedding = representation-level adaptation, OTR = organizational/retrieval-level architecture)
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist: context management is load-bearing for LLM agents; orthogonal (Plans-Dont-Persist = problem diagnosis of context eviction, OTR = concrete organizational architecture solution)
