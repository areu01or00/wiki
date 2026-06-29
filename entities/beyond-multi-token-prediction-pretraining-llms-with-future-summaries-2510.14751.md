---
title: "Beyond Multi-Token Prediction: Pretraining LLMs with Future Summaries"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [pretraining, llm, training-objective, long-range-dependencies]
sources: ["https://arxiv.org/abs/2510.14751"]
---

# Beyond Multi-Token Prediction: Pretraining LLMs with Future Summaries

## Overview
Argues that next-token prediction (NTP) struggles with long-horizon reasoning, planning, and creative writing because of teacher-forced training, and that multi-token prediction (MTP) only partially mitigates this by capturing short-range dependencies. Proposes future summary prediction (FSP) — an auxiliary head trained to predict a compact representation of the long-term future, preserving information relevant for long-form generations.

## Key Facts
- **Authors**: Mahajan, Divyat; Goyal, Sachin; Idrissi, Badr Youbi; Pezeshki, Mohammad; Mitliagkas, Ioannis; Lopez-Paz, David; Ahuja, Kartik
- **Year**: 2026 (ICLR 2026)
- **arXiv**: [2510.14751](https://arxiv.org/abs/2510.14751) (online 2026-03-25, submitted 2025-10-16)

## Key Contributions
- Diagnoses a structural limitation of NTP — long-horizon reasoning, planning, and creative writing suffer under teacher-forced training — and of MTP — it captures short-range dependencies but offers limited improvement on long-range tasks.
- Introduces Future Summary Prediction (FSP): an auxiliary head predicts a compact representation of the long-term future, preserving information relevant for long-form generations. Two variants: handcrafted summaries (e.g., bag-of-words summary of the future sequence) and learned summaries (embeddings from a reverse language model trained right-to-left).
- Demonstrates via large-scale pretraining experiments (3B and 8B parameters) that FSP improves over both NTP and MTP across math, reasoning, and coding benchmarks.
- Surfaces *future-summary-prediction-as-auxiliary-head-pretraining-objective primitive* as a structurally new axis of pretraining-objective design — distinct from NTP (token-level) and MTP (multi-token-output) because FSP's load-bearing primitive is *long-term-future-summary-via-auxiliary-head*, providing an information channel from the future that is not collapsed through teacher-forcing.

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent-concept discoveries.
- [[nitp-next-implicit-token-prediction-for-llm-pre-training-2605.24956]] — Sibling Run 77 emerging-pretraining-objective probe: NITP is *in-representation continuous supervision via shallow-layer self-targets* — augments NTP from inside the model with representation-space targets; Future-Summary-Prediction is *auxiliary-head future-summary prediction* — augments NTP from outside via an auxiliary head. Together they bracket the post-NTP pretraining-objective landscape between in-representation augmentation (NITP) and auxiliary-head augmentation (FSP) primitives.
- [[beyond-tokens-concept-level-training-objectives-for-llms-2601.11791]] — Sibling Run 77 emerging-pretraining-objective probe: Concept-Level is a *higher-level semantic grouping* primitive that replaces token-level with concept-level supervision; Future-Summary-Prediction is a *long-term-future auxiliary head* primitive that augments NTP with future-summaries at the output level. Together they bracket the post-NTP pretraining-objective landscape between semantic-replacement (Concept-Level) and future-summary-augmentation (FSP) primitives.