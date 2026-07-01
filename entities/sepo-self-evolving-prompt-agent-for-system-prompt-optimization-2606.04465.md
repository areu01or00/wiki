---
title: "SePO: Self-Evolving Prompt Agent for System Prompt Optimization"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [prompt-engineering, self-improvement, agent]
sources: ["https://arxiv.org/abs/2606.04465"]
---

# SePO: Self-Evolving Prompt Agent for System Prompt Optimization

## Overview
System prompt optimization improves agent behavior without modifying the underlying model, yielding human-readable, model-agnostic instructions. Existing methods build a prompt agent that refines task agents' system prompts, yet leave the prompt agent's own system prompt hand-engineered and fixed. SePO proposes Self-Evolving Prompt Optimization, which treats the prompt agent's own system prompt as a learnable artifact — enabling the prompt optimization agent to improve its own instructions via self-referential evolution.

## Key Facts
- **Authors**: Tao, Wangcheng; Wu, Han; Wong, Weng-Fai
- **Year**: 2026
- **arXiv**: [2606.04465](https://arxiv.org/abs/2606.04465)

## Key Contributions
- First framework where the prompt optimization agent improves its own system prompt via self-referential evolutionary loop
- Model-agnostic, human-readable prompt outputs — no gradient access required
- Demonstrates that the prompt optimization agent itself can suffer from suboptimal initial prompts, and that meta-level prompt optimization improves downstream task performance

## Related Papers
- [[alg-evolv-llm-driven-meta-evolution-algorithmic-trading-programs-2606.26173]] — Both papers explore LLM-driven self-improvement via evolutionary mechanisms; AlgoEvolve applies this to trading strategy discovery while SePO applies it to prompt optimization itself
- [[2606.04465]] — Self-reference
