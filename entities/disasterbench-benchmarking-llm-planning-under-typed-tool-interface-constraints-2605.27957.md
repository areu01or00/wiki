---
title: "DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent, planning-failure, benchmark, multi-agent]
sources: ["https://arxiv.org/abs/2605.27957"]
---

# DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints

## Overview
Disasters cause severe societal impacts, demanding rapid coordination of heterogeneous AI tools — from satellite analysis to flood prediction and damage assessment — into coherent multi-step workflows. As LLMs increasingly serve as orchestrators of such pipelines, effective coordination requires more than selecting semantically plausible tools: LLMs must generate executable workflows with correct parameter binding and dependency propagation. DisasterBench evaluates structured multi-agent planning over semantically similar but operationally distinct disaster-response tools.

## Key Facts
- **Authors**: Chen, Zhitong; Yin, Kai; Zhang, Weifeng; Wang, Zhiyuan; Dong, Xiangjue; Liu, Chengkai; Liu, Zhewei; Xiao, Yiming; Mostafavi, Ali; Caverlee, James
- **Year**: 2026
- **arXiv**: [2605.27957](https://arxiv.org/abs/2605.27957)

## Key Contributions
- **DisasterBench**: a benchmark for evaluating structured multi-agent planning over typed, operationally distinct disaster-response tools
- **First-Point-of-Failure (FPoF)**: localizes the earliest root cause in a predicted workflow, separating primary errors from downstream cascade effects
- **Typed tool interface constraint evaluation**: tests whether LLMs can correctly propagate dependencies and bind parameters across operationally distinct tools (distinct from semantically similar tool selection)

## Related Papers
- [[reflect-intervention-supported-error-attribution-for-silent-failures-in-llm-agent-traces-2606.09071]] — sibling: FPoF error attribution extends DisasterBench's failure localization
- [[sequential-consensus-for-multi-agent-llm-debates-a-wald-sprt-compute-governor-with-calibration-based-failure-detection-2605.19193]] — related: multi-agent failure detection methodology
