---
title: "Layer-Wise Perturbations via Sparse Autoencoders for Adversarial Text Generation"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [adversarial, representation, sparse-autoencoder, red-team, llm-security]
sources: ["https://arxiv.org/abs/2508.10404"]
---

# Layer-Wise Perturbations via Sparse Autoencoders for Adversarial Text Generation

## Overview
Proposes the Sparse Feature Perturbation Framework (SFPF), a black-box adversarial text generation method using sparse autoencoders to identify and manipulate critical features in transformer hidden layers. SAE models reconstruct representations, cluster successfully attacked texts to find highly-activated features, then perturb those features to generate adversarial examples that bypass SOTA defenses while preserving malicious intent. Enables interpretable red-teaming balancing adversarial effectiveness with safety alignment.

## Key Facts
- **Authors**: Huizhen Shu, Xuying Li, Qirui Wang, Yuji Kosuga, Mengqiu Tian, Zhuo Li
- **Year**: 2025
- **arXiv**: [2508.10404](https://arxiv.org/abs/2508.10404)
- **Subjects**: Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
- **Submitted**: 2025-08-14

## Key Contributions
- **Sparse Feature Perturbation Framework (SFPF)**: SAE-based identification and manipulation of critical features in LLM hidden layers for adversarial text generation
- **Layer-wise feature clustering**: Clusters successfully attacked texts post-SAE reconstruction to identify highly-activated features for targeted perturbation
- **Black-box attack design**: No white-box access required; leverages SAE interpretability to guide perturbation selection
- **Defense-agnostic evasion**: Generated adversarial texts bypass state-of-the-art defense mechanisms, revealing persistent vulnerabilities

## Related Papers
- [[belief-or-circuitry-causal-evidence-for-in-context-graph-learning-2605.08405]] — Causal mechanism decomposition framework; SFPF's feature perturbation is the adversarial counterpart to Belief-or-Circuitry's causal feature decomposition (both investigate what features matter in LLM representations)
- [[causality-is-key-for-interpretability-claims-to-generalise-2602.16698]] — Causal validity criterion for interpretability; SFPF's adversarial manipulation of SAE-identified features challenges the causal fidelity of interpretability methods (features that look causally important can be adversarially exploited)
