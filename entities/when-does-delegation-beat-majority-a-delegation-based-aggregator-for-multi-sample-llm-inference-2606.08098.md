---
title: "When Does Delegation Beat Majority? A Delegation-Based Aggregator for Multi-Sample LLM Inference"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [test-time-compute, multi-sample-inference, aggregation, majority-voting, primitive]
sources: ["https://arxiv.org/abs/2606.08098"]
---

# When Does Delegation Beat Majority? A Delegation-Based Aggregator for Multi-Sample LLM Inference

## Overview
Shows that **Propagational Proxy Voting (PPV)** — a delegation-based unsupervised aggregator — beats majority voting on MMLU-Pro by +1.5 pp overall and +2.24 pp on the non-trivial subset (paired McNemar p ≈ 1.0e-14, n = 8,099). PPV exposes two per-voter levers (`When` and `Whom`) that consume the two signals majority discards: within-group letter entropy (drives `When`) and between-group reasoning geometry (drives `Whom`). Partitions 128 sampled generations into 16 groups per question and feeds letter-level semantic entropy + reasoning-embedding centroid into a stochastic delegation matrix whose stationary distribution selects the consensus answer. No gold labels, no auxiliary training.

## Key Facts
- **Authors**: Sakai, Yasushi; Song, Allen; Larson, Kent
- **Year**: 2026
- **arXiv**: [2606.08098](https://arxiv.org/abs/2606.08098)
- **Citation date**: 2026-06-06 (online 2026-06-11)

## Key Contributions
- **Propagational Proxy Voting (PPV)**: an unsupervised consensus rule that exploits the within-group letter entropy and between-group reasoning geometry that majority voting discards.
- **`When × Whom` delegation levers**: `When` controls how much weight each voter keeps on its own pick (driven by letter entropy); `Whom` controls how it splits the remainder across peers (driven by per-question-centered embedding cosine).
- **Geometric-coherence signal**: includes a worked example where PPV overturns a 10-6 majority for the wrong letter — the 10-voter majority cluster is geometrically incoherent (mean within-cluster cosine -0.02) while the 6-voter minority is tight (+0.26), so propagated delegation mass concentrates on the minority.
- **Negative-result design-space constraints**: reports that no within-question ensemble of confidence modes closes the oracle gap, constraining the design space for unsupervised LLM aggregation.

## Related Papers
- [[odar-principled-adaptive-routing-for-llm-reasoning-via-active-inference-2602.23681]] — Sibling run-mate: free-energy-principled fusion replaces ad hoc voting (complementary: PPV exploits letter-entropy + reasoning-geometry; ODAR uses variational-free-energy + varentropy)
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Sibling run-mate: constrained-policy-optimization compute allocation (complementary: PPV aggregates samples; CP-TTCA allocates compute)
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — Sibling unified test-time-scaling framework integrating sequential and parallel modes