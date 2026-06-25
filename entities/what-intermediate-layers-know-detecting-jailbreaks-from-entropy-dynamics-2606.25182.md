---
title: "What Intermediate Layers Know: Detecting Jailbreaks from Entropy Dynamics"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [jailbreak-detection, safety, interpretability, entropy, intermediate-layers]
sources: ["https://arxiv.org/abs/2606.25182"]
---

# What Intermediate Layers Know: Detecting Jailbreaks from Entropy Dynamics

## Overview
This paper introduces an entropy-dynamics probe over intermediate transformer layers for detecting jailbreak attempts before they reach the final output distribution. The authors observe that adversarial prompts induce characteristic *entropy trajectories* across middle layers — abrupt compression followed by late-layer divergence — that are statistically distinguishable from benign prompt behavior. A lightweight classifier trained on these trajectories achieves strong jailbreak-detection performance at substantially lower latency than output-space refusal classifiers or LLM-judge cascades.

## Key Facts
- **Authors**: Nikolenko, Sofiia; Papucci, Michele; Rezaei, Mina
- **Year**: 2026
- **arXiv**: [2606.25182](https://arxiv.org/abs/2606.25182)
- **Subjects**: cs.CL

## Key Contributions
- Identifies a reproducible *entropy-dynamics signature* of adversarial prompts across intermediate layers: a mid-layer entropy drop (information crystallization) followed by a late-layer entropy rise (output-space evasion) that benign prompts rarely exhibit.
- Trains a small MLP probe on per-layer entropy statistics (mean, variance, gradient) that detects jailbreak attempts at >90% AUROC across 5 jailbreak families (GCG, PAIR, ArtPrompt, multilingual, cipher-based) without inspecting the final output token.
- Demonstrates that the probe can be deployed as a *pre-generation* guard — it inspects hidden states from a forward pass truncated at layer N/2, avoiding the cost of full-sequence decoding for detected adversarial inputs.
- Reports cross-model transfer: probes trained on one open-weight LLM family retain >80% of their detection performance when applied to models from a different family with shared tokenizer vocabulary, suggesting the entropy signature is partly vocabulary-induced.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 as a fresh 2026 contribution to LLM safety, jailbreak detection, and mechanistic interpretability.
