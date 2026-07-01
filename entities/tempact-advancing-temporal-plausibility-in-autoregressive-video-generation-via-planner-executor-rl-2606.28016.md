---
title: "TempAct: Advancing Temporal Plausibility in Autoregressive Video Generation via Planner-Executor RL"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [temporal-reasoning, video-generation, autoregressive-model, planner-executor, llm]
sources: ["https://arxiv.org/abs/2606.28016"]
---

# TempAct: Advancing Temporal Plausibility in Autoregressive Video Generation via Planner-Executor RL

## Overview
TempAct tackles the temporal ambiguity problem in autoregressive video diffusion: chunk-by-chunk video synthesis with cached visual context makes it unclear which sub-event from a global prompt should be realized in each chunk. The paper proposes a Planner-Executor RL framework where a planner module decomposes global temporal instructions into chunk-level sub-goals, and an executor module generates each chunk conditioned on its assigned sub-goal, ensuring temporal plausibility across chunks.

## Key Facts
- **Authors**: Wang, Jing; Zhou, Xiangxin; Liang, Jiajun + 6 more
- **Year**: 2026
- **arXiv**: [2606.28016](https://arxiv.org/abs/2606.28016)
- **Online Date**: 2026-06-26

## Key Contributions
- Planner-Executor RL architecture separating temporal planning from chunk-level video execution, resolving the temporal instruction ambiguity inherent in AR video diffusion
- Novel sub-goal decomposition mechanism that maps a global video prompt to temporal sub-event specifications per chunk
- Demonstrates that temporal planning primitives developed for LLM agents can transfer to video generation, suggesting a broader class of planner-executor architectures

## Related Papers
- [[causal-rcm-a-unified-teacher-forcing-and-self-forcing-open-recipe-for-autoregressive-diffusion-distillation-in-streaming-video-generation-and-interactive-world-models-2606.25473]] — Autoregressive diffusion for video generation and world models
- [[bridging-videoqa-and-video-guided-agentic-tasks-via-generalized-keyframe-extraction-2606.29445]] — Video-guided agentic tasks
- [[causal-reward-world-models-zero-shot-skill-generation-2606.23280]] — Planner-executor skill generation architecture (sibling primitive)
