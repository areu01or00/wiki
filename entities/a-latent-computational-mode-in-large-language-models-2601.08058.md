---
title: "A Latent Computational Mode in Large Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [interpretability, sparse-autoencoder, latent-reasoning, mechanistic, reasoning]
sources: ["https://arxiv.org/abs/2601.08058"]
---

# A Latent Computational Mode in Large Language Models

## Overview
Analyzes LLM internal representations with Sparse Autoencoders (SAEs) to identify a small set of latent features that are causally associated with reasoning behavior. Shows that **steering a single reasoning-related latent feature** can match CoT-prompted accuracy while producing shorter outputs, and that this internal reasoning state can **override prompt-level instructions discouraging explicit reasoning**. Argues multi-step reasoning is supported by latent internal activations that can be externally activated — CoT is one effective but not unique way to trigger them.

## Key Facts
- **Authors**: He, Zhenghao; Xiong, Guangzhi; Liu, Bohan; Sinha, Sanchit; Zhang, Aidong
- **Year**: 2026
- **arXiv**: [2601.08058](https://arxiv.org/abs/2601.08058)
- **Online date**: 2026-01-12

## Key Contributions
- **SAE-discovered latent-reasoning-feature primitive**: a small set of SAE features are causally associated with LLM reasoning across multiple model families and benchmarks, isolating reasoning to a mechanistically localizable substrate rather than emergent from prompt context alone
- **Single-feature steering matches CoT-prompted accuracy** without explicit CoT prompting, demonstrating that reasoning is triggered by *internal state activation* not by *verbalization*
- **Latent-state-overrides-prompt primitive**: the reasoning-related internal state activates *early in generation* and can override prompt-level instructions that discourage explicit reasoning — i.e., a learned behavioral attractor stronger than prompt conditioning
- **CoT-as-activation-trigger-not-cause primitive**: reframes CoT from "necessary mechanism for reasoning" to "one effective activation pathway" — opens up non-CoT reasoning primitives (latent steering) as a research direction
- **More efficient outputs from latent steering**: for large models, latent steering achieves CoT-comparable accuracy with shorter outputs — efficiency primitive beyond just capability

## Related Papers
- [[interpretability-can-be-actionable-2605.11161]] — Actionability-evaluates-interpretability primitive: this paper's SAE-located-reasoning-feature passes the concreteness×validation bar
- [[secret-mixtures-of-experts-inside-your-llm-2512.18452]] — Sibling discovery that locates MoE behavior inside dense MLPs; together they establish *internal-mechanistic-isolation* as a recurring interpretability primitive
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — External steering of CoT for controllability; this paper isolates the *internal* steering substrate that makes such control possible
- [[reasoninglens-hierarchical-visualization-and-diagnostic-auditing-for-large-reasoning-models-2606.23404]] — Trace-level diagnostic of reasoning failures; this paper identifies the *latent* substrate that ReasoningLens traces externally verbalize
- [[when-the-chain-of-thought-knows-better-failure-modes-in-multi-turn-reasoning-models-2606.10740]] — CoT vs Output 2×2 matrix in multi-turn safety; this paper shows CoT is *not* the only way to surface latent reasoning in the first place
- [[hidden-thoughts-are-not-secret-reasoning-trace-exposure-in-llms-2606.00642]] — Hidden CoT trace exposure; this paper shows internal reasoning state can be activated *without* CoT verbalization