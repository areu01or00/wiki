---
title: "Spectral DPPs via NEPv: A Scalable Continuous Relaxation of Determinantal MAP for Diversity-Aware Data Selection"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [data selection, diversity, DPP, training data, fine-tuning]
sources: ["https://arxiv.org/abs/2606.19411"]
---

# Spectral DPPs via NEPv: A Scalable Continuous Relaxation of Determinantal MAP for Diversity-Aware Data Selection

## Overview
Selecting a small, diverse, high-quality subset from a massive pool of candidates is a recurring primitive in modern ML — data curation for training and fine-tuning large models, active-learning batch acquisition, prompt and exemplar selection for in-context learning. Determinantal Point Processes (DPPs) provide a principled model for diversity-aware selection but suffer from combinatorial MAP inference. This paper introduces NEPv, a scalable continuous relaxation of DPP-MAP that enables differentiable, GPU-friendly optimization for diversity-aware data selection at LLM training scale.

## Key Facts
- **Authors**: Da Xu, Richard Yi
- **Year**: 2026
- **arXiv**: [2606.19411](https://arxiv.org/abs/2606.19411)

## Key Contributions
- First DPP method specifically benchmarked on LLM training data curation and fine-tuning data selection
- NEPv continuous relaxation enables GPU-efficient MAP inference for DPPs at million-scale candidate pools
- Demonstrates improved fine-tuning quality vs random/batch-Q sampling on multiple LLM families
- Provides open-source implementation for integration into LLM training pipelines

## Related Papers
- [[sequential-statistical-inference-for-large-language-models-representation-validity-and-monitoring-2606.07624]] — LLM post-deployment monitoring framework, complementary data-quality tracking for production systems
- [[are-we-measuring-strategy-or-phrasing-the-gap-between-surface-and-approach-level-diversity-in-llm-math-reasoning-2606.29985]] — Diversity evaluation in LLM reasoning, theoretical complement to the data diversity primitive
