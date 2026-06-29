---
title: "The Origins of Stochasticity: Comprehensive Investigations on Uncertainty Quantification for Large Language Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [uncertainty-quantification, stochasticity-taxonomy, llm-uncertainty, consensus-based-methods]
sources: ["https://arxiv.org/abs/2606.22792"]
---

# The Origins of Stochasticity: Comprehensive Investigations on Uncertainty Quantification for Large Language Models

## Overview
While traditional uncertainty taxonomy paradigms such as the dichotomy of aleatoric and epistemic uncertainties provide conceptual foundations, they often fail to capture the multi-component and multi-stage nature of LLM generation. This paper proposes a granular uncertainty taxonomy that systematically attributes LLM uncertainty into input-level, parameter-level, token-level, and decoding-process sources, and categorizes existing UQ methods into Bayesian, ensemble, consensus-based, and single-pass approaches.

## Key Facts
- **Authors**: Xiang-Jun Ou, Shuang Liang, Xin-Yu Hu, Rong-Hao Huang, Jing Wang, Shao-Qun Zhang
- **Year**: 2026
- **arXiv**: [2606.22792](https://arxiv.org/abs/2606.22792)
- **Subject**: Artificial Intelligence (cs.AI)
- **Submitted**: 22 Jun 2026

## Key Contributions
- **Granular 4-source uncertainty taxonomy**: Systematically attributes LLM uncertainty to input-level, parameter-level, token-level, and decoding-process sources — finer-grained than traditional aleatoric/epistemic dichotomy
- **4-category UQ method taxonomy**: Categorizes existing UQ methods into Bayesian, ensemble, consensus-based, and single-pass approaches
- **Consensus-based methods outperform**: Typed Deg and EigV consistently outperform other UQ approaches across diverse benchmarks (TriviaQA, GSM8K, HumanEval)
- **Empirical scaling law for LLM uncertainty**: Larger model scales correlate with lower uncertainty estimates — first systematic characterization of uncertainty scaling behavior
- **First comprehensive UQ taxonomy paper in the wiki** that unifies both uncertainty sources and UQ method categories

## Related Papers
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Between-the-Layers: intra-layer uncertainty via local information scores — orthogonal axis (hidden state geometry vs granular source taxonomy)
- [[uncertainty-quantification-for-hallucination-detection-in-llms-2510.12040]] — UQ for hallucination detection — orthogonal axis (UQ for hallucination vs comprehensive UQ taxonomy)
- [[itcr-inference-time-conformal-reasoning-with-valid-factuality-control-for-llms-2606.08831]] — ITCR: structure-level conformal UQ during reasoning generation — orthogonal axis (reasoning-graph structure UQ vs token/decoding process UQ)
