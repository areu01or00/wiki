---
title: "Quantifying Faithful Confidence Expression in Large Reasoning Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [calibration, large-reasoning-models, faithfulness, uncertainty, llm-reasoning]
sources: ["https://arxiv.org/abs/2606.03969"]
---

# Quantifying Faithful Confidence Expression in Large Reasoning Models

## Overview
Reliable uncertainty communication is critical to the trustworthiness of LLMs, yet faithful calibration (FC) — the alignment between models' intrinsic and (linguistically) expressed confidence — is a persistent failure mode. This challenge is particularly acute for large reasoning models (LRMs), whose extended reasoning traces are often interpreted by users as evidence of deliberation, competence, and reliability. This paper quantifies faithful confidence expression across multiple LRMs and proposes evaluation methods to measure the gap between intrinsic uncertainty and expressed confidence.

## Key Facts
- **Authors**: Areeb Gani, Asal Meskin, Gabrielle Kaili-May Liu, Arman Cohan
- **Year**: 2026
- **arXiv**: [2606.03969](https://arxiv.org/abs/2606.03969)

## Key Contributions
- Establishes a formal framework for measuring faithful calibration (FC) in large reasoning models — the alignment between intrinsic model uncertainty and linguistically expressed confidence
- Documents systematic FC failure modes in LRMs where extended reasoning traces create an illusion of reliability without corresponding intrinsic uncertainty reduction
- Demonstrates that LRMs express higher verbalized confidence than their intrinsic uncertainty warrants, particularly after extended chain-of-thought traces
- Proposes evaluation benchmarks and methodology for quantifying the faithfulness of confidence expression in extended-reasoning systems

## Related Papers
- [[emergent-concepts]] — Parent chain for emergent-concept discoveries
