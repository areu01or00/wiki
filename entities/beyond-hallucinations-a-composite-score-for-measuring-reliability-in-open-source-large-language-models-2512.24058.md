---
title: "Beyond Hallucinations: A Composite Score for Measuring Reliability in Open-Source Large Language Models"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [llm-reliability, hallucination, calibration, evaluation]
sources: ["https://arxiv.org/abs/2512.24058"]
---

# Beyond Hallucinations: A Composite Score for Measuring Reliability in Open-Source Large Language Models

## Overview
Beyond Hallucinations introduces a composite reliability score that goes beyond measuring hallucinations in isolation, instead evaluating LLM reliability holistically across calibration, overconfidence under input shifts, and factual inconsistency. Applied to LLaMA, Mistral, and Gemma, the score reveals systematic reliability differences across model families and sizes.

## Key Facts
- **Authors**: Research team evaluating open-source LLM reliability
- **Year**: 2025
- **arXiv**: [2512.24058](https://arxiv.org/abs/2512.24058)

## Key Contributions
- Novel composite reliability score combining hallucination rate, calibration error, and robustness under distribution shift
- First systematic reliability benchmarking of open-source LLMs (LLaMA, Mistral, Gemma) in decision-critical domains
- Reveals that model size alone does not predict reliability — smaller models can outperform larger ones on composite scoring

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts discovery page
