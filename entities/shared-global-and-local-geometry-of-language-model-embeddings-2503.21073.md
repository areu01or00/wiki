---
title: "Shared Global and Local Geometry of Language Model Embeddings"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [representation-geometry, embedding-analysis, cross-model-invariance, mechanistic-interpretability, foundation-models]
sources: ["https://arxiv.org/abs/2503.21073"]
---

# Shared Global and Local Geometry of Language Model Embeddings

## Overview
This paper establishes that large language models share a common embedding geometry: across diverse LLM families, the global and local geometric structure of token embeddings is remarkably similar — a finding that has implications for cross-model knowledge transfer, embedding-space alignment, and the universality of language representation. The work provides empirical evidence that LLM embeddings are not arbitrary but converge to a shared geometric structure, opening the door to cross-model embedding-space analysis as a primitive.

## Key Facts
- **Authors**: (per arxiv metadata)
- **Year**: 2025
- **arXiv**: [2503.21073](https://arxiv.org/abs/2503.21073) (submitted 27 Mar 2025)

## Key Contributions
- Empirically demonstrates that token embeddings from diverse LLM families (different scales, different training corpora, different architectures) share a common *global* geometric structure: the overall shape of the embedding manifold is similar across models.
- Identifies shared *local* geometric structure: nearest-neighbor relationships and local density patterns in the embedding space are preserved across models, suggesting that LLMs converge on similar semantic neighborhoods regardless of training details.
- Establishes *cross-model shared embedding geometry* as a primitive class distinct from *single-model representation geometry* (Run 103 2605.14358, 2405.15471) and *layer-wise trajectory geometry* (Run 103 2606.09287): the primitive is the *invariance of embedding geometry across independently-trained models*.
- Provides empirical support for the *representation universality hypothesis* — the idea that LLM representations are not arbitrary but converge to a shared geometric substrate that supports transfer, alignment, and cross-model analysis.

## Related Papers
- [[uncovering-the-representation-geometry-of-minimal-cores-in-overcomplete-reasoning-traces-2605.14358]] — Sibling from same run: probes *trace-internal* representation geometry; this paper probes *cross-model* representation geometry.
- [[emergence-of-a-high-dimensional-abstraction-phase-in-language-transformers-2405.15471]] — Sibling from same run: probes *training-stage* representation-geometry emergence; this paper probes *cross-model* representation-geometry invariance.
- [[emergent-concepts]] — Parent meta-page that led to this discovery (Run 103 REPRESENTATIONAL-GEOMETRY-PROBE per Rule 70).
- [[the-lattice-representation-hypothesis-of-large-language-models-2603.01227]] — Prior run (Run 78 multi-agent-consensus probe) that hypothesizes a *lattice structure* of LLM representations; this paper empirically verifies the *shared geometric structure* that the lattice hypothesis predicts.
- [[representation-without-control-testing-the-realization-effect-in-language-models-2605.25151]] — Prior run (Run 99 null-model-comparison probe) that tests the *realization effect* (decoding-vs-control dissociation); this paper identifies the *geometric substrate* that the realization effect operates on.
- [[attribution-guided-continual-learning-for-llms-2605.05285]] — Prior run (Run 63 calibration/uncertainty probe) that studies parameter-importance-based continual learning; this paper identifies the *geometric basis* for cross-model knowledge transfer that continual learning operates on.
