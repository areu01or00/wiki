---
title: "Scalable Circuit Learning for Interpreting Large Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [interpretability, mechanistic-interpretability, sparse-circuit-learning, sparse-autoencoder, llm-interpretability]
sources: ["https://arxiv.org/abs/2606.16939"]
---

# Scalable Circuit Learning for Interpreting Large Language Models

## Overview
Addresses the structural *high-dimensionality-of-SAE-features-makes-intervention-based-circuit-learning-computationally-prohibitive* failure mode of mechanistic interpretability where raw neurons are polysemantic and existing intervention-based circuit-discovery methods cannot scale to the feature dimensionality produced by sparse autoencoders. Proposes **CircuitLasso**, a scalable circuit-learning approach based on sparse linear regression that recovers circuits whose structural accuracy matches intervention-based methods at a fraction of the computational cost, then validates the utility of learned circuits via downstream domain generalization.

## Key Facts
- **Authors**: Yin, Naiyu; Wei, Dennis; Gao, Tian; Dhurandhar, Amit; Ramamurthy, Karthikeyan Natesan; Yu, Yue
- **Year**: 2026
- **arXiv**: [2606.16939](https://arxiv.org/abs/2606.16939) (online: 2026-06-15)

## Key Contributions
- **CircuitLasso** — sparse linear regression formulation of circuit discovery that scales to SAE-feature dimensionality without intervention-based computational cost
- Structural accuracy matching intervention-based SOTA on benchmark data, at a fraction of compute
- Recovered circuits expose how human-interpretable semantic features propagate through the model and influence predictions
- Validation via domain generalization: insights from learned circuits transferred to substantially-lower-cost downstream performance

## Related Papers
- [[emergent-concepts]] — Parent meta-page that led to this discovery
- [[interpretability-can-be-actionable-2605.11161]] — Position paper arguing interpretability should be evaluated by *actionability* (concreteness × validation four-quadrant grid) — CircuitLasso's domain-generalization validation is a concrete *actionability* demonstration
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Earlier SAE-based latent-reasoning-feature discovery (single-feature steering matches CoT prompting); CircuitLasso advances from single-feature steering to scalable *circuit-level* feature relationships