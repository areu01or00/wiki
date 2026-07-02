---
title: "DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [on-device, memory-agents, model-compression, distillation]
sources: ["https://arxiv.org/abs/2606.29961"]
---

# DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation

## Overview
LLM-based agents solving complex multi-turn tasks require large models, long contexts, and repeated inference — making deployment on resource-constrained devices impractical. DuoMem proposes dual-space distillation (working memory + episodic memory) to compress these capabilities into lightweight on-device agents without sacrificing task performance.

## Key Facts
- **Authors**: Hosseini, Peyman; Bohdal, Ondrej; Alajrami, Ahmed + 6
- **Year**: 2026
- **arXiv**: [2606.29961](https://arxiv.org/abs/2606.29961)

## Key Contributions
- Dual-space memory architecture: working memory (contextual) + episodic memory (stored experience)
- Knowledge distillation from large agents into compact on-device models
- Demonstrates capable on-device agents matching cloud-based performance
- Opens direction for memory-augmented mobile/smart-device LLM deployment

## Related Papers
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Agent-native memory system taxonomy and design considerations
- [[adamem-test-time-adaptive-memory-for-language-agents-2606.05684]] — Adaptive memory for language agents at test time
- [[elasticmem-latent-memory-as-a-learnable-resource-for-llm-agents-2605.30690]] — Learnable latent memory as a resource for LLM agents
