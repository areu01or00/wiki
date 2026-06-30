---
title: "MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [agent, self-supervision, multi-agent, rl]
sources: ["https://arxiv.org/abs/2606.19893"]
---

# MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments

## Overview
MetaResearcher scales deep research agent training across four synergistic dimensions: an Evolving Virtual World with adversarial misinformation, Discovery-Oriented Tasks (hypothesis generation, contradiction resolution), a Self-Reflective Meta-Reward mechanism within GRPO, and a Heterogeneous Multi-Agent Swarm architecture. Targets GAIA and Xbench-DS benchmarks.

## Key Facts
- **Authors**: Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Haocheng Deng, Bing Li
- **Year**: 2026
- **arXiv**: [2606.19893](https://arxiv.org/abs/2606.19893)

## Key Contributions
- Evolving Virtual World with temporal dynamics and adversarial misinformation for source credibility assessment
- Discovery-Oriented Tasks (hypothesis generation, contradiction resolution) beyond fact retrieval
- Self-Reflective Meta-Reward within GRPO: jointly optimizes answer correctness, search path efficiency, reflection depth, tool call diversity
- Heterogeneous Multi-Agent Swarm (Scout, Filter, Synthesizer) with coordinated RL
- Zero marginal API training cost via LiteResearcher infrastructure

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent concept discoveries
- [[teaching-large-reasoning-models-effective-reflection-2601.12720]] — SCFT + RLERR for training LRMs to filter superficial reflections
- [[reflect-an-effective-harness-system-for-complex-long-horizon-llm-reasoning-2605.05737]] — ReFlect harness for error detection and recovery in long-horizon reasoning
