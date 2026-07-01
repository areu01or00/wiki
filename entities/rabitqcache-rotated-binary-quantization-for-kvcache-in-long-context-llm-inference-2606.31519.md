---
title: "RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, kv-cache, quantization]
sources: ["https://arxiv.org/abs/2606.31519"]
---

# RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference

## Overview
Long-context LLM inference is severely bottlenecked by the massive Key-Value cache. RaBitQCache proposes a novel sparse attention framework using randomized rotated binary quantization to address the limitations of existing methods — static fixed-budget Top-k retrieval and computationally expensive biased proxy scores. The approach enables efficient KVCache compression while maintaining inference quality.

## Key Facts
- **Authors**: Li, Wenhao; Dong, Jinhao; Zhang, Hailin + 3
- **Year**: 2026
- **arXiv**: [2606.31519](https://arxiv.org/abs/2606.31519)

## Key Contributions
- Randomized rotate-and-quantize technique for KVCache compression
- Addresses long-context inference memory bottleneck that dominates for extended contexts
- Outperforms static Top-k sparse attention without computational overhead of proxy scoring
- First rotated binary quantization approach specifically for KVCache in long-context scenarios

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept discovery chain that led to this paper's identification
