---
title: "Evaluating the Interpretability of Sparse Autoencoders with Concept Annotations"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [interpretability, sparse-autoencoder, evaluation, mechanistic-interpretability, concept-annotation, llm]
sources: ["https://arxiv.org/abs/2606.24716"]
---

# Evaluating the Interpretability of Sparse Autoencoders with Concept Annotations

## Overview
First paper in the wiki to introduce a human-grounded, intervention-style evaluation framework for Sparse Autoencoders (SAEs) in vision and vision-language models — replacing proxy metrics or qualitative inspection with explicit measurement of semantic correspondence between SAE latents and human-annotated concepts, validated by targeted attribute perturbations. Introduces two synthetic benchmarks (synCUB, synCOCO) of paired images differing in exactly one attribute, enabling intervention-style SAE evaluation without user studies. Surfaces the **Fully-Binary Matching Pursuit (FBMP)** coalition-based matching procedure (supports many-to-one latent-to-concept mappings, consistently outperforms one-to-one baselines) and the **Targeted Attribute Perturbation Alignment Score (TAPAScore)** (measures whether matched concepts respond selectively and in the expected direction under targeted image-level attribute perturbations).

## Key Facts
- **Authors**: Klotz, Jonas; Dantas, Cassio F.; Jain, Pallavi (and others)
- **Year**: 2026
- **arXiv**: [2606.24716](https://arxiv.org/abs/2606.24716)
- **Online date**: 2026-06-23
- **Submission date**: 2026-06-23

## Key Contributions
- First **concept-annotated SAE-evaluation primitive** — moves SAE evaluation from proxy metrics toward explicit semantic-correspondence measurement against human-annotated concepts, validated by targeted attribute perturbations (not user studies)
- Introduces *synCUB* and *synCOCO* synthetic paired-image benchmarks (each pair differs in exactly one attribute) as the load-bearing evaluation substrate for intervention-style SAE testing in vision and vision-language models
- Formalizes **Fully-Binary Matching Pursuit (FBMP)** as a *coalition-based many-to-one matching procedure* between SAE latents and annotated concepts — surface *many-to-one-concept-matching-primitive* distinct from standard one-to-one concept-matching primitives
- Defines **Targeted Attribute Perturbation Alignment Score (TAPAScore)** as the *functional-validation primitive* — tests whether matched concepts respond selectively and in the expected direction under targeted image-level attribute perturbations
- Establishes **concept-level semantic correspondence** as the gold-standard measurement primitive for SAE evaluation, with sanity checks showing FBMP and TAPAScore are the only evaluated metrics that reliably detect interpretable vs non-interpretable features

## Related Papers
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Sibling Run 105 entity on scalable circuit learning; complements concept-annotation SAE evaluation by providing the *circuit-discoverability* substrate that concept-annotation can now evaluate
- [[interpretability-can-be-actionable-2605.11161]] — Position paper on making interpretability actionable via concreteness × validation; complements concept-annotation SAE evaluation by providing the actionability dimension that SAE interpretability must satisfy
- [[unlocking-the-black-box-of-latent-reasoning-an-interpretability-guided-approach-to-intervention-2606.01243]] — Latent-reasoning-vector identifiability via structural/causal/geometric probes; complements concept-annotation SAE evaluation by providing an alternative identifiability primitive (latent-vector probing) for comparison
- [[stable-and-steerable-sparse-autoencoders-with-weight-regularization-2603.04198]] — Run 106 sibling on SAE stability and steerability; complements concept-annotation SAE evaluation by surfacing *stable-features-as-evaluation-substrate* — concept-annotation measurement is most useful when features are stable across seeds
