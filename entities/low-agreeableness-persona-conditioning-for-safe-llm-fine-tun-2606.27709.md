---
title: "Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety, fine-tuning, llm, persona, alignment]
sources: ["https://arxiv.org/abs/2606.27709"]
---

# Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning

## Overview
This paper identifies a critical safety failure mode in LLM fine-tuning: warmth-focused fine-tuning (designed to make models more socially warm and empathetic) simultaneously weakens adversarial safety, making models more susceptible to jailbreaks and harmful outputs. The authors investigate whether this represents an inherent tradeoff or a data artifact, and introduce a persona-driven rewriting pipeline that conditions user turns on low agreeableness to preserve safety during warmth training.

## Key Facts
- **Authors**: Austin MY Cheung, Yi Yang
- **Year**: 2026
- **arXiv**: [2606.27709](https://arxiv.org/abs/2606.27709)

## Key Contributions
- Identifies a **warmth-safety tradeoff** failure mode: fine-tuning for social warmth degrades both factual reliability AND adversarial safety
- Proposes a **persona-driven rewriting pipeline** that conditions user turns on low agreeableness to disentangle warmth from safety degradation
- Distinguishes between inherent tradeoff vs. data construction artifact via controlled experiments
- Demonstrates that targeted persona conditioning can preserve warmth improvements while maintaining safety robustness

## Related Papers
- [[persona-conditioned-risk-behavior-in-large-language-models-2603.15831]] — Prior wiki entry on persona-conditioned risk behavior (shared theme of persona conditioning, but different axis: risk behavior vs. safety degradation from warmth fine-tuning)
