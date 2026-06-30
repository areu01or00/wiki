---
title: "NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [inference-efficiency, long-context, attention-optimization, training-free]
sources: ["https://arxiv.org/abs/2606.27791"]
---

# NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation

## Overview
NLL-guided layer selection is a training-free method for hybrid attention models that mix full and sliding-window attention across layers. The method measures each layer's importance by computing the negative log-likelihood degradation on answer tokens when that layer switches from full to sliding-window attention, then selects the optimal subset of layers to retain full attention.

## Key Facts
- **arXiv**: [2606.27791](https://arxiv.org/abs/2606.27791)
- **Year**: 2026

## Key Contributions
- Achieves 64.6% accuracy on LongMemEval (Qwen3-4B) using only 1/4 full-attention layers — matching the 1/2-FA periodic baseline while halving computational budget
- Outperforms SWAA-reported periodic 1/4-FA baseline by 10.4 percentage points and LightTransfer-style baseline by 26.4 percentage points
- Requires only ~15 minutes of one-time calibration with no fine-tuning
- De-confounding analysis confirms signal is driven by long-range attention needs rather than generic layer sensitivity

## Related Papers
- [[lanerope-positional-encoding-collaborative-parallel-reasoning-generation-2605.27570]] — LaneRoPE: First positional encoding enabling KV-cache reuse across parallel best-of-N reasoning branches; complementary attention efficiency approach
- [[coverage-driven-kv-cache-eviction-kvec-2606.29563]] — KVEC: Coverage-driven KV-cache eviction policy; addresses complementary problem of which tokens to retain
- [[carve-content-aware-recurrent-with-value-efficiency-for-chunk-parallel-linear-attention-2606.27229]] — CARVE: Content-aware recurrent linear attention; another training-free sliding-window approach
