---
title: "Density Ridge Selective Prediction for LLM and VLM Hallucination Detection via Kinematic Feature Density of Hidden State Trajectories"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [uncertainty-quantification, selective-prediction, hallucination-detection, density-ridge, manifold-recovery, kinematic-features, vlm, llm]
sources: ["https://arxiv.org/abs/2606.10198"]
---

# Density Ridge Selective Prediction for LLM and VLM Hallucination Detection via Kinematic Feature Density of Hidden State Trajectories

## Overview
A selective-prediction framework that recovers the LLM response manifold as the density ridge of a kernel density estimate built on a six-dimensional kinematic feature map of hidden-state generation trajectories — bridging the gap between unsupervised Semantic-Entropy detectors (label-free but plateau) and supervised probes (in-distribution-strong but scarce-label-fragile) via geometry-grounded ridge estimation.

## Key Facts
- **Authors**: Shamsi, Nina I.
- **Year**: 2026
- **arXiv**: [2606.10198](https://arxiv.org/abs/2606.10198)
- **Submission date**: 2026-06-08
- **Online date**: 2026-06-10

## Key Contributions
- **Six-dimensional kinematic feature map of hidden-state trajectories**: defines a compact kinematic feature representation for LLM generation trajectories that captures the geometric structure of the model's response dynamics — distinct from raw token-probability features (sequence-level semantics only) and supervised-probe features (in-distribution-strong but transfer-fragile).
- **Density-ridge recovery of the LLM response manifold**: applies kernel density estimation to the six-dimensional kinematic features and recovers the response manifold as the ridge of the density estimate, surfacing *response-manifold-as-density-ridge-primitive* as the structurally correct primitive for selective prediction when both label-scarcity (supervised-probe failure) and semantic-clustering-plateau (Semantic-Entropy failure) are present.
- **Unsupervised-yet-rigorous selective prediction**: delivers unsupervised detection (no labels required for ridge estimation) with stronger in-distribution performance than Semantic-Entropy and stronger cross-distribution robustness than supervised probes — surfacing *geometry-grounded-unsupervised-ridge-detection-primitive* as a load-bearing alternative to both label-heavy and cluster-plateau-prone baselines.
- **Cross-modal application to LLMs and VLMs**: unified framework for hallucination detection in both large language models and vision-language models via the same kinematic feature density-ridge primitive, surfacing *kinematic-feature-density-ridge-as-modality-agnostic-selective-prediction-primitive* as a load-bearing cross-modal primitive.

## Related Papers
- [[uncertainty-quantification-for-hallucination-detection-in-llms-2510.12040]] — Sibling UQ-as-trust-framework primitive: complementary survey framing that establishes UQ as central trustworthiness framework
- [[halluaudio-a-comprehensive-benchmark-for-hallucination-detection-in-large-audio-language-models-2604.19300]] — Sibling modality-specific hallucination-benchmark primitive: extends hallucination detection to audio-language models with modality-specific taxonomy
- [[hallucination-in-world-models-is-predictable-and-preventable-2606.27326]] — Sibling hallucination-as-compression-failure primitive: complementary compression-failure framing for world-model hallucinations
- [[the-anatomy-of-uncertainty-in-llms-a-three-component-semantic-framework-for-input-ambiguity-knowledge-gaps-and-decoding-randomness-2603.24967]] — Sibling three-component semantic-decomposition primitive: complementary UQ framework that decomposes uncertainty into causally-distinct components
- [[emergent-concepts]] — Parent meta-page for the emergent-concept discovery chain that surfaced this entity