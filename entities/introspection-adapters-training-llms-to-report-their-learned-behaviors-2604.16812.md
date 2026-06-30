---
title: "Introspection Adapters: Training LLMs to Report Their Learned Behaviors"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [interpretability, fine-tuning, behavioral-auditing, self-awareness, llm-security]
sources: ["https://arxiv.org/abs/2604.16812"]
---

# Introspection Adapters: Training LLMs to Report Their Learned Behaviors

## Overview
This paper introduces Introspection Adapters (IAs): a scalable approach to rapidly identify learned behaviors of many LLMs derived from a shared base model. The method fine-tunes models M_i from a base M with implanted behaviors b_i, then trains a single LoRA adapter (the IA) jointly across all fine-tunes to cause models to verbalize their implanted behaviors. The IA generalizes to unseen fine-tune methods — including to AuditBench for identifying hidden concerning behaviors and to detecting encrypted fine-tuning API attacks. IAs scale favorably with model size and training data diversity, representing a practical approach to auditing fine-tuned LLMs at scale.

## Key Facts
- **Authors**: Keshav Shenoy, Li Yang, Abhay Sheshadri, Sören Mindermann, Jack Lindsey, Sam Marks, Rowan Wang
- **Year**: 2026
- **arXiv**: [2604.16812](https://arxiv.org/abs/2604.16812)

## Key Contributions
- First LoRA-based introspection adapter that causes fine-tuned LLMs to self-report their learned behaviors in natural language
- Joint training across diverse fine-tune methods produces a generalizable IA that works on unseen fine-tune types
- Generalizes to AuditBench (state-of-the-art at identifying explicitly hidden concerning behaviors) and to encrypted fine-tuning API attack detection
- Scales favorably with model size and training data diversity
- Practical tool for auditing fine-tuned LLMs without requiring white-box access to the fine-tuned model itself

## Related Papers
- [[knowing-acting-probe-kapro-benchmarking-self-awareness-capability-of-llm-agents-2606.20661]] — KAPRO evaluates whether LLM agents know what they don't know; Introspection Adapters enable models to report what they have learned, forming a complementary metacognitive tooling pair
