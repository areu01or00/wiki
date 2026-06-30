---
title: "Symbolic Mechanistic Data Attribution: Tracing Training Influence to Learned Behavioral Policies"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [interpretability, data-attribution, training-dynamics]
sources: ["https://arxiv.org/abs/2606.29171"]
---

# Symbolic Mechanistic Data Attribution: Tracing Training Influence to Learned Behavioral Policies

## Overview
SMDA (Symbolic Mechanistic Data Attribution) bridges the gap between identifying which training examples build specific circuits and explaining how training data shapes high-level behavioral decisions. It uses sparse autoencoder (SAE) features to decompose how each SFT example shifts policy through feature-activation and output-probability pathways.

## Key Facts
- **Authors**: 
- **Year**: 2026
- **arXiv**: [2606.29171](https://arxiv.org/abs/2606.29171)

## Key Contributions
- Symbolic policy decomposition via Ridge regression over SAE features
- Delta_X (feature activation) and Delta_Y (output probability) pathway decomposition per training pair
- Cross-feature interference identification in individual training pairs
- Application to Llama-3.2-3B-Instruct refusal behavior analysis revealing systematic safety gaps

## Related Papers
- [[mechanistic-circuit-based-knowledge-editing-in-large-language-models-2604.05876]] — SAE-based circuit analysis methodology
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Circuit tracing methodology for LLM interpretability
