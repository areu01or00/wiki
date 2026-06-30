---
title: "Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [safety, fine-tuning, adversarial, llm-security, evasion]
sources: ["https://arxiv.org/abs/2606.27091"]
---

# Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation

## Overview
This paper reveals that fine-tuning LLMs for security classification can introduce evasion vulnerabilities invisible to standard held-out evaluation. The key finding is that fine-tuning concentrates and semantically specializes inherited model circuits, improving canonical accuracy while expanding transformation-sensitive attack surfaces (PowerShell alias substitution, command reconstruction, string construction, execution indirection, case mutation). A causal intervention localizes the classification circuit to a late-attention route inherited from the base model rather than created by fine-tuning.

## Key Facts
- **arXiv**: [2606.27091](https://arxiv.org/abs/2606.27091)
- **Key Subject**: Fine-tuning can improve task accuracy while expanding the evasion surface

## Key Contributions
- Demonstrates that held-out evaluation from the same distribution misses vulnerabilities introduced by fine-tuning itself
- Shows that fine-tuning concentrates inherited base-model circuits rather than creating new classification routes
- Proposes a pre-deployment monitoring method: linear probe at the classification boundary + indicator-token sign test
- Introduces a three-tier evasion benchmark covering iwr substitution, Invoke-Expression reconstruction, and case-mutated variants
- Surfaces *fine-tuning-circuit-inheritance* and *transformation-sensitive-attack-surface* as load-bearing FINE-TUNING-SAFETY primitives

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent LLM research discoveries
