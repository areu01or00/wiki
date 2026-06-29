---
title: "Categorical Prior Lock-in: Why In-Context Learning Fails for Structured Data"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [in-context-learning, structured-generation, primitive-class-declarative-lm-program]
sources: ["https://arxiv.org/abs/2606.11961"]
---

# Categorical Prior Lock-in: Why In-Context Learning Fails for Structured Data

## Overview
Investigates the limits of in-context learning for structured generation under distribution mismatch, using high-cardinality tabular data as a controlled test case, and identifies a structural failure mode termed *categorical prior lock-in*: the inability of ICL to update the model's prior over token distributions inherited from pre-training. Across two 7B-parameter open-weight models, ICL improves numerical fidelity with additional examples but exhibits a sharp ceiling on categorical distributions, failing to reproduce rare classes entirely — Parameter-efficient fine-tuning (LoRA) overcomes these limitations but introduces measurable memorization risk and, in some cases, destabilizes structured output generation, highlighting a fundamental trade-off between adaptability and privacy.

## Key Facts
- **Authors**: Pelusi, Antonio; Braghin, Stefano; Trombetta, Alberto
- **Year**: 2026
- **arXiv**: [2606.11961](https://arxiv.org/abs/2606.11961)

## Key Contributions
- **Categorical prior lock-in as a structural ICL failure primitive**: identifies that ICL for structured generation cannot update the model's pre-training prior over token distributions, producing a sharp ceiling on categorical distributions and failing to reproduce rare classes — the **first categorical-prior-lock-in diagnostic primitive for ICL on structured data** in the wiki.
- **Adaptability vs privacy trade-off characterization**: parameter-efficient fine-tuning (LoRA) overcomes the categorical-prior-lock-in ceiling but introduces measurable memorization risk and, in some cases, destabilizes structured output generation — surfaces the fundamental adaptability-vs-privacy trade-off.
- **High-cardinality tabular test bed as controlled-distribution-mismatch setting**: introduces high-cardinality tabular data as the controlled test case for ICL-vs-distribution-mismatch, extending the structural-evaluation methodology beyond the typical ICL benchmarks.
- **Two 7B-parameter open-weight model coverage**: Llama-class 7B models exhibit the categorical-prior-lock-in primitive across both numerical and categorical axes, establishing the primitive as architecture-agnostic at the parameter scale tested.

## Related Papers
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — Sibling paper on structured-output-constraint tax in open-weight LLMs — orthogonal primitive for structured-generation under output constraints.
- [[sample-efficient-demonstration-selection-for-in-context-learning-2506.08607]] — Sibling paper on sample-efficient demonstration selection for ICL — orthogonal primitive for ICL exemplar selection.
- [[distilling-examples-into-task-instructions-enhanced-in-context-2606.15641]] — Sibling paper on distilling examples into task instructions for enhanced ICL — orthogonal primitive for ICL task-instruction distillation.
- [[an-empirical-study-of-many-shot-in-context-learning-for-machine-translation-of-low-resource-languages-2604.02596]] — Sibling paper on many-shot ICL scaling for low-resource MT — orthogonal primitive for many-shot ICL scaling.