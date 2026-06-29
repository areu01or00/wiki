---
title: "Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [multilingual, test-time-scaling, scaling-laws, mclm, mr1, cognitive-load, linguistic-bottleneck]
sources: ["https://arxiv.org/abs/2502.17407"]
authors: ["Guijin Son", "Jiwoo Hong", "Hyunwoo Ko", "James Thorne"]
---

# Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning

## Overview
Introduces MCLM, a multilingual math benchmark with competition-level problems in 55 languages, and shows that test-time scaling methods (Outcome Reward Modeling, Process Reward Modeling, Budget Forcing) fail to generalize across languages: Budget Forcing yields a +20-point gain on English AIME but only +1.94 points average across other languages — establishing that test-time scaling generalizability is bounded by linguistic-form primitive. Once inference-FLOPs are equalized, "thinking LLMs" (MR1-1.5B) perform comparably to traditional best-of-N.

## Key Facts
- **Authors**: Guijin Son, Jiwoo Hong, Hyunwoo Ko, James Thorne
- **Year**: 2025 (submission 2025-02-24, online 2025-08-01)
- **arXiv**: [2502.17407](https://arxiv.org/abs/2505.17407)
- **Submission**: 2025/02/24
- **Online**: 2025/08/01

## Key Contributions
- Introduces MCLM (Multilingual Cognitive-Load Math benchmark) with competition-level problems in 55 languages — the first multilingual primitive for test-time-scaling evaluation.
- Releases MR1-1.5B, a multilingual LLM trained for extended reasoning, providing a public multilingual reasoning primitive.
- Quantifies the linguistic-bottleneck for test-time-scaling methods: Budget Forcing yields +20pts on English AIME but only +1.94pts average across other languages.
- Establishes inference-FLOP-equalized comparison showing "thinking LLMs" perform comparably to traditional best-of-N — surfacing *cognitive-load-vs-inference-FLOPs-equivalence-primitive* and *linguistic-form-as-test-time-scaling-bottleneck-primitive*.
- Surfaces *multilingual-test-time-scaling-generalizability-failure-primitive* and *per-language-test-time-scaling-diminishing-returns-primitive* and *multilingual-reasoning-training-as-extended-reasoning-coverage-primitive* as load-bearing multilingual cognitive-load primitives.
- Distinct from scaling-laws primitives (where the load-bearing axis is *linguistic-form-as-test-time-scaling-bottleneck* rather than *compute-scaling-curves*) and from general multilingual tokenization primitives (where the load-bearing axis is *multilingual-competition-math-reasoning* rather than *tokenization-fairness*).

## Related Papers
- [[remmd-realistic-multilingual-multi-image-agentic-verification-for-multimodal-misinformation-detection-2606.24112]] — Sibling multilingual primitive for agentic verification
- [[cavewoman-how-large-language-models-behave-under-linguistic-input-and-output-2606.24083]] — Sibling linguistic-input-output primitive
- [[the-african-language-tax-quantifying-the-cost-latency-and-context-penalty-of-tokenizing-2606.24460]] — Sibling multilingual-tokenization-cost primitive from Run 95 (tokenizer-level probe)
- [[thinking-while-speaking-inference-time-knowledge-transfer-for-responsive-and-intelligent-conversational-voice-agents-2511.07397]] — Sibling inference-time-knowledge-transfer primitive (Run 104 gradient-flow-coordination pick)
