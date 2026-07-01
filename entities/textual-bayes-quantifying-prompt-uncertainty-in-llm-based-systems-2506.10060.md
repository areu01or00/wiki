---
title: "Textual Bayes: Quantifying Prompt Uncertainty in LLM-Based Systems"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [uncertainty-quantification, bayesian-methods, prompt-engineering, llm-inference]
sources: ["https://arxiv.org/abs/2506.10060"]
---

# Textual Bayes: Quantifying Prompt Uncertainty in LLM-Based Systems

## Overview
A novel framework treating LLM-based systems as Bayesian probabilistic models — quantifying uncertainty over both the model's textual parameters and downstream predictions, while incorporating prior beliefs expressed in free-form text. Published at ICLR 2026.

## Key Facts
- **Authors**: Textual Bayes team (ICLR 2026)
- **Year**: 2025
- **arXiv**: [2506.10060](https://arxiv.org/abs/2506.10060)

## Key Contributions
- Frames LLM-based systems as Bayesian models with textual parameters
- Quantifies prompt sensitivity via posterior predictive distributions
- Incorporates free-form text priors into uncertainty estimation
- Enables principled UQ for black-box LLM APIs without internal model access

## Related Papers
- [[position-uncertainty-quantification-in-llms-is-just-unsupervised-clustering-2605.19220]] — Foundational critique this work builds upon or responds to
- [[can-llm-rerankers-predict-their-own-ranking-performance-2606.03535]] — Self-meta-evaluation for LLM outputs
