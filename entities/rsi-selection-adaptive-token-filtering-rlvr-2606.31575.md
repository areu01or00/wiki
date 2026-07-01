---
title: "Which Tokens Matter? Adaptive Token Selection for RLVR with the Relative Surprisal Index"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [training, reinforcement-learning, llm, inference-efficiency, token-filtering]
sources: ["https://arxiv.org/abs/2606.31575"]
---

# Which Tokens Matter? Adaptive Token Selection for RLVR with the Relative Surprisal Index

## Overview
Identifies a key tension in RL with Verifiable Rewards (RLVR): prior work disagreed on whether high-entropy or low-probability tokens should dominate gradient updates. Introduces the Relative Surprisal Index (RSI) — an information-theoretic metric coupling token entropy with selected-token probability — and RSI-Selection (RSI-S), an entropy-adaptive filtering method that resolves the contradiction. Achieves 2–3pp improvement over GRPO on AIME/AMC across Qwen2.5-1.5B/3B/7B.

## Key Facts
- **arXiv**: [2606.31575](https://arxiv.org/abs/2606.31575)
- **Year**: 2026

## Key Contributions
- RSI: principled metric coupling entropy + probability (resolves prior RLVR disagreement on token prioritization)
- RSI-S: adaptive token filtering retaining only stable RSI-interval tokens (filters both low-surprisal redundancy and high-surprisal instability)
- Empirical validation: 2–3pp avg@32 improvement over GRPO on AIME/AMC across model scales
- First principled reconciliation of contradictory high-entropy vs low-probability token paradigms in RLVR
- Theoretical grounding: RSI related to first-order logit-gradient norm and predictive entropy under selected-logit perturbation

## Related Papers
- [[experience-augmented-policy-optimization-for-llm-reasoning-2606.30420]] — Experience distillation for LLM reasoning (RLVR training paradigm overlap)
