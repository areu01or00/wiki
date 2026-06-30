---
title: "MATCH: Modulating Attention via In-Context Retrieval for Long-Context Transformers"
created: 2026-06-01
updated: 2026-07-02
type: entity
tags: [fine-tuning, uncertainty-quantification, llm, bayesian, variational, peft]
sources: ["https://arxiv.org/abs/2606.29844"]
---

# MATCH: Modulating Attention via In-Context Retrieval for Long-Context Transformers

## Overview
The quadratic cost of traditional attention mechanisms bottlenecks LLM scalability in long-context scenarios. Existing approaches enforce rigid structural constraints (local windows) at the cost of performance. MATCH introduces in-context retrieval modulation — dynamically adjusting attention based on retrieved context — achieving both efficiency and fidelity for long-document understanding.

## Key Facts
- **arXiv**: [2606.29844](https://arxiv.org/abs/2606.29844)
- **Date**: 2026-06-01

## Key Contributions
- Scalable variational Bayesian PEFT via orthogonalized low-rank adapters
- Principled uncertainty estimation for fine-tuned LLMs
- Self-assessment capability for safety-critical LLM deployments
