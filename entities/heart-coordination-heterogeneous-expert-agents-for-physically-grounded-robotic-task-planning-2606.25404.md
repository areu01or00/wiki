---
title: "HEART: Coordination of Heterogeneous Expert Agents for Physically Grounded Robotic Task Planning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multi-agent, llm, robotic-task-planning, heterogeneous-agents]
sources: ["https://arxiv.org/abs/2606.25404"]
---

# HEART: Coordination of Heterogeneous Expert Agents for Physically Grounded Robotic Task Planning

## Overview
HEART addresses the failure mode where single-LLM planners produce invalid or incomplete robotic task plans due to lack of structured reasoning about physical feasibility, reachability, and logical ordering. The framework decomposes complex instructions into atomic reasoning tasks allocated across role-specialized expert agents under a token budget, enabling real-world computational and communication efficiency.

## Key Facts
- **Authors**: Junho Lee, Seabin Lee, Wonjong Lee, Nayoung Kim, Moonjeong Kang, Changjoo Nam
- **Year**: 2026
- **arXiv**: [2606.25404](https://arxiv.org/abs/2606.25404)

## Key Contributions
- Heterogeneous multi-LLM expert agent decomposition under token budget constraints
- Structured feasibility, reachability, and logical-order reasoning in LLM-based robotic planning
- Token budget-aware communication protocol for real-world deployment efficiency
- Addresses physical/spatial constraint violations that cause single-LLM planner failures

## Related Papers
- [[agents-on-a-tree-atom-pathwise-coordination-for-multi-objective-molecular-optimization-2606.00008]] — ATOM's tree-structured pathwise coordination is the closest structural sibling to HEART's expert decomposition
- [[organize-then-retrieve-hierarchical-memory-navigation-for-efficient-long-horizon-llm-agents-2606.11680]] — OTR's hierarchical memory architecture complements HEART's expert decomposition for long-horizon tasks
- [[multi-agent-transactive-memory-knowledge-sharing-across-heterogeneous-agent-populations-2606.19911]] — Shared theme of heterogeneous multi-agent coordination
