---
title: "Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, probability-of-causation, PNS, necessity, sufficiency, null-model-comparison, theoretical-framework]
sources: ["https://arxiv.org/abs/2408.08210"]
---

# Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models

## Overview
González and Nori introduce a theoretical-practical framework that uses the **Probability of Necessity (PN)** and **Probability of Sufficiency (PS)** — two probabilistic measures essential for connecting causes to their effects in causal inference — to assess how effectively LLMs replicate real-world reasoning mechanisms, treating LLMs as abstract machines that process information through a natural language interface and examining the conditions under which suitable approximations of PN and PS can be computed. The paper marks a foundational step toward a deeper understanding of *when* LLMs are capable of reasoning, illustrated by math examples.

## Key Facts
- **Authors**: González, Javier; Nori, Aditya V.
- **Year**: 2024
- **arXiv**: [2408.08210](https://arxiv.org/abs/2408.08210)
- **Online Date**: 2024-08-15
- **Citation Date**: 2024-08-15

## Key Contributions
- **PN/PS framework for LLM reasoning**: introduces the first formal application of the Probability of Necessity (PN) and Probability of Sufficiency (PS) — two foundational primitives from causal inference — to characterize when LLMs are capable of reasoning, providing the first necessity-sufficiency-based null-model-comparison primitive in the wiki
- **Likelihood-of-Causation suite (PNS)**: extends PN/PS to the joint Probability of Necessity and Sufficiency (PNS) as a single scalar measure of causation, providing a unified primitive for assessing whether LLM outputs reflect true cause-effect reasoning versus surface-pattern matching
- **Abstract-machine natural-language interface view**: frames LLMs as abstract machines that process information through a natural language interface and derives the conditions under which PN/PS/PNS can be computed from input-output observations alone, providing a theoretical foundation for controlled-comparison studies
- **Necessity-vs-sufficiency decomposition**: separates the *necessity* question (would the conclusion fail without this step?) from the *sufficiency* question (is the step enough on its own to produce the conclusion?) as two distinct primitives that probe different aspects of reasoning capability
- **Math-example illustrations**: provides worked math examples showing how to operationalize PN/PS/PNS computations on LLM outputs, providing a reproducible recipe for controlled-comparison studies
- **First reasoning-emergence formal criterion**: marks the first paper in the wiki to propose a formal criterion (PN/PS/PNS) for the reasoning-emergence debate, anchoring the discussion in causal-inference primitives rather than benchmark scores

## Related Papers
- [[causal-methods-for-llm-development-and-evaluation-2605.25998]] — Sibling causal-methods framework for LLM development/evaluation; both papers use causal-inference primitives to assess LLM behavior
- [[causal-discovery-in-the-era-of-agents-2606.23608]] — Sibling causal-discovery framework in agentic systems; both papers apply causal-inference primitives to LLM/agent settings
- [[towards-a-universal-causal-reasoner-unico-2605.24873]] — Sibling universal causal reasoner; complements the PN/PS framework with a practical universal-reasoner implementation
- [[local-causal-attribution-of-chain-of-thought-reasoning-2606.21821]] — Sibling local-causal-attribution CoT framework; both papers use causal-inference primitives to localize reasoning behavior
- [[the-model-says-walk-how-surface-heuristics-override-implicit-constraints-in-llm-reasoning-2603.29025]] — Sibling minimal-pair heuristic-override controlled-comparison benchmark; both papers use controlled-comparison primitives (PN/PS here, minimal pairs in HOB) to assess LLM reasoning
- [[representation-without-control-testing-the-realization-effect-in-language-models-2605.25151]] — Sibling representational-decoding-causal-control dissociation; both papers surface the gap between representational presence and behavioral/causal control
- [[emergent-concepts]] — Parent page that led to this discovery
