---
title: "LLM-Guided Evolution for Medical Decision Pipelines"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [self-improvement, evolutionary-algorithms, medical, agent]
sources: ["https://arxiv.org/abs/2606.07342"]
---

# LLM-Guided Evolution for Medical Decision Pipelines

## Overview
Adapting large language models (LLMs) to clinical workflows often requires costly fine-tuning or manual prompt and pipeline engineering. This paper studies LLM-guided MAP-Elites evolution as an inference-time alternative for discovering medical decision strategies — replacing expensive fine-tuning with evolutionary search over the space of pipeline configurations guided by LLM feedback.

## Key Facts
- **Authors**: Sviridov, Ivan; Oskin, Artem; Panin, Ivan + 4
- **Year**: 2026
- **arXiv**: [2606.07342](https://arxiv.org/abs/2606.07342)

## Key Contributions
- First application of LLM-guided MAP-Elites evolution to medical decision pipelines
- Inference-time pipeline discovery — no fine-tuning required, reducing cost and enabling rapid adaptation to new clinical contexts
- Demonstrates MAP-Elites' quality-diversity properties preserve diverse clinical strategy archetypes while optimizing for efficacy

## Related Papers
- [[alg-evolv-llm-driven-meta-evolution-algorithmic-trading-programs-2606.26173]] — Both papers apply LLM-guided evolutionary search to domain-specific pipelines (trading vs medical); AlgoEvolve focuses on financial strategy discovery while this paper focuses on clinical decision strategies
- [[sepo-self-evolving-prompt-agent-for-system-prompt-optimization-2606.04465]] — Both papers explore self-referential LLM-driven improvement loops (SePO for prompts, this paper for pipeline configurations)
