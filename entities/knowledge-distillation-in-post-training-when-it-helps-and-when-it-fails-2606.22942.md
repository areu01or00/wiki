---
title: "Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails"
created: 2026-22-01
updated: 2026-22-01
type: entity
tags: [instruction-tuning, sft, code-llm, post-training]
sources: ["https://arxiv.org/abs/2606.22942"]
---

# Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails

## Overview
Supervised fine-tuning of code LLMs typically applies uniform cross-entropy loss to all response tokens, implicitly assuming every token provides equally useful learning signal. CODEBLOCK extends token-level selection methods to the code domain — supervising at statement-level vs token-level granularity based on contribution to final code quality. Code-specific issues like syntax correctness, indentation, and variable naming carry different learning signal weights than algorithmic content tokens.

## Key Facts
- **Authors**: [arXiv](https://arxiv.org/abs/2606.22942)
- **Year**: 2026
- **arXiv**: [2606.22942](https://arxiv.org/abs/2606.22942)

## Key Contributions
- Statement-level vs token-level granularity supervision for code SFT
- Code-specific loss weighting based on syntax correctness contribution
- Diagnostic framework for identifying high-value supervision tokens in code generation
- Empirical evaluation showing improved code quality at equal token counts

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts discovery chain
