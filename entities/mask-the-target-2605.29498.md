---
title: "Mask the Target: A Plug-and-Play Regularizer Against LoRA Forgetting"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [fine-tuning, parameter-efficiency, llm]
sources: ["https://arxiv.org/abs/2605.29498"]
---

# Mask the Target: A Plug-and-Play Regularizer Against LoRA Forgetting

## Overview
Low-Rank Adaptation (LoRA) has become one of the most widely used fine-tuning mechanisms for adapting large language models to new domains, tasks, and users. Yet adaptation performance alone can obscure an important failure mode: LoRA updates may improve performance on the target distribution while catastrophically degrading the model's original capabilities — a phenomenon the authors term "target forgetting." This paper proposes Mask the Target (MTT), a plug-and-play regularization framework that masks the most important target-distribution tokens during LoRA fine-tuning, forcing the model to retain its original capabilities even as it adapts to new tasks.

## Key Facts
- **Authors**: Runze Xu, Arpit Garg, Hemanth Saratchandran, Simon Lucey
- **Year**: 2026
- **arXiv**: [2605.29498](https://arxiv.org/abs/2605.29498)

## Key Contributions
- Introduces Mask the Target (MTT), a plug-and-play regularization framework for LoRA fine-tuning that masks important target-distribution tokens to prevent forgetting of original capabilities
- MTT is task-agnostic and requires no architectural modifications — works with any LoRA implementation
- Achieves SOTA retain-forget trade-offs across diverse domains: arithmetic reasoning, code generation, and instruction following
- Differentiates from prior unlearning methods (KnowledgeSmith model-editing-based, ATWU retain-conflict oracle, gradient-ascent baselines) by focusing on token-level masking rather than parameter-level constraints or external knowledge bases

## Related Papers
- [[selective-forgetting-for-large-reasoning-models-2604.03571]] — RAG-based CoT trace analysis for LRM-specific unlearning; orthogonal to MTT's token-masking mechanism for general LLMs
- [[learning-what-to-forget-improving-llm-unlearning-via-learned-token-level-importance-2606.06320]] — ATWU with alternating token-weighted optimization; orthogonal to MTT's masking-based approach
