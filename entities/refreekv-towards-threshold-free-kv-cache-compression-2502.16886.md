---
title: "ReFreeKV: Towards Threshold-Free KV Cache Compression"
created: 2025-02-01
updated: 2025-02-01
type: entity
tags: [llm, post-training]
sources: ["https://arxiv.org/abs/2502.16886"]
---

# ReFreeKV: Towards Threshold-Free KV Cache Compression

## Overview
KV cache compression methods require input-specific thresholds to achieve optimal performance, but threshold selection is impractical in open-domain deployment where inputs span diverse domains and difficulty levels. ReFreeKV eliminates this requirement via a threshold-free, content-adaptive KV cache eviction strategy that dynamically determines which key-value pairs to retain based on their accumulated attention contribution, without any task-specific or input-specific hyperparameter tuning.

## Key Facts
- **arXiv**: [2502.16886](https://arxiv.org/abs/2502.16886)
- **Date**: 2025-02-01

## Key Contributions
- Threshold-free KV cache compression — no input/domain-specific hyperparameter needed
- Content-adaptive eviction based on accumulated attention contribution rather than fixed budgets
- Lossless compression on diverse open-domain benchmarks; outperforms threshold-based methods in open-world settings
- Practical deployment advantage: no tuning required when switching between domains or task types


## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent concept discoveries

## Theme Framing
**Axis**: Inference efficiency — KV cache memory optimization without threshold tuning
