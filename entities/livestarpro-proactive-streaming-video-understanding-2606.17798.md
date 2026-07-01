---
title: "LiveStarPro: Proactive Streaming Video Understanding with Hierarchical Memory for Long-Horizon Streams"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [video-llm, streaming, memory, long-horizon]
sources: ["https://arxiv.org/abs/2606.17798"]
---

# LiveStarPro: Proactive Streaming Video Understanding with Hierarchical Memory for Long-Horizon Streams

## Overview
LiveStarPro is a live streaming assistant designed for proactive video understanding over long-horizon streams. It addresses three key challenges simultaneously: processing continuous video streams in real-time, deciding autonomously when to respond, and preserving long-horizon contextual memory. Key innovations include Streaming Verification Decoding (SVeD), Streaming Causal Attention Masks (SCAM), and Tree-Structured Hierarchical Memory (TSHM).

## Key Facts
- **Authors**: [Authors on arXiv]
- **Year**: 2026
- **arXiv**: [2606.17798](https://arxiv.org/abs/2606.17798)

## Key Contributions
- Streaming Verification Decoding (SVeD): single-pass perplexity verification for response timing without explicit silence tokens
- Streaming Causal Attention Masks (SCAM): incremental video-language alignment over variable-length streams
- Tree-Structured Hierarchical Memory (TSHM): recursive memory architecture for efficient retrieval from unbounded video streams
- 28.9% improvement in semantic correctness and 18.2% reduction in timing error; 1.58x inference speedup via KV cache optimization
