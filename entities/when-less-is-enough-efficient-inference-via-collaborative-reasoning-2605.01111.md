---
title: "When Less is Enough: Efficient Inference via Collaborative Reasoning"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [inference-efficiency, reasoning, collaborative-inference]
sources: ["https://arxiv.org/abs/2605.01111"]
---

# When Less is Enough: Efficient Inference via Collaborative Reasoning

## Overview
DUET (Dual-model Efficient Two-stage inference) splits reasoning into two stages: a high-capacity model outputs a compact reasoning signal, and a lightweight model decodes it into the final response. This collaborative approach eliminates up to 50% of reasoning tokens while maintaining accuracy by preserving critical intermediate information that naive truncation would discard.

## Key Facts
- **Authors**: Chen, Yilei; Gupta, Sharut; Paschalidis, Yannis + 2 others
- **Year**: 2026
- **arXiv**: [2605.01111](https://arxiv.org/abs/2605.01111)

## Key Contributions
- Dual-model collaborative inference (DUET) architecture
- Compact reasoning signal extraction preserves critical intermediate tokens
- Up to 50% token reduction without accuracy degradation
- Demonstrates that not all reasoning tokens are equally important

## Related Papers
- [[selfbudgeter-adaptive-token-allocation-for-efficient-llm-reasoning-2505.11274]] — Self-adaptive token budgeting via self-estimation
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — Agentic chain-of-thought steering
- [[beyond-accuracy-decomposing-reasoning-efficiency-llms-2602.09805]] — Decomposes reasoning into accuracy and efficiency components
