---
title: "Scaling RL for Code Generation with Synthetic Data and Curriculum"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [reinforcement-learning, code-generation, synthetic-data, curriculum-learning, multi-turn-generation, scaling]
sources: ["https://arxiv.org/abs/2603.24202"]
---

# Scaling RL for Code Generation with Synthetic Data and Curriculum

## Overview
Addresses the challenge of sustaining RL performance gains at scale for code generation by introducing a scalable multi-turn synthetic data generation pipeline in which a teacher model iteratively refines problems based on in-context student performance summaries, producing structured difficulty progressions without any teacher fine-tuning. Systematically studies how task difficulty, curriculum scheduling, and environment diversity interact during RL training across Llama3.1-8B Instruct and Qwen3-8B Base families.

## Key Facts
- **Authors**: Wang, Hao; Chen, Linyi; Patel, Anish; Schmidt, Robert
- **Year**: 2026
- **arXiv**: [2603.24202](https://arxiv.org/abs/2603.24202)

## Key Contributions
- **Multi-turn synthetic data generation pipeline**: teacher iteratively refines problems based on in-context student performance summaries, producing stepping stones (easier/harder variants of same core task) that support curriculum-based training without teacher fine-tuning
- **Curriculum-scheduling × environment-diversity interaction study**: systematic ablations on Llama3.1-8B Instruct and Qwen3-8B Base, with scaling experiments on Qwen2.5-32B — shows synthetic augmentation consistently improves in-domain code and in most cases out-of-domain math
- **Empirical insights into RL training dynamics**: provides evidence that curriculum design and data diversity jointly shape RL outcomes, not just data volume alone
- **Stepping-stone-as-curriculum primitive**: positions structured difficulty progressions as the load-bearing mechanism for sustaining RL gains at scale, distinct from single-turn synthetic-data approaches

## Related Papers
- [[gem-geometric-entropy-mixing-for-optimal-llm-data-curation-2605.26121]] — Sibling data-curation primitive (Geometric Entropy Mixing variational hypersphere) — both curate training data; GEM curates *selection* while this paper curates *difficulty progression*
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — Sibling on-policy-RL primitive (skill-distillation) — both improve RL via on-policy signals, OPID via skill-extraction and this paper via curriculum
- [[energy-based-fine-tuning-of-language-models-2603.12248]] — Sibling from Run 70 — sequence-level objectives, EBFT (verifier-free on-policy) complements synthetic-data curriculum (data-engineered on-policy)
