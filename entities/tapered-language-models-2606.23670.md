---
title: "Tapered Language Models"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [architecture, transformer, efficient-training, scaling, depth-allocation, llm-research, foundation-models]
sources: ["https://arxiv.org/abs/2606.23670"]
---

# Tapered Language Models

## Overview
This paper introduces Tapered Language Models (TLMs), an architectural principle that allocates more parameter capacity to earlier layers and less to later layers under a fixed total budget, inverting the uniform-width default inherited from the original Transformer. Across three model scales and four architectures (Transformer, Gated Attention, Hope-attention, and Titans), tapering MLP width via a smooth cosine schedule consistently improves perplexity and downstream benchmark performance over uniform baselines — at no additional parameter or compute cost — establishing depth-aware capacity allocation as a free, architecture-agnostic design lever.

## Key Facts
- **Authors**: Bayat, Reza; Behrouz, Ali; Courville, Aaron
- **Year**: 2026
- **Date**: 2026-06-22
- **arXiv**: [2606.23670](https://arxiv.org/abs/2606.23670)
- **Subjects**: Machine Learning (cs.LG)

## Key Contributions
- Identifies a non-uniformity in layer contributions: later layers refine the residual stream rather than transform it, motivating asymmetric capacity allocation
- Controlled experiment under fixed parameter budget: tapering capacity toward earlier layers improves perplexity over uniform-width baselines; the reverse allocation hurts
- Introduces Tapered Language Models (TLMs) — a general architectural principle where a parameter-bearing component is monotonically tapered across depth, with MLPs as the natural instantiation site (they dominate parameter count and expose width as a clean axis)
- Validates the principle across 3 model scales and 4 architectures (Transformer, Gated Attention, Hope-attention, Titans), using a smooth cosine taper schedule
- Achieves consistent improvements in both perplexity and downstream benchmark performance vs uniform baselines — at no additional parameter or compute cost (a "free lever hidden in plain sight")

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — Same-window architectural-efficiency work (KV-cache compression)
- [[qwen-agentworld-language-world-models-for-general-agents-2606.24597]] — Same-window foundation-model work