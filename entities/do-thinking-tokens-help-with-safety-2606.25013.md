---
title: "Do Thinking Tokens Help with Safety?"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [arxiv, emergent-concept, llm-research]
sources: ["https://arxiv.org/abs/2606.25013"]
---

# Do Thinking Tokens Help with Safety?

## Overview
Today's reasoning models use thinking tokens to attain stronger performance on benchmarks than their instruction-tuned counterparts. It is also generally believed that this more &#34;deliberative&#34; mode should improve alignment and safety, by providing the model a safe space to consider whether its planned answer to a request violates its safety principles. We present evidence that this intuition is not always correct. Across frontier open-weight reasoning models spanning GPT-OSS, Qwen, Olmo, and Phi families, we find that the eventual refusal/compliance outcome is already strongly predictable via a trained head on the first token's hidden representation ($0.84$-$0.95$ AUROC and $\sim88\%$ balanced accuracy for predicting refusal/compliance) before any visible thinking. The thinking process turns out to be more akin to prefix completion than to deliberative revision, with the final outcome rarely changing after the first $\sim20\%$ of thinking, despite giving the appearance of deliberation at the text level ($\sim74\%$ of text-level deliberations occur when the response distribution is already locked to one refusal/compliance side). We also find that existing inference-time and training-based safety interventions, despite being motivated by the goal of inducing deliberation, largely shift model behavior toward over-refusal while suppressing already-scarce deliberation signals. Our results suggest that safety behavior in current reasoning models is much less deliberative than commonly assumed, and highlight the need for methods that induce real safety deliberation.

## Key Facts
- **Authors**: Ri, Narutatsu, Panigrahi, Abhishek, Arora, Sanjeev
- **Year**: 2026
- **Date**: 2026-06-23
- **arXiv**: [2606.25013](https://arxiv.org/abs/2606.25013)
- **Subjects**: Machine Learning (cs.LG)

## Key Contributions
- Empirical evidence that "thinking tokens" do not improve safety as commonly assumed: refusal/compliance outcomes are 84-95% AUROC predictable from the first token's hidden state before any visible thinking
- The thinking process behaves more like prefix completion than deliberative revision: ~74% of text-level deliberations occur when the response distribution is already locked to one refusal/compliance side, and the final outcome rarely changes after the first ~20% of thinking
- Evaluation across frontier open-weight reasoning models (GPT-OSS, Qwen, Olmo, Phi) shows existing inference-time and training-based safety interventions largely shift behavior toward over-refusal while suppressing already-scarce deliberation signals
- Identifies a concrete research need: methods that induce *real* safety deliberation rather than rely on the appearance of deliberation

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this paper was first recorded via emergent-concept search.
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Complements the hidden-state safety analysis theme: the intermediate-layers paper detects jailbreaks from layer-N/2 entropy dynamics pre-generation, while the thinking-tokens paper finds refusal/compliance is locked from the first-token representation. Together they argue that much of LLM safety behavior is determined before full-sequence decoding.
