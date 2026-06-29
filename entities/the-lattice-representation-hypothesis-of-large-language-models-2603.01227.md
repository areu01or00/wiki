---
title: "The Lattice Representation Hypothesis of Large Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [representation-geometry, linear-representation-hypothesis, formal-concept-analysis, symbol-grounding, interpretability]
sources: ["https://arxiv.org/abs/2603.01227"]
arxiv_id: "2603.01227"
---

# The Lattice Representation Hypothesis of Large Language Models

## Overview
The Lattice Representation Hypothesis proposes that LLM embeddings encode conceptual hierarchies and logical operations as a symbolic structure — a concept lattice — induced by half-space intersections of linear attribute directions. This unifies the Linear Representation Hypothesis with Formal Concept Analysis (FCA), establishing a principled bridge between continuous embedding geometry and symbolic abstraction.

## Key Facts
- **Authors**: Bo Xiong et al.
- **Year**: 2026
- **arXiv**: [2603.01227](https://arxiv.org/abs/2603.01227)

## Key Contributions
- **Lattice Representation Hypothesis**: symbolic backbone that grounds conceptual hierarchies and logical operations in embedding geometry, unifying the Linear Representation Hypothesis with Formal Concept Analysis.
- **Mechanism**: linear attribute directions with separating thresholds induce a concept lattice via half-space intersections; each concept is a region defined by which attribute-direction thresholds are crossed.
- **Symbolic operations through geometry**: lattice meet (intersection) and join (union) operations on concepts have direct geometric implementations as half-space intersections and unions.
- **Canonical form**: when attribute directions are linearly independent, the lattice has a canonical form that recovers concept membership from embedding projections.
- **Empirical evidence on WordNet sub-hierarchies**: LLM embeddings encode concept lattices and their logical structure, validating that the lattice hypothesis captures genuine structure rather than post-hoc fitting.
- **First principled bridge** between continuous geometry and symbolic abstraction, providing a formal framework for how LLM representations can support symbolic reasoning without invoking discrete-symbol machinery at inference time.

## Related Papers
- [[comparing-linear-probes-mahalanobis-cosine-similarity-2606.19603]] — Sibling paper comparing linear probe geometries (Mahalanobis vs cosine); Lattice Representation builds directly on the Linear Representation Hypothesis that Comparing-Linear-Probes studies.
- [[interpretability-can-be-actionable-2605.11161]] — Sibling from Run 58 arguing interpretability should be evaluated by concreteness × validation; Lattice Representation provides a concrete interpretability framework that meets the concreteness bar.
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Sibling paper on geometry of refusal in safety-aligned LLMs; Lattice Representation Hypothesis provides a formal structure for how "refusal" attribute direction interacts with lattice semantics.
- [[manifold-bandits-bayesian-curriculum-learning-over-the-latent-geometry-of-large-language-models-2606.19750]] — Adjacent paper on latent geometry of LLMs as a bandit curriculum learning problem; Lattice Representation Hypothesis gives a discrete-algebraic counterpart to Manifold-Bandits' differential-geometric view.
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Sibling from Run 61 on latent-reasoning features via SAE; Lattice Representation Hypothesis provides a symbolic counterpart to Latent-Computational-Mode's neural-feature view of computation.