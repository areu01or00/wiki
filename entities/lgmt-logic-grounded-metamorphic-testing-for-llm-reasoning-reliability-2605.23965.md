---
title: "LGMT: Logic-Grounded Metamorphic Testing for Evaluating the Reasoning Reliability of LLMs"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [invariance, metamorphic-testing, first-order-logic, reasoning-reliability, prompt-perturbation, llm-evaluation]
sources: ["https://arxiv.org/abs/2605.23965"]
---

# LGMT: Logic-Grounded Metamorphic Testing for Evaluating the Reasoning Reliability of LLMs

## Overview
First **first-order-logic (FOL)-derived metamorphic testing primitive for LLM reasoning reliability**. LGMT constructs *semantically invariant test cases* by deriving metamorphic relations from formal logical equivalences and detects reasoning defects through cross-case consistency checking — exposing substantial hidden defects missed by traditional reference-based evaluations. The framework operates as an *oracle-free* reliability primitive that quantifies how robust an LLM's reasoning is under logically equivalent transformations, surfacing symbol-level and conclusion-level sensitivities that advanced prompting (Few-shot CoT) only partially mitigates.

## Key Facts
- **Authors**: LGMT authors (per arxiv 2605.23965) — published 2026-05-12, online 2026-06-07
- **Year**: 2026
- **arXiv**: [2605.23965](https://arxiv.org/abs/2605.23965) (online 2026-06-07, submitted 2026-05-12)

## Key Contributions
- **First FOL-derived metamorphic-testing-as-LLM-primitive in the wiki**: leverages first-order logic to derive metamorphic relations from formal logical equivalences and constructs *semantically invariant* test cases — moving LLM evaluation beyond isolated correctness toward robustness under logical invariance.
- **Oracle-free consistency-checking primitive**: detects reasoning defects through cross-case consistency checking on the FOL-derived test cases, removing dependence on expensive human-written reference answers.
- **Symbol-level + conclusion-level sensitivity primitives**: identifies that LLM reasoning reliability is particularly fragile under symbol-level and conclusion-level variations — a fine-grained taxonomy of perturbation-induced failure modes.
- **Few-shot-CoT-partial-mitigation primitive**: documents that even advanced prompting (Few-shot CoT) only partially mitigates these invariance failures — distinguishing prompting-time fixes from architecture-level reliability primitives.
- **Six-LLM empirical demonstration primitive**: experiments on six state-of-the-art LLMs expose substantial hidden defects missed by traditional reference-based evaluations, validating LGMT as a principled and scalable reasoning-failure diagnostic.

## Related Papers
- [[forex-a-formal-verification-framework-for-explainable-reasoning-in-logical-fallacy-detection-and-annotation-2606.21867]] — Sibling formal-verification primitive for logical-fallacy detection (Rule 63 axiomatic-formalization); LGMT narrows the scope from *proof-assistant verification of natural-language explanations* to *FOL-derived metamorphic invariance testing for reasoning reliability*.
- [[formalizing-latent-thoughts-four-axioms-of-thought-representation-in-llms-2606.27378]] — Sibling axiomatic-formalization primitive (Rule 63) introducing four-axiom (Causality/Minimality/Separability/Stability) framework for latent thought representations; LGMT complements by extending *axiomatic-grounding* into the *invariance-under-input-perturbation* dimension.
- [[logicgraph-benchmarking-multi-path-logical-reasoning-via-neuro-symbolic-generation-and-verification-2602.21044]] — Sibling neuro-symbolic-grounding primitive (Rule 47) for multi-path logical reasoning; LGMT operates at the *invariance-testing* layer rather than the *neuro-symbolic-generation* layer.
- [[emergent-concepts]] — Parent meta-page tracking emergent-concept search discoveries.