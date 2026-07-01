---
title: "ConCise: Training-Free Conclusion-Chain State Compression for Cost-Efficient Multi-Step RAG Services"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [RAG, inference-efficiency, KV-cache]
sources: ["https://arxiv.org/abs/2606.28361"]
---

# ConCise: Training-Free Conclusion-Chain State Compression for Cost-Efficient Multi-Step RAG Services

## Overview
ConCise is a training-free state-layer protocol that restructures cross-round context transmission for multi-step RAG services. It replaces raw-text accumulation with an append-only chain of structured conclusions, compressing cumulative context growth from O(N²) to approximately O(N). A fused generation mechanism jointly emits reasoning and conclusions in a single API call, eliminating repeated input billing from serial dual-invocation overhead. Achieves 64.63% average token savings while maintaining acceptable accuracy across 12 paired configurations spanning 3 models and 2 datasets.

## Key Facts
- **arXiv**: [2606.28361](https://arxiv.org/abs/2606.28361)

## Key Contributions
- Training-free state compression replacing raw-text accumulation with structured conclusion chains
- Reduces cumulative context growth from O(N²) to O(N) for multi-step RAG
- Fused generation mechanism: joint reasoning + conclusion emission in single API call
- 64.63% average token savings while maintaining acceptable accuracy
- Deployment-friendly: no pretrained modules or GPU-level KV cache access required (unlike KV cache compression approaches)
- Compatible with API-native, Serverless, and edge-side deployments

## Related Papers
- [[fork-think-with-confidence-parallel-reasoning-via-confidence-based-forking-2606.31484]] — Both target LLM inference cost reduction via different mechanisms (Fork-Think: parallel reasoning efficiency; ConCise: RAG state compression)
- [[thinkprobe-structural-profiling-of-llm-reasoning-traces-via-thought-graphs-2606.29067]] — ThinkProbe profiles reasoning structure; ConCise compresses the context carrying that reasoning across RAG rounds
