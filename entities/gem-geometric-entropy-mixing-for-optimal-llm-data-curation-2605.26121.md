---
title: "GEM: Geometric Entropy Mixing for Optimal LLM Data Curation"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [data-curation, llm, pretraining, geometric-entropy, mixing, hypersphere, do-remi, regmix, variational, mm-algorithm]
sources: ["https://arxiv.org/abs/2605.26121"]
---

# GEM: Geometric Entropy Mixing for Optimal LLM Data Curation

## Overview
Reformulates LLM pre-training data curation as a variational problem on the hypersphere, introducing a Geometric Entropy Mixing (GEM) framework that counteracts human-taxonomy ontological misalignment and Euclidean-embedding anisotropy. Decouples the generative prior and optimizes via a provable Minorize-Maximize (MM) algorithm, with teacher-student distillation scaling to web-scale corpora and a Geometric Influence Score (GIS) for interpretable taxonomy generation.

## Key Facts
- **Authors**: Min, Yue
- **Year**: 2026
- **arXiv**: [2605.26121](https://arxiv.org/abs/2605.26121)

## Key Contributions
- **Variational hypersphere formulation**: data curation as a variational problem on the unit hypersphere, where embedding anisotropy is encoded into the geometry rather than fought against by Euclidean heuristics
- **Minorize-Maximize (MM) algorithm**: provably convergent optimization that decouples the generative prior from the mixing balance, with theoretical guarantees on counteracting cluster collapse
- **Teacher-student distillation to web-scale**: geometric fidelity from controlled-distribution GE algorithms transferred to web-scale corpora via distillation, enabling practical deployment
- **Geometric Influence Score (GIS)**: interpretable per-sample scoring mechanism that simultaneously serves as an axis for automated taxonomy generation
- **State-of-the-art on DoReMi and RegMix integration**: when GEM-derived mixing is plugged into established mixing strategies (DoReMi, RegMix), average downstream accuracy improves by up to 1.2% on 1.1B-parameter models

## Related Papers
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Sibling data-mixing work — AC-ODM is *online* mixing with actor-critic feedback during training, GEM is *pre-training-curation* mixing via geometric entropy on the hypersphere — together they bracket the LLM data-mixing surface between online-feedback and offline-geometric-entropy primitives
- [[fastmix-fast-data-mixture-optimization-via-gradient-descent-2606.14971]] — Sibling data-mixing optimization work — FastMix optimizes mixture weights via gradient descent, GEM optimizes mixture geometry via variational hypersphere — together they bracket the LLM data-mixing surface between gradient-descent-weight and variational-geometry primitives
- [[demystifying-training-time-augmentation-for-data-constrained-language-model-pretraining-2606.16246]] — Sibling data-constrained pretraining work — Demystifying addresses *augmentation* under data scarcity, GEM addresses *mixing geometry* under standard-scale data — together they bracket the data-constrained pretraining surface between augmentation-side and mixing-geometry-side primitives
- [[emergent-concepts]] — Parent wiki page

## Theme Context
**Domain pivot from agent-failure (Runs 55-57) to data-curation / world-model / interpretability axes (Run 58)**: Runs 55-57 clustered on agent-failure surfaces (memory-credit-assignment / trading-eval / silent-failure mechanism + component-modular-failure-taxonomy). Per pitfall-91 domain-diversity tracker, Run 58 deliberately pivots to training-data + world-model + interpretability axes to maintain wiki primitive diversity.
