---
title: "Energy-Based Fine-Tuning of Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [energy-based-model, fine-tuning, language-model, sequence-level-supervision, on-policy, feature-matching]
sources: ["https://arxiv.org/abs/2603.12248"]
---

# Energy-Based Fine-Tuning of Language Models

## Overview
Introduces EBFT (energy-based fine-tuning), a fine-tuning objective for language models that targets sequence-level statistics of the completion distribution rather than next-token prediction under teacher forcing. Uses strided block-parallel sampling to generate multiple rollouts from nested prefixes concurrently, then performs on-policy policy-gradient updates based on aggregated feature embeddings.

## Key Facts
- **Authors**: Liu, Qiang; Park, Sungjin; Chen, Wei
- **Year**: 2026
- **arXiv**: [2603.12248](https://arxiv.org/abs/2603.12248)

## Key Contributions
- **Sequence-level feature-matching objective**: targets statistics of the completion distribution rather than token-level cross-entropy under teacher forcing, providing dense semantic feedback without a task-specific verifier or preference model
- **Strided block-parallel sampling**: enables efficient generation of multiple rollouts from nested prefixes concurrently, batching feature extraction across rollouts for tractable on-policy updates
- **Theoretical bridge**: connects EBFT to KL-regularized feature-matching and energy-based modeling, establishing it as a principled alternative to RLVR that doesn't require reward models
- **Empirical parity with RLVR**: across Q&A coding, unstructured coding, and translation, EBFT matches RLVR and outperforms SFT on downstream accuracy while achieving lower validation cross-entropy than both methods

## Related Papers
- [[gem-geometric-entropy-mixing-for-optimal-llm-data-curation-2605.26121]] — Sibling data-curation primitive (Geometric Entropy Mixing variational hypersphere curation) — EBFT inverts the role: instead of curating training data, EBFT curates the *target distribution* via energy-based feature matching
- [[beyond-reward-engineering-a-data-recipe-for-long-context-reinforcement-learning-2606.18831]] — Sibling data-recipe-for-RL primitive — EBFT offers the post-training objective alternative that removes the reward model requirement entirely
- [[scaling-rl-for-code-generation-with-synthetic-data-and-curriculum-2603.24202]] — Sibling from Run 70 — both sequence-level objectives, EBFT complements synthetic-data curriculum with a verifier-free on-policy primitive
