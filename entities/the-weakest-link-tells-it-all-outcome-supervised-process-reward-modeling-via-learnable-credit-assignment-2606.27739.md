---
title: "The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [process-reward-modeling, credit-assignment, causal-reasoning, llm-reasoning]
sources: ["https://arxiv.org/abs/2606.27739"]
---

# The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment

## Overview
LCA (Learnable Credit Assignment) addresses the fundamental credit assignment challenge in outcome-supervised Process Reward Models (PRMs): learning process-level feedback from only final-answer correctness. It formalizes outcome-supervised PRM as a Multiple Instance Learning (MIL) problem and introduces the Weakest Link Assignment principle — a reasoning chain is only as strong as its weakest step — operationalized via Softmax-Weighted-Sum (SWS) pooling. LCA proves Bayes consistency and consistently outperforms state-of-the-art outcome-supervised PRMs across multiple reasoning tasks and backbone models.

## Key Facts
- **Authors**: Tianyu Jia, Yue Fang, Hongxin Ding, Rihong Qiu, Zhibang Yang, Zhijing Wu, Xu Chu, Junfeng Zhao, Yasha Wang
- **Year**: 2026
- **arXiv**: [2606.27739](https://arxiv.org/abs/2606.27739)
- **Subjects**: Machine Learning (cs.LG)

## Key Contributions
- **Weakest Link Assignment principle**: A reasoning chain's quality is determined by its weakest step; credit is anchored to step correctness rather than uniform or causal baselines
- **MIL formalization**: Formalizes outcome-supervised PRM as a Multiple Instance Learning problem to handle mutual dependence and redundancy among reasoning states
- **Softmax-Weighted-Sum (SWS) pooling**: An MIL pooling technique tailored for strong dependence and redundancy, enabling joint learning of credit assignment and reward modeling
- **Bayes consistency proof**: Provides theoretical guarantees under mild assumptions
- **State-of-the-art results**: Consistently outperforms existing outcome-supervised PRMs across GSM8K, StrategyQA, and ARC-Challenge with Llama-3-8B-Instruct and Mistral-7B-Instruct backbones

## Related Papers
- [[off-the-shelf-llms-as-process-scorers-training-free-prm-alternative-chunk-level-guided-generation-2606.01682]] — Training-free PRM alternative via off-the-shelf LLM scoring; LCA complements by learning credit assignment rather than fixed-length chunk decomposition
- [[unsupervised-process-reward-models-2605.10158]] — Unsupervised PRM discovery; LCA extends by learning from outcome supervision rather than auto-regressivenext-token prediction
- [[est-prm-stress-testing-process-reward-models-before-they-become-load-bearing-2606.00437]] — Stress-testing PRMs; LCA addresses the credit assignment challenge that PRMs face when used as load-bearing reasoning infrastructure
- [[veribound-pac-bayesian-generalization-bounds-for-process-reward-models-trained-with-formal-verification-tools-2606.20740]] — PAC-Bayesian bounds for PRMs; LCA provides the learnable credit assignment mechanism that formal verification tools require for principled reward modeling
- [[memory-r2-fair-credit-assignment-for-long-horizon-memory-augmented-llm-agents-2605.21768]] — Fair credit assignment for memory-augmented agents; LCA's weakest-link principle provides a principled credit attribution framework applicable to multi-step agentic reasoning
