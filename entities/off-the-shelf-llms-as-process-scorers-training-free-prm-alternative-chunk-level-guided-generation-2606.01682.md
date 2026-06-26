---
title: "Off-the-Shelf LLMs as Process Scorers: Training-Free Alternative to PRMs for Mathematical Reasoning"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [reasoning, prm, process-reward, inference-time, training-free, math, llm]
sources: ["https://arxiv.org/abs/2606.01682"]
---

# Off-the-Shelf LLMs as Process Scorers: Training-Free Alternative to PRMs for Mathematical Reasoning

## Overview
A training-free process-reward alternative for mathematical reasoning: a small generator model samples k fixed-length candidate chunks, while a stronger off-the-shelf LLM scores each chunk via likelihoods (without generating text). Two selection rules — Likelihood-Guided Selection (LGS) and Contrastive-Guided Selection (CGS) — steer small-model generation *before* errors can propagate. CGS matches or outperforms Qwen2.5-Math-PRM-72B guided search on most benchmarks without any reward-model training.

## Key Facts
- **Authors**: Chegini, Atoosa; Feizi, Soheil (and collaborators)
- **Year**: 2026
- **arXiv**: [2606.01682](https://arxiv.org/abs/2606.01682)
- **Online date**: 2026-06-04

## Key Contributions
- **Chunk-Level Guided Generation (CLGG)** — a training-free framework where a small model samples k fixed-length candidate chunks and a stronger LLM scores them via likelihoods, with the selected chunk committed before the next step. This decouples process scoring from reward-model training while still intervening *during* generation rather than after.
- **Length-bias diagnosis** — the paper identifies a systematic length bias in variable-length step scoring that persists even after length normalization, and shows fixed-length chunking avoids this confound. This is a structural finding about likelihood-based process scorers that matters for any future PRM-replacement work.
- **Contrastive-Guided Selection (CGS)** — subtracts the small model's log-probability from the large model's, favoring chunks where the large model diverges from the small. This bias-aware selection rule converts "off-the-shelf likelihood" into a discriminating signal and outperforms majority voting by up to 28 percentage points.
- **Strong empirical results without reward-model training** — Qwen2.5-7B guided by Qwen2.5-72B reaches 81.8% on MATH and 63.6% on Minerva Math at k=16, surpassing majority voting by 4–6 pp and matching PRM-guided search on most benchmarks. Production-relevant: shorter reasoning traces than PRM-guided search.

## Why this matters for the wiki
The first **training-free PRM replacement** in the wiki: it eliminates the expensive step-level-label collection that PRM training requires, while still intervening mid-generation rather than post-hoc. Distinct from Run 64's [reasoning-failure-mode-2-axis-taxonomy](#) (failure-mode-classification), Run 65's [SFT-vs-RL-unified-objective-framework](#) (training-side), and Run 56's [Agentic-Trading R0-R3 audit](#) (deployment-evaluation). The CGS contrastive-scoring rule is a structural counterpoint to existing reward-model-quality primitives — it says you don't need a trained PRM if your off-the-shelf LLM is large enough to score the small model's chunks.

## Related Papers
- [[discretizing-reward-models-2606.21795]] — Reward-model oversensitivity as structural failure mode; discretizing-reward-models and chunk-level-guided-generation both attack the "trained reward signal is brittle" failure mode but from opposite ends (post-training discretization vs training-free likelihood scoring)
- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — Local-branch routing for test-time scaling; sibling test-time-scaling primitive but routes branches via trained controller rather than chunk-level likelihood scoring
- [[efficientrollout-system-aware-self-speculative-decoding-for-rl-rollouts-2606.18967]] — System-aware speculative decoding for non-stationary RL rollouts; both papers attack "small model + large scorer" composition but in inference-time vs RL-rollout regimes