---
title: "An Empirical Study of Many-Shot In-Context Learning for Machine Translation of Low-Resource Languages"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [in-context-learning, many-shot, machine-translation, low-resource, sample-efficiency, deployment-economics, llm-research]
sources: ["https://arxiv.org/abs/2604.02596"]
---

# An Empirical Study of Many-Shot In-Context Learning for Machine Translation of Low-Resource Languages

## Overview
Empirical study of many-shot in-context learning (ICL) for English→low-resource machine translation across ten truly low-resource languages (e.g., Bribri, Dari, Falam, Limbum, Manipuri, etc.). Investigates how ICL scaling laws interact with example selection under context-length budget constraints for low-resource language communities, where many-shot ICL is a deployment-economics question as much as a quality question.

## Key Facts
- **Authors**: Lu, Yinhan; Jhajj, Gaganpreet; Zhang, Chen; et al.
- **Year**: 2026
- **Date**: 2026-06-23
- **arXiv**: [2604.02596](https://arxiv.org/abs/2604.02596)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- Empirical characterization of **many-shot ICL scaling behavior** for low-resource MT — measured how example-count scaling interacts with example-selection quality, exposing the dual budget of context-length cost and per-example informativeness
- Many-shot ICL quality depends strongly on example selection, and the **inference-cost-vs-quality frontier** shifts unfavorably for low-resource languages where community-scale compute budgets cannot absorb the context-length expansion
- Establishes **ICL context-length budget as a sample-efficiency primitive** for low-resource deployment — distinct from the high-resource regime where context-length cost is amortized across larger user populations
- Concrete guidance on **example selection under context-length constraints** as a load-bearing engineering primitive for LLM deployment in low-resource language communities

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Sample-efficient pretraining primitive (different layer but same sample-efficiency theme)
- [[endprompt-efficient-long-context-extension-via-terminal-anchoring-2605.14589]] — Long-context efficiency primitive
- [[the-impossibility-triangle-of-long-context-modeling-2605.05066]] — Long-context trade-offs primitive