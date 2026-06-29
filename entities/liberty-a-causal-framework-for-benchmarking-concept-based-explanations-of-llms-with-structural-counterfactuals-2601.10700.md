---
title: "LIBERTy: A Causal Framework for Benchmarking Concept-Based Explanations of LLMs with Structural Counterfactuals"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [identifiability, structural-causal-model, counterfactual, concept-explanation, benchmark, faithfulness]
sources: ["https://arxiv.org/abs/2601.10700"]
---

# LIBERTy: A Causal Framework for Benchmarking Concept-Based Explanations of LLMs with Structural Counterfactuals

## Overview
First framework in the wiki that **grounds concept-based explanation benchmarking for LLMs in explicitly defined Structural Causal Models (SCMs)** and generates structural counterfactual pairs by propagating interventions on a concept through the SCM until an LLM produces the counterfactual text. Introduces three datasets (disease detection, CV screening, workplace-violence prediction) and a new evaluation metric, *order-faithfulness*, that measures whether concept-based explanation methods respect the SCM-derived partial order.

## Key Facts
- **Authors**: Gilat Toker, Nitay Calderon, Ohad Amosy, Roi Reichart
- **Year**: 2026
- **arXiv**: [2601.10700](https://arxiv.org/abs/2601.10700) (online 2026-01-18, submitted 2026-01-15)

## Key Contributions
- **First SCM-grounded counterfactual benchmark for LLM concept-based explanations in the wiki**: replaces costly human-written counterfactuals (the prevailing proxy in prior benchmarks) with SCM-derived structural counterfactual pairs — interventions on a concept are propagated through the SCM until the LLM generates the counterfactual.
- **Three structurally-diverse benchmark datasets**: disease detection, CV screening, and workplace-violence prediction — covering high-stakes decision domains where explanation faithfulness is load-bearing.
- **Order-faithfulness metric**: a new evaluation metric that asks whether a concept-based explanation method's predicted effects respect the partial order induced by the SCM — going beyond point-estimate faithfulness to causal-ordering faithfulness.
- **Five-LLM comparative evaluation revealing substantial headroom**: evaluates a wide range of concept-based explanation methods across five LLMs and finds substantial headroom for improvement — directly surfacing which explanation methods actually identify the SCM-grounded concept effects.
- **Systematic analysis of model sensitivity to interventions**: LIBERTy enables a clean decomposition of where LLMs are sensitive vs. insensitive to concept interventions — the load-bearing diagnostic for whether a concept is *identifiable* from text-only LLM behavior.

## Related Papers
- [[causal-methods-for-llm-development-and-evaluation-2605.25998]] — Sibling discovery: causal-methods survey covering intervention + counterfactual + mediation primitives — LIBERTy is the *SCM-grounded-counterfactual-for-explanation-evaluation* primitive the survey identifies as the missing benchmark substrate.
- [[representation-without-control-testing-the-realization-effect-in-language-models-2605.25151]] — Sibling null-model-comparison primitive (Rule 66) testing whether LLM representations *control* behavior; LIBERTy complements this by asking whether *concept-based explanations* control behavior under SCM-grounded interventions.
- [[interpretability-can-be-actionable-2605.11161]] — Sibling interpretability-position paper arguing interpretability should be evaluated by concreteness×validation four-quadrant actionability; LIBERTy is the *SCM-grounded-actionability-benchmark-for-concept-explanations* primitive that operationalizes the actionability quadrant.
- [[does-reasoning-emerge-examining-the-probabilities-of-causation-in-large-language-models-2408.08210]] — Sibling probability-of-causation framework (Rule 66); LIBERTy provides the *SCM-grounded-counterfactual substrate* that probability-of-causation can be evaluated against for LLM explanations.
- [[emergent-concepts]] — Parent meta-page tracking emergent-concept search discoveries.