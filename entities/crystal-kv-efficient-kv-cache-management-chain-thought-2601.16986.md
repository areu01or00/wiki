---
title: "Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [kv-cache, inference-efficiency, chain-of-thought]
sources: ["https://arxiv.org/abs/2601.16986"]
---

# Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle

## Overview
Crystal-KV addresses the excessive memory overhead of long CoT think-stage sequences in the KV cache. The key insight is the "answer-first principle": CoT emphasizes the final answer, rendering conventional uniform KV compression strategies ineffective. Crystal-KV maps answer preferences into think-stage attention maps, distinguishing between tokens that should be retained vs evicted, enabling lossless or minimal-loss KV cache compression for reasoning models.

## Key Facts
- **Authors**: Zihan Wang, Cheng Tang, Lei Gong, Cheng Li, Chao Wang, Teng Wang, Wenqi Lou, Xuehai Zhou
- **Year**: 2026
- **arXiv**: [2601.16986](https://arxiv.org/abs/2601.16986)

## Key Contributions
- Answer-first principle: CoT tokens are not uniform — the final answer token and its supporting reasoning chain have outsized importance
- Crystal-KV identifies answer-critical attention heads and applies differentiated eviction policies
- Achieves significant KV cache compression while maintaining CoT reasoning accuracy
- First KV cache management framework designed specifically for long-output reasoning models (o1/o3/R1-class)

## Related Papers
- [[self-regulated-agentic-reasoning-simulative-planning-2605.22138]] — SR²AM: Long CoT sequences enabled by Crystal-KV's memory efficiency
- [[polaris-typed-planning-governed-execution-agentic-ai-2601.11816]] — POLARIS: Typed DAG execution guards complement Crystal-KV's resource efficiency for deployed agents
