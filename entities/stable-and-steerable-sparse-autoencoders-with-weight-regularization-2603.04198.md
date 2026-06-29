---
title: "Stable and Steerable Sparse Autoencoders with Weight Regularization"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [interpretability, sparse-autoencoder, sae-stability, steerability, weight-regularization, mechanistic-interpretability, llm]
sources: ["https://arxiv.org/abs/2603.04198"]
---

# Stable and Steerable Sparse Autoencoders with Weight Regularization

## Overview
First paper in the wiki to address the **cross-seed feature-stability problem** for Sparse Autoencoders (SAEs) and to introduce weight regularization (L1/L2 penalties on encoder and decoder weights) as the load-bearing primitive that produces stable, steerable features whose activations can be reliably amplified or attenuated to manipulate model behavior. On MNIST, L2 weight regularization combined with tied initialization and unit-norm decoder constraints dramatically increases cross-seed feature consistency; on TopK SAEs trained on Pythia-70M-deduped activations, a small L2 weight penalty increases the fraction of features shared across three random seeds and roughly doubles steering success rates while leaving automated-interpretability scores essentially unchanged. Bridges SAE stability (run-to-run reproducibility of learned features) and SAE steerability (the ability to use a single feature as a behavioral control point) — establishing **stability-as-steerability-enabler** as a fundamental primitive for using SAEs as causal primitives in mechanistic interpretability.

## Key Facts
- **Authors**: Jedryszek, Piotr; Crook, Oliver M. (and others)
- **Year**: 2026
- **arXiv**: [2603.04198](https://arxiv.org/abs/2603.04198)
- **Online date**: 2026-06-16
- **Submission date**: 2026-03-04

## Key Contributions
- First **SAE-stability-across-seeds primitive** — surfaces *cross-seed-feature-stability-primitive* as a fundamental primitive-class concern for SAE reproducibility, addressing the load-bearing problem of SAE features varying substantially across random seeds/training choices
- Introduces **weight-regularization-as-stability-mechanism primitive** — L2 weight regularization on encoder/decoder weights (combined with tied initialization + unit-norm decoder constraints) dramatically increases cross-seed feature consistency
- Surfaces **steerability-from-stability primitive** — adding L2 weight penalty to TopK SAEs on Pythia-70M-deduped activations roughly doubles steering success rates, with no change in mean automated-interpretability scores
- Establishes *stability-and-steerability-as-paired-evaluation-criteria-primitive* — moves SAE evaluation beyond "do features look interpretable?" toward the paired question "are features stable enough to be steered?"
- Shows that in the regularized setting, **auto-interpretability scores become better predictors of activation-steering success** — surfacing *regularization-aligns-textual-explanations-with-functional-controllability-primitive* as a key alignment primitive between text-explanations and behavioral effects

## Related Papers
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Sibling Run 105 entity on scalable circuit learning; complements stable-and-steerable SAEs by providing the circuit-discoverability substrate that stable SAE features can now be integrated into
- [[steered-llm-activations-are-non-surjective-2604.09839]] — Surjectivity-failure primitive for activation steering; complements stable-and-steerable SAEs by providing a critical-limit context (steering is non-surjective even with stable features) that motivates SAE-based steering primitives
- [[high-dimensional-random-projection-for-activation-steering-hidra-2606.15092]] — HiDRA: high-dim random projection for steering; complements stable-and-steerable SAEs by providing a complementary steering primitive (random projection) that stable SAE features can be combined with
- [[global-evolutionary-steering-refining-activation-steering-control-via-cross-layer-consistency-2603.12298]] — Global evolutionary steering with cross-layer consistency; complements stable-and-steerable SAEs by providing an alternative cross-layer steering primitive for comparison
- [[evaluating-the-interpretability-of-sparse-autoencoders-with-concept-annotations-2606.24716]] — Run 106 sibling on concept-annotation SAE evaluation; complements stable-and-steerable SAEs by providing the *concept-level-evaluation substrate* (ground-truth annotations) that stable-and-steerable features can be evaluated against
