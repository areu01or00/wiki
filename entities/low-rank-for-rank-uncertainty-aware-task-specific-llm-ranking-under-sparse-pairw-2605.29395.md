---
title: "Low Rank for Rank: Uncertainty-Aware Task-Specific LLM Ranking under Sparse Pairwise Comparisons"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [evaluation, calibration, uncertainty, ranking, llm]
sources: ["https://arxiv.org/abs/2605.29395"]
---

# Low Rank for Rank: Uncertainty-Aware Task-Specific LLM Ranking under Sparse Pairwise Comparisons

## Overview
Pairwise human-preference platforms like Chatbot Arena have become central to LLM evaluation, but reliable task-specific ranking remains challenging with sparse comparisons. The paper proposes a low-rank structured uncertainty model that enables accurate task-specific LLM ranking even when pairwise comparison data is sparse — addressing the calibration gap between global leaderboard rankings and per-task model performance.

## Key Facts
- **Authors**: Li, Jiachun; Simchi-Levi, David; Sun, Will Wei
- **Year**: 2026
- **arXiv**: [2605.29395](https://arxiv.org/abs/2605.29395)

## Key Contributions
- Low-rank uncertainty model for task-specific LLM ranking under sparse pairwise comparisons
- Addresses the calibration gap between global leaderboard position and per-task performance
- Enables accurate model selection with fewer human preference annotations
- Framework applies to Chatbot Arena-style pairwise evaluation platforms

## Related Papers
- [[evirank-evidence-based-confidence-estimation-for-llm-based-ranking-2606.04727]] — Complementary approach to LLM ranking through evidence-based confidence estimation
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Uncertainty estimation via intra-layer local information scores, shared calibration methodology
