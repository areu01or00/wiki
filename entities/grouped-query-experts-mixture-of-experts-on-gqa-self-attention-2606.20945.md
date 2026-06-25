---
title: "Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [architecture, moe, attention, efficient-inference, transformer]
sources: ["https://arxiv.org/abs/2606.20945"]
---

# Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention

## Overview
Grouped Query Experts (GQE) is a sparse-activation layer that bolts a mixture-of-experts (MoE) module on top of grouped-query attention (GQA): within each GQA group a router selects k query-head experts per token while the key/value heads remain dense and unchanged. The authors show that at the 250M scale on a fixed 30B-token budget, GQE matches the all-active GQA baseline in downstream accuracy while activating only half the query heads per token, preserving the KV-cache benefits of GQA while reducing active query-head compute.

## Key Facts
- **Authors**: Tripathi, Vishesh; Kumar, Abhay
- **Year**: 2026
- **Date**: 2026-06-18
- **arXiv**: [2606.20945](https://arxiv.org/abs/2606.20945)
- **Subjects**: Machine Learning (cs.LG)

## Key Contributions
- GQE design that composes MoE routing on the query-head axis while leaving the KV cache dense — a rare compositional pattern that preserves inference-time memory efficiency while introducing input-dependent activation
- Empirical match to all-active GQA at the 250M / 30B-token scale with ~50% active query heads, suggesting that per-token query-head routing is a viable sparse-activation axis for attention (complementary to the standard FFN MoE axis)
- A design pattern for "MoE inside attention" that is orthogonal to and composable with existing FFN-level MoE (DeepSeek-MoE, Mixtral), opening up a 2D sparse-activation design space for transformers
- Long-context relevance: the savings compound as sequence length grows because per-token query routing is constant-cost whereas pairwise attention scales quadratically

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — Companion attention-mechanism analysis questioning learnability claims; together with GQE the two papers exemplify the attention research frontier's two-way stretch between representational analyses and architectural proposals
