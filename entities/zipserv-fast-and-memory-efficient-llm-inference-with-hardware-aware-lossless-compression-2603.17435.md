---
title: "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [inference-efficiency, memory-optimization, kv-cache, compression, llm-serving]
sources: ["https://arxiv.org/abs/2603.17435"]
---

# ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression

## Overview
Addresses memory and bandwidth bottlenecks in bit-exact LLM serving through lossless compression co-designed with GPU architectures. Solves the fundamental mismatch where traditional entropy codecs produce variable-length bitstreams that break SIMT parallelism, causing inference slowdowns despite memory savings.

## Key Facts
- **Authors**: ZipServ team
- **Year**: 2026
- **arXiv**: [2603.17435](https://arxiv.org/abs/2603.17435)

## Key Contributions
- Lossless compression framework co-designed for GPU architectures
- Solves SIMT parallelism breakage from variable-length entropy bitstreams
- Reduces memory traffic without inference slowdown
- Hardware-aware codec design matching GPU memory hierarchy
- Bit-exact serving preserving model output precision

## Related Papers
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — Related KV-cache compression work
- [[zipserv-fast-and-memory-efficient-llm-inference-with-hardware-aware-lossless-compression-2603.17435]] — Self-reference
