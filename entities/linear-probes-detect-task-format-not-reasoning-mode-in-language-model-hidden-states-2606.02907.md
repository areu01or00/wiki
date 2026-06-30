---
title: "Linear Probes Detect Task Format, Not Reasoning Mode, in Language Model Hidden States"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [interpretability, representation-geometry, llm]
sources: ["https://arxiv.org/abs/2606.02907"]
---

# Linear Probes Detect Task Format, Not Reasoning Mode, in Language Model Hidden States

## Overview
Linear probing is widely used to claim that LLMs learn distinct geometric representations for different reasoning types. This paper rigorously tests that claim using Qwen3-14B on deductive, inductive, and abductive benchmarks — finding that apparent geometric separation is entirely driven by format confounds, not reasoning-mode representations.

## Key Facts
- **Authors**: Subramanyam Sahoo, Vinija Jain, Aman Chadha, Divya Chaudhary
- **Year**: 2026
- **arXiv**: [2606.02907](https://arxiv.org/abs/2606.02907)

## Key Contributions
- Rigorously tested linear probing for reasoning-mode detection across deductive/inductive/abductive benchmarks
- Found that geometric separation is entirely driven by task-format confounds, not genuine reasoning-mode structure
- Introduced residualization controls to isolate true reasoning geometry from format artifacts
- First paper demonstrating that linear-probe geometry does NOT track reasoning mode in LLM hidden states

## Related Papers
- [[emergent-causal-geometric-dynamics-across-depth-in-large-language-models-2602.04931]] — Geometric representation analysis in LLM depth layers (prior work this extends)
