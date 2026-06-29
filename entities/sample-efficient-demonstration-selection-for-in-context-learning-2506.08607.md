---
title: "Sample Efficient Demonstration Selection for In-Context Learning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [in-context-learning, demonstration-selection, sample-efficiency, best-arm-identification, bandits, llm-research]
sources: ["https://arxiv.org/abs/2506.08607"]
---

# Sample Efficient Demonstration Selection for In-Context Learning

## Overview
Formulates the exemplar (demonstration) selection problem for in-context learning (ICL) as a **top-m best-arms identification** problem from the multi-armed bandit literature. The key challenge is the exponentially large number of candidate demonstration arms, addressed via CASE (Challenger Arm Sampling for Exemplar selection), a sample-efficient algorithm that identifies the m-best demonstrations under context-length budget constraints.

## Key Facts
- **Authors**: Purohit, Kiran; Venktesh, V; Bhattacharya, Sourangshu; et al.
- **Year**: 2025
- **Date**: 2025-06-10
- **arXiv**: [2506.08607](https://arxiv.org/abs/2506.08607)
- **Subjects**: Computation and Language (cs.CL); Machine Learning (cs.LG)

## Key Contributions
- **Best-arm-identification formulation for exemplar selection** — surfaces the sample-efficiency-of-demonstration-selection primitive for ICL, distinct from generic few-shot-pool sampling primitives (where the load-bearing axis is *top-m best-arm identification under exponentially-large-arm-budgets* rather than *uniform-random-or-diversity-sampling*)
- **CASE (Challenger Arm Sampling for Exemplar selection)** — a sample-efficient bandit algorithm for identifying the m-best demonstrations when the candidate pool is exponentially large, avoiding exhaustive evaluation
- Establishes **exemplar selection as a multi-armed-bandit problem** — the load-bearing primitive for sample-efficient ICL under context-length budget constraints where exhaustive evaluation is infeasible
- Bridges bandit theory and LLM ICL — the **best-arm-identification primitive** becomes a structural primitive for moving ICL beyond ad-hoc selection toward principled sample-efficient demonstration discovery

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Sample-efficient LLM pretraining (different layer but same sample-efficiency theme)
- [[an-empirical-study-of-many-shot-in-context-learning-for-machine-translation-of-low-resource-languages-2604.02596]] — Many-shot ICL sample-efficiency sibling discovery (same run)
- [[manifold-bandits-bayesian-curriculum-learning-over-the-latent-geometry-of-large-language-models-2606.19750]] — Bayesian-curriculum bandit primitive