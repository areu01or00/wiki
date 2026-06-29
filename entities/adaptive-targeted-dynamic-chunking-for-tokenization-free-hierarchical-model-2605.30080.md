---
title: "Adaptive Targeted Dynamic Chunking for Tokenization-Free Hierarchical Model"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [tokenization-free, byte-level, hierarchical, dynamic-chunking, curriculum-learning, llm-architecture]
sources: ["https://arxiv.org/abs/2605.30080"]
---

# Adaptive Targeted Dynamic Chunking for Tokenization-Free Hierarchical Model

## Overview
First paper in the wiki to introduce **curriculum-learning-based adaptive compression-ratio control** for tokenization-free hierarchical LLM architectures. Adaptive Targeted Dynamic Chunking (ATDC) uses a curriculum to progressively adjust the byte-compression ratio during training — transitioning from low to high compression to stabilize the learning process. On FineWeb-Edu 100B, ATDC achieves competitive Bits-Per-Byte (BPB) performance vs. conventional byte-level and token-level baselines, with more stable training dynamics and superior final downstream-task performance compared to fixed-compression models.

## Key Facts
- **Authors**: ATDC authors (2026)
- **Year**: 2026
- **arXiv**: [2605.30080](https://arxiv.org/abs/2605.30080)
- **Online Date**: 2026-05-28
- **Domain**: tokenization-free-architecture × byte-level-modeling × hierarchical-architecture × dynamic-chunking × curriculum-learning

## Key Contributions
- **Curriculum-driven byte-compression control**: ATDC progressively adjusts the target compression ratio from low to high during training — establishing **training-schedule-aware compression** as a primitive for tokenization-free hierarchical models
- **Target-compression → BPIC relationship**: provides an analytical relationship between the target compression ratio and Bytes-Per-Innermost-Chunk (BPIC), enabling **chunk-size evolution tracking** throughout training
- **Tokenization-free alternative to BPE/Unigram**: byte-level hierarchical architecture that eliminates vocabulary design, OOV errors, and language-specific constraints — establishing **tokenization-architecture-orthogonality** as a design axis
- **Stability-vs-flexibility primitive**: exhibits more stable training dynamics AND superior final performance across diverse downstream tasks compared to fixed-compression models — splits the **fixed-vs-adaptive-compression** trade-off that has constrained prior tokenization-free work
- **Compression-ratio as a controllable hyperparameter**: BPB performance competitive with conventional byte-level and token-level baselines at the **same effective compression budget** — establishing the **compression-budget-equivalence** primitive
- **Cross-discipline primitive**: bridges tokenization-engineering × hierarchical-architecture × curriculum-learning × chunked-compression — surfaces **dynamic-chunking** as a structural alternative to fixed-vocabulary tokenization

## Related Papers
- [[mingram-a-minimalist-unigram-tokenizer-with-high-compression-and-competitive-morphological-fidelity-2606.27019]] — Tokenizer-compression primitive that improves BPE/Unigram trade-offs; sibling from Run 95 that addresses the **fixed-vocabulary side** of the tokenization debate — together they bracket the **with-vocabulary vs without-vocabulary** axis
- [[the-african-language-tax-quantifying-the-cost-latency-and-context-penalty-of-tokenizing-2606.24460]] — Tokenization fairness across African languages; sibling from Run 95 that surfaces the deployment-cost consequences of fixed-vocabulary design — ATDC's tokenization-free approach provides a structural remedy
- [[dart-diffusion-inspired-speculative-decoding-for-fast-llm-inference-2601.19278]] — Diffusion-inspired parallel-drafting primitive; complements ATDC by addressing inference efficiency at the token-stream level rather than the byte-chunk level
- [[information-aware-kv-cache-compression-for-long-reasoning-2606.26875]] — Information-aware KV-cache compression; complements ATDC's byte-chunk compression as a **memory-side compression primitive** distinct from the **input-side byte-chunk compression** ATDC operates on
- [[continuum-memory-architectures-for-long-horizon-llm-agents-2601.09913]] — Continuum-memory architectural primitive; complements ATDC's hierarchical chunking by extending the **chunk-as-memory** idea to long-horizon agent state
- [[human-inspired-memory-architecture-for-llm-agents-2605.08538]] — Human-inspired memory architecture for LLM agents; complements ATDC's hierarchical byte-chunking by treating the **chunk** as a biological-memory analog