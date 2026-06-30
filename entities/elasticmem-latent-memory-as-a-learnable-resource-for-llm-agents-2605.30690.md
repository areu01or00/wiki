---
title: "ElasticMem: Latent Memory as a Learnable Resource for LLM Agents"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [memory, llm-agents, architecture]
sources: ["https://arxiv.org/abs/2605.30690"]
---

# ElasticMem: Latent Memory as a Learnable Resource for LLM Agents

## Overview
ElasticMem treats memory not as a fixed retrieval resource but as a learnable latent space that LLM agents can grow, compress, and query — solving the token-overhead and noise-sensitivity problems of fixed-capacity memory augmentation. The method learns memory representations end-to-end rather than storing raw text or relying on rigid nearest-neighbor retrieval.

## Key Facts
- **Authors**: Anonymous (arXiv submitter, 2026-05)
- **Year**: 2026
- **arXiv**: [2605.30690](https://arxiv.org/abs/2605.30690)

## Key Contributions
- Introduces learnable latent memory as a parametric resource (not text retrieval, not fixed-capacity store)
- Demonstrates that end-to-end training of memory representations outperforms concatenation-based and fixed-retrieval baselines on long-horizon agent tasks
- Reduces token overhead compared to text-concatenation memory while maintaining fidelity of past experience
- Shows personalization and coherent reasoning over extended interaction histories

## Related Papers
- [[scout-active-information-foraging-for-long-text-understanding-with-decoupled-epistemic-states-2605.04496]] — SCOUT: decoupled epistemic states for long-document information foraging (orthogonal axis: architecture for sparse retrieval vs learnable parametric memory)
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist: context management as load-bearing for LLM agents (orthogonal axis: eviction policy vs learnable memory growth)
