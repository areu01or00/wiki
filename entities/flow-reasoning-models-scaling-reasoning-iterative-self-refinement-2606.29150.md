---
title: "Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, discrete-flow-models, iterative-refinement, structured-problem-solving]
sources: ["https://arxiv.org/abs/2606.29150"]
---

# Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement

## Overview
Flow Reasoning Models apply discrete flow matching — a non-autoregressive generative framework — to structured reasoning tasks. By framing reasoning as a flow process over discrete states (e.g., Sudoku cells, logic constraints), the model learns to iteratively refine its solution trajectory. Self-conditioning at each step enables the model to verify partial solutions and guide the flow toward consistent final answers.

## Key Facts
- **Authors**: Helbling, Alec; Bryutkin, Andrey; Martino, Mauro + 2
- **Year**: 2026
- **arXiv**: [2606.29150](https://arxiv.org/abs/2606.29150)

## Key Contributions
- First application of discrete flow models to structured reasoning (Sudoku, Zebra puzzles) — tasks requiring constraint satisfaction rather than sequence continuation
- Iterative self-refinement via flow matching, where each denoising step is a reasoning step conditioned on the current state
- Self-conditioning signal allows the model to detect and correct constraint violations mid-flow rather than at the final output
- Demonstrates scaling properties: larger flow models improve reasoning accuracy more efficiently than equivalent autoregressive models on the same tasks

## Related Papers
- [[making-expert-reasoning-learnable-with-self-distillation-2602.02405]] — Expert reasoning distillation; Flow Reasoning differs by using flow matching instead of autoregressive distillation for structured reasoning tasks
- [[flowr2a-learning-reward-to-action-distribution-for-multimodal-driving-planning-2606.24231]] — FlowR2A applies flow matching to driving planning; Flow Reasoning extends the flow paradigm to logical reasoning tasks with self-conditioning
