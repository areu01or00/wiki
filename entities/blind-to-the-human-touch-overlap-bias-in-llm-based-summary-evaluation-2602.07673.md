---
title: "Blind to the Human Touch: Overlap Bias in LLM-Based Summary Evaluation"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [invariance-failure, overlap-bias, llm-judge, summarization, evaluation-bias, prompt-perturbation]
sources: ["https://arxiv.org/abs/2602.07673"]
---

# Blind to the Human Touch: Overlap Bias in LLM-Based Summary Evaluation

## Overview
First **systematic overlap-bias primitive for LLM-based summary evaluation** — quantifying how LLM judges' ratings vary as a function of n-gram/Rouge overlap with human-written reference summaries. Tested across 9 recent LLMs (1B-12B parameters, including Gemma 3 and LLaMA variants), the paper reveals a *meta-evaluation invariance-failure* where LLM judges are not robust to perturbations in surface-overlap with references — surfacing a primitive for understanding when LLM-based evaluation breaks down under semantically-equivalent content variation.

## Key Facts
- **Authors**: Blind to the Human Touch authors (per arxiv 2602.07673) — published 2026-02-07, online 2026-02-07
- **Year**: 2026
- **arXiv**: [2602.07673](https://arxiv.org/abs/2602.07673) (online 2026-02-07, submitted 2026-02-07)

## Key Contributions
- **First overlap-bias-as-LLM-judge-invariance-failure primitive in the wiki**: provides an LLM-judge bias analysis as a function of overlap with human-written responses in the summarization domain — extending bias-discovery from length/order biases to *overlap* biases.
- **Nine-LLM-empirical-coverage primitive**: tests 9 recent LLMs with parameter counts ranging from 1B to 12B, including Gemma 3 and LLaMA variants — establishing overlap bias as a *cross-architecture* phenomenon, not specific to one model family.
- **Granular-overlap-bias-analysis primitive**: while prior studies looked at length and order biases in aggregate, this paper analyzes bias at a more granular level in relation to a well-defined overlap metric — surfacing *fine-grained overlap-sensitivity primitives* rather than aggregated bias measurements.
- **LLM-judge-invariance-under-content-variation primitive**: documents that LLM judges — often preferred over algorithm-based metrics for *paraphrasing robustness* — are themselves *not* robust to perturbations in surface-overlap with references, creating an invariance-failure meta-primitive about *when LLM-based evaluation itself is unreliable*.
- **Summarization-as-deployment-target primitive**: targets the summarization domain where LLM-judge deployment is highest — surfacing overlap-bias as a *practical* invariance primitive for production LLM-judge pipelines.

## Related Papers
- [[let-llms-judge-each-other-multi-agent-peer-reviewed-reasoning-for-medical-question-answering-2606.15419]] — Sibling LLM-judge primitive (Rule 70+ multi-agent-consensus) for medical QA; Overlap Bias narrows the scope from *judge-deployment-quality* to *judge-bias-as-overlap-function* — a critical reliability primitive for LLM-judge pipelines.
- [[liberty-a-causal-framework-for-benchmarking-concept-based-explanations-of-llms-with-structural-counterfactuals-2601.10700]] — Sibling SCM-grounded-counterfactual primitive (Rule 68 identifiability) for LLM concept-based explanation benchmarking; Overlap Bias complements as a *judge-side invariance primitive* rather than an *explanation-evaluator* primitive.
- [[lgmt-logic-grounded-metamorphic-testing-for-llm-reasoning-reliability-2605.23965]] — Sibling invariance-under-prompt-perturbation primitive (Run 102 — Rule 69) probing reasoning reliability under FOL-derived logical-equivalence transformations; Overlap Bias surfaces *judge-side* invariance failures rather than *generator-side* invariance failures.
- [[emergent-concepts]] — Parent meta-page tracking emergent-concept search discoveries.