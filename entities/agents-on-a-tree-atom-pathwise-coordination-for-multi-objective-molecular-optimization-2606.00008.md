---
title: "Agents on a Tree: Pathwise Coordination for Multi-Objective Molecular Optimization"
created: "2026-06-30"
updated: "2026-06-30"
type: entity
tags: [multi-agent, coordination, tree-search, molecular-optimization, pathwise-coordination]
sources: ["https://arxiv.org/abs/2606.00008"]
---

# Agents on a Tree: Pathwise Coordination for Multi-Objective Molecular Optimization

## Overview
ATOM formulates multi-objective molecular optimization as a tree-structured search where each node hosts a specialized agent for a particular objective or decision context. Rather than enforcing global consensus across all agents (which collapses diverse trade-offs), ATOM agents coordinate pathwise along different branches of the tree, maintaining and comparing alternative molecular evolution trajectories simultaneously. A global memory of past optimization behaviors supports balanced exploration vs. exploitation across objectives. This tree-structured interaction enables reasoning over long-horizon dependencies inherent in molecular design, with experiments on multi-objective benchmarks (activity, synthesizability, ADMET properties) showing improved Pareto coverage and hypervolume over strong baselines.

## Key Facts
- **Authors**: Jia Zhang, Tengfei Ma, Tianle Li, Daojian Zeng, Xieping Gao, Xiangxiang Zeng
- **Year**: 2026 (submitted Mar 27, 2026)
- **arXiv**: [2606.00008](https://arxiv.org/abs/2606.00008)
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- Tree-structured multi-agent coordination: each node = atomic operation + specialist agent; coordination is pathwise (along branches) rather than global consensus
- Global memory of past optimization behaviors enables balanced exploration/exploitation across objectives without collapsing trade-off diversity
- Long-horizon dependency reasoning via tree structure addresses premature convergence inherent in single-policy or fixed-scalarization approaches
- Improved Pareto coverage and hypervolume on multi-objective molecular optimization benchmarks vs. strong baselines
- First tree-structured pathwise multi-agent coordination for multi-objective optimization in the wiki

## Related Papers
- [[connect-the-dots-training-llms-for-long-lifecycle-agents-with-cross-domain-generalization-via-reinforcement-learning-2606.20002]] — Connect the Dots: long-lifecycle agent training with cross-domain RL generalization; orthogonal to ATOM (Connect-the-Dots = agent training methodology, ATOM = multi-agent coordination architecture for combinatorial optimization)
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — EnterpriseClawBench: real-workplace session benchmark for enterprise agents; orthogonal to ATOM (EnterpriseClawBench = agent evaluation benchmark, ATOM = multi-agent coordination framework)
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist: context management is load-bearing for LLM agents; orthogonal to ATOM (Plans-Dont-Persist = single-agent context management failure, ATOM = multi-agent tree-structured coordination)
