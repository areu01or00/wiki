---
title: "Scaling LLM Inference Beyond Amdahl's Limits via Eliminating Non-Scalable Overheads"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [architecture, llm, inference-efficiency, distributed-systems]
sources: ["https://arxiv.org/abs/2606.01927"]
---

# Scaling LLM Inference Beyond Amdahl's Limits via Eliminating Non-Scalable Overheads

## Overview
This paper identifies why tensor parallelism (TP) scales sub-linearly as TP degree grows — due to cross-GPU communication and non-scalable runtime work predicted by Amdahl's Law — and proposes an empirical optimal TP degree (t_e) that balances memory efficiency against KV-cache contention and swapping overheads.

## Key Facts
- **Authors**: Alan Zhao, Cyril Y. He, Wei Xu
- **Year**: 2026
- **arXiv**: [2606.01927](https://arxiv.org/abs/2606.01927)

## Key Contributions
- Identifies empirical optimal TP degree t_e balancing memory efficiency and KV-cache overhead
- Characterizes non-scalable runtime work that limits TP scaling
- Provides guidance for cluster-wide LLM deployment given fixed GPU count
- Validates KV-cache contention as a key scaling bottleneck

## Related Papers
- [[twinquant-learnable-subspace-decomposition-for-4bit-llm-quantization-2606.01556]] — TwinQuant: quantization subspace decomposition (same efficiency primitive family)
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — KV cache quantization (same KV-cache optimization family)
