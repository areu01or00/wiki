---
title: "Formalizing Latent Thoughts: Four Axioms of Thought Representation in LLMs"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [interpretability, latent-reasoning, axiomatic-evaluation, representation-quality]
sources: ["https://arxiv.org/abs/2606.27378"]
arxiv_id: "2606.27378"
---

# Formalizing Latent Thoughts: Four Axioms of Thought Representation in LLMs

## Overview
First paper in the wiki to introduce an *axiomatic evaluation framework for latent thought representations in LLMs* — defining four functional axioms (Causality, Minimality, Separability, and Stability) and computing quantitative measures for each independently of downstream benchmark accuracy. Surfaces *latent-state-as-axiom-system-primitive* and *representation-quality-decoupled-from-task-performance-primitive* as load-bearing primitives for distinguishing representational failures from model-capacity failures — the structural gap benchmark accuracy has been silently masking.

## Key Facts
- **Authors**: Seddik, Fahd; Fard, Fatemeh
- **Year**: 2026
- **arXiv**: [2606.27378](https://arxiv.org/abs/2606.27378)
- **Online date**: 2026-05-07

## Key Contributions
- **Four-axiom framework**: formalizes four functional axioms of latent thought representation — Causality (representation depends on input, not artifacts), Minimality (no redundant dimensions), Separability (task-relevant distinctions preserved), Stability (robust to perturbations) — each with a quantitative measure computed directly on the representation, independent of downstream accuracy.
- **Audit of 23 reasoning tasks across model families**: applied the framework to open-weight LLMs across dense, reasoning-distilled, and RL-trained families; finds that *no candidate satisfies all four axioms simultaneously* — surfacing the gap between benchmark performance and representational quality.
- **Distinguishes task-type from within-task distinctions**: representations distinguish task type reliably but cannot distinguish between two questions within the same task — a structural separation property benchmark scores cannot expose.
- **Structural rather than capacity-bound failure**: representations encode little information beyond what is already present in the input embedding; the failure is consistent across dense, reasoning-distilled, and RL-trained model families, indicating the gap is structural rather than a property of model size or training procedure.

## Related Papers
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Sibling paper isolating latent reasoning features via SAE; Formalizing Latent Thoughts adds the axiomatic-decoupling-from-task-performance axis
- [[reasoninglens-hierarchical-visualization-and-diagnostic-auditing-for-large-reasoning-models-2606.23404]] — Reasoning-trace visualization and auditing; Formalizing Latent Thoughts is the formal-axiom counterpart
- [[reasoning-models-struggle-to-control-their-chains-of-thought-2603.05706]] — Controllability gap; Formalizing Latent Thoughts provides the representational-axiom primitives for diagnosing it
- [[interpretability-can-be-actionable-2605.11161]] — Position paper on actionable interpretability; Formalizing Latent Thoughts is the axiom-system instance
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Circuit-level interpretability; Formalizing Latent Thoughts is the representation-axiom counterpart
- [[verytrace-verifying-reasoning-traces-through-compilable-formalism-2606.24124]] — Run 96 sibling: compiles traces via DSL; Formalizing Latent Thoughts formalizes via axioms
- [[forex-a-formal-verification-framework-for-explainable-reasoning-in-logical-fallacy-detection-and-annotation-2606.21867]] — Run 96 sibling: Lean4 verification of explanations; Formalizing Latent Thoughts axiomatizes the latent representation itself
- [[hidden-thoughts-are-not-secret-reasoning-trace-exposure-in-llms-2606.00642]] — Trace-exposure analysis; Formalizing Latent Thoughts surfaces the representation quality the trace exposes