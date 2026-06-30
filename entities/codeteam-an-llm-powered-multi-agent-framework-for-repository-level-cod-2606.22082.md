---
title: "CodeTeam: An LLM-Powered Multi-Agent Framework for Repository-Level Code Generation"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [llm, multi-agent, code-generation, planning, tool-use]
sources: ["https://arxiv.org/abs/2606.22082"]
---

# CodeTeam: An LLM-Powered Multi-Agent Framework for Repository-Level Code Generation

## Overview
CodeTeam is an LLM-based multi-agent framework for Natural Language to Repository Generation (NL2Repo) — constructing entire software repositories from natural-language requirements. It separates planning, decision-making, and implementation into distinct cooperating agents with specialized roles, using a hierarchical planner, decision maker, and implementation agents with cross-file dependency awareness.

## Key Facts
- **Authors**: (to be filled from paper)
- **Year**: 2026
- **arXiv**: [2606.22082](https://arxiv.org/abs/2606.22082)

## Key Contributions
- Hierarchical multi-agent architecture separating Planner, Decision Maker, and Implementation agents for repository-level code generation
- Iterative debugging protocol resolving cross-file inconsistencies through targeted test execution and selective revision
- NL2Repo benchmark covering 10 real-world software domains; 47% improvement in functional correctness, 3x reduction in cross-file interface errors

## Related Papers
- [[sequential-consensus-for-multi-agent-llm-debates-a-wald-sprt-compute-governor-with-calibration-based-failure-detection-2605.19193]] — Sequential Consensus: Multi-agent debate with compute governor and calibration-based failure detection — distinct from CodeTeam's code-specialist planning hierarchy
- [[the-value-of-variance-mitigating-debate-collapse-in-multi-agent-systems-via-uncertainty-driven-policy-optimization-2602.07186]] — Value of Variance: Debate collapse prevention via uncertainty-driven policy — orthogonal to CodeTeam's code-generation focus
