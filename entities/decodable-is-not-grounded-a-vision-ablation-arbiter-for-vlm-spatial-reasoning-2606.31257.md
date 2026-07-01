---
title: "Decodable Is Not Grounded: A Vision-Ablation Arbiter for VLM Spatial Reasoning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [interpretability, vlm, grounding, causal-reasoning, mechanistic-interpretability]
sources: ["https://arxiv.org/abs/2606.31257"]
---

# Decodable Is Not Grounded: A Vision-Ablation Arbiter for VLM Spatial Reasoning

## Overview
Linear probing and steering recovery systematically overstate what a VLM actually grounds in images. A one-line causal control — replacing the image with a gray blank — exposes that probing overstates grounding across all 14 VLMs studied. The taxonomy reveals three regimes: grounded (vision-dependent, correct), prior (vision-independent, a directional default), and inverted (causally controllable but deployed with wrong sign). The blank-image arbiter cleanly separates the three and should be a default control for latent-knowledge and steering claims in VLMs.

## Key Facts
- **Authors**: Chih-Ting Liao, Fei Shen, Xin Cao, Tat-Seng Chua
- **Year**: 2026
- **arXiv**: [2606.31257](https://arxiv.org/abs/2606.31257)

## Key Contributions
- **Blank-image causal arbiter** — replaces image with gray blank to expose whether VLM spatial reasoning is grounded (vision-dependent), a prior (vision-independent default), or inverted (below-chance, wrong sign); first systematic causal control for VLM grounding
- **Three grounding regimes taxonomy** — horizontal is grounded, vertical is a prior, depth is inverted; holds across 14 VLMs spanning 6 language model families and 2B–27B scales
- **Scale-emergent inversions** — decode-vs-deploy inversion replicates on 7/8 models across 5 families; minimal edit that re-deploys varies by geometry (rotation for cleanest models, trained low-rank edit for distributed inversions)
- **Training-free projection** — lifts near-chance axis from 59% to 79% via training-free projection, exactly the signature of unlocking latent knowledge

## Related Papers
- [[density-ridge-selective-prediction-for-llm-and-vlm-hallucination-detection-via-kinematic-feature-density-of-hidden-state-trajectories-2606.10198]] — related VLM interpretability via trajectory analysis
- [[closer-vln-closed-loop-self-verified-retrieval-augmented-reasoning-aerial-vision-language-navigation-2606.28397]] — related VLM spatial reasoning
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — related interpretability methodology
