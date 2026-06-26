---
title: "Value Alignment Tax: Measuring Value Trade-offs in LLM Alignment"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [alignment, value-tradeoff, framework, schwartz, evaluation]
sources: ["https://arxiv.org/abs/2602.12134"]
authors: ["Chen, Jiajun", "Shen, Hua"]
year: 2026
---

# Value Alignment Tax: Measuring Value Trade-offs in LLM Alignment

## Overview
Introduces **VAT (Value Alignment Tax)**, a framework that quantifies *how alignment-induced changes propagate across interconnected values relative to achieved on-target gain* — capturing the system-level dynamics of value expression under alignment interventions such as prompting, fine-tuning, or preference optimization. Built on Schwartz value theory with paired pre-post normative judgments, VAT surfaces structured co-movement among values that remain largely invisible to target-only evaluation.

## Key Facts
- **Authors**: Chen, Jiajun; Shen, Hua
- **Year**: 2026
- **arXiv**: [2602.12134](https://arxiv.org/abs/2602.12134)
- **Online date**: 2026-04-26 (submitted 2026-02-12)

## Key Contributions
- **Value Alignment Tax (VAT) framework** — quantifies value trade-offs as alignment-induced changes propagating across interconnected values relative to on-target gain; surfaces *intended improvements* AND *unintended side effects* in a single measurement
- **Schwartz-value-theory grounding** — built on a controlled scenario-action dataset grounded in Schwartz's universal-value theory, collecting paired pre-post normative judgments to analyze alignment effects across models, values, and interventions
- **Structured co-movement discovery** — alignment often produces uneven and structured co-movement among values, revealing systematic trade-offs between target and non-target values that are *invisible under conventional target-only evaluation* but *evident via VAT*
- **Process-level alignment-risk evaluation** — VAT enables evaluation of process-level alignment risks (not just endpoint alignment), offering new insights into the *dynamic* nature of value alignment in LLMs
- **Open-sourced dataset and code** — full Schwartz-grounded scenario-action dataset + analysis code released for community benchmarking

## Related Papers
- [[emergent-concepts]] — Parent wiki page
- [[deeper-is-not-always-better-mitigating-the-alignment-tax-via-confident-layer-decoding-2606.21906]] — Sibling alignment-tax-mitigation work; orthogonal axis (Deeper-Is-Not-Always-Better's *layer-decoding mitigation* vs VAT's *value-tradeoff measurement* — together they bracket the alignment-tax surface between *measurement* and *mitigation* primitives)
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — Sibling constraint-tax work; orthogonal axis (Constraint-Tax addresses *structured-output tool-calling suppression*, VAT addresses *value-co-movement-suppression* — together they bracket the *alignment-induced-suppression* surface across both behavioral and value dimensions)
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — Sibling alignment-defense-impossibility work (Run 70); orthogonal axis (Defense-Trilemma proves *wrapper-defense impossibility* via topology, VAT measures *value-alignment unintended-suppression* via Schwartz co-movement — together they bracket the *alignment-defense surface* between formal-impossibility-theorems and empirical-tradeoff-measurement primitives)
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Sibling safety-alignment-geometry work; orthogonal axis (Geometry-of-Refusal analyzes *safety-geometry-as-refusal-mechanism*, VAT analyzes *value-co-movement-as-alignment-effect* — together they bracket the safety-alignment surface between geometry-of-refusal and value-co-movement primitives)
- [[improving-text-to-music-generation-with-human-preference-2606.21670]] — Sibling human-preference-optimization work; orthogonal axis (Improving-Music-Generation uses *human-preference for capability-side optimization*, VAT measures *value-suppression side-effects of human-preference* — together they bracket the preference-optimization surface between capability-improvement and value-tradeoff-measurement primitives)

---
*Run 71 — Rule 38 NEGATIVE-RESULT-PROBE escape hatch (axis: alignment tax measurements / VAT-as-process-level-tradeoff-framework primitive).*
