---
title: "SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [architecture, llm, inference-efficiency, quantization]
sources: ["https://arxiv.org/abs/2606.26587"]
---

# SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference

## Overview
SharQ is a training-free inference method that combines semi-structured activation sparsity with FP4 quantization for LLM activation compression. It addresses the key challenge that activations contain input-dependent outliers that dominate block scales in FP4 quantization, and that directly applying N:M sparsity masks discards moderate values, coupling sparsification loss with quantization error.

## Key Facts
- **Authors**: Haoqian Meng, Yilun Luo, Yafei Zhao, Wenyuan Liu, Huaqing Zheng, Xindian Ma, Peng Zhang
- **Year**: 2026
- **arXiv**: [2606.26587](https://arxiv.org/abs/2606.26587)

## Key Contributions
- Training-free method combining activation sparsity with FP4 quantization
- Online sparse-dense decomposition to handle input-dependent outliers
- Decouples sparsification loss from quantization error
- Demonstrates that FP4 quantization and activation sparsity are complementary and can be jointly optimized

## Related Papers
- [[twinquant-learnable-subspace-decomposition-for-4bit-llm-quantization-2606.01556]] — TwinQuant: learnable subspace decomposition for 4-bit quantization (same quantization primitive family)
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — KV cache quantization via rope-aware bit allocation (same efficiency primitive family)
