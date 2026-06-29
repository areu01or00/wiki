---
title: "Mutual Reinforcement Learning: Experience Sharing Across Heterogeneous LLM Policies"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reinforcement-learning, multi-agent, post-training, llm, experience-sharing, cross-agent-teaching]
sources: ["https://arxiv.org/abs/2605.07244"]
---

# Mutual Reinforcement Learning: Experience Sharing Across Heterogeneous LLM Policies

## Overview
We introduce Mutual Reinforcement Learning, a framework for concurrent RL post-training in which heterogeneous LLM policies exchange typed experience while keeping separate parameters, objectives, and tokenizers. The framework combines a Shared Experience Exchange (SEE), Multi-Worker Resource Allocation (MWRA), and a Tokenizer Heterogeneity Layer (THL) that retokenizes text and aligns token-level traces across incompatible vocabularies. This substrate makes the experience-sharing design question operational across model families.

## Key Facts
- **Authors**: not extracted
- **Year**: 2026
- **arXiv**: [2605.07244](https://arxiv.org/abs/2605.07244)

## Key Contributions
- Introduces the **tokenizer-heterogeneity-aware peer-teaching substrate** for LLM post-training — for the first time in the wiki, peer teaching is operationalized across heterogeneous LLM families with different vocabularies
- Defines three controlled peer-teaching probes on top of GRPO: Peer Rollout Pooling (PRP) at the data level, Cross-Policy GRPO Advantage Sharing (XGRPO) at the value level, and Success-Gated Transfer (SGT) at the outcome level
- Derives a contextual-bandit stability-support trade-off characterization: PRP pays density-ratio variance + THL residual costs, XGRPO preserves on-policy actor support while changing scalar baselines, and SGT supplies a rescue-set score direction toward verified peer successes
- Demonstrates that **outcome-level success transfer (SGT)** occupies the favorable point of the trade-off in the evaluated regime — a peer-teaching design principle distinct from data-level or value-level sharing

## Related Papers
- [[synapse-federated-tool-routing-via-typed-compendium-artifacts-2602.00911]] — Sibling Run-92 collaborative-learning pick that established typed federated artifacts with per-field DP for cross-client routing; MRL extends the typed-artifact idea to RL post-training across heterogeneous LLM tokenizers
- [[supervised-fine-tuning-versus-reinforcement-learning-a-study-of-post-training-methods-for-large-language-models-2603.13985]] — Unified SFT/RL post-training framework (Run-60 pick) that MRL extends with cross-model-family peer teaching
- [[on-the-generalization-gap-in-self-evolving-language-model-reasoning-2606.01075]] — Theoretical self-evolving analysis whose single-model self-improvement framing MRL extends with explicit peer teaching across model families