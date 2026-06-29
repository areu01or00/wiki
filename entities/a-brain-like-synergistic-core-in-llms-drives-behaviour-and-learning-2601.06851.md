---
title: "A Brain-like Synergistic Core in LLMs Drives Behaviour and Learning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [information-geometry, mechanistic-interpretability, llm-theory]
sources: ["https://arxiv.org/abs/2601.06851"]
---

# A Brain-like Synergistic Core in LLMs Drives Behaviour and Learning

## Overview
Decomposes the information content of activations across model components in multiple LLM families using Partial Information Decomposition (PID), revealing a brain-like architecture where middle-layer components carry synergy (information only available through joint integration) while early and late layers rely on redundancy — and shows that ablating the synergistic core proportionally degrades both outputs and downstream learning.

## Key Facts
- **Authors**: Pedro Urbina-Rodriguez, Zafeirios Fountas, Fernando E. Rosas, Jun Wang, Andrea I. Luppi, Haitham Bou-Ammar, Murray Shanahan, Pedro A. M. Mediano
- **Year**: 2026
- **arXiv**: [2601.06851](https://arxiv.org/abs/2601.06851)
- **Submission date**: 11 Jan 2026

## Key Contributions
- **First Partial Information Decomposition (PID) characterization of LLM internal activations across multiple model families** — applies Williams–Beer redundancy and synergy decompositions (I(red), I(syn)) to layer- and component-wise activation distributions, surfacing synergy ↔ redundancy structure that maps onto the brain's integrative-core / peripheral-overhead split.
- **Synergistic core localized to middle layers across architectures** — early layers (token-level / embedding-driven) and late layers (output-projection-driven) are redundancy-dominated; middle layers carry the synergy the model needs to integrate disparate contextual cues.
- **Empirical causal validation**: perturbing the synergistic core causes the largest behavioral / predictive drop; perturbing the redundant core has the smallest effect — converting a *descriptive* PID measurement into an *interventional* information-geometric primitive.
- **Learning-phase parallels with biological systems**: the synergistic-core architecture appears stable across fine-tuning, mirroring mammalian cortex-versus-peripheral ratios in information integration.
- **Information-geometric primitive for mechanistic interpretability**: extends conceptual-bottleneck analyses (Local-Causal-Attribution, Latent-Computational-Mode) by replacing gradient-based feature attribution with information-theoretic *synergy magnitude* as the load-bearing primitive.

## Related Papers
- [[early-warning-signals-of-grokking-via-loss-landscape-geometry-2602.16967]] — Loss-landscape geometry primitive that shares information-geometry framing over parameter space.
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Local-information-score primitive layered inside transformers; complementary to the synergy-geometry decomposition here.
- [[formalizing-latent-thoughts-four-axioms-of-thought-representation-in-llms-2606.27378]] — Latent-thought axiomatization of LLM internal representations that the synergistic-core architecture instantiates empirically.
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Mixture-of-experts task-routing as another information-flow-based primitive over LLM components.
- [[memory-for-autonomous-llm-agents-mechanisms-evaluation-emerging-frontiers-2603.07670]] — Agent-memory architecture that the synergistic-core decomposition predicts should localize its synergy in specific layer windows.
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — SAE-isolated latent-reasoning primitive that the synergistic-core finding re-frames in information-geometric (PID) rather than feature-decomposition terms.
