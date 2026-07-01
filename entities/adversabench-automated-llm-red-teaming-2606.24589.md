---
title: "AdversaBench: Automated LLM Red-Teaming with Multi-Judge Confirmation and Cross-Model Transferability"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [safety, red-teaming, adversarial-evaluation, benchmark]
sources: ["https://arxiv.org/abs/2606.24589"]
---

# AdversaBench: Automated LLM Red-Teaming with Multi-Judge Confirmation and Cross-Model Transferability

## Overview
Scaling adversarial evaluation of large language models requires both a method for generating hard inputs and a reliable way to confirm that resulting failures are real. AdversaBench is an end-to-end red-teaming pipeline that mutates seed prompts with five structured operators, queries a target model, and confirms failures through a three-judge panel with a meta-judge tiebreaker. The framework's cross-model transferability analysis reveals which adversarial prompts generalize across LLM families.

## Key Facts
- **Authors**: Khandelwal, Khanak
- **Year**: 2026
- **arXiv**: [2606.24589](https://arxiv.org/abs/2606.24589)
- **Date**: 2026/06/23

## Key Contributions
- Introduces a structured **five-operator mutation framework** (semantic inversion, recursive decomposition, constraint violation, authority impersonation, context stitching) for generating adversarial prompts at scale
- Proposes a **three-judge panel with meta-judge tiebreaker** architecture for reliably confirming whether a model failure is genuine vs. a false positive
- Provides systematic **cross-model transferability analysis** showing which adversarial operators and prompt patterns generalize across different LLM families (GPT, Claude, Gemini, Llama)
- Enables automated red-teaming at scale, reducing manual red-team effort while maintaining evaluation reliability

## Related Papers
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Adaptive jailbreak architecture and red-teaming methodology
- [[be-your-own-red-teamer-safety-alignment-via-self-play-and-reflective-experience-replay-2601.10589]] — Self-play red teaming for safety alignment
- [[do-encoders-suffice-a-systematic-comparison-of-encoder-and-decoder-safety-judges-for-llm-adversarial-evaluation-2606.25782]] — Safety judge evaluation methodology (complementary evaluation framework)
