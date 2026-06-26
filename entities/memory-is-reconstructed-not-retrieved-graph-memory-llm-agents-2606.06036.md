---
title: "Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [agent-memory, memory-graph, reconstruction, retrieval-alternative, long-horizon, llm-agents]
sources: ["https://arxiv.org/abs/2606.06036"]
---

# Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents

## Overview
MRAgent replaces the standard retrieve-then-reason memory pipeline for LLM agents with an *active reconstruction* mechanism built on a Cue-Tag-Content graph, allowing memory access to be adapted dynamically to intermediate evidence discovered during inference. The architecture reframes long-interaction memory as graph-conditioned reconstruction rather than static retrieval, enabling reasoning to dynamically explore relational structure rather than depend on a single retrieved context.

## Key Facts
- **Authors**: Ji, Shuo; Li, Yibo; Hooi, Bryan
- **Year**: 2026
- **arXiv**: [2606.06036](https://arxiv.org/abs/2606.06036)
- **Date**: 2026/06/04

## Key Contributions
- Identifies the structural limitation of the static retrieve-then-reason pipeline: it cannot adapt memory access to intermediate evidence uncovered during inference.
- Proposes MRAgent, a framework that represents memory as a Cue-Tag-Content associative graph combined with an active reconstruction mechanism.
- Reframes long-interaction memory as graph-conditioned reconstruction during inference, enabling dynamic relational exploration beyond a single retrieved context.

## Related Papers
- [[agent-memory-characterization-and-system-implications-of-stateful-long-horizon-workloads-2606.06448]] — sibling systems-level memory characterization; MRAgent's graph-reconstruction sits at the *access-layer* while Agent Memory Characterization surveys the *system-layer* trade-offs across storage/extraction/consolidation/control
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — sibling framework-level memory-survey; MRAgent is one of the candidate architectures that Are-We-Ready evaluates for agent-native deployment
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — sibling long-context retrieval-evolution work; EvoEmbedding evolves retrieval representations over time, MRAgent reconstructs from a graph rather than retrieving from a fixed index — together they bracket the long-context-memory surface between *evolving retrieval representations* (EvoEmbedding) and *graph-conditioned reconstruction* (MRAgent)
- [[trustmem-trustworthy-memory-consolidation-llm-agents-long-term-memory-2606.25161]] — sibling memory-consolidation work for long-term agent memory; TrustMem focuses on consolidation reliability, MRAgent focuses on access pattern during inference
- [[memtoolagent-leveraging-memory-tool-using-agents-environment-user-feedback-2606.07909]] — sibling tool-use-memory-mechanism work; MemToolAgent uses memory-as-tool, MRAgent uses graph-as-reconstruction substrate — different surface of agent-memory design
- [[emergent-concepts]] — parent wiki page
