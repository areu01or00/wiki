---
title: "CLEAR-MoE: Shared-Basis Expert Extraction from Frozen Vision Transformers via Calibration-Driven Layer Selection"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [architecture, llm, mixture-of-experts, calibration]
sources: ["https://arxiv.org/abs/2606.28516"]
---

# CLEAR-MoE: Shared-Basis Expert Extraction from Frozen Vision Transformers via Calibration-Driven Layer Selection

## Overview
CLEAR-MoE is a four-phase post-training pipeline that converts a frozen pretrained Vision Transformer (ViT) into a sparse Mixture-of-Experts (MoE) model without updating backbone weights. The method selects FFN layers by sparsity, clusterability, and output sensitivity; decomposes selected layers into a shared low-rank SVD basis and per-cluster residual experts via k-means; and trains lightweight routers supervised by cluster labels. This enables building sparse MoE models from dense frozen ViTs — a form of calibration-driven architecture discovery.

## Key Facts
- **Authors**: Hossain, Md Irtiza; Ayesha, Humaira; Sifat, Junaid Ahmed
- **Year**: 2026
- **arXiv**: [2606.28516](https://arxiv.org/abs/2606.28516)

## Key Contributions
- **Frozen-to-Sparse MoE conversion**: No backbone weight updates required — preserves original pretraining quality while gaining sparse MoE routing efficiency
- **Calibration-driven layer selection**: Scores FFN layers by sparsity, clusterability, and output sensitivity — a form of architecture self-diagnosis
- **Shared low-rank SVD basis decomposition**: Decomposes selected FFN layers into a shared basis plus per-cluster residual experts — reduces parameter overhead while maintaining expert diversity
- **Lightweight learned routers**: Trains cluster-label-supervised routers that route tokens to the right expert cluster — simpler than end-to-end MoE routing

## Related Papers
- *Soft-to-Hard Routing in Sparse MoE Models* (2605.02124) — Studies the theoretical singularity at the routing-tie boundary in softmax-routed MoE models. CLEAR-MoE takes a complementary empirical/architectural approach, directly constructing sparse routers rather than studying the softmax-temperature limit.
- *Grammar-Constraint GCD Jailbreak* (2606.11817) — Run 307's GCD Jailbreak paper studies MoE model vulnerability under grammar-constraint exploits. CLEAR-MoE's calibration-driven expert selection framework provides the architectural substrate (sparse MoE from frozen ViT) for understanding expert routing behavior under distribution shift.
