---
title: "Uncovering the Representation Geometry of Minimal Cores in Overcomplete Reasoning Traces"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [representation-geometry, reasoning-traces, chain-of-thought, mechanistic-interpretability, compression]
sources: ["https://arxiv.org/abs/2605.14358"]
---

# Uncovering the Representation Geometry of Minimal Cores in Overcomplete Reasoning Traces

## Overview
This paper studies how much of a long chain-of-thought trace is actually necessary for preserving the final prediction, recasting overcomplete reasoning as a representation-geometry problem and identifying a "minimal core" — a geometrically characterized subset of trace tokens that carries the predictive geometry of the full trace. The work bridges chain-of-thought compression and representation geometry by asking: when an LLM generates 1000+ tokens of reasoning, what is the representation-geometry signature of the subset that actually determines the answer?

## Key Facts
- **Authors**: Chowdhury, Sanjoy; Manocha, Dinesh
- **Year**: 2026
- **arXiv**: [2605.14358](https://arxiv.org/abs/2605.14358) (submitted 14 May 2026)

## Key Contributions
- Formalizes overcomplete chain-of-thought traces through a representation-geometry lens: the long trace is treated as a point cloud in token-representation space, and the minimal core is the smallest subset of trace tokens whose representation geometry is sufficient to recover the full trace's prediction.
- Identifies a geometrically-coherent minimal core that, despite comprising only a small fraction of the trace, preserves the final answer — empirically demonstrating that chain-of-thought is geometrically overcomplete.
- Bridges reasoning-trace compression (a long-standing inference-cost concern) with representation-geometry analysis (a mechanistic-interpretability concern), opening a new research direction: instead of asking "which tokens are most important?" (a token-level question), the paper asks "what is the geometric structure of the trace in representation space?" (a representation-geometry question).
- Provides empirical evidence that LLM reasoning traces are not just semantically redundant (multiple paths to the answer) but geometrically redundant (multiple sub-regions of representation space that individually suffice).

## Related Papers
- [[emergence-of-a-high-dimensional-abstraction-phase-in-language-transformers-2405.15471]] — Sibling from same run: surfaces *training-stage* representation geometry (abstraction-phase emergence); this paper surfaces *trace-internal* representation geometry (minimal cores).
- [[shared-global-and-local-geometry-of-language-model-embeddings-2503.21073]] — Sibling from same run: surfaces *cross-model* representation-geometry invariance; this paper surfaces *cross-token* representation-geometry invariance within a single trace.
- [[emergent-concepts]] — Parent meta-page that led to this discovery (Run 103 REPRESENTATIONAL-GEOMETRY-PROBE per Rule 70).
- [[early-warning-signals-of-grokking-via-loss-landscape-geometry-2602.16967]] — Prior run (Run 97 emergent-capabilities probe) that surfaces *loss-landscape geometry* as a primitive class; this paper extends geometry into *representation-space geometry* — same primitive-class (geometry-as-primitive) but at a different substrate (representation vs. loss).
- [[manifold-bandits-bayesian-curriculum-learning-over-the-latent-geometry-of-large-language-models-2606.19750]] — Prior representation-geometry primitive that probes the *latent geometry* of LLMs via Bayesian curriculum learning; complements this paper's *trace-internal representation geometry*.
