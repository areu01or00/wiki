---
title: "AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [agent-memory, inference-efficiency, llm-agents]
sources: ["https://arxiv.org/abs/2606.21144"]
---

# AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents

## Overview
AdaMem addresses the "remember everything" problem in LLM agent memory systems — where agents uniformly extract and store all dialogue, leading to inference cost explosions and finite context overflow. The framework learns write-control policies: efficiently keeping only the information each future use-case actually needs, by predicting retrieval utility at write time.

## Key Facts
- **arXiv**: [2606.21144](https://arxiv.org/abs/2606.21144)

## Key Contributions
- Proposes learned write-control for LLM agent memory — predict retrieval utility before storing
- Addresses the tension between memory comprehensiveness and inference cost/context budgets
- Shows selective memory yields better task performance than comprehensive memory at lower compute cost

## Related Papers
- [[adamem-test-time-adaptive-memory-for-language-agents-2606.05684]] — AdaMem test-time adaptive memory (prior related work)
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Agent-native memory system benchmark
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — Evolvable representations for agentic memory
