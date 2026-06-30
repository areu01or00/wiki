---
title: "Belief at Risk: Quantifying Agentic AI Model Risk with LLM-Inferred Bayesian State Filters"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [agentic-ai, risk-quantification, bayesian, pomdp, uncertainty]
sources: ["https://arxiv.org/abs/2606.15473"]
---

# Belief at Risk: Quantifying Agentic AI Model Risk with LLM-Inferred Bayesian State Filters

## Overview
This paper develops a formal mathematical framework for quantifying **agentic AI model risk** — the risk that uncertain beliefs in autonomous AI systems lead to dangerous actions when coupled with control decisions. The key insight is that agentic AI creates a unique risk profile: unlike static deployment, autonomous systems couple belief states to action consequences, requiring risk quantification that accounts for temporal belief propagation and tail-risk functionals. The main contribution connects POMDP theory, Bayesian filtering, coherent risk measures, and quantitative portfolio risk management to construct a unified framework for agentic AI risk.

## Key Facts
- **Authors**: Chen, Y.; Zhang, W.; Rodriguez, A.; Kumar, R.
- **Year**: 2026
- **arXiv**: [2606.15473](https://arxiv.org/abs/2606.15473)

## Key Contributions
- First formal mathematical framework for **agentic AI model risk** — risk arising from uncertain beliefs coupled to autonomous actions
- POMDP formulation with **Bayesian belief updates** over latent states as the core risk propagation mechanism
- **LLM-inferred state filters** — using LLMs to infer latent belief states that are not directly observable
- Connection to **coherent risk measures** (CVaR, EVaR) from quantitative finance
- **Control-dependent loss functionals** — risk that is action-dependent, not just state-dependent
- Tail-risk quantification for autonomous AI deployment scenarios

## Related Papers
- [[agentic-world-modeling-foundations-capabilities-laws-and-beyond-2604.22748]] — Agentic World Modeling: Surveys the foundational primitives for agentic LLMs including world models, planning, and risk; Belief at Risk provides the quantitative risk framework complementing the descriptive foundations in this survey.
- [[probing-lack-of-stable-internal-beliefs-llms-2603.25187]] — Probing Lack of Stable Internal Beliefs: Studies LLM internal belief stability; Belief at Risk extends this to agentic action contexts where unstable beliefs have quantified consequences.
- [[oppo-bayesian-value-recursion-for-token-level-credit-assignment-in-llm-reasoning-2605.21851]] — OPPO Bayesian Value Recursion: Uses Bayesian recursion for credit assignment; Belief at Risk applies similar Bayesian recursion machinery to risk quantification in agentic systems.
- [[veribound-pac-bayesian-generalization-bounds-for-process-reward-models-trained-with-formal-verification-tools-2606.20740]] — VeriBound PAC-Bayesian Generalization: PAC-Bayesian bounds for PRMs; Belief at Risk uses Bayesian formalism for a different target — agentic risk rather than process reward.
