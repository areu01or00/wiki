---
title: "MemLearner: Learning to Query Context Memory for Video World Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [world-model, memory, video-generation, llm]
sources: ["https://arxiv.org/abs/2606.31734"]
---

# MemLearner: Learning to Query Context Memory for Video World Models

## Overview
Video World Models predict future world states from user actions and history frames but suffer from memory inconsistency over extended durations. MemLearner addresses this by learning an adaptive context query mechanism using query tokens that bridge context and predicted tokens. The method leverages the video generation model's own pre-trained visual priors for context querying, without training additional modules from scratch. Evaluated on long videos with occlusions and dynamic objects, MemLearner significantly outperforms prior world models in scene consistency and memory quality.

## Key Facts
- **Authors**: Anonymous (arXiv:2606.31734)
- **Year**: 2026
- **arXiv**: [2606.31734](https://arxiv.org/abs/2606.31734)

## Key Contributions
- **Learned adaptive context query**: query tokens bridge context frames and predicted tokens — learns which context to retrieve rather than using rule-based fixed-window retrieval
- **Pre-trained visual priors reuse**: leverages the video generation model's own representations for context querying, avoiding additional module training from scratch
- **Occlusion and dynamic object handling**: trained on long videos with scene occlusions and dynamic objects paired with camera pose annotations; multi-dataset strategy uses both annotated rendered and unannotated real-world videos
- **Memory consistency improvement**: significantly outperforms prior video world models in scene consistency and memory quality under challenging occlusion and dynamic scenarios
- **First learned query-based memory for video world models**: prior methods used fixed retrieval windows; MemLearner is the first to learn what to remember from context in a world model

## Related Papers
- [[worldevolver-self-evolving-world-models-for-llm-agent-planning-2606.30639]] — WorldEvolver focuses on self-evolving world models for agent planning; MemLearner addresses the foundational memory consistency problem that enables such agents to operate over long horizons
- [[specgen-accelerating-agentic-kernel-optimization-with-speculative-generation-2606.17518]] — SpecGen accelerates agentic kernel optimization via speculative generation; MemLearner provides the memory infrastructure that long-horizon agents need for consistent scene reasoning
