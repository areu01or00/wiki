---
title: "Secret Mixtures of Experts Inside Your LLM"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [mechanistic-interpretability, mixture-of-experts, mlp, sparse-autoencoder, transformer-architecture]
sources: ["https://arxiv.org/abs/2512.18452"]
---

# Secret Mixtures of Experts Inside Your LLM

## Overview
Hypothesizes and empirically validates that the **MLP layers in dense LLMs secretly approximate a sparsely-activating Mixture-of-Experts (MoE) computation** — providing a mechanistic explanation for the effectiveness of MoE-based transformers and suggesting new directions for low-rank router design. The theoretical bridge uses **Sparse Autoencoder (SAE) structure** in activation space.

## Key Facts
- **Authors**: Boix-Adsera, Enric
- **Year**: 2025
- **arXiv**: [2512.18452](https://arxiv.org/abs/2512.18452)

## Key Contributions
- Formalizes a **theoretical bridge between MoE layers and SAE structure** in activation space, framing the dense-MLP-as-MoE hypothesis as testable sparse-approximation in pretrained LLMs.
- Empirically validates that **MLP activations in pretrained LLMs can be approximated by sparse MoE layers** — but only because of *structure in the distribution of neural-network activations*. The same approximation fails on Gaussian data, ruling out generic sparsity explanations.
- Suggests **new directions for MoE architecture design based on low-rank routers**, leveraging the discovered dense-MLP-as-MoE structure to design more parameter-efficient routing mechanisms.

## Related Papers
- [[emergent-concepts]] — Parent discovery surface for emergent-concept exploration runs.
- [[grouped-query-experts-mixture-of-experts-on-gqa-self-attention-2606.20945]] — Companion work applying MoE to attention layers; this paper explains *why* dense MLPs work — they secretly approximate the same MoE computation.