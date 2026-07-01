---
title: "ThinkProbe: Beyond Accuracy — Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning-evaluation, benchmarking, interpretability]
sources: ["https://arxiv.org/abs/2606.29067"]
---

# ThinkProbe: Beyond Accuracy — Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs

## Overview
ThinkProbe introduces a structural analysis framework for LLM reasoning traces, converting each trace into a Thought Graph (8 node types, 6 edge types) and deriving a 19-metric five-dimensional cognitive profile (5D-CP: Breadth, Depth, Structure, Metacognitive, Efficiency). Applied to 4,200 traces from 7 reasoning models, it reveals that reasoning structure is a stable model-level property — between-model variance exceeds between-domain variance by up to 4x across four of five cognitive dimensions. Structure shows genuine sensitivity to question domain, exposing cognitive profiles invisible to accuracy-based evaluation alone.

## Key Facts
- **arXiv**: [2606.29067](https://arxiv.org/abs/2606.29067)

## Key Contributions
- Converts LLM reasoning traces into Thought Graphs with 8 node types and 6 edge types
- Derives 19-metric five-dimensional cognitive profile (5D-CP) via non-generative pipeline
- Reveals reasoning structure is a stable model-level property (between-model variance > between-domain variance)
- Exposes structurally distinct cognitive profiles invisible to accuracy-based evaluation
- Provides structural sensitivity to question domain not captured by accuracy metrics

## Related Papers
- [[fork-think-with-confidence-parallel-reasoning-via-confidence-based-forking-2606.31484]] — Fork-Think optimizes reasoning efficiency at test time; ThinkProbe provides the evaluation framework to measure structural reasoning properties
- [[concise-training-free-conclusion-chain-state-compression-for-cost-efficient-multi-step-rag-2606.28361]] — ConCise compresses RAG reasoning state; ThinkProbe profiles the structure of the reasoning process itself
