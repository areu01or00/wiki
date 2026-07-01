---
title: "Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, architecture, chain-of-thought, latent-reasoning]
sources: ["https://arxiv.org/abs/2606.31779"]
---

# Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers

## Overview
Language models typically reason via explicit chain-of-thought (CoT), generating intermediate steps token-by-token. Latent CoT performs multi-step reasoning in the model's hidden states instead. This paper introduces LOTUS (Looped Transformers with parallel supervision on latents), the first latent-CoT method that achieves performance competitive with explicit CoT. LOTUS bridges the gap by supervising latents in parallel rather than sequentially, enabling the model to learn multi-step reasoning without the compute cost of autoregressive token generation at each step.

## Key Facts
- **Authors**: Fan, Ying; Svete, Anej; Lee, Kangwook
- **Year**: 2026
- **arXiv**: [2606.31779](https://arxiv.org/abs/2606.31779)
- **Date**: 2026-06-30

## Key Contributions
- First latent-CoT method competitive with explicit CoT — resolves the long-standing gap between the two reasoning paradigms
- LOTUS architecture: parallel supervision on latent reasoning states instead of sequential token-level supervision
- Reduces the per-step compute cost of multi-step reasoning by keeping computation in hidden states rather than generating intermediate tokens
- Provides interpretability benefit: latent reasoning states can be inspected directly, unlike explicit token sequences

## Related Papers
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — CoT steering for controllable reasoning
- [[coft-counterfactual-conformal-decoding-fair-chain-of-thought-2605.30641]] — Conformal decoding for chain-of-thought fairness
