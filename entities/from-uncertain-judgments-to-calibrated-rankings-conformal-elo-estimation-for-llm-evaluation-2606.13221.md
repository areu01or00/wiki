---
title: "From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [calibration, benchmarking, llm-evaluation, conformal-prediction]
sources: ["https://arxiv.org/abs/2606.13221"]
---

# From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation

## Overview
LLM-as-a-judge is a scalable alternative to human annotation, but judge scores carry systematic errors — position bias, self-preference, and intransitivity — that miscalibrate resulting rankings. This paper applies **conformal prediction to the LLM-as-a-judge pipeline**, reframing evaluation as an Elo-like ranking problem and providing coverage guarantees at both the individual score level and the ranking level. The conformal Elo estimator produces ranking intervals with finite-sample coverage, surfacing which model comparisons are reliable and which require human adjudication.

## Key Facts
- **Authors**: Kargi, Bora; Salinas, David
- **Year**: 2026
- **arXiv**: [2606.13221](https://arxiv.org/abs/2606.13221)
- **Published**: 2026/06/11

## Key Contributions
- **Conformal Elo framework**: Provides finite-sample coverage guarantees for pairwise LLM comparisons, replacing point estimates with prediction sets that contain the true ranking with user-specified probability
- **Quantifies judge-human disagreement**: Characterizes systematic judge errors (position bias, self-preference, intransitivity) at two complementary levels — individual scores and ranking positions
- **Practical deployment**: Shows which model comparisons can be trusted automatically and which require human annotation, reducing annotation cost by ~40% while maintaining coverage guarantees
- **First conformal ranking method for LLM evaluation**: Prior CP work on LLM evaluation focused on single-output coverage; this paper extends to full ranking intervals

## Related Papers
- [[clustered-self-assessment-uncertainty-quantification-llms-2606.03846]] — Self-assessment uncertainty quantification for LLMs
- [[aura-adaptive-uncertainty-aware-refinement-llm-judge-2606.19714]] — Adaptive uncertainty-aware refinement for LLM judges
- [[qval-cheaply-evaluating-dense-supervision-signals-for-long-horizon-llm-agents-2606.32034]] — QVal: dense supervision signal evaluation for LLM agents (newly added this run)
