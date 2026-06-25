---
title: "FastMix: Fast Data Mixture Optimization via Gradient Descent"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [training-data, data-mixture, pretraining, bilevel-optimization, llm-training]
sources: ["https://arxiv.org/abs/2606.14971"]
---

# FastMix: Fast Data Mixture Optimization via Gradient Descent

## Overview
Reformulates data mixture selection for LLM pre-training and post-training as a bilevel optimization problem in which mixture coefficients and model parameters are jointly learned via a single proxy-model training run, with per-source loss weights derived from gradient-based updates. Tan, Haoru; Wu, Sitong; Chen, Yanfeng; Xia, Jun; Xie, Ruobing; Xia, Bin; Sun, Xingwu; Qi, Xiaojuan show the approach substantially reduces search cost versus prior heuristic or simulation-based data-mixture discovery while outperforming baselines on both pre- and post-training data-mixture tasks.

## Key Facts
- **Authors**: Tan, Haoru; Wu, Sitong; Chen, Yanfeng; Xia, Jun; Xie, Ruobing; Xia, Bin; Sun, Xingwu; Qi, Xiaojuan
- **Year**: 2026
- **arXiv**: [2606.14971](https://arxiv.org/abs/2606.14971)
- **Subjects**: cs.LG, cs.CL
- **Date**: 2026-06-12

## Key Contributions
- Reformulates data-mixture selection as bilevel optimization: mixture ratios are mathematically equivalent to assigning per-source loss weights under uniform source sampling, embedding mixture coefficients into the differentiable iterative optimization objective
- Implements an approximate iterative procedure alternating (i) inner-loop model-parameter updates on data sampled according to current mixture ratios and (ii) outer-loop mixture-ratio updates from validation feedback — gradient-based, no predefined heuristics, no resource-intensive simulations
- Trains only a single proxy model end-to-end rather than multiple model variants, substantially reducing search cost over prior methods
- Reports consistent improvements over baselines across both pre- and post-training data-mixture tasks while drastically reducing the compute required to discover a competitive mixture
- Code released at https://github.com/hrtan/fastmix

## Related Papers
- [[holistic-data-scheduler-for-llm-pre-training-via-multi-objective-reinforcement-learning-2606.24133]] — LLM pre-training data scheduler via multi-objective RL
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Online data-mixing actor-critic for sample-efficient LLM pretraining
- [[demystifying-training-time-augmentation-for-data-constrained-language-model-pretraining-2606.16246]] — Training-time augmentation for data-constrained LLM pretraining
