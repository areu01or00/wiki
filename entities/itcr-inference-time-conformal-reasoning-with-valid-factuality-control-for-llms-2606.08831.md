---
title: "Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [uncertainty-quantification, reasoning, conformal-prediction, llm]
sources: ["https://arxiv.org/abs/2606.08831"]
---

# Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models

## Overview
Large language models increasingly perform multi-step reasoning where intermediate claims form implicit directed acyclic graphs whose correctness is structurally conditioned on ancestors. This makes factuality uncertainty structural, not a trivial accumulation of node-wise errors. ITCR integrates conformal prediction directly into reasoning graph generation, learning a structure-level factuality uncertainty function that aggregates claim-level signals over reasoning DAGs without complex modeling assumptions.

## Key Facts
- **Authors**: Ting Wang, Yuanjie Shi, Yan Yan, Huan Zhang
- **Year**: 2026
- **arXiv**: [2606.08831](https://arxiv.org/abs/2606.08831)
- **Subject**: Artificial Intelligence (cs.AI)
- **Submitted**: 7 Jun 2026
- **Venue**: Accepted at ICML 2026

## Key Contributions
- **Structure-level factuality UQ**: Learns a graph-level factuality uncertainty function aggregating claim-level signals over reasoning DAGs without complex modeling assumptions
- **Conformal threshold for generation**: Designs non-conformity score based on graph-level factuality uncertainty; calibrates conformal threshold to decide when to stop generation
- **Nested generation with valid coverage**: Theoretically shows generation is nested, yielding valid coverage guarantees for factuality control
- **Inference-time intervention**: Unlike post-hoc CP methods, ITCR intervenes during generation — more accurate than post-hoc pruned graphs

## Related Papers
- [[coft-counterfactual-conformal-decoding-fair-chain-of-thought-2605.30641]] — COFT: counterfactual-conformal decoding for fair CoT — shares conformal prediction methodology but orthogonal (COFT is token-level post-hoc, ITCR is structure-level during generation)
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Between-the-Layers: intra-layer uncertainty estimation via local information scores — orthogonal axis (attention-level hidden state vs reasoning graph structure)
- [[uncertainty-quantification-for-hallucination-detection-in-llms-2510.12040]] — UQ for hallucination detection — orthogonal axis (UQ for factuality vs UQ for hallucination)
