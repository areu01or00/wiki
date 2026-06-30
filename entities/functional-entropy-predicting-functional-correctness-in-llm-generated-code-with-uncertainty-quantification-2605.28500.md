---
title: "Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [uncertainty-quantification, code-generation, evaluation]
sources: ["https://arxiv.org/abs/2605.28500"]
---

# Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification

## Overview
Functional Entropy evaluates how well uncertainty quantification (UQ) methods predict functional correctness in LLM-generated code. The paper systematically benchmarks entropy-based, ensemble-based, and Bayesian UQ techniques on code generation tasks, finding that functional entropy — a measure of the distribution spread over functionally correct vs incorrect outputs — correlates strongly with ground-truth correctness.

## Key Facts
- **Authors**: [arXiv](https://arxiv.org/abs/2605.28500)
- **Year**: 2025
- **arXiv**: [2605.28500](https://arxiv.org/abs/2605.28500)

## Key Contributions
- Introduces **functional entropy** as a UQ metric for code generation: measures the entropy of output distribution over functionally correct vs incorrect code candidates
- Systematically evaluates 6 UQ methods (verbal confidence, token entropy, sequence entropy, ensemble disagreement, Monte Carlo dropout, deep ensembles) on HumanEval+ and MBPP+
- Finds that functional entropy outperforms all other UQ methods at predicting code correctness, with ensemble disagreement as the second-best
- Demonstrates that **token-level entropy is poorly calibrated** for code correctness (high token entropy can still produce correct code)
- Proposes **CQR-UQ** (Conformalized Quantile Regression for code UQ) as a post-hoc calibration method

## Related Papers
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Intra-layer uncertainty estimation via local information scores; complementary to functional entropy at the representation level
- [[quantifying-aleatoric-uncertainty-of-in-context-learning-for-robust-measure-of-llm-prediction-confidence-2606.19353]] — ICL confidence quantification; shares the calibration-under-distribution-shift theme with Functional Entropy
- [[from-signals-to-transfer-probe-based-uncertainty-estimation-llm-2606.27679]] — Probe-based uncertainty estimation; orthogonal method for UQ without ensemble overhead
