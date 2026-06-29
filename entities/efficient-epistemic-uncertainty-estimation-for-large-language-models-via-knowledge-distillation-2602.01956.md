---
title: "Efficient Epistemic Uncertainty Estimation for Large Language Models via Knowledge Distillation"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [uncertainty-quantification, epistemic-uncertainty, knowledge-distillation, hallucination-detection]
sources: ["https://arxiv.org/abs/2602.01956"]
---

# Efficient Epistemic Uncertainty Estimation for Large Language Models via Knowledge Distillation

## Overview
Addresses the computational intractability of Deep Ensembles for epistemic uncertainty (EU) estimation at LLM scale by proposing a knowledge distillation framework that uses small draft models to efficiently estimate token-level EU. Uses Jensen-Shannon divergence among drafts as a variance proxy and KL divergence between draft mixture and target as a bias proxy, theoretically grounded in Bias-Variance Decomposition. Online Stochastic Distillation (OSD) approximates target aggregation and Data-Diverse Drafts (DDD) enhances draft diversity. Achieves 37% reduction in estimation error (RMSE) on GSM8K and hallucination detection competitive with heavy perturbation-based methods at negligible inference cost.

## Key Facts
- **Authors**: Seonghyeon Park, Jewon Yeom, Jaewon Sok, Jeongjae Park, Heejun Kim, Taesup Kim
- **Year**: 2026
- **arXiv**: [2602.01956](https://arxiv.org/abs/2602.01956)
- **Submitted**: 2 Feb 2026

## Key Contributions
- First knowledge distillation approach to efficient epistemic uncertainty estimation at LLM scale (bypasses full-scale ensembling)
- Theoretical grounding via Bias-Variance Decomposition: EU ≈ JS-divergence(drafts) [variance] + KL(mixture‖target) [bias]
- Online Stochastic Distillation (OSD): efficient approximation of target aggregation
- Data-Diverse Drafts (DDD): maximize draft diversity for better target approximation
- Practical deployment: hallucination detection competitive with TokUR at negligible cost
- Key insight: small draft models can capture uncertainty-relevant information from the target LLM without full ensemble

## Related Papers
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Intra-layer local information scores for uncertainty estimation
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — Calibrated verifier telemetry for knowledge-intensive tasks
