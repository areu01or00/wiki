---
title: "MiniMax Sparse Attention"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [attention-mechanism, long-context, inference-efficiency, sparse-attention, model-architecture]
sources: ["https://arxiv.org/abs/2606.13392"]
---

# MiniMax Sparse Attention

## Overview
Ultra-long-context capability is increasingly indispensable for frontier LLMs (agentic workflows, repository-scale code reasoning, persistent memory), yet the quadratic cost of softmax attention makes joint attention over hundreds of thousands to millions of tokens untenable at deployment scale. MiniMax Sparse Attention (MSA) introduces a blockwise sparse attention built upon Grouped Query Attention (GQA): a lightweight Index Branch scores key-value blocks and selects a Top-k subset per GQA group, enabling group-specific sparse retrieval while the Main Branch performs exact block-sparse attention over only the selected blocks. MSA achieves 28.4× per-token attention compute reduction at 1M context with on-par accuracy, and 14.2×/7.6× wall-clock speedup on H800 for prefill/decoding.

## Key Facts
- **Authors**: Xunhao Lai, Weiqi Xu, Yufeng Yang, Qiaorui Chen, Yang Xu, Lunbin Zeng, et al.
- **Year**: 2026
- **arXiv**: [2606.13392](https://arxiv.org/abs/2606.13392)

## Key Contributions
- **MSA architecture**: Grouped Query Attention + lightweight Index Branch for Top-k KV block selection + Main Branch for exact block-sparse attention over selected blocks only
- **GPU co-design**: exp-free Top-k selection and KV-outer sparse attention to improve tensor-core utilization under block-granular access
- **Production model**: powers a publicly-released natively multimodal 109B-parameter model with MSA
- **Speedup**: 28.4× compute reduction, 14.2× prefill and 7.6× decoding wall-clock speedup on H800

## Related Papers
- [[vericache-turning-lossy-kv-cache-into-lossless-llm-inference-2605.17613]] — KV-cache optimization (orthogonal: VeriCache targets lossy KV-cache recovery; MSA targets sparse attention architecture for long context)
- [[information-aware-kv-cache-compression-for-long-reasoning-2606.26875]] — KV-cache compression for long reasoning (orthogonal: KV-cache compression is a memory-hierarchy approach; MSA is an attention-architecture approach)
- [[endprompt-efficient-long-context-extension-via-terminal-anchoring-2605.14589]] — Long context extension techniques (orthogonal: EndPrompt targets context extension; MSA targets efficient sparse attention at long context)
