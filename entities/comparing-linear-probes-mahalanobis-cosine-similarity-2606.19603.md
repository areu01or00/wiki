---
title: "Comparing Linear Probes with Mahalanobis Cosine Similarity"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [interpretability, linear-probe, probing, representation-learning, mahalanobis, cosine-similarity, cross-domain-generalization]
sources: ["https://arxiv.org/abs/2606.19603"]
---

# Comparing Linear Probes with Mahalanobis Cosine Similarity

## Overview
Ying, Hase, and Kriegeskorte argue that the standard practice of comparing linear probes via raw cosine similarity is structurally miscalibrated — different layers of the same network induce probes whose geometry is dominated by layer-specific activation statistics, so a "0.95 cosine similarity" between a mid-layer and late-layer probe can mask the fact that the two probes are tracking *different* features in their respective layers' native coordinate frames. They introduce Mahalanobis Cosine Similarity (MCS), a task-aware refinement that reweights the inner product between two probe directions by the test-data covariance, and show that MCS — unlike raw cosine similarity — has near-perfect predictive power for cross-domain generalization (R² = 0.98) when comparing probes across layers, models, and training regimes.

## Key Facts
- **Authors**: Zhuofan Josh Ying, Peter Hase, Nikolaus Kriegeskorte
- **Year**: 2026
- **arXiv**: [2606.19603](https://arxiv.org/abs/2606.19603)
- **Subjects**: cs.LG, cs.CL
- **Submitted**: 2026-06-17

## Key Contributions
- Identifies a systematic conflation in linear-probe comparison: raw cosine similarity between probe directions depends on the layer's activation covariance, so probes from layers with different variance structure cannot be meaningfully compared without re-weighting — a methodological-level problem in interpretability research where cross-layer and cross-model probe comparisons are routine.
- Proposes Mahalanobis Cosine Similarity (MCS), a test-data-covariance-weighted inner product that recovers a task-aware refinement of cosine similarity and reduces to standard cosine similarity in the isotropic-covariance limit.
- Empirically validates that MCS near-perfectly predicts cross-domain generalization (R² = 0.98) across a sweep of probes on the same model and across models, while raw cosine similarity fails to predict the same generalization pattern — surfacing *probe geometry under the right metric* as a load-bearing primitive for interpretability cross-comparison.
- Demonstrates practical consequences: probe selection (e.g., "which layer learns the most invariant representation?") and model-comparison conclusions that are inverted under raw cosine similarity become consistent and theoretically grounded under MCS, providing a methodology-correctness fix rather than yet another probe design.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 (representation-learning / probing / interpretability theme).
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Sibling entry on interpretability-driven detection; both papers reason about hidden-state-level statistics as observable probes (entropy trajectories vs probe-direction geometry) and argue that the *right probe on hidden-state statistics* is the load-bearing primitive for downstream claims.
- [[hydrahead-from-head-level-functional-heterogeneity-to-specialized-attention-hybridization-2606.20097]] — Sibling entry on head-level functional heterogeneity; HydraHead is a structural-level diagnosis of attention-head specialization, MCS-Ying is a probe-comparison-level diagnosis of layer-level representation similarity — both papers push back against treating layer/head outputs as interchangeable primitives and surface the metric-correctness axis as a methodology concern.
- [[forecasting-future-behavior-as-a-learning-task-2606.11445]] — Sibling entry on behavior-forecasting evaluation; both papers emphasize *task-aware metric construction* — MCS reweights by test-data covariance, Forecasting Future Behavior argues that forecasting accuracy must be measured on the right temporal horizon — extending the eval-as-discipline wave into the linear-probe comparison surface.