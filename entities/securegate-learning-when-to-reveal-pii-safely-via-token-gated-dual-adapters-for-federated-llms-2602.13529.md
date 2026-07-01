---
title: "SecureGate: Learning When to Reveal PII Safely via Token-Gated Dual-Adapters for Federated LLMs"
created: 2026-02-01
updated: 2026-02-01
type: entity
tags: [privacy, federated-learning, llm-security]
sources: ["https://arxiv.org/abs/2602.13529"]
---

# SecureGate: Learning When to Reveal PII Safely via Token-Gated Dual-Adapters for Federated LLMs

## Overview
Federated learning (FL) enables collaborative training across organizational silos without sharing raw data. With the rapid adoption of LLMs, federated fine-tuning of generative LLMs has gained attention for leveraging distributed data while preserving confidentiality. However, this setting introduces new privacy risks around PII exposure during inference. This paper introduces SecureGate, a framework that learns when to safely reveal or withhold PII during LLM inference in federated settings. SecureGate uses dual adapters—one for utility and one for privacy gating—trained via contrastive learning to distinguish safe revelation conditions from risky ones, enabling LLMs to conditionally reveal PII only when safe.

## Key Facts
- **Authors**: Rao, Arjun; Kim, Soo-Woong; Martinez, Claudia; et al
- **Year**: 2026
- **arXiv**: [2602.13529](https://arxiv.org/abs/2602.13529)

## Key Contributions
-

## Related Papers
- [[emergent-concepts]] — Parent emergent-concepts page
