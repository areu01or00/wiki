---
title: "Uncertainty Quantification via Invariant-Measure Conformal Prediction"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [calibration, safety, uncertainty, conformal-prediction]
sources: ["https://arxiv.org/abs/2606.31607"]
---

# Uncertainty Quantification via Invariant-Measure Conformal Prediction

## Overview
Standard conformal prediction (CP) provides finite-sample coverage guarantees under the exchangeability assumption. This paper extends CP to **learned stochastic dynamical systems** — environments where trajectory data are temporally dependent, state distributions evolve over time, and recursive predictions break the exchangeability assumption. The invariant-measure CP framework replaces the i.i.d. assumption with stationarity, enabling valid uncertainty quantification in safety-critical control and monitoring pipelines where standard CP would fail.

## Key Facts
- **Authors**: Bakhtiaridoust, Mohammadhossein; Baumann, Dominik; Deka, Shankar
- **Year**: 2026
- **arXiv**: [2606.31607](https://arxiv.org/abs/2606.31607)
- **Published**: 2026/06/30

## Key Contributions
- **Invariant-measure conformal prediction**: Replaces exchangeability with stationarity assumption, providing finite-sample coverage guarantees for temporally dependent data streams
- **Dynamical systems extension**: Shows that standard split-CP fails catastrophically under recursive prediction in evolving state distributions; invariant-measure CP succeeds where it fails
- **Safety-critical deployment readiness**: Framework validated on control and monitoring pipelines where CP-based uncertainty is the load-bearing signal for human-in-the-loop decisions
- **Distinction from existing conformal LLM work**: Prior LLM CP work (layerwise CP, ITCP, CoFT) assumes exchangeability; this paper shows that deployed LLM pipelines are non-exchangeable and need the invariant-measure variant

## Related Papers
- [[llms-uncertainty-quantification-via-adaptive-conformal-semantic-entropy-2605.04295]] — Adaptive conformal semantic entropy for LLM uncertainty quantification
- [[itcr-inference-time-conformal-reasoning-with-valid-factuality-control-for-llms-2606.08831]] — Inference-time conformal reasoning for factuality control
- [[origins-of-stochasticity-comprehensive-investigations-on-uncertainty-quantification-for-llms-2606.22792]] — Stochasticity origins in LLM uncertainty quantification
