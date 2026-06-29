---
title: "When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm-agents, search, benchmarking, ambiguity-handling, interactive-reasoning]
sources: ["https://arxiv.org/abs/2606.27669"]
---

# When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search

## Overview
Search agents powered by LLMs are increasingly used for complex information-seeking tasks. Existing benchmarks assume user queries are complete and explicit, but real-world search requests are frequently vague, underspecified, or factually incorrect. This paper introduces DiscoBench, a benchmark for clarification-aware deep search that evaluates whether search agents can proactively identify ambiguity, ask effective clarification questions, and recover correct reasoning paths through user interaction.

## Key Facts
- **Authors**: Yiling Tao, Shihan Deng, Meiling Tao, Pengzhi Wei, Zhichao Hu, Zhihao Zhu
- **Year**: 2026
- **arXiv**: [2606.27669](https://arxiv.org/abs/2606.27669)
- **Subjects**: Computation and Language (cs.CL)
- **Comments**: 26 pages, 7 figures, 12 tables

## Key Contributions
- DiscoBench: 211 samples and 463 ambiguity instances across 11 real-world domains, covering 4 ambiguity types
- First benchmark to systematically evaluate clarification-aware deep search in LLM agents
- User simulator for multi-turn interaction enabling scalable evaluation
- Four-perspective evaluation: task utility, ambiguity detection, interaction strategy, and cost efficiency
- Key finding: ambiguity detection and effective clarification are distinct capabilities; repeatedly searching instead of asking often performs worse than direct guessing

## Related Papers
- [[emergent-concepts]] — Parent meta-page for emergent-concept discoveries
- [[tap-file-based-protocol-heterogeneous-llm-agent-collaboration-2606.14445]] — tap: File-based protocol for heterogeneous agent collaboration (orthogonal: clarification-aware search vs. file-based protocol communication)
- [[mas-promptbench-when-does-prompt-optimization-improve-multi-agent-llm-2606.23664]] — MAS-PromptBench: Multi-agent prompt optimization (orthogonal: clarification interaction vs. prompt optimization benchmarking)
