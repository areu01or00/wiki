---
title: "Discrete Causal Representations from Heterogeneous Domains: A Bayesian Approach with Social Survey Applications"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [causal-representation-learning, bayesian-methods, domain-shift, social-survey]
sources: ["https://arxiv.org/abs/2606.06288"]
---

# Discrete Causal Representations from Heterogeneous Domains: A Bayesian Approach with Social Survey Applications

## Overview
The paper addresses causal representation learning (CRL) from heterogeneous data sources — particularly social survey data where observations come from distinct domains with different measurement structures. The key insight is that causal variables must be identifiable even when the measurement model (how latent causes map to observations) varies across domains. The authors propose a Bayesian framework that jointly infers latent causal states and domain-specific measurement parameters, enabling discovery of shared causal structure across heterogeneous environments.

## Key Facts
- **Authors**: Garg, Ankur; Stettler, Michael; Schein, Aaron + 1
- **Year**: 2026
- **arXiv**: [2606.06288](https://arxiv.org/abs/2606.06288)

## Key Contributions
- Bayesian identification of discrete causal representations across heterogeneous domains (different measurement models per domain)
- Formal conditions under which latent causal variables remain identifiable when distribution shifts occur through sparse, localized causal mechanisms
- Application to social survey data where the same underlying attitudes are measured via different question formats across surveys
- Demonstrates that domain heterogeneity — rather than being a nuisance — can actually aid causal variable discovery by providing independent measurement constraints

## Related Papers
- [[causal-methods-for-llm-development-and-evaluation-2605.25998]] — Broader survey of causal methods applied to LLM development and evaluation, connecting the CRL framework to language model analysis
- [[causality-is-key-for-interpretability-claims-to-generalise-2602.16698]] — Foundational argument that causal structure is essential for interpretability claims to generalize across distributions
- [[causal-discovery-in-the-era-of-agents-2606.23608]] — CRL applied specifically in the agent context, where heterogeneous interaction data creates natural domain-shift scenarios for causal discovery
