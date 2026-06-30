---
title: "Cache-Resident LLM Inference in GB-Scale Last-Level Caches"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, hardware, memory-hierarchy, llm]
sources: ["https://arxiv.org/abs/2606.25353"]
---

# Cache-Resident LLM Inference in GB-Scale Last-Level Caches

## Overview
The paper exploits 3D-stacked GB-scale last-level CPU caches for efficient LLM inference by keeping model weights cache-resident. It presents a cache-resident execution model that decouples weight-centric operators from attention/KV-cache management into separate resource domains, enabling weight residency while scaling KV capacity independently. Achieves 2.04x-11.51x TPOT speedup on Llama-3.2-3B and Llama-2-7B using commodity CPU hardware.

## Key Facts
- **arXiv**: [2606.25353](https://arxiv.org/abs/2606.25353)
- **Year**: 2026
- **Theme**: inference efficiency / hardware / memory hierarchy

## Key Contributions
- **Cache-resident execution model**: Separates weight-centric operators from attention/KV-cache management into dedicated resource domains
- **Weight-attention decoupled architecture**: Keeps reusable weights in cache while scaling KV capacity independently of pipeline depth
- **Relaxed synchronization**: From operator boundaries to true sub-operator dependencies, reducing coordination overhead
- **Hardware**: Multi-socket CPU cluster with 3D-stacked GB-scale last-level caches — no GPU required
- **Results**: 2.04x-11.51x TPOT on Llama-3.2-3B and Llama-2-7B; up to 13.9x TPOT in analytical model across model sizes, context lengths, batch sizes

## Related Papers
- [[sharq-bridging-activation-sparsity-and-fp4-quantization-for-llm-inference-2606.26587]] — Activation sparsity + quantization for inference efficiency
- [[context-recycling-for-long-horizon-llm-inference-2606.26105]] — Context recycling for long-horizon inference
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — KV-cache quantization
- [[vericache-turning-lossy-kv-cache-into-lossless-llm-inference-2605.17613]] — Lossy KV-cache recovery
