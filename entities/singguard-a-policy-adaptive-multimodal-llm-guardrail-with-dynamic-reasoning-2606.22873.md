---
title: "SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety, guardrail, multimodal, vlm, policy-adaptive]
sources: ["https://arxiv.org/abs/2606.22873"]
---

# SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning

## Overview
SingGuard is a policy-adaptive multimodal guardrail framework for VLMs that treats safety policies as runtime inputs, enabling policy-grounded safety assessment across diverse deployment contexts. It supports a fast-to-slow reasoning spectrum from direct safety judgments to policy-deliberation, optimized via decoupled RL.

## Key Facts
- **Authors**: 
- **Year**: 2026
- **arXiv**: [2606.22873](https://arxiv.org/abs/2606.22873)
- **Online Date**: 2026-06-25

## Key Contributions
- First policy-adaptive multimodal guardrail treating active policy as runtime input with natural-language rule checking
- Fast-slow reasoning spectrum (direct judgment → policy-grounded deliberation) with Fast-Slow Decoupled RL optimization
- SingGuard-Bench: 56,340 examples across 80+ fine-grained risk types spanning multimodal QA, adversarial attack, and dynamic-rule settings
- Cross-modal joint-risk evaluation: cases where each modality is harmless in isolation but composition implies unsafe intent
- State-of-the-art average F1 across six benchmark families; policy-following accuracy improves from 0.6465 to 0.7415 under runtime policy shifts

## Related Papers
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Safety alignment geometry (sibling refusal/instability work)
- [[normguard-reward-preserving-norm-constraints-in-flow-matching-reinforcement-learning-2606.27771]] — Norm constraint enforcement in generation (sibling norm-preservation work)
- [[emergent-concepts]] — Parent meta-page for emergent concept discoveries
