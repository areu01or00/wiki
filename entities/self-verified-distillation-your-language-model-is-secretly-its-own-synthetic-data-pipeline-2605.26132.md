---
title: "Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [distillation, self-improvement, post-training, synthetic-data]
sources: ["https://arxiv.org/abs/2605.26132"]
---

# Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline

## Overview
Can post-trained LLMs further improve themselves using only unlabeled prompts, without external teachers or tool feedback? This paper studies self-improvement starting only from unlabeled seed questions with no ground-truth solutions, across math, science, and coding domains. Self-Verified Distillation (SVD) is a post-training refinement algorithm where the LLM acts as its own synthetic data generator and verifier simultaneously.

## Key Facts
- **Authors**: Tony Lee, Percy Liang
- **Year**: 2025
- **arXiv**: [2605.26132](https://arxiv.org/abs/2605.26132)

## Key Contributions
- Shows LLMs can self-improve using only unlabeled prompts — no external teachers, no ground-truth solutions required
- Self-Verified Distillation: LLM generates synthetic questions, produces answers, then verifies its own outputs to create preference pairs for DPO-style refinement
- Achieves gains in math (GSM8K, MATH), science (GPQA), and coding (HumanEval) without any external supervision
- First demonstration of self-distillation with self-generated preference labels (no annotation pipeline needed)

## Related Papers
- [[stop-when-further-reasoning-won't-help-attention-state-adaptive-generation-in-reasoning-models-2606.15070]] — Learning when to stop reasoning during inference
- [[adamem-test-time-adaptive-memory-for-language-agents-2606.05684]] — Test-time adaptation mechanisms for language agents
