---
title: "Compute Optimal Tokenization"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [tokenization, efficiency, architecture, scaling-laws]
sources: ["https://arxiv.org/abs/2605.01188"]
---

# Compute Optimal Tokenization

## Overview
Extends classical scaling laws to jointly optimize tokenization granularity (compression rate) and model scale/data amount. The paper finds that optimal compression rate decreases with compute budget — smaller compute budgets favor higher compression (shorter sequences, more tokens) while larger budgets benefit from lower compression (longer tokens, fewer but richer tokens). Latent tokenization and multilingual generalization are also characterized.

## Key Facts
- **Authors**: Limisiewicz, Tomasz; Pagnoni, Artidoro; Iyer, Srini + 6
- **Year**: 2026
- **arXiv**: [2605.01188](https://arxiv.org/abs/2605.01188)

## Key Contributions
- First joint optimization of tokenizer compression rate and model scaling laws
- Counter-intuitive finding: optimal compression decreases with compute (not constant across scales)
- Latent tokenization enables adjustable compression for specific languages/domains
- Character vs byte level analysis: similar performance at large scale but different compute trajectories
- Guides tokenizer selection for compute-constrained deployment scenarios

## Related Papers
- [[mingram-a-minimalist-unigram-tokenizer-with-high-compression-and-competitive-morphological-fidelity-2606.27019]] — Proposes a high-compression unigram tokenizer whose compression ratio this paper's theory can predict
- [[the-african-language-tax-quantifying-the-cost-latency-and-context-penalty-of-tokenizing-2606.24460]] — Empirical measurement of tokenization inefficiency for African languages; this paper's optimal compression analysis explains why BPE disadvantages morphologically rich languages
- [[adaptive-targeted-dynamic-chunking-for-tokenization-free-hierarchical-model-2605.30080]] — Alternative approach to variable-granularity tokenization; this paper's findings provide the theoretical foundation for when chunking vs tokenization is compute-optimal
