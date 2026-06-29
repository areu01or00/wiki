---
title: "Patch-Effect Graph Kernels for LLM Interpretability"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [interpretability, mechanistic-interpretability, activation-patching, graph-kernel, circuit-comparison, llm]
sources: ["https://arxiv.org/abs/2605.06480"]
---

# Patch-Effect Graph Kernels for LLM Interpretability

## Overview
First paper in the wiki to formalize **patch-effect graph kernels** as the primitive comparison substrate for mechanistic-interpretability circuit analysis — reframing activation-patching profiles as graphs over model components, then comparing them via graph kernels that scale across diverse prompts and task families where raw patch-effect tensors are high-dimensional and unstructured. Evaluated on GPT-2 Small using Indirect Object Identification (IOI) and related tasks, surfacing three graph-construction methods (direct-influence via causal mediation, partial-correlation, co-influence) and demonstrating that localized edge-slot features provide higher classification accuracy than global graph-shape descriptors, with screened paired-patching validation confirming CI/PC-selected candidate edges correspond to stronger activation-influence effects than random or low-rank candidates.

## Key Facts
- **Authors**: Fernandez-Boullon, Ruben; Olivieri, David N. (and others)
- **Year**: 2026
- **arXiv**: [2605.06480](https://arxiv.org/abs/2605.06480)
- **Online date**: 2026-05-07
- **Submission date**: 2026-05-07

## Key Contributions
- First **patch-effect-graph-kernel primitive** — reframes activation-patching profiles as graphs over model components (attention heads, MLPs, residual streams) and embeds/compares them via graph kernels, turning mechanistic-interpretability circuit comparison into a graph-machine-learning problem
- Introduces three graph-construction methods — *direct-influence via causal mediation (CI)* + *partial-correlation (PC)* + *co-influence* — as alternative primitives for constructing patch-effect graphs from activation-patching data
- Surfaces **localized edge-slot features > global graph-shape descriptors** as the discriminative-structural-signal primitive: edge-local features provide higher classification accuracy than global graph-summary statistics, establishing *edge-slot-locality-as-load-bearing-primitive* for kernel-based circuit comparison
- Establishes **screened-paired-patching validation** as a *causal-edge-selection-validation primitive*: shows CI/PC-selected candidate edges correspond to stronger activation-influence effects than random or low-rank candidates — providing the validation substrate that any patch-effect-graph claim should address
- Defines **rigorous-prompt-only and raw-patch-effect control baselines** as *benchmark primitives* that explicitly bound the evidential scope of circuit-level claims by defining strong baselines any kernel-based circuit-discovery claim should outperform

## Related Papers
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Sibling Run 105 entity on scalable circuit learning; complements patch-effect graph kernels by providing scalable-circuit-discoverability substrate that patch-effect graph kernels can now compare across seeds
- [[local-causal-attribution-of-chain-of-thought-reasoning-2606.21821]] — Run 102 sibling on local causal attribution of CoT reasoning; complements patch-effect graph kernels by providing causal-tracing-evaluation evidence that patch-effect-graph-kernel comparison can build on
- [[unlocking-the-black-box-of-latent-reasoning-an-interpretability-guided-approach-to-intervention-2606.01243]] — Latent-reasoning-vector identifiability via structural/causal/geometric probes; complements patch-effect graph kernels by providing an alternative primitive for causal identification of reasoning steps (latent-vector vs graph-based)
- [[evaluating-the-interpretability-of-sparse-autoencoders-with-concept-annotations-2606.24716]] — Run 106 sibling on concept-annotation SAE evaluation; complements patch-effect graph kernels by providing the *concept-annotation-measurement substrate* that patch-effect-graph-kernel circuit comparisons can be cross-validated against
