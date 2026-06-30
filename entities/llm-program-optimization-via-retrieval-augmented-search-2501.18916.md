---
title: "LLM Program Optimization via Retrieval Augmented Search"
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [llm, program-optimization, retrieval-augmented, ras, in-context-learning]
sources: ["https://arxiv.org/abs/2501.18916"]
---

# LLM Program Optimization via Retrieval Augmented Search

## Overview
This paper proposes Retrieval Augmented Search (RAS), a blackbox method for LLM-based program optimization that retrieves in-context examples from slow-fast program pairs to guide the LLM toward more efficient implementations. The key insight is that natural language descriptions of optimization opportunities outperform raw source code as retrieval keys.

## Key Facts
- **Authors**: Unknown (from arxiv 2501.18916)
- **Year**: 2025
- **arXiv**: [2501.18916](https://arxiv.org/abs/2501.18916)

## Key Contributions
- Proposes RAS: beam search over candidate optimizations guided by retrieved slow-fast program pairs
- Demonstrates that LLM-generated NL descriptions of optimization opportunities significantly outperform source code as retrieval keys
- Introduces AEGIS for interpretability by decomposing training examples into atomic edits
- Shows RAS achieves superior program optimization compared to non-retrieval baselines

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept discovery chain
