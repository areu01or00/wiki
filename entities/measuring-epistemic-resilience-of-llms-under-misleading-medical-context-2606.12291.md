---
title: "Measuring Epistemic Resilience of LLMs Under Misleading Medical Context"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [safety, llm, medical, adversarial-robustness, evaluation]
sources: ["https://arxiv.org/abs/2606.12291"]
---

# Measuring Epistemic Resilience of LLMs Under Misleading Medical Context

## Overview
Demonstrates that expert-level medical-exam scores do NOT imply safe medical judgment: when misleading context is injected into questions LLMs originally answer correctly, they abandon the correct answer. Introduces **epistemic resilience** as the formal property (maintain correct judgment under adversarial context) and **MedMisBench** as the benchmark (10,932 medical items × 48,889 misleading context-option combinations).

## Key Facts
- **Authors**: Zhou, Hongjian; Zou, Xinyu; Wu, Jinge; Wu, Sean; Yu, Junchi
- **Year**: 2026
- **arXiv**: [2606.12291](https://arxiv.org/abs/2606.12291)
- **Citation date**: 2026-06-10 (online: 2026-06-15)

## Key Contributions
- Reframes "high medical score implies safe medical advice" as a fragile assumption that does not survive adversarial context injection
- Formalizes **epistemic resilience** as the load-bearing safety property: ability to maintain correct judgment under misleading context
- Introduces MedMisBench with 10,932 medical items and 48,889 misleading context-option combinations
- Provides empirical evidence that frontier LLMs abandon correct answers when misleading context is injected — failure mode distinct from hallucination
- Establishes a diagnostic primitive distinguishing robustness-as-score from robustness-as-judgment-under-adversarial-input

## Related Papers
- [[the-illusion-of-multi-agent-advantage-2606.13003]] — MAS-advantage empirical falsification; sibling primitive showing automatic systems also fail under adversarial deployment
- [[the-impossibility-triangle-of-long-context-modeling-2605.05066]] — long-context impossibility triangle; sibling primitive with orthogonal adversarial surface (length rather than misleading context)
- [[maxproof-scaling-mathematical-proof-with-generative-verifier-rl-and-population-level-test-time-scaling-2606.13473]] — population-level test-time scaling sibling from Run 72; orthogonal mathematical-verifier primitive
