---
title: "SimpleSearch-VL: A Simple Recipe for Multimodal Agentic Deep Search"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multimodal, agent, retrieval, benchmark]
sources: ["https://arxiv.org/abs/2606.31504"]
---

# SimpleSearch-VL: A Simple Recipe for Multimodal Agentic Deep Search

## Overview
SimpleSearch-VL is an efficient multimodal agentic search framework that improves the agent's own search-and-verification process without scaling data, tools, or auxiliary model components. It combines Factorized Adaptive Rollout (FAR) for sampling efficiency with explicit chain-of-thought verification for evidence assessment. Achieves 15-16 average point improvements on Qwen3-VL agentic baselines with only 5K supervised trajectories + 2K RL data, and competitive performance with Gemini-3-Pro.

## Key Facts
- **Authors**: Dai, Ming; Lu, Zhihong; Gu, Jinjie + 5
- **Year**: 2026
- **arXiv**: [2606.31504](https://arxiv.org/abs/2606.31504)
- **Date**: 2026-06-30

## Key Contributions
- Factorized Adaptive Rollout (FAR): forms informative training groups while using redundant samples to expose hard examples
- Evidence-verified reasoning: explicit CoT verification of retrieved visual and textual cues against query context
- Lightweight tool interface with webpage self-summary — no external dependencies
- 5K supervised + 2K RL data achieves strong agentic baselines; matches Gemini-3-Pro at 30B-A3B scale

## Related Papers
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — Chain-of-thought learnability and verification
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — Agentic CoT steering
- [[agent-skill-evaluation-and-evolution-frameworks-benchmarks-2606.11435]] — Agent skill evaluation benchmarks
