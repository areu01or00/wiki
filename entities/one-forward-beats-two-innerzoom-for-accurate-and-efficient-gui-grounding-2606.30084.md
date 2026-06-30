---
title: "One Forward Beats Two: InnerZoom for Accurate and Efficient GUI Grounding"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [gui-agent, mllm, grounding, efficiency, test-time-compute]
sources: ["https://arxiv.org/abs/2606.30084"]
---

# One Forward Beats Two: InnerZoom for Accurate and Efficient GUI Grounding

## Overview
MLLM-based GUI grounding methods commonly formulate target localization as autoregressive coordinate generation, requiring models to retain region-level evidence while decoding spatial tokens. InnerZoom proposes a single-forward approach that bypasses this difficulty by learning spatial zoom tokens that dynamically re-encode the relevant region, enabling accurate, efficient GUI interaction without multi-step decoding.

## Key Facts
- **Authors**: (from arXiv abstract — see paper)
- **Year**: 2026
- **arXiv**: [2606.30084](https://arxiv.org/abs/2606.30084)

## Key Contributions
- Proposes spatial zoom tokens that dynamically re-encode relevant GUI regions in a single forward pass
- Eliminates the need for multi-step autoregressive coordinate generation in GUI grounding
- Demonstrates improved accuracy and efficiency over prior MLLM-based GUI grounding approaches
- Load-bearing axis: single-forward MLLM GUI grounding without iterative decoding

## Related Papers
- [[dustin-draft-augmented-sparse-verification-for-efficient-long-context-generation-with-speculative-decoding-2606.24957]] — Draft-augmented sparse verification for long-context generation
- [[efficient-epistemic-uncertainty-estimation-for-large-language-models-via-knowledge-distillation-2602.01956]] — Efficient uncertainty estimation via knowledge distillation
- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — Trainable test-time scaling via branch routing
