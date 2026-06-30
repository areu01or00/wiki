---
title: "Detecting Unfaithful Chain-of-Thought via Circuit-Guided Internal-External Discrepancy"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [interpretability, llm-reasoning, circuit-analysis]
sources: ["https://arxiv.org/abs/2605.25603"]
---

# Detecting Unfaithful Chain-of-Thought via Circuit-Guided Internal-External Discrepancy

## Overview
CIE-Scorer (Circuit-guided Internal-External Discrepancy Scorer) detects unfaithful chain-of-thought reasoning by comparing the model's internal computational circuit traces against its external reasoning traces. Faithful CoT reasoning should align with the model's internal computation; unfaithful traces diverge.

## Key Facts
- **Authors**: 
- **Year**: 2025
- **arXiv**: [2605.25603](https://arxiv.org/abs/2605.25603)

## Key Contributions
- Circuit-guided internal-external discrepancy scoring for instance-level CoT unfaithfulness detection
- Efficient sentence-level circuit tracing from informative reasoning tokens
- Internal and external reasoning graph construction with Fused Gromov-Wasserstein distance measurement
- State-of-the-art performance on FaithCoT-Bench with reduced circuit construction cost

## Related Papers
- [[mechanistic-circuit-based-knowledge-editing-in-large-language-models-2604.05876]] — Circuit-level analysis methodology for LLM internal computation
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Circuit discovery and tracing for LLM interpretability
