---
title: "Multi-Bitwidth Quantization for LLMs Using Additive Codebooks"
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [inference-efficiency, quantization, model-compression, llm]
sources: ["https://arxiv.org/abs/2606.12876"]
---

# Multi-Bitwidth Quantization for LLMs Using Additive Codebooks

## Overview
This paper introduces Drop-by-Drop, a novel multi-bitwidth post-training quantization framework that enables inference-time precision control over LLM weights without retraining. The key insight is using additive codebooks that allow mixed-precision representation where different layers or tokens can use different bit-widths dynamically, adapting to heterogeneous hardware constraints and varying inference budgets.

## Key Facts
- **Authors**: Liza Babaoglu, Shuangyi Chen, Ashish Khisti
- **Year**: 2026
- **arXiv**: [2606.12876](https://arxiv.org/abs/2606.12876)

## Key Contributions
- Drop-by-Drop framework: additive codebook-based multi-bitwidth quantization enabling runtime precision switching
- Achieves lossless or near-lossless quantization at mixed bit-widths (e.g., 4-bit, 6-bit, 8-bit) on the same weight matrices
- Enables hardware-adaptive inference where deployment can trade off accuracy vs. memory/compute based on device constraints
- Demonstrates on LLaMA and Mistral models with <0.5 perplexity degradation at 4-bit mixed precision

## Related Papers
- [[twinquant-learnable-subspace-decomposition-for-4bit-llm-quantization-2606.01556]] — Learnable subspace decomposition for 4-bit quantization
- [[sharq-bridging-activation-sparsity-and-fp4-quantization-for-llm-inference-2606.26587]] — FP4 quantization bridging activation sparsity
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — Bit allocation specifically for KV cache quantization
