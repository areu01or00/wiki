---
title: "Where Does the Signal Live? A Web Data Recipe for Medical Encoder Pretraining"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [data-curation, web-data, medical-encoder, pretraining, dense-terminology, mlm]
sources: ["https://arxiv.org/abs/2606.22079"]
---

# Where Does the Signal Live? A Web Data Recipe for Medical Encoder Pretraining

## Overview
Surfaces whether web-scale data curation — proven for decoder LLM pretraining — also benefits encoder Masked Language Modeling in dense-terminology domains like medicine, where encoders have historically been trained on small manually-curated corpora that limit scalability and writing-style diversity (a bottleneck especially severe in non-English clinical settings). Proposes a recipe that combines domain-relevant document filtering with quality signals adapted to encoder MLM, showing that web-curated data improves medical encoder pretraining at scale.

## Key Facts
- **Authors**: Huang, Bofeng; Sun, Jacques; Bouchacourt, Diane; Barascud, Nicolas; Fogel, Fajwel
- **Year**: 2026
- **arXiv**: [2606.22079](https://arxiv.org/abs/2606.22079)
- **Date**: 2026/06/20

## Key Contributions
- Diagnoses the encoder-vs-decoder pretraining-data asymmetry: encoders for dense-terminology domains have been confined to small manually-curated corpora while decoder LLMs benefit from web-scale curation.
- Investigates whether web-scale data curation transfers to encoder MLM in dense-terminology domains like medicine, especially under non-English clinical settings.
- Introduces a web-data recipe combining domain-relevant document filtering with quality signals adapted to encoder MLM, surfacing *signal-location-aware-curation* as the load-bearing primitive for domain-specific encoder pretraining.

## Related Papers
- [[beyond-reward-engineering-a-data-recipe-for-long-context-reinforcement-learning-2606.18831]] — sibling data-recipe-for-RL work; Beyond-Reward-Engineering focuses on data recipes for long-context RL, Where-Does-the-Signal-Live focuses on data recipes for medical encoder pretraining — together they bracket the data-recipe-as-discipline surface between *post-training RL data curation* (Beyond-Reward-Engineering) and *domain-specific encoder pretraining data curation* (Where-Does-the-Signal-Live)
- [[openthoughts-agent-data-recipes-for-agentic-models-2606.24855]] — sibling data-recipe-for-agentic-models work; OpenThoughts-Agent provides (task, trajectory) data recipes for agentic fine-tuning, Where-Does-the-Signal-Live provides web-curation recipes for encoder pretraining — together they bracket the data-recipe discipline between *agentic fine-tuning supervision* (OpenThoughts-Agent) and *domain-specific encoder pretraining* (Where-Does-the-Signal-Live)
- [[emergent-concepts]] — parent wiki page
