---
title: "When is Your LLM Steerable?"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm, steering, inference-control, interpretability]
sources: ["https://arxiv.org/abs/2606.11599"]
---

# When is Your LLM Steerable?

## Overview
When is Your LLM Steerable? investigates whether activation steering success can be predicted from early hidden-state dynamics at the start of generation, before full rollout. It introduces ASTEER, a testbed of 1.4M steered generations across 150 concepts, and trains a GBDT classifier that achieves ~0.7 macro-F1 using early-layer features — demonstrating that steerability is predictable from cheap-to-compute internal state signals.

## Key Facts
- **Authors**: [arXiv 2606.11599](https://arxiv.org/abs/2606.11599)
- **Year**: 2026
- **arXiv**: [2606.11599](https://arxiv.org/abs/2606.11599)

## Key Contributions
- **ASTEER testbed**: 1.4M steered generations, 150 concepts, each with steering success/failure labels — largest published steering evaluation dataset
- **Early hidden-state predictor**: GBDT classifier trained on features comparing hidden states before/after steering across layers and initial decoding steps
- **~0.7 macro-F1 on unseen concepts**: Steerability is predictable from early generation dynamics without full rollout
- **Steering strength search acceleration**: Predictor guides steering strength selection, achieving near-optimal performance at small fraction of full-evaluation cost
- **Layer-wise propagation analysis**: Steering effects propagate along layers and token positions in structured, predictable ways
- **Three-class prediction**: Under-steer / succeed / over-steer classification

## Key Findings
- Early hidden states (after first few tokens) encode substantial structured information about eventual steering efficacy
- Steering success is highly prompt/concept/model/configuration dependent — grid search is expensive but early-state features can predict outcomes
- Layer-wise analysis reveals consistent propagation patterns: steering effects amplify through mid-layers and peak at specific token positions

## Related Papers
- [[minimal-oversight-uncertainty-aware-governance-for-delegated-ai-systems-2606.15563]] — Uncertainty-aware governance for AI delegation
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Intermediate-layer analysis for capability detection
