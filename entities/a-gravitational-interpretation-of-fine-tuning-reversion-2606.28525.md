---
title: "A Gravitational Interpretation of Fine-Tuning Reversion"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [alignment, safety, fine-tuning, interpretability]
sources: ["https://arxiv.org/abs/2606.28525"]
---

# A Gravitational Interpretation of Fine-Tuning Reversion

## Overview
This paper proposes a "gravitational interpretation" of fine-tuning reversion: early pre-training creates dominant behavioral manifolds that later alignment phases inherit a persistent reversion component pointing back toward. The paper identifies a history-defined reversion direction (v_rev) in activation space that causally mediates early post-alignment reversion — selectively blocking motion along v_rev reduces harmfulness from 19.0% to 8.5% with minimal task cost.

## Key Facts
- **Authors**: Samuele Poppi, Nils Lukas
- **Year**: 2026
- **arXiv**: [2606.28525](https://arxiv.org/abs/2606.28525)

## Key Contributions
- Identifies v_rev — a history-defined reversion direction in activation space — as the causal mediator of fine-tuning reversion
- Shows alignment with v_rev rises from cos=0.429 after first update to 0.647 by step 20; every observed alignment exceeds p99 of isotropic null
- Demonstrates blocking v_rev motion changes final alignment from 0.648 to -0.211 and reduces harmfulness from 19.0% to 8.5% with little task cost
- Proposes the "gravitational interpretation": later fine-tuning phases are shallow displacements from dominant early manifolds, with a persistent reversion component pointing back
- Connects across generative settings: safety erosion, capability re-emergence, latent trait transfer

## Related Papers
- [[evirank-evidence-based-confidence-estimation-for-llm-based-ranking-2606.04727]] — Evidence-based confidence estimation relevant to alignment quality assessment
- [[v-zero-answer-label-free-on-policy-distillation-contrastive-evidence-2606.25319]] — On-policy distillation and alignment stability
- [[minority-sentinel-when-to-overturn-majority-voting-in-multi-agent-llm-debates-2606.29270]] — Multi-agent debate collapse prevention mechanisms
