---
title: "Multi-Block Diffusion Language Models"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [llm, diffusion-models, language-generation, inference-efficiency, model-architecture]
sources: ["https://arxiv.org/abs/2606.29215"]
---

# Multi-Block Diffusion Language Models

## Overview
Block Diffusion Language Models (BD-LMs) improve diffusion-based text generation with KV caching and flexible-length generation. This paper extends them from Single-Block Diffusion (SingleBD) to Multi-Block Diffusion (MultiBD), where a running-set of consecutive blocks is decoded concurrently for inter-block parallelism. The key contribution is Multi-block Teacher Forcing (MultiTF), which integrates teacher forcing and diffusion forcing by training on bounded noise-groups conditioned on clean prefixes, with randomized noise-schedulers that better match MultiBD inference states. An optimized Block Buffer decoding algorithm achieves up to 2.7x wall-clock acceleration.

## Key Facts
- **Authors**: Unknown (per arxiv page)
- **Year**: 2026
- **arXiv**: [2606.29215](https://arxiv.org/abs/2606.29215)

## Key Contributions
- Multi-Block Diffusion (MultiBD) architecture enabling concurrent decoding of consecutive blocks for inter-block parallelism
- Multi-block Teacher Forcing (MultiTF) bridging the gap between training and inference states
- Block Buffer mechanism preserving prefix-cache reuse and static input shapes while achieving 9.34 TPF (tokens per forward pass)
- First multi-block concurrent decoding framework for diffusion language models in the wiki

## Related Papers
- [[reinforcement-learning-with-metacognitive-feedback-elicits-faithful-uncertainty-expression-in-llms-2606.32032]] — Sibling paper from same discovery run (Metacognitive Feedback for LLM uncertainty)
- [[ko-widesearch-a-korean-breadth-search-benchmark-for-exhaustive-set-enumeration-by-web-agents-2606.27595]] — Sibling paper from same discovery run (Korean Web Agent Benchmark)
