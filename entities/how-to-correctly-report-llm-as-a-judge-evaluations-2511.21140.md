---
title: "How to Correctly Report LLM-as-a-Judge Evaluations"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [evaluation, alignment, llm-as-judge, benchmarking]
sources: ["https://arxiv.org/abs/2511.21140"]
---

# How to Correctly Report LLM-as-a-Judge Evaluations

## Overview
LLMs are widely used as scalable evaluators (LLM-as-a-Judge) in place of human annotators, but imperfect sensitivity and specificity of judge LLMs induce bias in naive evaluation scores. This paper provides a rigorous statistical framework for correctly reporting LLM-as-a-Judge evaluations, accounting for judge model reliability and providing bias-corrected evaluation scores.

## Key Facts
- **Authors**: Lee, Chungpa; Zeng, Thomas; Jeong, Jongwon + 2
- **Year**: 2025
- **arXiv**: [2511.21140](https://arxiv.org/abs/2511.21140)

## Key Contributions
- Identifies systematic bias in naive LLM-as-a-Judge scoring due to imperfect judge sensitivity/specificity
- Proposes a plug-in framework that corrects this bias and enables reliable inter-model comparison
- Provides statistical rigor for evaluation reporting — moving beyond point estimates to confidence-aware reporting
- Addresses the critical problem that different judge LLMs have different reliability profiles, invalidating direct score comparisons

## Related Papers
- [[benchmarking-llm-as-a-judge-for-long-form-output-evaluation-2606.01629]] — Prior systematic comparison of LLM-as-Judge paradigms for open-ended tasks
