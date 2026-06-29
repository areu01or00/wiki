---
title: "Data-efficient Fine-tuning for LLM-based Recommendation"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [data-pruning, coreset-selection, few-shot-fine-tuning, recommendation, sample-efficiency, llm-research]
sources: ["https://arxiv.org/abs/2401.17197"]
---

# Data-efficient Fine-tuning for LLM-based Recommendation

## Overview
Proposes **data pruning for efficient LLM-based recommendation** — identifying representative samples tailored for LLM few-shot fine-tuning as a coreset-selection problem. Addresses the practical cost barrier of fine-tuning LLMs on rapidly expanding recommendation data, where the cost of full-data fine-tuning limits deployment.

## Key Facts
- **Authors**: Lin, Xinyu; Wang, Wenjie; Li, Yongqi; et al.
- **Year**: 2024
- **Date**: 2024-06-04
- **arXiv**: [2401.17197](https://arxiv.org/abs/2401.17197)
- **Subjects**: Information Retrieval (cs.IR); Machine Learning (cs.LG)

## Key Contributions
- **Data pruning as a primitive for LLM fine-tuning** — formalizes "find the smallest subset that preserves recommendation fine-tuning quality" as a coreset-selection problem, distinct from generic data-pruning primitives (where the load-bearing axis is *data-pruning-for-LLM-recommendation-fine-tuning* rather than *data-pruning-for-vision-classifier-training*)
- Identifies representative samples for **LLM few-shot fine-tuning in recommendation** — establishes the *sample-efficiency-as-deployment-enabler* primitive for the recommendation domain where fine-tuning cost is the load-bearing deployment barrier
- **Coreset-selection for LLM domain-adaptation** — surfaces a structurally distinct sample-efficiency primitive that operates on the FT layer rather than the ICL layer, complementing Run 100's exemplar-selection primitive
- Bridges coreset-selection literature and LLM fine-tuning, establishing **data-pruning-as-deployment-enabler** as a sample-efficiency primitive for vertical-domain LLM adaptation

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Sample-efficient pretraining sibling primitive (different layer, same sample-efficiency theme)
- [[sample-efficient-demonstration-selection-for-in-context-learning-2506.08607]] — Sample-efficient demonstration selection sibling discovery (same run, ICL layer)
- [[an-empirical-study-of-many-shot-in-context-learning-for-machine-translation-of-low-resource-languages-2604.02596]] — Many-shot ICL sample-efficiency sibling discovery (same run, deployment layer)