---
title: "Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety, evaluation, adversarial, encoder]
sources: ["https://arxiv.org/abs/2606.25782"]
---

# Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation

## Overview
Safety evaluation of LLM outputs has generally relied on LLM-based judges, which are effective but slow and expensive at scale. This paper evaluates whether fine-tuned modern encoder classifiers from the ModernBERT family can reliably identify harmful LLM outputs in user-model conversations without substantial performance loss — offering a faster, cheaper alternative to decoder-only LLM judges.

## Key Facts
- **Authors**: Han Jeon, Shiv Medler, Joseph Voyles, Matt Wood
- **Year**: 2026
- **arXiv**: [2606.25782](https://arxiv.org/abs/2606.25782)
- **Date**: 24 Jun 2026 (submitted)

## Key Contributions
- **Encoder vs decoder safety judge comparison**: systematic evaluation of ModernBERT-family encoder classifiers vs LLM-based judges on safety evaluation tasks
- **ModernBERT and Ettin evaluation**: fine-tuned encoder classifiers assessed for reliability in identifying harmful outputs across diverse adversarial evaluation scenarios
- **Cost-efficiency analysis**: quantifies the trade-off between safety evaluation accuracy and deployment cost/latency
- **Threshold calibration**: analyzes how encoder classifiers perform at various decision thresholds compared to LLM judges

## Related Papers
- [[ras-measuring-llm-safety-through-refusal-alignment-2606.25750]] — Safety measurement via refusal alignment (complementary methodology, different evaluation paradigm)
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Red-teaming methodology for safety evaluation (complementary: this paper focuses on automated judge evaluation)
- [[evaluating-the-interpretability-of-sparse-autoencoders-with-concept-annotations-2606.24716]] — Interpretability tools for understanding what safety classifiers learn
