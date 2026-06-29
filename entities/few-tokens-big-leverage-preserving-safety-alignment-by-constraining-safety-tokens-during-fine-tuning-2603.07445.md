---
title: "Few Tokens, Big Leverage: Preserving Safety Alignment by Constraining Safety Tokens During Fine-tuning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [alignment, fine-tuning, safety, token-level]
sources: ["https://arxiv.org/abs/2603.07445"]
---

# Few Tokens, Big Leverage: Preserving Safety Alignment by Constraining Safety Tokens During Fine-tuning

## Overview
Identifies that safety-aligned behavior in LLMs is reflected at the token-level through concentrated output confidence on a small subset of safety-related tokens. Proposes constraining these safety tokens during fine-tuning as a lightweight mechanism to preserve alignment without full-parameter training, enabling safer fine-tuning of aligned models for downstream tasks.

## Key Facts
- **Authors**: Guoli Wang, Haonan Shi, Tu Ouyang, An Wang
- **Year**: 2026
- **arXiv**: [2603.07445](https://arxiv.org/abs/2603.07445)

## Key Contributions
- First identification that safety-aligned behavior is token-level and concentrated on a small subset of safety-related tokens
- Proposes safety-token constraint during fine-tuning as a lightweight alignment-preserving mechanism
- Demonstrates that constraining safety tokens preserves alignment while allowing task-specific adaptation
- Enables fine-tuning-as-a-service (FaaS) scenarios where model owners can personalize models without degrading safety
- Provides empirical validation across diverse downstream tasks and model sizes

## Related Papers
- [[gradshield-alignment-preserving-finetuning-2605.14194]] — GradShield alignment-preserving fine-tuning defense (same fine-tuning safety theme)
- [[school-of-reward-hacks-hacking-harmless-tasks-generalizes-to-misaligned-behavior-in-llms-2508.17511]] — School of Reward Hacks: reward hacking generalization from fine-tuning (RLHF-cascading alignment degradation primitive)
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Geometry of refusal behavior in safety-aligned LLMs
