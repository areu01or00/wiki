---
title: "HMARS: A Hierarchical Multi-Agent Memory System for Long-Context Reasoning"
created: 2026-06-01
updated: 2026-06-01
type: entity
tags: [llm-agents, memory-systems, long-context, multi-agent]
sources: ["https://arxiv.org/abs/2606.28349"]
---

# HMARS: A Hierarchical Multi-Agent Memory System for Long-Context Reasoning

## Overview
Long-context reasoning requires models to access, retrieve, and integrate evidence scattered across documents, dialogues, and accumulated interaction histories. Standard retrieval-augmented generation reduces this to top-K chunk retrieval, but passive access discards relevant information. HMARS introduces a hierarchical multi-agent memory system where specialized agents manage memory at different temporal granularities, enabling proactive retrieval and synthesis across very long contexts.

## Key Contributions
- Proposes hierarchical multi-agent memory architecture with specialized agents at different temporal granularities
- Enables proactive retrieval vs passive RAG chunk retrieval for long-context tasks
- Validates on multi-document QA, dialogue summarization, and long-horizon agent tasks
- First hierarchical multi-agent memory system for long-context reasoning in the wiki

## Key Facts
- **arXiv**: [2606.28349](https://arxiv.org/abs/2606.28349)

## Related Papers
- [[emergent-concepts]] — Parent emergent-concepts chain that led to this discovery
