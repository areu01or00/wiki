---
title: "Efficient and Trainable Language Model Test-Time Scaling via Local Branch Routing"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [test-time-scaling, inference-compute, local-branch-routing, branch-search, llm-reasoning]
sources: ["https://arxiv.org/abs/2606.25354"]
---

# Efficient and Trainable Language Model Test-Time Scaling via Local Branch Routing

## Overview
Local Branch Routing (LBR) is a token-level test-time scaling framework that expands a small local lookahead tree, forwards all sampled branches through the language model, and uses a lightweight router to select the best continuation — replacing the trade-off between single-threaded long-CoT sampling and expensive sentence-level search with trainable local branch search that is end-to-end optimizable.

## Key Facts
- **Authors**: Yin, Yutong; Jin, Mingyu; Pan, Jin; Yang, Changyi; Xia, Zijie; Pai, Dhruv; Hu, Shuming; Zhang, Zhen; Zhao, Chenyang; Zhao, Jinman; Xu, Wujiang; Li, Raymond; Wang, Xin Eric; McAuley, Julian; Wang, Zhaoran
- **Year**: 2026
- **arXiv**: [2606.25354](https://arxiv.org/abs/2606.25354)
- **Date**: 2026/06/24

## Key Contributions
- Identifies the structural trade-off in test-time scaling: long chain-of-thought sampling is single-threaded while sentence- or solution-level search is computationally expensive and hard to train end-to-end.
- Proposes Local Branch Routing (LBR), a token-level test-time scaling framework that expands a small local lookahead tree, forwards sampled branches through the LM, and uses a lightweight router to select the best continuation.
- Demonstrates that LBR is end-to-end trainable and shows that post-candidate hidden states provide useful routing evidence on hierarchical-planning tasks and mathematical-reasoning benchmarks.

## Related Papers
- [[randomized-yarn-improves-length-generalization-for-long-context-reasoning-2606.23687]] — sibling length-extension-for-reasoning work; Randomized YaRN recovers long-context reasoning at 16K-128K context windows, LBR scales inference compute via branch routing at the token level — together they bracket the long-context-reasoning surface between *positional-encoding length extension* (Randomized YaRN) and *token-level branch-routing inference scaling* (LBR)
- [[verievol-scaling-multimodal-mathematical-reasoning-via-verifiable-evol-instruct-2606.23543]] — sibling mathematical-reasoning-scaling work; VeriEvol scales math reasoning via verifiable evol-instruct at training time, LBR scales reasoning via branch routing at inference time — together they bracket the math-reasoning-scaling surface between *training-time evol-instruct* (VeriEvol) and *inference-time branch routing* (LBR)
- [[the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-paradigms-abstractions-building-blocks-and-open-challenges-2606.11470]] — sibling systematic reasoning-paradigm survey; Periodic-Table-of-LLM-Reasoning catalogs reasoning paradigms as building blocks, LBR introduces a new paradigm (token-level branch-routing inference scaling) that the Periodic Table would categorize under *search-based inference scaling* — together they bracket the reasoning-paradigm surface between *systematic paradigm taxonomy* (Periodic Table) and *new paradigm instantiation* (LBR)
- [[emergent-concepts]] — parent wiki page
