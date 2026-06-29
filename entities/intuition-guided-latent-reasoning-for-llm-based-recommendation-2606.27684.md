---
title: "Intuition-Guided Latent Reasoning for LLM-Based Recommendation"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [recommendation-systems, latent-reasoning, llm-user-modeling]
sources: ["https://arxiv.org/abs/2606.27684"]
---

# Intuition-Guided Latent Reasoning for LLM-Based Recommendation

## Overview
IntuRec addresses a key failure mode in LLM-based recommendation: unconstrained latent reasoning starts from hidden representations misaligned with target item embeddings, producing suboptimal reasoning trajectories. Inspired by cognitive neuroscience (human reasoning guided by intuition as a latent prior), IntuRec anchors latent reasoning with recommendation intuition — extracting top-K candidates from user history as an intuition source, then converting them into a preference-aligned intuition embedding that initializes the reasoning start point.

## Key Facts
- **Authors**: Chang Liu, Yimeng Bai, Xiaoyan Zhao, Yang Zhang, Qifan Wang, Fuli Feng, Wenge Rong
- **Year**: 2026
- **arXiv**: [2606.27684](https://arxiv.org/abs/2606.27684)
- **Submitted**: 26 Jun 2026
- **Subjects**: Information Retrieval (cs.IR)

## Key Contributions
- **Intuition-anchored latent reasoning**: Two-stage framework — extraction stage generates top-K candidates as intuition source; injection stage transforms candidates into preference-aligned intuition embedding
- **Self- and cross-attention for intuition embedding**: Cross-attention mechanisms transform the candidate set into an embedding that aligns with user preference structure
- **Grounded reasoning start point**: By initializing the latent reasoning at a semantically grounded position, IntuRec explores the preference space along more accurate trajectories
- **Multi-domain experiments**: Evaluated on multiple real-world recommendation datasets, consistently outperforming state-of-the-art baselines

## Related Papers
- [[data-efficient-fine-tuning-for-llm-based-recommendation-2401.17197]] — Data-efficient fine-tuning for LLM recommendation, the prior art this work extends with intuition-guided latent reasoning
- [[unlocking-the-black-box-of-latent-reasoning-an-interpretability-guided-approach-to-intervention-2606.01243]] — Latent reasoning interpretability framework that provides the theoretical grounding for the intuition-anchoring approach in IntuRec
