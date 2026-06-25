---
title: "Forecasting Future Behavior as a Learning Task"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [interpretability, large-reasoning-models, behavior-forecasting, alignment, safety]
sources: ["https://arxiv.org/abs/2606.11445"]
---

# Forecasting Future Behavior as a Learning Task

## Overview
Argues that the canonical interpretability route — *explain* a model's behavior, then use the explanation to *forecast* its future behavior — breaks down for Large Reasoning Models (LRMs) because (a) single-token explanation methods do not generalize to long trajectories and (b) LRMs' trajectory natural-language is often unfaithful. Proposes instead to **bypass explanation entirely** and treat behavior forecasting itself as a supervised learning task, training a **Behavior Forecaster** that operates on a single reasoning trajectory and predicts what the model will do next.

## Key Facts
- **Authors**: Levy, Mosh; Goldberg, Yoav; Stickland, Asa Cooper
- **Year**: 2026
- **arXiv**: [2606.11445](https://arxiv.org/abs/2606.11445)
- **Date**: 2026-06-09

## Key Contributions
- **Diagnoses a structural breakdown of the explanation→forecast pipeline for LRMs**: trajectory-level explanation is technically available but empirically unfaithful, so forecasts derived from explanations inherit that unfaithfulness
- Proposes **Behavior Forecasting as a learning task** — direct supervised learning of next-trajectory prediction from reasoning trajectories, sidestepping the unfaithful-explanation bottleneck
- Provides an **alternative trust anchor**: rather than asking users to *understand* the LRM and then trust it, train an auxiliary forecaster that earns trust by being right about future behavior, decoupling trust from interpretability

## Related Papers
- [[emergent-concepts]] — Parent meta-page; discovered via emergent-concept search on 2026-06-25
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Sibling mechanistic-interpretability work on jailbreak detection (intermediate-layer entropy dynamics)
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — Sibling CoT-reasoning-evaluability work that raises the same diagnosis that *natural-language reasoning traces are not learnable signals in the way we hope*
