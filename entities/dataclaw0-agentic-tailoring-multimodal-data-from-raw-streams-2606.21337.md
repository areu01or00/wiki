---
title: "DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [data, multimodal, agents, llm-research, post-training, vlm]
sources: ["https://arxiv.org/abs/2606.21337"]
---

# DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams

## Overview
DataClaw0 reframes multimodal data preparation as an agentic capability rather than a heuristic pipeline, introducing the Agentic Data Tailoring paradigm where an AI agent actively refines and structures raw multimodal streams to align with downstream task intents. The authors train a 9B DataClaw_0 model via a two-stage pipeline (semantic synthesis grounded in deterministic Factual Anchors, then SFT + GRPO) and demonstrate that agent-tailored data delivers downstream quality gains on video generation, real-world VQA, and GUI navigation at a fraction of the cost of manual curation.

## Key Facts
- **Authors**: Wan, Cong; Guo, Zeyu; Cai, Zijian; Li, Jiangyang; Dong, SongLin; Peng, Lin; Luo, Xiangyang; Ma, Zhiheng; Gong, Yihong
- **Year**: 2026
- **Date**: 2026-06-19
- **arXiv**: [2606.21337](https://arxiv.org/abs/2606.21337)
- **Subjects**: Machine Learning (cs.LG)

## Key Contributions
- Agentic Data Tailoring paradigm that elevates data processing from heuristic pipelines to a learnable agent capability aligned with user/downstream intents
- Two-stage training pipeline combining generative semantic synthesis with deterministic Factual Anchors to overcome data scarcity for high-order data-refinement capabilities
- DataClaw_0-9B trained with SFT + Group Relative Policy Optimization (GRPO), demonstrating downstream improvements on video generation, VQA, and GUI navigation under limited-data regimes
- DataClaw_0-val, the first dedicated benchmark for data-refinement capability, validated against downstream post-training rather than only intrinsic metrics
- Evidence that "data entropy" in raw multimodal streams can be substantially reduced by an agent whose objective is downstream-task utility rather than reconstruction fidelity

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[autodata-an-agentic-data-scientist-to-create-high-quality-synthetic-data-2606.25996]] — Companion work showing that the data-generation side of the agentic loop can itself be agentic and meta-optimized
