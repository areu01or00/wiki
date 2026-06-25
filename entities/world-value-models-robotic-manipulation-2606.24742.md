---
title: "World Value Models for Robotic Manipulation"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [robotics, world-model, value-function, manipulation, vla]
sources: ["https://arxiv.org/abs/2606.24742"]
---

# World Value Models for Robotic Manipulation

## Overview
Wang, Li, Cui, Gao, Zhan, Yu, and Ma marry world models with value estimation to construct a generalist robotic value model (WVM) that provides accurate task progression scoring for mixed-quality manipulation data, and introduce Suboptimal-Value-Bench — a multi-embodiment benchmark of 800 suboptimal trajectories with human-labeled frame annotations — to evaluate value models on the non-expert regime where most large-scale manipulation data actually lives.

## Key Facts
- **Authors**: Wang, Zhihao; Li, Jianxiong; Cui, Yu; Gao, Yuan; Zhan, Xianyuan; Yu, Junzhi; Ma, Xiao
- **Year**: 2026
- **arXiv**: [2606.24742](https://arxiv.org/abs/2606.24742)
- **Category**: cs.RO, cs.AI, cs.CV
- **Date**: 2026-06-19

## Key Contributions
- Argues that VLM-backboned value models lack the temporal modeling capabilities required for accurate value estimation, and that world-model backbones are the natural foundation because they are pre-trained on temporally dense observations.
- Constructs a generalist World Value Model (WVM) that grounds current belief using historical context and plans over future outcomes, achieving SOTA Value-Order Correlation on standard benchmarks.
- Introduces Suboptimal-Value-Bench, a multi-embodiment benchmark of 800 suboptimal trajectories with high-fidelity human-labeled frame annotations — explicitly designed to evaluate value models on the non-expert data that dominates large-scale manipulation corpora.
- Shows WVM maintains SOTA performance on Suboptimal-Value-Bench, establishing robustness on both expert and suboptimal data, and improves downstream manipulation policy learning when used as a data-quality filter.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[world-action-models-a-survey-2606.20781]] — Sibling survey disambiguating WAMs from broader world models / video generators / VLA policies; WVM is the value-estimation counterpart that scores which of those predictive-action trajectories is worth keeping.
- [[ebench-elemental-diagnosis-of-generalist-mobile-manipulation-policies-2606.18239]] — Sibling multi-axis-diagnostic benchmark showing that aggregate success rate masks capability-specific collapses in generalist manipulation; WVM provides the data-selection signal that prevents such collapses by filtering expert-only trajectories.
- [[qwen-agentworld-language-world-models-for-general-agents-2606.24597]] — Sibling world-model work for language-only agents; together they frame world models as the load-bearing primitive across both embodied and linguistic agent surfaces.