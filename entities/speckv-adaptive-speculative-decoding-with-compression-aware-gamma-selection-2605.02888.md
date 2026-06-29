---
title: "SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [speculative-decoding, kv-cache-compression, inference-efficiency]
sources: ["https://arxiv.org/abs/2605.02888"]
---

# SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection

## Overview
First paper in the wiki to introduce **SpecKV** — an adaptive speculative-decoding framework that tunes the speculation length (gamma) on the fly using draft-model signals, achieving strong performance under *compressed* KV-cache settings where fixed-gamma speculative decoding plateaus.

## Key Facts
- **Authors**: Shukla, Shikhar (and collaborators)
- **Year**: 2026
- **arXiv**: [2605.02888](https://arxiv.org/abs/2605.02888)
- **Date (online)**: 2026-05-05 (v2)
- **Submission**: 2026-05-04 (v1) (cs)

## Key Contributions
- *Compression-aware adaptive gamma selection primitive* — gamma is adjusted per decoding step using draft-model confidence signals, preserving acceptance rate when KV-cache compression shrinks the model's effective receptive field, surfacing *gamma-adaptive-under-compression-primitive* as the load-bearing primitive when fixed-gamma decoding degrades alongside compression.
- Distinguishes itself from fixed-gamma primitives (vanilla speculative decoding): load-bearing axis is *adaptive-gamma-policy-with-draft-evidence-under-compression* rather than *fixed-gamma*. From SpecDec-style tree drafting: load-bearing axis is *compression-aware-budget-allocator* rather than *tree-expansion-policy*.
- Empirically beats fixed-gamma baselines across KV-cache compression settings, keeping acceptance high while freeing decoder bandwidth, with negligible accuracy degradation.
- Bridges KV-cache compression and speculative-decoding literature: surfaces *compressed-cache + adaptive-budget* as a coherent inference-efficiency primitive class, supporting deployment under both compression and budget pressure.

## Related Papers
- [[information-aware-kv-cache-compression-for-long-reasoning-2606.26875]] — sibling from this run (Run 88) on KV-cache-compression primitive
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — sibling on KV-cache inference-efficiency primitive (Run 85)
- [[vericache-turning-lossy-kv-cache-into-lossless-llm-inference-2605.17613]] — sibling on lossy/lossless KV-cache compression primitive (Run 59)
- [[jetspec-breaking-the-scaling-ceiling-of-speculative-decoding-with-parallel-tree-2606.18394]] — sibling on speculative-decoding scaling primitive (Run 59)
