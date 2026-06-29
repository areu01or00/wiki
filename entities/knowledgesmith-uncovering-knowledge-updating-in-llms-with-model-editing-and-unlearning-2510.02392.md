---
title: "KnowledgeSmith: Uncovering Knowledge Updating in LLMs with Model Editing and Unlearning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [knowledge-editing, machine-unlearning, llm, evaluation-framework]
sources: ["https://arxiv.org/abs/2510.02392"]
---

# KnowledgeSmith: Uncovering Knowledge Updating in LLMs with Model Editing and Unlearning

## Overview
KnowledgeSmith is a unified framework that systematically studies the knowledge updating mechanisms of large language models. By casting knowledge editing and machine unlearning as instances of one constrained optimization problem, the paper provides the first rigorous comparative evaluation of how LLMs update, forget, and retain knowledge across multiple data scales and graph-theoretic intervention levels.

## Key Facts
- **Authors**: Yinyi Luo, Zhidian Zhou, Hao Chen, Kai Qiu, Marios Savvides, Sharon Li, Jindong Wang
- **Year**: 2025 (ICLR 2026)
- **arXiv**: [2510.02392](https://arxiv.org/abs/2510.02392)

## Key Contributions
- Unified constrained optimization framing that subsumes both editing and unlearning as special cases
- Automatic dataset generator providing structured interventions across graph levels and data scales
- Discovery of a **consistency-capacity trade-off**: unlearning preserves task integrity better while editing is more effective in low-data regimes
- Finding that LLMs do not exhibit human-like knowledge updating across different knowledge levels

## Related Papers
- [[emergent-concepts]] — Parent emergent-concepts wiki page that this discovery extends
