---
title: "Interpretability Can Be Actionable"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [interpretability, actionability, evaluation-criteria, position-paper, mechanistic-interpretability, deployment, sae, circuits]
sources: ["https://arxiv.org/abs/2605.11161"]
---

# Interpretability Can Be Actionable

## Overview
A position paper arguing that the central missing ingredient in interpretability research is not new methods but evaluation criteria: interpretability should be evaluated by *actionability* — the extent to which insights enable concrete decisions and interventions beyond interpretability research itself. Defines actionable interpretability along two dimensions (concreteness and validation), analyzes barriers to real-world impact, and presents a five-domain framework for actionable interpretability.

## Key Facts
- **Authors**: Orgad, Hadas
- **Year**: 2026
- **arXiv**: [2605.11161](https://arxiv.org/abs/2605.11161)

## Key Contributions
- **Actionability framing**: invert the interpretability evaluation question from "does this method produce explanations?" to "do the explanations enable concrete decisions and interventions?" — the missing-ingredient argument is that methods have proliferated without translation to practical impact
- **Two-dimensional actionability metric**: *concreteness* (can a stakeholder point to a specific decision the insight enables?) × *validation* (does the insight produce a measurable outcome when acted on?) — yielding a four-quadrant grid for evaluating interpretability work
- **Five-domain leverage map**: identifies domains where interpretability offers unique leverage (safety alignment, model debugging, scientific discovery, deployment monitoring, policy/governance) — explicitly contrasting with "interpretability as exploration-only" framing
- **Barriers analysis**: surfaces structural reasons interpretability has not translated to practice — research incentives reward novelty over utility, evaluation metrics reward explanation-quality rather than decision-quality, and the field lacks shared benchmarks for downstream-action validation
- **Evaluation criteria aligned with practical outcomes**: a structured proposal that establishes actionability as a core objective rather than a downstream side-effect — arguing that without this pivot, interpretability research will continue to accumulate methods without translating to impact

## Related Papers
- [[secret-mixtures-of-experts-inside-your-llm-2512.18452]] — Sibling Run 55 mechanistic-interpretability work — Secret-Mixtures uses *SAE structure in dense MLP activations* to mechanistically interpret MoE-like sparsity — Actionable-Interpretability provides the *evaluation-criteria primitive* that asks whether the SAE-MoE insight enables a concrete decision (e.g., designing low-rank routers), Secret-Mixtures is one example of an interpretability finding that survives the actionability bar
- [[emergent-concepts]] — Parent wiki page

## Theme Context
**Domain pivot from agent-failure (Runs 55-57) to data-curation / world-model / interpretability axes (Run 58)**: Runs 55-57 clustered on agent-failure surfaces. Per pitfall-91 domain-diversity tracker, Run 58 deliberately pivots to training-data + world-model + interpretability axes to maintain wiki primitive diversity. Interpretability-Can-Be-Actionable targets the *interpretability-research-evaluation-criteria* surface — structurally orthogonal to agent-failure (which asks "where does the agent fail?") by treating the *meta-question of whether the field's methods translate to deployment decisions* as the load-bearing object.
