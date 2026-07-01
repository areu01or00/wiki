---
title: "RaMem: Contextual Reinstatement for Long-term Agentic Memory"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent, memory, long-term-memory, retrieval, context]
sources: ["https://arxiv.org/abs/2606.22844"]
---

# RaMem: Contextual Reinstatement for Long-term Agentic Memory

## Overview
Long-term memory has become increasingly important for LLM agents operating across extended interactions. While recent memory systems have made past experiences more persistent and retrievable, retrieval alone does not ensure that a memory provides valid evidence for the current query. When experiences are compressed into reusable fragments, memories from different situations may appear equally relevant if they involve recurring entities or user states — a failure the authors call context collapse. RaMem (Contextual Reinstatement for Agentic Memory) addresses this through four coordinated stages: evidence anchoring, recall condition induction, validity-aware retrieval, and context-preserved synthesis. Experiments on long-term memory benchmarks show consistent F1 gains of more than 10% across several backbones.

## Key Facts
- **Authors**: Yang, Wei; Kan, Bryce; Li, Shixuan + 5
- **Year**: 2026
- **arXiv**: [2606.22844](https://arxiv.org/abs/2606.22844)

## Key Contributions
- Identifies and formalizes context collapse as a key failure mode for memory retrieval in LLM agents
- Proposes RaMem: four-stage framework (evidence anchoring → recall condition induction → validity-aware retrieval → context-preserved synthesis)
- Achieves 10%+ F1 gains on long-term memory benchmarks across multiple backbone models
- Provides a mechanism for turning retrieved memory fragments into contextually verifiable evidence

## Related Papers
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Agent-native memory system taxonomy
- [[evoembedding-evolvable-representations-for-long-context-retrieval-2606.21649]] — Evolvable representations for long-context agentic memory
