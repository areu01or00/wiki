---
title: "Position: Uncertainty Quantification in LLMs is Just Unsupervised Clustering"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [uncertainty-quantification, calibration, theory, llm]
sources: ["https://arxiv.org/abs/2605.19220"]
---

# Position: Uncertainty Quantification in LLMs is Just Unsupervised Clustering

## Overview
This position paper argues that mainstream UQ methods for LLMs are fundamentally misaligned with what they claim to measure — they are, in practice, unsupervised clustering algorithms that partition the model's internal representations without any ground-truth calibration signal. The authors demonstrate this through systematic experiments showing that popular UQ methods (softmax entropy, MC dropout, hidden-state distance metrics) produce cluster-like structures that correlate poorly with actual prediction errors. The paper's central contribution is a theoretical and empirical reframing: UQ in LLMs should be redefined around what is actually measurable and meaningful, not around assumed distributional properties that don't hold in practice.

## Key Facts
- **Authors**: N/A (arxiv 2605.19220)
- **Year**: 2025
- **arXiv**: [2605.19220](https://arxiv.org/abs/2605.19220)

## Key Contributions
- Position paper: UQ methods for LLMs are unsupervised clustering, not true uncertainty estimation
- Proposes that "uncertainty" in LLMs as currently measured is a category error
- Shows softmax entropy, MC dropout, hidden-state distance all produce cluster-like structures
- Calls for redefining UQ metrics around measurable properties (e.g., calibration error on held-out tasks)
- First formal critique of the epistemological foundations of LLM uncertainty quantification in the wiki

## Related Papers
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Intra-layer local information scores for LLM uncertainty estimation
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Calibration collapse under fine-tuning reward hacking
- [[calidist-calibrating-large-language-models-via-behavioral-robustness-to-distraction-2606.05799]] — Calibrating LLMs via behavioral robustness to distraction
