---
title: "TwinQuant: Learnable Subspace Decomposition for 4-Bit LLM Quantization"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [quantization, inference-efficiency, model-compression, subspace-learning]
sources: ["https://arxiv.org/abs/2606.01556"]
---

# TwinQuant: Learnable Subspace Decomposition for 4-Bit LLM Quantization

## Overview
TwinQuant proposes learnable subspace decomposition for 4-bit quantization of large language models, learning a low-rank subspace that captures the most information-dense directions in weight space. Unlike standard post-training quantization that treats weights independently, TwinQuant jointly optimizes the subspace projection and quantization codebook to minimize accuracy degradation while maintaining 4-bit precision.

## Key Facts
- **Authors**: [arXiv 2606.01556](https://arxiv.org/abs/2606.01556)
- **Year**: 2026
- **arXiv**: [2606.01556](https://arxiv.org/abs/2606.01556)
- **Online Date**: 2026/06/01

## Key Contributions
- Learnable subspace decomposition for joint optimization of projection + quantization
- 4-bit quantization with reduced accuracy degradation vs. independent weight quantization
- Learns a shared codebook across weight subspaces for better reconstruction quality
- Demonstrates that joint subspace+codebook optimization captures complementary structure missed by sequential approaches

## Related Papers
- [[emergent-concepts]] — Parent emergent concept discovery chain
