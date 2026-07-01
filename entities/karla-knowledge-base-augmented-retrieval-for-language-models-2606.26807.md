---
title: "KARLA: Knowledge-base Augmented Retrieval for Language Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [rag, knowledge-editing, factual-grounding, llm]
sources: ["https://arxiv.org/abs/2606.26807"]
---

# KARLA: Knowledge-base Augmented Retrieval for Language Models

## Overview
KARLA enables an LLM to automatically pull factual knowledge from a knowledge base during token generation, without retraining. The core innovation is training the model to produce special tokens that trigger a knowledge base query. This allows: (1) factual knowledge updates without LLM retraining, (2) facts traceable to the knowledge base for transparency, and (3) smaller models achieving the same factual accuracy as larger models. KARLA improves factual grounding in both short and long-form generation and allows factual revisions to take effect through KB edits rather than parameter updates.

## Key Facts
- **Authors**: Unknown (awaiting author metadata from arxiv)
- **Year**: 2026
- **arXiv**: [2606.26807](https://arxiv.org/abs/2606.26807)

## Key Contributions
- **Token-triggered KB retrieval**: LLM generates special tokens that trigger knowledge base queries during generation
- **No retraining required**: Factual updates take effect through KB edits, not parameter updates
- **Transparent fact tracing**: Facts in LLM output can be traced back to the knowledge base
- **Smaller models with larger accuracy**: Smaller models achieve comparable factual accuracy via KB augmentation
- **First**: First token-triggered KB retrieval method enabling parameter-free factual updates in LLMs

## Related Papers
- [[chartwalker-benchmarking-the-cross-chart-rag-task-with-hierarchical-knowledge-graphs-2606.23997]] — ChartWalker cross-chart RAG benchmark (shared RAG evaluation theme)
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — EvoEmbedding evolvable representations for retrieval and agentic memory (shared retrieval + memory theme)
