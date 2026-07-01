---
title: "Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [continual-learning, small-language-model, personalization, edge-deployment, catastrophic-forgetting]
sources: ["https://arxiv.org/abs/2606.27634"]
---

# Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis

## Overview
Small Language Models (SLMs) on edge devices (laptops, phones) increasingly need to personalize to individual users over time — adapting to writing style, domain vocabulary, and task preferences. This creates a continual learning setting where each personalization update risks catastrophic forgetting of prior adaptations. The paper introduces stability monitoring analysis to track forgetting across sequential personalization sessions, finding that SLMs exhibit distinct forgetting profiles from larger models — with higher susceptibility to intra-task interference and lower recovery from replay-based methods.

## Key Facts
- **Authors**: Paula, Thomas S.; Kupssinskü, Lucas S.; Barros, Rodrigo C.
- **Year**: 2026
- **arXiv**: [2606.27634](https://arxiv.org/abs/2606.27634)
- **Date**: 2026-06-26

## Key Contributions
- First systematic study of catastrophic forgetting in sequential SLM personalization on edge devices
- Introduces stability monitoring as an evaluation framework for per-session forgetting in SLM adapters
- Finds SLMs have distinct forgetting profiles from LLMs: higher intra-task interference, lower replay recovery
- Demonstrates that LoRA-rank and adapter placement significantly affect forgetting vs. plasticity tradeoffs in the sequential setting

## Related Papers
- [[elasticmem-latent-memory-as-a-learnable-resource-for-llm-agents-2605.30690]] — Edge SLM personalization complements elastic memory systems: both address resource-constrained agent adaptation over time
- [[attribution-guided-continual-learning-for-llms-2605.05285]] — CL for LLMs with attribution-guided regularization; this paper extends the CL problem to the SLM/edge setting with sequential user data
- [[dyna-dynamic-episodic-memory-networks-for-augmenting-large-language-models-with-temporal-knowledge-graphs-in-continuous-learning-2606.15778]] — Dynamic episodic memory for continuous learning; both address temporal knowledge persistence in CL settings
