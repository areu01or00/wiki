---
title: "Robust Uncertainty Quantification for Self-Evolving Large Language Models via Continual Domain Pretraining"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [uncertainty-quantification, continual-learning, self-evolving-llm, calibration, robustness]
sources: ["https://arxiv.org/abs/2510.22931"]
---

# Robust Uncertainty Quantification for Self-Evolving Large Language Models via Continual Domain Pretraining

## Overview
Continual Learning (CL) enables self-evolving LLMs to adapt amid rapid knowledge growth, but establishing statistical reliability guarantees for LLMs under CL — particularly uncertainty quantification (UQ) — is underexplored. This paper provides rigorous UQ for self-evolving LLMs by accounting for the distributional shift introduced by continual domain pretraining, ensuring calibrated confidence estimates remain reliable as the model evolves.

## Key Facts
- **Authors**: Zhou, Xiaofan; Cheng, Lu
- **Year**: 2025
- **arXiv**: [2510.22931](https://arxiv.org/abs/2510.22931)

## Key Contributions
- Establishes statistical reliability guarantees (conformal prediction-style coverage) for LLMs undergoing continual domain pretraining
- Shows that naive UQ methods fail under CL distributional shift — model confidence becomes miscalibrated as knowledge evolves
- Proposes robust UQ framework that adapts to distributional shift introduced by CL updates
- Bridges two underexplored intersections: UQ + continual learning + LLM self-evolution

## Related Papers
- [[clustered-self-assessment-uncertainty-quantification-llms-2606.03846]] — Clustered self-assessment UQ for LLMs
