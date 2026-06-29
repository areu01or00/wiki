---
title: "Beyond Tokens: Concept-Level Training Objectives for LLMs"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [pretraining, llm, training-objective, semantic-abstraction]
sources: ["https://arxiv.org/abs/2601.11791"]
---

# Beyond Tokens: Concept-Level Training Objectives for LLMs

## Overview
Argues that next-token prediction (NTP) operates at the token level and treats deviations from a single reference continuation as errors even when alternative continuations are equally plausible or semantically equivalent (e.g., "mom" vs. "mother"), biasing models toward surface form rather than underlying meaning. Proposes a shift from token-level to concept-level prediction, where concepts group multiple surface forms of the same idea, and demonstrates that concept-aware models achieve lower perplexity, improved robustness under domain shift, and stronger performance than NTP-based models.

## Key Facts
- **Authors**: Iyer, Laya; Somani, Pranav; Guo, Alice; Jurafsky, Dan; Shani, Chen
- **Year**: 2026
- **arXiv**: [2601.11791](https://arxiv.org/abs/2601.11791) (online 2026-01-21)

## Key Contributions
- Diagnoses a structural mismatch in NTP — token-level loss penalizes valid abstractions, paraphrases, or conceptually correct reasoning paths by treating "mom" and "mother" as different targets when they refer to the same concept, biasing models toward surface form rather than underlying meaning.
- Proposes a shift from token-level to concept-level prediction: concepts group multiple surface forms of the same idea (e.g., "mom," "mommy," "mother" → MOTHER), and the model is trained to predict the next concept rather than the next token.
- Introduces multiple methods for integrating conceptual supervision into LLM training, showing that concept-aware models achieve lower perplexity, improved robustness under domain shift, and stronger performance on diverse NLP benchmarks than NTP-based models.
- Surfaces *concept-level-supervision-as-semantic-replacement-primitive* as a structurally new axis of pretraining-objective design — distinct from NTP (token-level) and multi-token prediction (multiple future tokens at the output) because Concept-Level's load-bearing primitive is *semantic-grouping-as-supervision-target*, replacing surface-form targets with meaning-level targets that recover semantically-equivalent continuations.

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent-concept discoveries.
- [[nitp-next-implicit-token-prediction-for-llm-pre-training-2605.24956]] — Sibling Run 77 emerging-pretraining-objective probe: NITP is *representation-space continuous supervision* that augments token-level with continuous self-targets; Concept-Level is *semantic-replacement* that replaces token-level with concept-level targets. Together they bracket the post-NTP pretraining-objective landscape between token-level-augmentation (NITP) and token-level-replacement (Concept-Level) primitives.
- [[beyond-multi-token-prediction-pretraining-llms-with-future-summaries-2510.14751]] — Sibling Run 77 emerging-pretraining-objective probe: Future-Summary-Prediction is *long-term-future auxiliary head* that adds a future-summary channel to NTP; Concept-Level is *semantic-replacement* that swaps tokens for concepts in the supervision target. Together they bracket the post-NTP pretraining-objective landscape between future-summary-augmentation (FSP) and semantic-replacement (Concept-Level) primitives.