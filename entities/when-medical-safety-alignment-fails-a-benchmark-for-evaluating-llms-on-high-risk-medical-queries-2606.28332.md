---
title: "When Medical Safety Alignment Fails: A Benchmark for Evaluating LLMs on High-Risk Medical Queries"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [safety-alignment, medical-ai, benchmark, llm-safety]
sources: ["https://arxiv.org/abs/2606.28332"]
---

# When Medical Safety Alignment Fails: A Benchmark for Evaluating LLMs on High-Risk Medical Queries

## Overview
This paper introduces MedHarm, a high-risk medical safety benchmark with 1,100 medically grounded queries across 10 safety-critical categories (toxicology, pharmacology, covert poisoning, anesthesia, fetal harm). Unlike broad medical QA benchmarks, MedHarm targets realistic prompts requiring refusal, caution, or safe redirection rather than direct helpfulness. The benchmark reveals a substantial gap between apparent alignment and actual medical safety.

## Key Facts
- **arXiv**: [2606.28332](https://arxiv.org/abs/2606.28332)
- **Year**: 2026
- **Theme**: medical-safety / benchmark / alignment

## Key Contributions
- Introduces MedHarm: 1,100 high-risk medical safety queries across 10 safety-critical categories (toxicology, pharmacology, covert poisoning, anesthesia, fetal harm)
- Evaluates 15 LLMs spanning general-purpose, medical-purpose, closed-source, and downstream SFT models, plus 4 guardrail models
- Reveals that aligned models can still produce unsafe or actionable medical responses; medical fine-tuning can amplify harmful specificity
- External guardrails reduce some failures while introducing brittle blocking and weak safe helpfulness
- Key insight: medical safety cannot be inferred from general alignment or medical capability alone — domain-specific stress testing is required

## Related Papers
- [[clinical-reasoning-graphs-structured-evaluation-of-llm-diagnostic-reasoning-reveals-competence-without-consistency-2606.29876]] — Structured evaluation of LLM diagnostic reasoning
- [[athena-r1-an-ai-agent-for-treatment-reasoning-over-a-biomedical-tool-universe-2606.28692]] — Medical AI agent reasoning
- [[be-your-own-red-teamer-safety-alignment-via-self-play-and-reflective-experience-replay-2601.10589]] — Self-play safety alignment red-teaming
