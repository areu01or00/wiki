---
title: "Unlearners Can Lie: Evaluating and Improving Honesty in LLM Unlearning"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [llm-unlearning, honesty, safety, representation-alignment, trustworthiness]
sources: ["https://arxiv.org/abs/2605.08765"]
---

# Unlearners Can Lie: Evaluating and Improving Honesty in LLM Unlearning

## Overview
Introduces a formal definition of *unlearning honesty* with two criteria (preserving both utility and honesty on retained knowledge; effective forgetting while acknowledging limitations) and a suite of evaluation metrics covering utility, retained-set honesty, forgetting effectiveness, rejection rate, and refusal stability. Demonstrates that all 9 evaluated unlearning methods across 3 mainstream families fail to meet these standards, and presents ReVa (representation-alignment procedure) that fine-tunes feature-randomized unlearned models to acknowledge forgotten knowledge.

## Key Facts
- **Authors**: Gu, Renjie; Du, Jiazhen; Zhang, Yihua; Liu, Sijia
- **Year**: 2026
- **arXiv**: [2605.08765](https://arxiv.org/abs/2605.08765)
- **Online date**: 2026-05-09
- **Submission date**: 2026-05-09

## Key Contributions
- **Formal definition of unlearning honesty** — (1) preserve utility and honesty on retained knowledge; (2) ensure effective forgetting while encouraging the model to acknowledge its limitations and respond consistently to questions related to forgotten knowledge
- **Evaluation suite for unlearning honesty** — metrics covering utility, retained-set honesty, forgetting effectiveness, rejection rate, and refusal stability in Q&A and MCQ settings
- **Empirical diagnosis that all current methods fail** — 9 methods across 3 mainstream families all fail to meet honesty standards; unlearned models hallucinate, generate abnormal token sequences, or behave inconsistently
- **ReVa — representation-alignment procedure** — fine-tunes feature-randomized unlearned models to acknowledge forgotten knowledge; achieves highest rejection rate after two rounds of interaction (nearly doubling the second-best) and remarkably *also improves honesty on the retained set*

## Related Papers
- [[emergent-concepts]] — Parent wiki page where this discovery is logged
- [[revisiting-parameter-based-knowledge-editing-in-llms-2606.00570]] — Sibling Run-63 knowledge-editing theoretical-limits primitive (dimensional-collapse hypothesis, retrieval-stronger-than-parameter-editing) — together they bracket the LLM-knowledge-modification surface between *editing-as-dimension-collapse* (Revisiting-Parameter-Based-KE) and *unlearning-as-honesty-deficit* (Unlearners-Can-Lie)
- [[uncertainty-quantification-for-hallucination-detection-in-llms-2510.12040]] — Sibling Run-63 UQ-as-trustworthiness-framework primitive — together they bracket the LLM-trustworthiness surface between *uncertainty quantification framework* (UQ-for-Hallucination) and *unlearning honesty framework* (Unlearners-Can-Lie)
- [[openbiorq-unsolved-biomedical-research-questions-for-agents-2606.21959]] — Sibling Run-50 abstention-as-research-discipline primitive — together they bracket the LLM-honesty surface between *abstention discipline in agentic research* (OpenBioRQ) and *unlearning honesty formalization* (Unlearners-Can-Lie)
- [[the-verification-horizon-no-silver-bullet-for-coding-agent-rewards-2606.26300]] — Sibling verification-co-evolution primitive — together they bracket the LLM-honesty surface between *verifier signal stability* (Verification-Horizon) and *unlearning honesty stability* (Unlearners-Can-Lie)