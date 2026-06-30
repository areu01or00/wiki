---
title: "Accordion-Thinking: Self-Regulated Step Summaries for Efficient and Readable LLM Reasoning"
created: "2026-07-04"
updated: "2026-07-04"
type: entity
tags: [inference-efficiency, reasoning, chain-of-thought]
sources: ["https://arxiv.org/abs/2602.03249"]
---

# Accordion-Thinking: Self-Regulated Step Summaries for Efficient and Readable LLM Reasoning

## Overview
Accordion-Thinking addresses the KV-cache and attention quadratic complexity bottleneck in long Chain-of-Thought reasoning by enabling LLMs to self-regulate step granularity through dynamic summarization. The model learns to compress less-critical reasoning steps while preserving detailed computation on critical inference junctures.

## Key Facts
- **Authors**: Zhicheng Yang
- **Year**: 2026
- **arXiv**: [2602.03249](https://arxiv.org/abs/2602.03249)

## Key Contributions
- First end-to-end framework for self-regulated CoT step granularity via dynamic summarization
- Reduces KV-cache size and attention cost while maintaining reasoning accuracy
- Enables readable output by preserving natural step boundaries in compressed representations
- Works across diverse reasoning domains (math, logic, code generation)

## Related Papers
- [[lanerope-positional-encoding-collaborative-parallel-reasoning-generation-2605.27570]] — LaneRoPE: Positional Encoding for Collaborative Parallel Reasoning (test-time efficiency theme, different mechanism — KV reuse across branches)
- [[prune-you-generate-online-rollout-pruning-faster-better-2603.24840]] — Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR (test-time efficiency theme, different mechanism — policy pruning vs step summarization)
- [[emergent-concepts]] — Emergent Concepts parent page
