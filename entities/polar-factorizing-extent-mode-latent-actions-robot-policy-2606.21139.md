---
title: "PoLAR: Factorizing Extent and Mode in Latent Actions for Robot Policy Learning"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [robotics, latent-action, representation-learning, factorize, flow-matching, policy-learning]
sources: ["https://arxiv.org/abs/2606.21139"]
---

# PoLAR: Factorizing Extent and Mode in Latent Actions for Robot Policy Learning

## Overview
Jeong, Yu, Jo, Chun, and Kim address a structural ambiguity in latent action pretraining for robot policies — where existing methods encode each observation-transition pair as a single unstructured representation that entangles *transition extent* (how much changed) with *transition mode* (what kind of change) — by proposing Polar Latent Actions with Radial structure (PoLAR), which imposes a radial-direction geometry on latent actions, encouraging the radius to encode transition extent and the angular direction to encode transition mode, yielding a factorized latent representation that improves downstream policy learning and supports composable behavior transfer.

## Key Facts
- **Authors**: Jeong, Youngjoon; Yu, Jihwan; Jo, Minsoo; Chun, Junha; Kim, Taesup
- **Year**: 2026
- **arXiv**: [2606.21139](https://arxiv.org/abs/2606.21139)
- **Date**: 2026-06-19

## Key Contributions
- Diagnoses a structural ambiguity in latent action pretraining: existing methods encode each transition as a single unstructured representation that conflates *transition extent* (how much changed between observations) with *transition mode* (what kind of change), making the latent space hard to interpret and limiting how downstream policies can compose behaviors.
- Proposes PoLAR (Polar Latent Actions with Radial structure), which imposes a radial-direction geometry on latent actions — radius encodes transition extent, angular direction encodes transition mode — yielding a factorized representation that mirrors the geometric primitives of the underlying visual change.
- Surfaces a methodology-level contribution: factorized latent spaces that align with the geometric primitives of the underlying phenomenon (extent vs mode in transitions) are a structurally stronger inductive bias than unstructured embeddings, supporting composable behavior transfer and downstream interpretability.
- Demonstrates improved downstream policy learning and cleaner behavior composition compared to unstructured-latent baselines, complementing the broader flow-matching and world-model representation-learning wave (WVM, Foresight, WAM) by isolating the factorize-extent-from-mode axis as a load-bearing inductive bias for latent action pretraining.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[world-value-models-robotic-manipulation-2606.24742]] — Sibling robotics representation-learning work on the value-estimation axis; both papers argue for richer, geometry-aware representations as the substrate for downstream policy learning — WVM uses world-model latents for value estimation, PoLAR uses polar-structured latents for action pretraining.
- [[worldlines-benchmarking-and-modeling-long-horizon-stateful-2606.18847]] — Sibling long-horizon embodied work; both papers surface a *geometry-of-representation* angle on embodied agents — WorldLines uses two complementary memory streams (visibility-aware + action-native state trails), PoLAR uses two complementary latent axes (radius for extent, angle for mode).
- [[flowr2a-learning-reward-to-action-distribution-for-multimodal-driving-planning-2606.24231]] — Sibling robotics policy-learning work on the multimodal driving surface; both extend representation-learning insights into downstream policy learning — FlowR2A from reward-to-action distributions, PoLAR from factorized latent actions.