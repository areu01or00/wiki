---
title: "GradShield: Alignment Preserving Fine-tuning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [alignment, fine-tuning, safety, defense]
sources: ["https://arxiv.org/abs/2605.14194"]
---

# GradShield: Alignment Preserving Fine-tuning

## Overview
Proposes GradShield, a method that protects the safety alignment of LLMs during fine-tuning by measuring Fisher Information of Hidden States (FIHS) and using it to constrain gradient updates on alignment-critical parameters. Addresses the vulnerability of aligned LLMs to harmful fine-tuning attacks in fine-tuning-as-a-service (FaaS) scenarios where third parties can finetune models on potentially harmful datasets.

## Key Facts
- **Authors**: (authors not yet extracted from paper)
- **Year**: 2026
- **arXiv**: [2605.14194](https://arxiv.org/abs/2605.14194)

## Key Contributions
- First method to use Fisher Information of Hidden States (FIHS) for alignment-preserving fine-tuning
- Protects aligned LLMs against harmful fine-tuning attacks in FaaS scenarios
- Demonstrates that alignment-critical parameters can be identified via FIHS and selectively protected
- Enables third-party fine-tuning while preserving original safety alignment
- Provides defense applicable to both full-parameter and parameter-efficient fine-tuning (LoRA)

## Related Papers
- [[few-tokens-big-leverage-preserving-safety-alignment-by-constraining-safety-tokens-during-fine-tuning-2603.07445]] — Few Tokens Big Leverage: safety-token constraint for preserving safety during fine-tuning (same alignment-preserving fine-tuning primitive)
- [[safety-alignment-as-continual-learning-mitigating-the-alignment-tax-via-orthogonal-gradient-projection-2602.07892]] — Orthogonal gradient projection for alignment preservation during fine-tuning
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Geometric analysis of refusal behavior in safety-aligned LLMs
